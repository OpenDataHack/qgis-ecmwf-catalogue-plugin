# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DataLoader
                                 A QGIS plugin
 Plugin for Data visualisation
                             -------------------
        begin                : 2017-03-05
        copyright            : (C) 2017 by Sagar
        email                : jas_96@hotmail.co.uk
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DataLoader class from file DataLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .data_loader import DataLoader
    return DataLoader(iface)
