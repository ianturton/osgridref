"""
/***************************************************************************
Name                 : OS Grid Reference expressions
Description          : Set of expressions for QGIS
Date                 : Apr 21, 2020
copyright            : (C) 2020 by Ian Turton
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

Updates/New:
- 2020-04-21: Copied skeleton from ibama_expressions
- 2020-04-01:
    - Refactored using global
- 2020-03-23:
    - Rename: getDateSentinel to getDateSentinel1
    - New: getDateSentinel2
- 2020-02-12:
    - New: getUTM, getCRSLayer
    - Update: getCRSLayer, area_crs
    - Remove(exists in default expressions): is_selected, dms_x, dms_y, existsFile, getFileName

"""
__author__ = 'Ian Turton'
__date__ = '2020-04-21'
__copyright__ = '(C) 2020, Ian Turton'
__revision__ = '$Format:%H$'


from qgis.core import (
    QgsExpression
)
from qgis.utils import qgsfunction

groupName = "OS Grid References"
gridLetters = [["SV", "SQ", "SL", "SF", "SA", "NV", "NQ", "NL", "NF", "NA", "HV", "HQ", "HL"],
               ["SW", "SR", "SM", "SG", "SB", "NW", "NR", "NM", "NG", "NB", "HW", "HR", "HM"],
               ["SX", "SS", "SN", "SH", "SC", "NX", "NS", "NN", "NH", "NC", "HX", "HS", "HN"],
               ["SY", "ST", "SO", "SJ", "SD", "NY", "NT", "NO", "NJ", "ND", "HY", "HT", "HO"],
               ["SZ", "SU", "SP", "SK", "SE", "NZ", "NU", "NP", "NK", "NE", "HZ", "HU", "HP"],
               ["TV", "TQ", "TL", "TF", "TA", "OV", "OQ", "OL", "OF", "OA", "JV", "JQ", "JL"],
               ["TW", "TR", "TM", "TG", "TB", "OW", "OR", "OM", "OG", "OB", "JW", "JR", "JM"]]


@qgsfunction(args='auto', group=groupName, usesgeometry=True)
def gridSquare(size, geometry, feature, parent):
    """
  <h4>Return</h4>OS Grid Refernce including 100km grid letters (NY581908)
  <p><h4>Syntax</h4>gridSquare(size, geometry)</p>
  <p><h4>Example</h4>gridSquare(100, $geometry) --> TF</p>
  <p><h4>Example</h4>gridSquare(10, $geometry)  --> TF30</p>
  <p><h4>Example</h4>gridSquare(1, $geometry)   --> TF3903</p>
  <p><h4>Example</h4>gridSquare(.1, $geometry)  --> TF392033</p>
  <p><h4>Example</h4>gridSquare(.01, $geometry) --> TF39280332</p>
  <p><h4>Example</h4>gridSquare(.001, $geometry)--> TF3928703326</p>
    """
    centroid = geometry.centroid()
    easting = centroid.asPoint().x()
    northing = centroid.asPoint().y()
    xText = "%06d" % easting
    yText = "%07d" % northing
    x = int(xText[:1])
    y = int(yText[:2])

    gl = gridLetters[x][y]

    result = gl

    if size == 100:
        return result
    elif size == 10:
        return gl + xText[1:2] + yText[2:3]
    elif size == 1:
        return gl + xText[1:3] + yText[2:4]
    elif size == .1:
        return gl + xText[1:4] + yText[2:5]
    elif size == .01:
        return gl + xText[1:5] + yText[2:6]
    elif size == .001:
        return gl + xText[1:6] + yText[2:7]
    else:
        return "Invalid Size parameter "+str(size)


def registerFunctions(isRegister=True):
    t_register = (QgsExpression.registerFunction, lambda f: f)
    u_register = (QgsExpression.unregisterFunction, lambda f: f.name())
    (funcReg, funcArg) = t_register if isRegister else u_register
    g = globals()
    l_func = (g[v] for v in g if hasattr(g[v], 'usesGeometry'))
    for f in l_func:
        funcReg(funcArg(f))
