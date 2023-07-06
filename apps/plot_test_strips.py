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
outfldrs = [r'D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\eastern_30_84\c182_strips\ShapeFiles',
            r'D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\eastern_30_78\c182_strips\ShapeFiles',
            r'D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\eastern_30_72\c182_strips\ShapeFiles',
            r'D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\eastern_36_84\c182_strips\ShapeFiles',
            r'D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\eastern_36_78\c182_strips\ShapeFiles',
            r'D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\eastern_36_72\c182_strips\ShapeFiles',
            r'D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\eastern_42_84\c182_strips\ShapeFiles',
            r'D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\eastern_42_78\c182_strips\ShapeFiles',
            r'D:\0-ProjectData\2022_LESLA_PhaseII\LESLA_traditional\eastern_42_72\c182_strips\ShapeFiles',
]
sz = 10
for output_fldr in outfldrs:
    mp.addVectorLayer(
        fn=os.path.join(output_fldr, 'low_risk_test_strips.shp'),
        Tag="low_risk",
        color="0,0,255,255",
        linestyle="solid",
        size=sz,
    )
    mp.addVectorLayer(
        fn=os.path.join(output_fldr, 'med_risk_test_strips.shp'),
        Tag="med_risk",
        color="255,255,0,255",
        linestyle="solid",
        size=sz,
    )
    mp.addVectorLayer(
        fn=os.path.join(output_fldr, 'high_risk_test_strips.shp'),
        Tag="high_risk",
        color="255,0,0,255",
        linestyle="solid",
        size=sz,
    )

mp.show()
qgs.exec_()
