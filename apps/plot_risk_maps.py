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

mp.addRasterLayer(
    fn=r"D:\0-ProjectData\2022_LESLA_PhaseII\Flight_Test_Maps\flight_test_36_77\flight_test_risk_n35800w77700_viz.tif",
    Tag="landcover risk",
    mapType=mapTypes.RiskMapTransparent,
)

outfldrs = [
    r"D:\0-ProjectData\2022_LESLA_PhaseII\Flight_Test_Maps\flight_test_36_77\c182_strips\ShapeFiles"
]
sz = 10
for output_fldr in outfldrs:
    mp.addVectorLayer(
        fn=os.path.join(output_fldr, "low_risk_test_strips.shp"),
        Tag="low_risk",
        color="0,0,255,255",
        linestyle="solid",
        size=sz,
    )
    mp.addVectorLayer(
        fn=os.path.join(output_fldr, "med_risk_test_strips.shp"),
        Tag="med_risk",
        color="255,255,0,255",
        linestyle="solid",
        size=sz,
    )
    mp.addVectorLayer(
        fn=os.path.join(output_fldr, "high_risk_test_strips.shp"),
        Tag="high_risk",
        color="255,0,0,255",
        linestyle="solid",
        size=sz,
    )

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
