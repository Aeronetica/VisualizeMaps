# from qgis.PyQt.QtWidgets import QFileDialog
# #import qgis._gui.QgsMapCanvas as canvas
# import os
# from PIL import Image

class toolBarActions:
    def __init__(self, description, connectFunction, checkable=True, toolbar=0) -> None:
        self.description = description
        self.connectFunction = connectFunction
        self.checkable = checkable
        self.toolbar = toolbar
    