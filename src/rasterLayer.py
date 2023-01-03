import mapViewerWindow as mvw
from qgis.core import QgsRasterLayer, QgsHillshadeRenderer
from PyQt5.QtGui import QPainter


class rasterLayer:
    def __init__(self, uri, maptype, name, provider='') -> None:
        self.uri = uri
        self.maptype = maptype
        self.name = name
        if (provider == ''):
            self.lyr = QgsRasterLayer(self.uri, self.name)
        else:
            self.lyr = QgsRasterLayer(self.uri, self.name, provider)
        if maptype == mvw.mapTypes.Terrain:
            self.layer_style = "styles/blankTerrain.qml"
        elif maptype == mvw.mapTypes.Obstacle:
            self.layer_style = "styles/ObstacleFree.qml"
        elif maptype == mvw.mapTypes.Wavefront:
            self.layer_style = "styles/WavefrontStyle.qml"
        elif maptype == mvw.mapTypes.Airspace:
            self.layer_style = "styles/AirspaceStyle.qml"
        elif maptype == mvw.mapTypes.VectorField:
            self.layer_style = "styles/VectorFieldStyle.qml"
        elif maptype == mvw.mapTypes.RiskMap:
            self.layer_style = "styles/RiskMapStyle.qml"
        elif maptype == mvw.mapTypes.NewRiskEqn:
            self.layer_style = "styles/newRiskEqn.qml"
        elif maptype == mvw.mapTypes.Slope:
            self.layer_style = "styles/slopeMap.qml"
        elif maptype == mvw.mapTypes.Population:
            self.layer_style = "styles/population.qml"
        elif maptype == mvw.mapTypes.landingComposite:
            self.layer_style = "styles/landingComposite.qml"
        elif maptype == mvw.mapTypes.landCover:
            self.layer_style = "styles/BaseLandCover.qml"
        elif maptype == mvw.mapTypes.density:
            self.layer_style = "styles/density.qml"
        elif maptype == mvw.mapTypes.utm_5_population:
            self.layer_style = "styles/population_utm_5.qml"
        elif maptype == mvw.mapTypes.Default:
            self.layer_style = "styles/blankTerrain.qml"
        else:
            return
        self.lyr.loadNamedStyle(self.layer_style)
        self.addHillLayer()

    def addHillLayer(self):
        self.hillLyr = QgsRasterLayer(self.uri, self.name + "Hill")
        zf = 8
        zfNew = zf  # * 24.74 / layer.rasterUnitsPerPixelX()
        newAlt = (
            10
            * 24.74
            / (
                self.hillLyr.rasterUnitsPerPixelX()
                * self.hillLyr.rasterUnitsPerPixelY()
            )
        )
        # if(newAlt < 2):
        #     newAlt = .1
        r = QgsHillshadeRenderer(self.hillLyr.dataProvider(), 1, 180, newAlt)
        print("Raster units = " + str(self.hillLyr.rasterUnitsPerPixelX()))
        print("New zf = " + str(zfNew) + "  New Alt " + str(newAlt))
        r.setZFactor(zfNew)
        self.hillLyr.setRenderer(r)
        self.hillLyr.setBlendMode(QPainter.CompositionMode_Multiply)
