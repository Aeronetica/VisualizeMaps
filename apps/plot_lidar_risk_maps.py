from qgis.core import *
from mapViewerWindow import mapViewerWindow
import os
from mapViewerWindow import mapTypes
# from qgis.PyQt.QtWidgets import *
# from qgis.PyQt.QtCore import *
# from qgis._gui import *


QgsApplication.setPrefixPath("C:\\OSGeo4W\\apps\\qgis", True)
qgs = QgsApplication([], True)
qgs.initQgis()
mp = mapViewerWindow()
mp.loadDefaultLyrs()
print(os.getcwd())

# mp.addRasterLayer(
#     fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\test_maps_3_35_119\test_3_landcover_n34800w119200_viz.tif",
#     Tag="landcover risk",
#     mapType=mapTypes.RiskMap)
# mp.addRasterLayer(
#     fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\test_maps_3_35_119\test_3_population_n34800w119200_viz.tif",
#     Tag="population risk",
#     mapType=mapTypes.RiskMap)
# mp.addRasterLayer(
#     fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\test_maps_3_35_119\test_3_slope_n34800w119200_viz.tif",
#     Tag="slope risk",
#     mapType=mapTypes.RiskMap)
# mp.addRasterLayer(
#     fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\test_maps_3_35_119\test_3_risk_n34800w119200_viz.tif",
#     Tag="total risk",
#     mapType=mapTypes.RiskMap)


mp.addRasterLayer(
    fn=r"\\wsl.localhost\Ubuntu\home\loydhook\data\lidar_data\LELSA_Data\vis_lidar_diff.tif",
    Tag="LidarRisk",
    mapType=mapTypes.LidarRiskMap)


# mp.addRasterLayer(
#     fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\test_35_119\test_population_n34800w119200_viz.tif",
#     Tag="119 pop",
#     mapType=mapTypes.RiskMap)

# mp.addRasterLayer(
#     fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\test_35_120\test_risk_n34800w120200_viz.tif",
#     Tag="120",
#     mapType=mapTypes.RiskMap)

mp.show()
qgs.exec_()