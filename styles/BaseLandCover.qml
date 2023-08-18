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
        <colorrampshader classificationMode="1" clip="0" colorRampType="INTERPOLATED">
          <item color="#000000" label="undefined" alpha="0" value="0"/>
          <item color="#0000FF" label="Open Water" alpha="255" value="11"/>
          <item color="#FFFFFF" label="Perinnial Ice/snow" alpha="255" value="12"/>
          <item color="#FFCCCC" label="Developed, Open Space" alpha="255" value="21"/>
          <item color="#FF9999" label="Developed Low Intensity" alpha="255" value="22"/>
          <item color="#FF5555" label="Developed Med Intensity" alpha="255" value="23"/>
          <item color="#FF0000" label="Developed High Intensity" alpha="255" value="24"/>
          <item color="#F0E68C" label="Barren Land" alpha="255" value="31"/>
          <item color="#008000" label="Deciduous Forest" alpha="255" value="41"/>
          <item color="#006400" label="Evergreen Forest" alpha="255" value="42"/>
          <item color="#228B22" label="Mixed Forest" alpha="255" value="43"/>
          <item color="#9ACD32" label="Dwarf Scrub" alpha="255" value="51"/>
          <item color="#90EE90" label="Shrub/Scrub" alpha="255" value="52"/>
          <item color="#7CFC00" label="Grassland/Herbaceous" alpha="255" value="71"/>
          <item color="#90EE90" label="Sedge/Herbaceous" alpha="255" value="72"/>
          <item color="#98FB98" label="Lichens" alpha="255" value="73"/>
          <item color="#3CB371" label="Moss" alpha="255" value="74"/>
          <item color="#CCCC00" label="Pasture/Hay" alpha="255" value="81"/>
          <item color="#ADFF2F" label="Cultivated Crops" alpha="255" value="82"/>
          <item color="#556B2F" label="Woody Wetlands" alpha="255" value="90"/>
          <item color="#6B8E23" label="Emegent Herb Wetlands" alpha="255" value="95"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeBlue="128" colorizeRed="255" colorizeGreen="128" colorizeStrength="100" saturation="0" grayscaleMode="0" colorizeOn="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
