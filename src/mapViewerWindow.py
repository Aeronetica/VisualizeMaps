from PyQt5.QtGui import QPainter
from qgis.core import *
from osgeo import gdal
from PyQt5.QtGui import *
from qgis._gui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtCore import *
import ntpath, os
import PIL.Image as Image
from pyproj import CRS
from pyproj import Transformer
import toolBarActions as tb
import rasterLayer as rlyr
import vectorLayer as vlyr
import json


class mapTypes:
    Default = 0
    Airspace = 1
    Terrain = 2
    Hillshade = 3
    Obstacle = 4
    Wavefront = 5
    AirspaceSlice = 6
    VectorField = 7
    BitPacked = 8
    v_FlightPath = 9
    v_ArrowField = 10
    RiskMap = 11
    NewRiskEqn = 12
    Slope = 13
    Population = 14
    landingComposite = 15
    landCover = 16
    vector = 17
    latlon = 18
    background = 19
    foreground = 20
    density = 21
    utm_5_population = 22
    transparent_risk = 23

    def __init__(self, itemType=0, itemName="", filename=""):
        self.mapType = itemType
        self.mapName = itemName
        self.fn = filename


class mapViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IO-Aero GIS Analysis Application")
        # Some flags I don't know if some of these are needed anymore
        self.maps = {
            "background": [],
            "foreground": [],
            "latlon": [],
            "user_rasters": [],
            "user_vectors": [],
        }
        self.rasterLayers = []
        self.baseRasterLayers = []
        self.vectorLayers = []
        self.mapInfos = []
        self.toolBarActions = []
        self.latlonLayer = []
        self.rasterCounter = -1
        self.currentRasterLayer = -1
        self.allRasOn = True
        self.hillshade = True
        self.baseEspgOn = False
        self.minDiffOn = False
        self.labelsOn = True
        self.percentagesOn = True
        self.tdtOn = False
        self.dtedOn = True
        self.layerhillshade = True
        self.rastersOn = True
        self.vectorsOn = True
        self.latlonOn = True
        self.loadDefaultLyrs()
        self.buildCanvas()
        self.addBaseToolBar()
        self.addUserToolBar()
        self.turnOnUserTools()

    def addBaseToolBar(self):
        self.actionZoomIn = QAction("Zoom on Area", self)
        self.actionZoomOut = QAction("Zoom out", self)
        self.actionPan = QAction("Pan", self)
        self.actionHome = QAction("Home Extent", self)
        self.actionQueryRas = QAction("Query Point", self)
        self.actionZoomIn.setCheckable(True)
        self.actionZoomOut.setCheckable(True)
        self.actionPan.setCheckable(True)
        self.actionQueryRas.setCheckable(True)
        self.actionZoomIn.triggered.connect(self.zoomIn)
        self.actionZoomOut.triggered.connect(self.zoomOut)
        self.actionPan.triggered.connect(self.pan)
        self.actionHome.triggered.connect(self.home)
        self.actionQueryRas.triggered.connect(self.queryRas)

        self.toolbar = self.addToolBar("Main Actions")
        self.toolbar.addAction(self.actionZoomIn)
        self.toolbar.addAction(self.actionZoomOut)
        self.toolbar.addAction(self.actionPan)
        self.toolbar.addAction(self.actionHome)
        self.toolbar.addAction(self.actionQueryRas)
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False)  # false = in
        self.toolZoomIn.setAction(self.actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True)  # true = out
        self.toolZoomOut.setAction(self.actionZoomOut)
        self.toolQuery = QgsMapToolEmitPoint(self.canvas)
        self.toolQuery.setAction(self.actionQueryRas)
        self.toolQuery.canvasClicked.connect(self.displayPoint)
        self.addToolBarBreak()

    def addUserToolBar(self):
        self.toolBarActions.append(
            tb.toolBarActions(description="Save JPG", connectFunction=self.saveJPG)
        )
        self.toolBarActions.append(
            tb.toolBarActions(
                description="Toggle Rasters On/Off", connectFunction=self.toggle_rasters
            )
        )
        self.toolBarActions.append(
            tb.toolBarActions(
                description="Toggle Vectors On/Off",
                connectFunction=self.toggle_vector_layers,
            )
        )
        self.toolBarActions.append(
            tb.toolBarActions(
                description="Lat Lon",
                connectFunction=self.toggleLatLon,
                checkable=False,
            )
        )
        self.toolBarActions.append(
            tb.toolBarActions(
                description="Cycle Rasters",
                connectFunction=self.cycle_rasters,
            )
        )

    def turnOnUserTools(self):

        self.toolbar2 = self.addToolBar("User Actions")
        for action in self.toolBarActions:
            thisAction = QAction(action.description, self)
            thisAction.setCheckable = action.checkable
            thisAction.triggered.connect(action.connectFunction)
            if action.toolbar == 0:
                self.toolbar2.addAction(thisAction)

    def addVectorLayer(
        self,
        fn,
        mapType=None,
        Tag="",
        color="255,0,0,255",
        size=3,
        linestyle: str = "dot",
    ):
        if not os.path.exists(fn):
            print("No map exists at " + fn)
            return
        print("Adding vector layer at " + fn)
        vl = vlyr.vectorLayer(fn, mapType, Tag)
        vl.buildUserLyr(color=color, linestyle=linestyle, size=size)
        # self.vectorLayers.append(vl)
        self.maps["user_vectors"].append(vl)
        self.canvas.setLayers(self.returnLayerList())

    def loadDefaultLyrs(self):
        # The below is the bing map... for just the aerial data ...tiles/a% for the labeled data .../tiles/h%  the h is the key.. Just the labels is ho
        rl = rlyr.rasterLayer(
            uri="type=xyz&url=http://ecn.t3.tiles.virtualearth.net/tiles/a%7Bq%7D.jpeg?g%3D1&zmax=18&zmin=0",
            maptype=mapTypes.background,
            name="OSM",
            provider="wms",
        )
        self.maps["background"] = rl
        # self.rasterLayers.append(rl)
        self.epsg = rl.lyr.crs().authid()
        self.home_extent = rl.lyr.extent()
        print(self.epsg)

        rl = rlyr.rasterLayer(
            uri="type=xyz&url=http://ecn.t3.tiles.virtualearth.net/tiles/ho%7Bq%7D.jpeg?g%3D1&zmax=18&zmin=0",
            maptype=mapTypes.foreground,
            name="OSM",
            provider="wms",
        )
        self.maps["foreground"] = rl
        # self.rasterLayers.append(rl)

        self.addLatLonLyr()  # Use default params

    def addLatLonLyr(
        self,
        filename=r"maps/vectorMaps/reproj-latLon_Shapefile.shp",
        color="155, 155,155,255",
        linestyle="dot",
        width=0.45,
    ):
        vl = vlyr.vectorLayer(filename=filename, maptype=mapTypes.latlon, name="")
        vl.buildLatLonLyr(color=color, linestyle=linestyle, width=width)
        self.maps["latlon"] = vl
        self.vectorLayers.insert(0, vl)

    def addRasterLayer(self, fn, mapType=None, Tag="", srcEpsg=None, overwrite=False):
        if not os.path.exists(fn):
            print("No map exists at " + fn)
            return
        rl = rlyr.rasterLayer(fn, mapType, Tag)
        if len(self.rasterLayers) == 0:
            self.home_extent = rl.lyr.extent()
            self.canvas.setExtent(self.home_extent)
            self.canvas.refresh()
        else:
            self.home_extent.combineExtentWith(rl.lyr.extent())
            self.canvas.setExtent(self.home_extent)
            self.canvas.refresh()
        self.maps["user_rasters"].append(rl)
        # self.rasterLayers.append(rl)
        self.rasterCounter += 1
        self.currentRasterLayer = len(self.rasterLayers) - 1
        self.canvas.setLayers(self.returnLayerList())

    def buildCanvas(self):
        self.canvas = QgsMapCanvas()
        self.canvas.enableAntiAliasing(True)
        self.canvas.setCanvasColor(Qt.black)
        self.canvas.setExtent(self.home_extent)
        self.backOn = True
        self.latlonOn = True
        self.canvas.setLayers(self.returnLayerList())
        self.setCentralWidget(self.canvas)

    def toggleLatLon(self):
        self.latlonOn = not self.latlonOn
        self.canvas.setLayers(self.returnLayerList())

    def toggle_vector_layers(self):
        self.vectorsOn = not self.vectorsOn
        self.canvas.setLayers(self.returnLayerList())

    def returnLayerList(self):
        LayerList = []
        if self.backOn and self.labelsOn:
            LayerList.append(self.maps["foreground"].lyr)

        if self.latlonOn:
            LayerList.append(self.maps["latlon"].lyr)

        if len(self.maps["user_vectors"]) > 0 and self.vectorsOn:
            for vl in self.maps["user_vectors"]:
                LayerList.append(vl.lyr)

        if self.rastersOn:
            if self.allRasOn:
                for rl in self.maps["user_rasters"]:
                    print("Showing raster tagged " + rl.name)
                    if self.layerhillshade is True:
                        LayerList.append(rl.hillLyr)
                    LayerList.append(rl.lyr)
            elif (
                len(self.maps["user_rasters"]) > self.currentRasterLayer
                and self.rasterCounter >= 0
            ):
                print(
                    "Showing raster tagged "
                    + self.maps["user_rasters"][self.currentRasterLayer].name
                )
                if self.layerhillshade is True:
                    LayerList.append(
                        self.maps["user_rasters"][self.currentRasterLayer].hillLyr
                    )
                LayerList.append(self.maps["user_rasters"][self.currentRasterLayer].lyr)

        if self.backOn == True:
            LayerList.append(self.maps["background"].lyr)
        return LayerList

    def setRenderHillshade(self, layer, zf):  # set render type to 'hillshade'
        zfNew = zf  # * 24.74 / layer.rasterUnitsPerPixelX()
        newAlt = (
            10 * 24.74 / (layer.rasterUnitsPerPixelX() * layer.rasterUnitsPerPixelY())
        )
        # if(newAlt < 2):
        #     newAlt = .1
        r = QgsHillshadeRenderer(layer.dataProvider(), 1, 180, newAlt)
        print("Raster units = " + str(layer.rasterUnitsPerPixelX()))
        print("New zf = " + str(zfNew) + "  New Alt " + str(newAlt))
        r.setZFactor(zfNew)
        layer.setRenderer(r)
        layer.setBlendMode(QPainter.CompositionMode_Multiply)

    def saveJPG(self):
        if os.path.exists("config/path.json"):
            with open("config/path.json") as json_file:
                path_dict=json.load(json_file)
                open_path = path_dict["save_path"]
        else:
            open_path=r"D:\\"
                
        jpgFile = QFileDialog.getSaveFileName(
            self, "Save Image As", open_path, "jpg Files (*.jpg)"
        )
        if jpgFile[0] == "":
            print(
                "Select File in the correct way right now we have <" + jpgFile[0] + ">"
            )
            return
        tmpFile = os.path.splitext(jpgFile[0])[0] + "_tmp.jpg"

        self.canvas.saveAsImage(tmpFile)
        lowRes = Image.open(tmpFile)
        lowRes_rgb = lowRes.convert("RGB")
        lowRes_rgb.save(jpgFile[0], "JPEG", optimize=True, quality=90)

        print("Canvas Image Saved at <" + jpgFile[0] + ">")
        if os.path.exists(tmpFile):
            os.remove(tmpFile)
        jgwFile = os.path.splitext(jpgFile[0])[0] + "_tmp.jgw"
        if os.path.exists(jgwFile):
            os.remove(jgwFile)
        save_path = {"save_path": os.path.split(jpgFile[0])[0]}
        with open("config/path.json", "w") as outfile:
            json.dump(save_path, outfile, indent=2)

    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)

    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)

    def pan(self):
        self.canvas.setMapTool(self.toolPan)

    def home(self):
        self.canvas.setExtent(self.home_extent)
        self.canvas.refresh()

    def toggle_rasters(self):
        if not self.rastersOn:
            self.allRasOn = True  # Turn all the rasters on
        self.rastersOn = not self.rastersOn
        self.canvas.setLayers(self.returnLayerList())

    def queryRas(self, pointTool):
        self.canvas.setMapTool(self.toolQuery)

    def displayPoint(self, pointTool):
        x = pointTool.x()
        y = pointTool.y()
        trans = Transformer.from_crs(3857, 4326)
        reppt = trans.transform(x, y)
        # reppt = gt.reprojectPt(src_epsg=self.epsg, dst_epsg='EPSG:4326', tuple=[x,y, 0])
        print(
            "Query Point: "
            + "Lat: "
            + str(reppt[0])
            + " Lon: "
            + str(reppt[1])
            + ":x,y:"
            + str(x)
            + ","
            + str(y)
        )
        # for (lyr, map) in zip(self.rasterLayers, self.mapInfos):
        for rl in self.maps["user_rasters"]:
            ident1 = rl.lyr.dataProvider().sample(pointTool, 1)
            if ident1[1] == True:
                print(f"Value of {rl.name} map is {ident1[0]}")

    def cycle_rasters(self):
        if self.allRasOn:
            self.allRasOn = False
            self.currentRasterLayer = 0
        else:
            self.currentRasterLayer = (self.currentRasterLayer + 1) % len(
                self.maps["user_rasters"]
            )
        self.canvas.setLayers(self.returnLayerList())


