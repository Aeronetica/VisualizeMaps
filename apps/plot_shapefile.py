from qgis.core import *
from mapViewerWindow import mapViewerWindow

QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis", True)
qgs = QgsApplication([], True)
qgs.initQgis()
mp = mapViewerWindow()
mp.loadDefaultLyrs()

mp.addVectorLayer(
    fn=r"C:\0-Data\0-LESLAII\VectorData\Lidar\boundingBox_Edwards.shp",
    Tag="low_risk",
    color="0,0,255,255",
    linestyle="solid",
    size=10,
)

mp.show()
qgs.exec_()