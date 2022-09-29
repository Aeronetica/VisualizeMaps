<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" version="3.10.2-A Coruña" minScale="1e+08" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property key="WMSBackgroundLayer" value="false"/>
    <property key="WMSPublishDataSourceUrl" value="false"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <rasterrenderer alphaBand="-1" classificationMax="61" type="singlebandpseudocolor" classificationMin="-47" band="1" opacity="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader colorRampType="INTERPOLATED" classificationMode="1" clip="0">
          <colorramp name="[source]" type="gradient">
            <prop k="color1" v="0,0,4,255"/>
            <prop k="color2" v="252,255,164,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.0196078;2,2,12,255:0.0392157;5,4,23,255:0.0588235;10,7,34,255:0.0784314;16,9,45,255:0.0980392;22,11,57,255:0.117647;30,12,69,255:0.137255;38,12,81,255:0.156863;47,10,91,255:0.176471;56,9,98,255:0.196078;64,10,103,255:0.215686;73,11,106,255:0.235294;81,14,108,255:0.254902;89,16,110,255:0.27451;97,19,110,255:0.294118;105,22,110,255:0.313725;113,25,110,255:0.333333;120,28,109,255:0.352941;128,31,108,255:0.372549;136,34,106,255:0.392157;144,37,104,255:0.411765;152,39,102,255:0.431373;160,42,99,255:0.45098;168,46,95,255:0.470588;176,49,91,255:0.490196;183,53,87,255:0.509804;191,57,82,255:0.529412;198,61,77,255:0.54902;204,66,72,255:0.568627;211,71,67,255:0.588235;217,77,61,255:0.607843;223,83,55,255:0.627451;228,90,49,255:0.647059;233,97,43,255:0.666667;237,105,37,255:0.686275;241,113,31,255:0.705882;244,121,24,255:0.72549;247,130,18,255:0.745098;249,139,11,255:0.764706;250,148,7,255:0.784314;251,157,7,255:0.803922;252,166,12,255:0.823529;252,176,20,255:0.843137;251,186,31,255:0.862745;250,196,42,255:0.882353;248,205,55,255:0.901961;246,215,70,255:0.921569;244,225,86,255:0.941176;242,234,105,255:0.960784;242,242,125,255:0.980392;245,249,146,255"/>
          </colorramp>
          <item label="-47" alpha="178" value="-47" color="#ff011a"/>
          <item label="-46.9" alpha="128" value="-46.9" color="#f97f04"/>
          <item label="-10" alpha="125" value="-10" color="#f5e906"/>
          <item label="-9.9" alpha="0" value="-9.9" color="#ff00ff"/>
          <item label="60.9" alpha="0" value="60.9" color="#80cdc1"/>
          <item label="61" alpha="255" value="61" color="#0734ff"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeRed="255" colorizeStrength="100" saturation="0" grayscaleMode="0" colorizeGreen="128" colorizeOn="0" colorizeBlue="128"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
