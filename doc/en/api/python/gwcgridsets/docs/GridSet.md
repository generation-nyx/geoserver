# GridSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the gridset. Should be unique. | [optional] 
**description** | **str** | Description of the gridset | [optional] 
**srs** | [**GridSetSrs**](GridSetSrs.md) |  | [optional] 
**extent** | [**GridSetExtent**](GridSetExtent.md) |  | [optional] 
**align_top_left** | **bool** | Whether the y-coordinate of the tile origin is at the top (true) or bottom (false). | [optional] [default to False]
**resolutions** | [**GridSetResolutions**](GridSetResolutions.md) |  | [optional] 
**meters_per_unit** | **float** | The number of meters per coordinate unit. | [optional] 
**pixel_size** | **float** | The assumed pixel size of the display device, in meters. | [optional] 
**scale_names** | [**GridSetScaleNames**](GridSetScaleNames.md) |  | [optional] 
**tile_height** | **int** | The height of a tile in pixels. | [optional] 
**tile_width** | **int** | The width of a tile in pixels. | [optional] 
**y_coordinate_first** | **bool** | By default the coordinates are {x,y}, this flag reverses the output for WMTS getcapabilities. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


