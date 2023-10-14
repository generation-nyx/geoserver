# Layer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the layer. | [optional] 
**enabled** | **bool** | Indicates whether tile caching is enabled for this layer. | [optional] 
**in_memory_cached** | **bool** | Determines if the layer is cached. | [optional] 
**name** | **str** | The name of the layer. | [optional] 
**mime_formats** | **list[str]** | List of formats to be supported (ie. img/jpeg...). | [optional] 
**grid_subsets** | [**LayerGridSubsets**](LayerGridSubsets.md) |  | [optional] 
**meta_width_height** | **int** | The metatiling factors used for this layer. | [optional] 
**expire_cache** | **int** | How old the tile may be before it is refetched from the backend. | [optional] 
**expire_clients** | **int** | The HTTP expiration header sent to client. | [optional] 
**parameter_filters** | **object** | A list of parameter filters, meaning parameters the client may specify that GWC will forward to the backend. | [optional] 
**gutter** | **int** | The gutter is a buffer around the image that is sliced away when saving the tiles to disk. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


