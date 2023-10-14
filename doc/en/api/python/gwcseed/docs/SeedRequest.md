# SeedRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the layer to seed, reseed, or truncate. | [optional] 
**bounds** | [**SeedRequestBounds**](SeedRequestBounds.md) |  | [optional] 
**grid_set_id** | **str** | The projection used for the layer. | [optional] 
**zoom_start** | **int** | The zoom level to start seeding. | [optional] 
**zoom_stop** | **int** | The zoom level to stop seeding. | [optional] 
**type** | **str** | Type can be seed (add tiles), reseed (replace tiles), or truncate (remove tiles). | [optional] 
**thread_count** | **int** | Number of seeding threads to run in parallel. If type is truncate only one thread will be used regardless of this parameter. | [optional] 
**parameters** | [**SeedRequestParameters**](SeedRequestParameters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


