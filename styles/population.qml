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
          <item color="#00FF00" label="" alpha="0" value="0"/>
          <item color="#FFFFAA" label="" alpha="150" value="5"/>
          <item color="#FFE200" label="" alpha="150" value="25"/>
          <item color="#FFF300" label="" alpha="150" value="50"/>
          <item color="#FFBF00" label="" alpha="150" value="100"/>
          <item color="#FF6A00" label="" alpha="150" value="500"/>
          <item color="#FF0800" label="" alpha="150" value="2500"/>
          <item color="#CA0000" label="" alpha="150" value="5000"/>
          <item color="#68330034" label="" alpha="150" value="50000"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeBlue="128" colorizeRed="255" colorizeGreen="128" colorizeStrength="100" saturation="0" grayscaleMode="0" colorizeOn="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
