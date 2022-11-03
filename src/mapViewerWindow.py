from PyQt5.QtGui import QPainter
from qgis.core import *
from osgeo import gdal
from PyQt5.QtGui import *
from qgis._gui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtCore import *
import ntpath, os
import PIL.Image as Image

import toolBarActions as tb

class mapTypes():
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
    def __init__(self, itemType=0, itemName='', filename=''):
        self.mapType = itemType
        self.mapName = itemName
        self.fn = filename

class mapViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # The below is the bing map... for just the aerial data ...tiles/a% for the labeled data .../tiles/h%  the h is the key.. Just the labels is ho
        self.backGroundLayer = QgsRasterLayer(
            "type=xyz&url=http://ecn.t3.tiles.virtualearth.net/tiles/a%7Bq%7D.jpeg?g%3D1&zmax=18&zmin=0", "OSM", "wms")
        self.foreGroundLayer = QgsRasterLayer(
            "type=xyz&url=http://ecn.t3.tiles.virtualearth.net/tiles/ho%7Bq%7D.jpeg?g%3D1&zmax=18&zmin=0", "OSM", "wms")

        self.setWindowTitle('IO-Aero GIS Analysis Application')
        #Some flags I don't know if some of these are needed anymore
        self.rasterLayers = []
        self.baseRasterLayers = []
        self.vectorLayers = []
        self.hillLayers = []
        self.mapInfos = []
        self.toolBarActions = []
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
        self.openBackgroundVectorLayers()
        self.buildCanvas()
        self.addBaseToolBar()
        self.addUserToolBar()
        self.turnOnTools()
        
    def addBaseToolBar(self):
        self.actionZoomIn = QAction("Zoom on Area", self)
        self.actionZoomOut = QAction("Zoom out", self)
        self.actionPan = QAction("Pan", self)
        self.actionHome = QAction("Home Extent", self)
        self.actionZoomIn.setCheckable(True)
        self.actionZoomOut.setCheckable(True)
        self.actionPan.setCheckable(True)
        self.actionZoomIn.triggered.connect(self.zoomIn)
        self.actionZoomOut.triggered.connect(self.zoomOut)
        self.actionPan.triggered.connect(self.pan)
        self.actionHome.triggered.connect(self.home)
    
    def addUserToolBar(self):
        self.toolBarActions.append(tb.toolBarActions(description='Save JPG', connectFunction=self.saveJPG))    
            
    def turnOnTools(self):
        self.toolbar = self.addToolBar("Main Actions")
        self.toolbar.addAction(self.actionZoomIn)
        self.toolbar.addAction(self.actionZoomOut)
        self.toolbar.addAction(self.actionPan)
        self.toolbar.addAction(self.actionHome)
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False)  # false = in
        self.toolZoomIn.setAction(self.actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True)  # true = out
        self.toolZoomOut.setAction(self.actionZoomOut)
        self.addToolBarBreak()
        self.toolbar2 = self.addToolBar("User Actions")
        for action in self.toolBarActions:
            thisAction = QAction(action.description, self)
            thisAction.setCheckable = action.checkable
            thisAction.triggered.connect(action.connectFunction)
            if(action.toolbar == 0):
                self.toolbar2.addAction(thisAction)
                


    def openBackgroundVectorLayers(self):
        latLonLines = r'maps/vectorMaps/reproj-latLon_Shapefile.shp'
        lyr = QgsVectorLayer(latLonLines, 'Lat Lon Lines')
        lineSymbol = QgsLineSymbol.createSimple(
            {'color': '155,155,155,255', 'line_style': 'dot', 'width': '.45'})
        lyr.renderer().setSymbol(lineSymbol)
        print(lyr.renderer().symbol().symbolLayers()[0].properties())
        print('Type:', lyr.renderer().type(), ' Dump:', lyr.renderer().dump())
        # Print the labels on the screen
        label_settings = QgsPalLayerSettings()
        label_settings.drawLabels = True
        label_settings.fieldName = 'Label'
        label_settings.enabled = True
        label_settings.placement = QgsPalLayerSettings.Line
        text_format = QgsTextFormat()
        font_set = QFont("Bavaria")
        font_set.setPointSize(12);
        font_set.setWeight(QFont.Bold);

        text_format.setFont(font_set)
        text_format.setSize(8)
        text_format.setColor(QColor(155, 155, 155, 255))
        label_settings.setFormat(text_format)
        lyr.setLabeling(QgsVectorLayerSimpleLabeling(label_settings))
        lyr.setLabelsEnabled(True)
        self.vectorLayers.append(lyr)

    def addRasterLayer(self, fn, mapType=None, Tag='', srcEpsg=None, overwrite=False):
        if (not os.path.exists(fn)):
            print('No file at ' + fn + ' exists.... no map being added')
            return
        lyr = QgsRasterLayer(fn, Tag)
        if (mapType == mapTypes.Terrain):
            lyr.loadNamedStyle('styles/blankTerrain.qml')
        elif (mapType == mapTypes.Obstacle):
            lyr.loadNamedStyle('styles/ObstacleFree.qml')
        elif (mapType == mapTypes.Wavefront):
            lyr.loadNamedStyle('styles/WavefrontStyle.qml')
        elif (mapType == mapTypes.Airspace):
            lyr.loadNamedStyle('styles/AirspaceStyle.qml')
        elif (mapType == mapTypes.VectorField):
            lyr.loadNamedStyle('styles/VectorFieldStyle.qml')
        elif (mapType == mapTypes.RiskMap):
            lyr.loadNamedStyle('styles/RiskMapStyle.qml')
        elif (mapType == mapTypes.NewRiskEqn):
            lyr.loadNamedStyle('styles/newRiskEqn.qml')
        elif (mapType == mapTypes.Slope):
            lyr.loadNamedStyle('styles/slopeMap.qml')
        elif (mapType == mapTypes.Population):
            lyr.loadNamedStyle('styles/population.qml')
        elif (mapType == mapTypes.landingComposite):
            lyr.loadNamedStyle('styles/landingComposite.qml')
        # elif (mapType == mapTypes.RiskMap):
        #     lyr.loadNamedStyle('styles/CostMapTemplate.qml')
        #lyr.loadNamedStyle('styles/NormMode.qml')
        #lyr.loadNamedStyle('styles/testStyle.qml')
        if len(self.rasterLayers) == 0:
            self.home_extent = lyr.extent()
            self.canvas.setExtent(self.home_extent)
            self.canvas.refresh()
        else:
            self.home_extent.combineExtentWith(lyr.extent())
            self.canvas.setExtent(self.home_extent)
            self.canvas.refresh()
        self.rasterLayers.append(lyr)
        lyr = QgsRasterLayer(fn, Tag+'Hill')
        self.setRenderHillshade(layer=lyr, zf=8)
        self.hillLayers.append(lyr)
        self.mapInfos.append(mapTypes(itemType=mapType, itemName=Tag, filename=fn))
        self.rasterCounter+=1
        self.currentRasterLayer = len(self.rasterLayers)-1
        self.canvas.setLayers(self.returnLayerList())

    def buildCanvas(self):
        self.canvas = QgsMapCanvas()
        self.canvas.enableAntiAliasing(True)
        self.canvas.setCanvasColor(Qt.black)
        self.home_extent = self.backGroundLayer.extent()
        self.canvas.setExtent(self.home_extent)
        self.backOn = True
        self.latlonOn = True
        self.canvas.setLayers(self.returnLayerList())
        self.setCentralWidget(self.canvas)

    def returnLayerList(self):
        LayerList = []

        if self.backOn == True and self.labelsOn == True:
            LayerList.append(self.foreGroundLayer)
        for lyr in self.vectorLayers:
            LayerList.append(lyr)
        if self.rastersOn:
            if self.allRasOn:
                for i in range(0,len(self.rasterLayers)):
                    print('Showing raster tagged ' + self.mapInfos[i].mapName)
                    if self.layerhillshade is True:
                        LayerList.append(self.hillLayers[i])
                    LayerList.append(self.rasterLayers[i])
            elif len(self.rasterLayers) > self.currentRasterLayer and self.rasterCounter >= 0:
                print('Showing raster tagged ' + self.mapInfos[self.currentRasterLayer].mapName)
                if self.layerhillshade is True:
                     LayerList.append(self.hillLayers[self.currentRasterLayer])
                LayerList.append(self.rasterLayers[self.currentRasterLayer])

        if self.backOn == True:
            LayerList.append(self.backGroundLayer)
        return LayerList
    
    def setRenderHillshade(self, layer, zf):  # set render type to 'hillshade'
        zfNew = zf# * 24.74 / layer.rasterUnitsPerPixelX()
        newAlt = 10 * 24.74 / (layer.rasterUnitsPerPixelX() * layer.rasterUnitsPerPixelY())
        # if(newAlt < 2):
        #     newAlt = .1
        r = QgsHillshadeRenderer(layer.dataProvider(), 1, 180, newAlt)
        print('Raster units = ' + str(layer.rasterUnitsPerPixelX()))
        print('New zf = ' + str(zfNew) + '  New Alt ' + str(newAlt))
        r.setZFactor(zfNew)
        layer.setRenderer(r)
        layer.setBlendMode(QPainter.CompositionMode_Multiply)

    def saveJPG(self):
        
        jpgFile = QFileDialog.getSaveFileName(self, 'Save Image As',
                                                r'C:\0-Data\0-GeneratedData',
                                                "jpg Files (*.jpg)")
        if (jpgFile[0] == ''):
            print('Select File in the correct way right now we have <' + jpgFile[0] + '>')
            return
        tmpFile = os.path.splitext(jpgFile[0])[0] + '_tmp.jpg'
        self.canvas.saveAsImage(tmpFile)
        lowRes = Image.open(tmpFile)
        lowRes_rgb = lowRes.convert('RGB')
        lowRes_rgb.save(jpgFile[0], "JPEG", optimize=True, quality=90)

        print('Canvas Image Saved at <' + jpgFile[0] + '>')
        if os.path.exists(tmpFile):
            os.remove(tmpFile)
        jgwFile = os.path.splitext(jpgFile[0])[0] + '_tmp.jgw'
        if os.path.exists(jgwFile):
            os.remove(jgwFile)

    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)

    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)

    def pan(self):
        self.canvas.setMapTool(self.toolPan)

    def home(self):
        self.canvas.setExtent(self.home_extent)
        self.canvas.refresh()
         
if __name__ == "__main__":

    QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis", True)
    qgs = QgsApplication([], True)
    qgs.initQgis()
    mp = mapViewerWindow()
    mp.addRasterLayer(
        fn=r'D:/0-SourceData/Landcover/nlcd_2019_land_cover/nlcd_2019_land_cover_l48_20210604.img',
        Tag='Landcover', mapType=mapTypes.Default)
    # mp.addRasterLayer(
    #     fn=r'../maps/rasterMaps/reproj-TDM1_DEM__30_N47E008_DEM_OrigVect.tif',
    #     Tag='OrigVect', mapType=mapTypes.Terrain)


    mp.show()
    qgs.exec_()