from qgis.core import *
from mapViewerWindow import mapViewerWindow
import os
from mapViewerWindow import mapTypes
# from qgis.PyQt.QtWidgets import *
# from qgis.PyQt.QtCore import *
# from qgis._gui import *


QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis", True)
qgs = QgsApplication([], True)
qgs.initQgis()
mp = mapViewerWindow()
mp.loadDefaultLyrs()

mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\test_maps_2\test_map_2_elevation_n33900w119100_viz.tif",
    Tag="elevation",
    mapType=mapTypes.Terrain)
mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\test_maps_2\test_map_2_slope_n33900w119100_viz.tif",
    Tag="slope",
    mapType=mapTypes.RiskMap)
mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\test_maps_2\test_map_2_population_n33900w119100_viz.tif",
    Tag="population",
    mapType=mapTypes.RiskMap)
mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\test_maps_2\test_map_2_landcover_n33900w119100_viz.tif",
    Tag="landcover",
    mapType=mapTypes.RiskMap)
mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\test_maps_2\test_map_2_risk_n33900w119100_viz.tif",
    Tag="risk",
    mapType=mapTypes.RiskMap)

mp.show()
qgs.exec_()