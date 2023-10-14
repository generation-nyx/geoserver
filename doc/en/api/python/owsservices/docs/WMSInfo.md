# WMSInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Status of the service | [optional] 
**name** | **str** | Name of the service. This value is unique among all instances of ServiceInfo and can be used as an identifier. | [optional] 
**title** | **str** | Title of the service | [optional] 
**workspace** | **str** | Workspace the service is specific or local to. Will not exist if the service is global. | [optional] 
**maintainer** | **str** | maintainer of the service | [optional] 
**abstrct** | **str** | description of the service | [optional] 
**access_constraints** | **str** |  | [optional] 
**fees** | **str** |  | [optional] 
**versions** | [**WMSInfoVersions**](WMSInfoVersions.md) |  | [optional] 
**keywords** | **list[str]** | Keywords associated with the service. | [optional] 
**cite_compliant** | **bool** | Status of service CITE compliance. | [optional] 
**online_resource** | **str** |  | [optional] 
**schema_base_url** | **str** | The base url for the schemas describing the service. | [optional] 
**verbose** | **bool** | Flag indicating if the service should be verbose or not. | [optional] 
**metadata_link** | [**list[WMSInfoMetadataLink]**](WMSInfoMetadataLink.md) |  | [optional] 
**watermark** | [**WMSInfoWatermark**](WMSInfoWatermark.md) |  | [optional] 
**interpolation** | **str** |  | [optional] 
**get_feature_info_mime_type_checking_enabled** | **bool** | Flag indicating if getFeatureInfo MIME type checking is enabled | [optional] 
**get_map_mime_type_checking_enabled** | **bool** | Flag indicating if getMap MIME type checking is enabled. | [optional] 
**dynamic_styling_disabled** | **bool** | status of dynamic styling (SLD and SLD_BODY params) allowance | [optional] 
**max_buffer** | **int** | Maximum search radius for GetFeatureInfo | [optional] 
**max_request_memory** | **int** | Max amount of memory, in kilobytes, that each WMS request can allocate (each output format will make a best effort attempt to respect it, but there are no guarantees). 0 indicates no limit. | [optional] 
**max_rendering_time** | **int** | Max time, in seconds, a WMS request is allowed to spend rendering the map. Various output formats will do a best effort to respect it (raster formats, for example, will account just rendering time, but not image encoding time). | [optional] 
**max_rendering_errors** | **int** | Max number of rendering errors that will be tolerated before stating the rendering operation failed by throwing a service exception back to the client | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