if __name__ == "__main__":

    QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis", True)
    qgs = QgsApplication([], True)
    qgs.initQgis()
    mp = mapViewerWindow()
    print(os.getcwd())
    ras = os.path.join(
        os.getcwd(), "maps/rasterMaps/nlcd_2019_land_cover_l48_20210604_viz.tif"
    )
    vec = os.path.join(os.getcwd(), "maps/vectorMaps/LESLA_traditional_areas.shp")
    # print("Opening raster at: " + ras)
    # mp.addRasterLayer(
    #     fn="maps/rasterMaps/nlcd_2019_land_cover_l48_20210604_viz.tif",
    #     Tag="Landcover",
    #     mapType=mapTypes.landCover,
    # )
    # mp.addVectorLayer(fn=vec)
    mp.addVectorLayer(
        fn="maps/vectorMaps/LESLA_traditional_areas_v1.shp",
        color="255,0,0,255",
        size=10,
    )
    mp.addVectorLayer(
        fn="maps/vectorMaps/LESLA_submaps_v1.shp", color="0,0,255,255", size=10
    )
    # mp.addRasterLayer(
    #     fn=r'../maps/rasterMaps/reproj-TDM1_DEM__30_N47E008_DEM_OrigVect.tif',
    #     Tag='OrigVect', mapType=mapTypes.Terrain)

    mp.show()
    qgs.exec_()
