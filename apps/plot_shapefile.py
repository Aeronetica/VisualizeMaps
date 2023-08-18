from qgis.core import *
from mapViewerWindow import mapViewerWindow

QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis", True)
qgs = QgsApplication([], True)
qgs.initQgis()
mp = mapViewerWindow()
mp.loadDefaultLyrs()

mp.addVectorLayer(
    fn=r"\\wsl.localhost\Ubuntu\home\loydhook\data\lidar_data\Example_Shapefiles.shp",
    Tag="low_risk",
    color="0,0,255,255",
    linestyle="solid",
    size=10,
)

mp.show()
qgs.exec_()