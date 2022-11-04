import mapViewerWindow as mvw
from qgis.core import QgsVectorLayer, QgsMarkerSymbol, QgsLineSymbol, \
                      QgsSingleSymbolRenderer, QgsWkbTypes, QgsPalLayerSettings, \
                      QgsTextFormat, QgsVectorLayerSimpleLabeling
from PyQt5.QtGui import QColor, QFont


class vectorLayer:
    def __init__(self, filename, maptype, name) -> None:
        self.filename = filename
        self.maptype = maptype
        self.name = name
        
    def buildLatLonLyr(self, color='155, 155, 155, 255', linestyle='dot', width=.45):
        self.lyr = QgsVectorLayer(self.filename, "Lat Lon Lines")
        lineSymbol = QgsLineSymbol.createSimple(
            {"color": color, "line_style": linestyle, "width": str(width)}
        )
        self.lyr.renderer().setSymbol(lineSymbol)
        # print(lyr.renderer().symbol().symbolLayers()[0].properties())
        # print("Type:", lyr.renderer().type(), " Dump:", lyr.renderer().dump())
        # Print the labels on the screen
        label_settings = QgsPalLayerSettings()
        label_settings.drawLabels = True
        label_settings.fieldName = "Label"
        label_settings.enabled = True
        label_settings.placement = QgsPalLayerSettings.Line
        text_format = QgsTextFormat()
        font_set = QFont("Bavaria")
        font_set.setPointSize(12)
        font_set.setWeight(QFont.Bold)

        text_format.setFont(font_set)
        text_format.setSize(8)
        clrs = [int(s) for s in color.split(',')]
        text_format.setColor(QColor(clrs[0], clrs[1], clrs[2], clrs[3]))
        label_settings.setFormat(text_format)
        self.lyr.setLabeling(QgsVectorLayerSimpleLabeling(label_settings))
        self.lyr.setLabelsEnabled(True)
        
    def buildUserLyr(self, color='255,0,0,255', linestyle='dot', size=4, width=.45):
        self.lyr = QgsVectorLayer(self.filename, self.name)
        if (self.lyr.hasFeatures() == 0):
            return
        features = self.lyr.getFeatures()
        for feature in features:
            print(feature.geometry().type())
            #print(QgsWkbTypes.LineGeometry)
            if(feature.geometry().type() == QgsWkbTypes.PointGeometry):
                type='Point'
                break
            elif(feature.geometry().type() == QgsWkbTypes.LineGeometry):
                type='Line'
                break
            else:
                type='Undef'
        if(type == 'Point'):
            sym1 = QgsMarkerSymbol.createSimple(
                {"color": color, "size": str(size), "outline_style": "no"}
            )
            self.lyr.setRenderer(QgsSingleSymbolRenderer(sym1))
        elif(type == 'Line'):
            width = .1 * size
            lineSymbol = QgsLineSymbol.createSimple(
                {"color": color, "line_style": linestyle, "width": str(width)}
            )
            self.lyr.renderer().setSymbol(lineSymbol)
        #print(self.lyr.renderer().symbol().symbolLayers()[0].properties())
        #print("Type:", self.lyr.renderer().type(), " Dump:", self.lyr.renderer().dump())
