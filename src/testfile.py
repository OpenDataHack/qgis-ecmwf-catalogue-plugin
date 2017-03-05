#!/usr/bin/env python
#
# Copyright 2015 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0
#
# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.
#
# **************************************************************************
# Function      : compute_wind_speed_height
#
# Author (date) : Cristian Simarro (20/11/2015)
#
# Category      : COMPUTATION
#
# OneLineDesc   : Computes the u/v components of the wind at certain height
#
# Description   : Computes computes the u/v components of the wind at certain height.
#                 First, it calculates the geopotential of each model level. Once the requested height
#                 is found between two model levels, the program will vertically interpolate the u/v component values.
#                 Based on code from Nils Wedi, the IFS documentation:
#                 https://software.ecmwf.int/wiki/display/IFS/CY41R1+Official+IFS+Documentation
#                 part III. Dynamics and numerical procedures
#                 optimised implementation by Dominique Lucas.
#                 ported to Python by Cristian Simarro
#
# Parameters    : -w wind                - height in meters you want to know u/v components
#                 tq.grib                - grib file with all the levelist of t and q
#                 uv.grib                - grib file with all the levelists of u/v
#                 zlnsp.grib             - grib file with levelist 1 for params z and lnsp
#                 -o output   (optional) - name of the output file (default='uv_out_<wind>.grib')
#
# Return Value  : output (default='uv_out_<wind>.grib')
#                 A fieldset the u/v components values for at the specified height
#
# Dependencies  : None
#
# Example Usage :
#                 python compute_wind_speed_height.py tq_ml_20151116_0.grib zlnsp_ml_20151116_0.grib uv_ml_20151116_0.grib -w 100
 
from numpy import *
import sys,math,os
import argparse
from gribapi import *
 
PARAMS = ["u","v"]
 
