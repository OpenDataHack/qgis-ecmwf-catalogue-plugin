from __future__ import print_function
import traceback
import sys
 
from gribapi import *
 
INPUT = 'windDataSet.grib'
VERBOSE = 1  # verbose error reporting
 
 
def example():
    with open(INPUT) as f:
 
        keys = [
            'shortName'
            ]
 
        while 1:
            gid = grib_new_from_file(f)
            if gid is None:
                break
 
            for key in keys:
                if not grib_is_defined(gid, key):
                    raise ValueError("Key '%s' was not defined" % key)
                print('%s=%s' % (key, grib_get(gid, key)))
 
            #print('There are %d values, average is %f, min is %f, max is %f'
#                  % (grib_get_size(gid, 'values'),
#                     grib_get(gid, 'average'),
#                     grib_get(gid, 'min'),
#                     grib_get(gid, 'max')))
            for x in grib_get_values(gid):
                print("%s has value = %s   and it's id = %s" % (grib_get(gid, key), x))
 
            grib_release(gid)
 
 
def main():
    try:
        example()
    except GribInternalError as err:
        if VERBOSE:
            traceback.print_exc(file=sys.stderr)
        else:
            print(err.msg, file=sys.stderr)
 
        return 1
 
if __name__ == "__main__":
    sys.exit(main())
