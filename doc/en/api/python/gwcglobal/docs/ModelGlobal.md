# ModelGlobal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_information** | [**ServiceInformation**](ServiceInformation.md) |  | [optional] 
**runtime_stats_enabled** | **bool** | Whether runtime statistics are being gathered. Runtime statistics run, by default, every three second and provide data about how many requests the system has been serving in the past 3, 15 and 60 seconds, as well as aggregate numbers. | [optional] 
**wmts_cite_compliant** | **bool** | Whether the server is running in WMTS strict compliance mode. | [optional] 
**backend_timeout** | **int** | The number of seconds GWC will wait for a backend server to return something before closing the connection. | [optional] 
**version** | **str** | The GeoWebCache version. Read-only. | [optional] 
**identifier** | **str** | The unique identifier for this global server configuration. Read-only. | [optional] 
**location** | **str** | The location of this configuration. Read-only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


