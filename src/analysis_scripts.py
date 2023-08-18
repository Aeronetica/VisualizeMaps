from qgis.core import *
from mapViewerWindow import mapViewerWindow
import os
from mapViewerWindow import mapTypes


def analyze_c182_strips(base_fldr: str, file_key: str, file_pos_id: str):
    QgsApplication.setPrefixPath("C:\\OSGeo4W\\apps\\qgis", True)
    qgs = QgsApplication([], True)
    qgs.initQgis()
    mp = mapViewerWindow()
    mp.loadDefaultLyrs()
    print(os.getcwd())

    mp.addRasterLayer(
        fn=os.path.join(base_fldr, f"{file_key}_risk_{file_pos_id}_viz.tif"),
        Tag="total risk",
        mapType=mapTypes.RiskMapTransparent,
    )
    mp.addRasterLayer(
        fn=os.path.join(base_fldr, f"{file_key}_slope_risk_{file_pos_id}_viz.tif"),
        Tag="slope risk",
        mapType=mapTypes.RiskMapTransparent,
    )
    mp.addRasterLayer(
        fn=os.path.join(base_fldr, f"{file_key}_landcover_risk_{file_pos_id}_viz.tif"),
        Tag="landcover risk",
        mapType=mapTypes.RiskMapTransparent,
    )
    mp.addRasterLayer(
        fn=os.path.join(base_fldr, f"{file_key}_population_risk_{file_pos_id}_viz.tif"),
        Tag="population risk",
        mapType=mapTypes.RiskMapTransparent,
    )
    mp.addRasterLayer(
        fn=os.path.join(base_fldr, f"{file_key}_lidar_risk_{file_pos_id}_viz.tif"),
        Tag="lidar risk",
        mapType=mapTypes.RiskMapTransparent,
    )

    outfldrs = [os.path.join(base_fldr, r"c182_strips\ShapeFiles")]
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

    mp.show()
    qgs.exec_()
