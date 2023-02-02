<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" minScale="1e+08" version="3.10.2-A Coruña" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <rasterrenderer classificationMax="nan" classificationMin="nan" band="1" alphaBand="-1" opacity="1" type="singlebandpseudocolor">
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader classificationMode="1" clip="0" colorRampType="DISCRETE">
          <item color="#000000" label="" alpha="255" value="0.0"/>
          <item color="#00FF00" label="" alpha="255" value="1.0"/>
          <item color="#FFFF00" label="" alpha="255" value="3.0"/>
          <item color="#FF0000" label="" alpha="255" value="9.0"/>
          <item color="#800080" label="" alpha="255" value="10.0"/>
          <item color="#800080" label="" alpha="255" value="14.9"/>
          <item color="#FFFFFF" label="" alpha="255" value="15.0"/>
          <item color="#FFFFFF" label="" alpha="255" value="200.0"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeBlue="128" colorizeRed="255" colorizeGreen="128" colorizeStrength="100" saturation="0" grayscaleMode="0" colorizeOn="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