def main(u_v,out_name,h):
 
    #some checks and information printing
    print "Using as input files:\n   " ,u_v
    print "The result will be stored in:\n   ",out_name
 
    if os.path.exists(out_name):
        os.remove(out_name)
    fout = open(out_name,'w')
    Rd = 287.06
    RG = 9.80665
    index_keys = ["date","time","shortName","level","step"]
 
    values= {}
    pv = {}
    out = {}
    gid_out = {}
    values_plev = {}
    values_lev = {}
     
    h=int(h)
    iiduv = grib_index_new_from_file(u_v,index_keys)
     
    counter=0
    # iterate date
    for date in grib_index_get(zlnsp,'date'):
        grib_index_select(zlnsp,'date',date)
        grib_index_select(iidtq,'date',date)
        grib_index_select(iiduv,'date',date)
        # iterate step
        for time in grib_index_get(zlnsp,'time'):
            grib_index_select(zlnsp,'time',time)
            grib_index_select(iidtq,'time',time)
            grib_index_select(iiduv,'time',time)
            grib_index_select(zlnsp,'level',1)
            grib_index_select(zlnsp,'step',0)
            grib_index_select(zlnsp,'shortName','z')
            gid = grib_new_from_index(zlnsp)
 
            #gridType must be gridded, not spectral
            if grib_get(gid,"gridType",str) == "sh":
                print(sys.argv[0]+' [ERROR] fields must be gridded, not spectral')
                sys.exit(1)
 
            # surface geopotential
            values["z"] = grib_get_values(gid)
            z_h = values["z"]
            pv = grib_get_array(gid,'pv')
            levelSizeNV = grib_get(gid,'NV',int)/2 -1
             
            grib_release(gid)
            
            # iterate step all but geopotential z wich is always step 0 (an)
            for step in grib_index_get(iidtq,'step'):
                # we need to get z and lnsp from the first level to do the calculations
                z_h = values["z"]
                # heigh in geopotential
                my_z = h*RG + z_h
                z_f_prev = z_h
                 
                grib_index_select(iidtq,'step',step)
                grib_index_select(iiduv,'step',step)
 
                for shortName in ["lnsp"]:
                   grib_index_select(zlnsp,'shortName',shortName)
                   grib_index_select(zlnsp,'step',step)
                   gid = grib_new_from_index(zlnsp)
                   if grib_get(gid,"gridType",str) == "sh":
                       print(sys.argv[0]+' [ERROR] fields must be gridded, not spectral')
                       sys.exit(1)
                   values[shortName] = grib_get_values(gid)
                   pv = grib_get_array(gid,'pv')
                   levelSizeNV = grib_get(gid,'NV',int)/2 -1
                   grib_release(gid)
    
                # surface pressure
                sp = exp(values["lnsp"])
 
                # get the coefficients for computing the pressures
                # how many levels are we computing?
                grib_index_select(iidtq,'shortName',"t")
                levelSize=max(grib_index_get(iidtq,"level",int))
                if levelSize != levelSizeNV:
                    print(sys.argv[0]+' [WARN] total levels should be: '+str(levelSizeNV)+' but it is '+str(levelSize))
                A = pv[0:levelSize+1]
                B = pv[levelSize+1:]
                Ph_levplusone = A[levelSize] + (B[levelSize]*sp)
 
                # We want to integrate up into the atmosphere, starting at the ground
                # so we start at the lowest level (highest number) and keep
                # accumulating the height as we go.
                # See the IFS documentation:
                # https://software.ecmwf.int/wiki/display/IFS/CY41R1+Official+IFS+Documentation
                # part III
                # For speed and file I/O, we perform the computations with numpy vectors instead
                # of fieldsets.
                 
                #initialize values for the output
                for param in PARAMS:
                    grib_index_select(iiduv,'level',1)
                    grib_index_select(iiduv,'shortName',param)
                    gid = grib_new_from_index(iiduv)
                    gid_out[param]=grib_clone(gid)
                    grib_release(gid)
                    out[param]=zeros(sp.size)
                found = [False for i in range(sp.size)]
                for lev in list(reversed(range(1,levelSize+1))):
                    # select the levelist and retrieve the vaules of t and q
                    # t_level: values for t
                    # q_level: values for q
                    grib_index_select(iidtq,'level',lev)
                    grib_index_select(iidtq,'shortName',"t")
                    gid = grib_new_from_index(iidtq)
                    t_level = grib_get_values(gid)
                    grib_release(gid)
                    grib_index_select(iidtq,'shortName',"q")
                    gid = grib_new_from_index(iidtq)
                    q_level = grib_get_values(gid)
                    grib_release(gid)
 
                    # compute moist temperature
                    t_level = t_level * (1.+0.609133*q_level)
 
                    # compute the pressures (on half-levels)
                    Ph_lev = A[lev-1] + (B[lev-1] * sp)
 
                    if lev == 1:
                        dlogP = log(Ph_levplusone/0.1)
                        alpha = log(2)
                    else:
                        dlogP = log(Ph_levplusone/Ph_lev)
                        dP    = Ph_levplusone-Ph_lev
                        alpha = 1. - ((Ph_lev/dP)*dlogP)
 
                    TRd = t_level*Rd
 
                    # z_f is the geopotential of this full level
                    # integrate from previous (lower) half-level z_h to the full level
                    z_f = z_h + (TRd*alpha)
 
                    # z_h is the geopotential of 'half-levels'
                    # integrate z_h to next half level
                    z_h=z_h+(TRd*dlogP)
 
                    Ph_levplusone = Ph_lev
                    # retrieve u/v params for the current level
                    for param in PARAMS:
                        grib_index_select(iiduv,'level',lev) #136
                        grib_index_select(iiduv,'shortName',param)
                        gidp=grib_new_from_index(iiduv)
                        values_lev[param] = grib_get_values(gidp)
                        grib_release(gidp)
                        if (lev < levelSize):
                            grib_index_select(iiduv,'level',lev+1) #137
                            gidp=grib_new_from_index(iiduv)
                            values_plev[param] = grib_get_values(gidp)
                            grib_release(gidp)
                        else:
                            values_plev[param] = zeros(sp.size)
                    # search if the provided wind height converted to geopotential (my_z) is between
                    # the current level (z_f) and the previous one (z_f_prev)
                    for i in arange(z_f_prev.size):
                        if found[i]: continue
                        if my_z[i] >= z_f_prev[i] and my_z[i] < z_f[i]:
                            found[i]=True
                            # when found, interpolate vertically to get the value
                            # store it in out[param] to be written at the end
                            for param in PARAMS:
                                out[param][i] = ( (values_lev[param][i] * ( my_z[i]-z_f_prev[i])) + \
                                                 (values_plev[param][i] * (z_f[i] - my_z[i]) ) ) /  \
                                                 (z_f[i] - z_f_prev[i])
                    # update z_f_prev
                    z_f_prev=z_f
 
                # simple error check
                for i in arange(sp.size):
                    if not found[i]:
                        print "point ",i,"not found..."
 
                # write the values in the fout file
                for param in PARAMS:
                    grib_set_values(gid_out[param],out[param])
                    grib_write(gid_out[param],fout)
                    grib_release(gid_out[param])
    grib_index_release(iidtq)
    grib_index_release(iiduv)
    grib_index_release(zlnsp)
    fout.close()
    print("Done")
 
if __name__ == "__main__":
    request_date=0
    request_time=0
    wind = 100
    parser = argparse.ArgumentParser(
        description='Python tool to calculate the Z of the model levels')
    parser.add_argument("-w","--wind", help="height to calculate the wind components",required=True)
    parser.add_argument("-o","--output", help="name of the output file")
    parser.add_argument('z_lnsp', metavar='zlnsp.grib', type=str,
                   help='grib file with geopotential(z) and Logarithm of surface pressure(lnsp) for the ml=1')
    parser.add_argument('u_v', metavar='uv.grib', type=str,
                   help='grib file with u and v component of wind for the model levels')
    args = parser.parse_args()
    for fname in (args.z_lnsp,args.u_v):
        if not os.path.isfile(fname):
            print "[ERROR] file %s does not exist" %(fname)
            sys.exit(1)
    if args.wind:
        wind = args.wind
    out_name = 'uv_out_'+wind+'m.grib'
    if args.output:
        out_name=args.output
 
    #calling main function
    main(lnsp,args.u_v,out_name,wind)
