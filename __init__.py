# -*- coding: UTF-8 -*-
"""
/***************************************************************************
Name                 : OSGB Grid Reference expressions
Description          : Set of expressions for QGIS
Date                 : Apr 21, 2020
copyright            : (C) 2020 by Ian Turton, Astun Technology
email                : ianturton@astuntechnology.com

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
__author__ = 'Ian Turton'
__date__ = '2020-04-21'
__copyright__ = '(C) 2020, Ian Turton'
__revision__ = '$Format:%H$'

from qgis.PyQt.QtCore import QObject

from .functions import registerFunctions


def classFactory(iface):
    return OSGridExpressionsPlugin(iface)


class OSGridExpressionsPlugin(QObject):
    def __init__(self, iface):
        super().__init__()

    def initGui(self):
        registerFunctions()

    def unload(self):
        registerFunctions(False)
