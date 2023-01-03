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
print(os.getcwd())

# mp.addRasterLayer(
#     fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\viz_maps\test_map_1_risk_landcover_n33900w119100_viz.tif",
#     Tag="landcover risk",
#     mapType=mapTypes.RiskMap)
# mp.addRasterLayer(
#     fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\viz_maps\test_map_1_risk_population_n33900w119100_viz.tif",
#     Tag="population risk",
#     mapType=mapTypes.RiskMap)
# mp.addRasterLayer(
#     fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\viz_maps\test_map_1_risk_slope_n33900w119100_viz.tif",
#     Tag="slope risk",
#     mapType=mapTypes.RiskMap)
# mp.addRasterLayer(
#     fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\viz_maps\test_map_1_risk_n33900w119100_viz.tif",
#     Tag="total risk",
#     mapType=mapTypes.RiskMap)
mp.addVectorLayer(
    fn=r"C:/0-Data/0-LESLAII/VectorData/low_risk_test_strips.shp",
    Tag="low_risk",
    color="0,0,255,255",
    linestyle="solid",
    size=10,
)
mp.addVectorLayer(
    fn=r"C:/0-Data/0-LESLAII/VectorData/med_risk_test_strips.shp",
    Tag="med_risk",
    color="255,255,0,255",
    linestyle="solid",
    size=10,
)
mp.addVectorLayer(
    fn=r"C:/0-Data/0-LESLAII/VectorData/high_risk_test_strips.shp",
    Tag="high_risk",
    color="255,0,0,255",
    linestyle="solid",
    size=10,
)

mp.show()
qgs.exec_()
