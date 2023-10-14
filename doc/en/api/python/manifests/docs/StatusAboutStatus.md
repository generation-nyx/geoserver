# StatusAboutStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** | Module identifier based on artifact bundle. For example, gs-main, gs-oracle.  | [optional] 
**name** | **str** | Human readable name (from GeoServer documentation), or as defined in the extension pom.xml.  | [optional] 
**component** | **str** | Optional component identifier within module. For example, rendering-engine.  | [optional] 
**version** | **str** | Human readable version, ie. for geotools it would be 15-SNAPSHOT  | [optional] 
**message** | **str** | Optional status message such as what Java rendering engine is in use, or the library path if the module/driver is unavailable  | [optional] 
**is_enabled** | **bool** | Returns whether the module is enabled in the current GeoServer configuration.  | [optional] 
**is_available** | **bool** | Returns whether the module is available to GeoServer  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


