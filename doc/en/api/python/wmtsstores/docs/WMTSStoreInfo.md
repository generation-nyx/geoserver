# WMTSStoreInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the WMTS store | [optional] 
**description** | **str** | Description of the WMTS store | [optional] 
**type** | **str** | Type of store. Set to WMTS. | [optional] 
**enabled** | **bool** | Whether the store is enabled | [optional] 
**workspace** | [**WMTSStoreInfoWorkspace**](WMTSStoreInfoWorkspace.md) |  | [optional] 
**metadata** | [**WMTSStoreInfoMetadata**](WMTSStoreInfoMetadata.md) |  | [optional] 
**default__** | **bool** | Whether the store is the default store of the workspace | [optional] 
**capabilities_url** | **str** | Location of the WMTS capabilities URL where the store originates | [optional] 
**user** | **str** | User name to use when connecting to the remote WMTS | [optional] 
**password** | **str** | Password or hash to use when connecting to the remote WMTS | [optional] 
**max_connections** | **float** | Maximum number of simultaneous connections to use | [optional] 
**read_timeout** | **str** | Time in seconds before read time out | [optional] 
**connect_timeout** | **str** | Time in seconds before connection time out | [optional] 
**wmts_layers** | [**list[WMTSStoreInfoWmtsLayers]**](WMTSStoreInfoWmtsLayers.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


