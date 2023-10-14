# Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | **str** | Requested bounding box | [optional] 
**body_as_string** | **str** | Body of the request (for POST/PUT) | [optional] 
**body_content_length** | **int** | Request body content lenght | [optional] 
**body_content_type** | **str** | Request body content type | [optional] 
**category** | **str** | Can be OWS or REST | [optional] 
**end_time** | **str** | Request completion time | [optional] 
**error_message** | **str** | The error message, in case the request failed, empt otherwise | [optional] 
**host** | **str** | Host GeoServer is running on | [optional] 
**http_method** | **str** | HTTP method of the request (e.g., GET, POST, ...) | [optional] 
**http_referer** | **str** | HTTP referrer, if any | [optional] 
**id** | **str** | Request identifier | [optional] 
**internal_host** | **str** | Name of the host GeoServer is running on | [optional] 
**operation** | **str** | OGC operation, e.g. GetMap, GetFeature (available only for OWS requests) | [optional] 
**ows_version** | **str** | OGC protocol version (e.g., 1.1.0, 1.1.3) | [optional] 
**path** | **str** | HTTP request path (e.g. \&quot;/topp/wms\&quot;) | [optional] 
**query_string** | **str** | The HTTP request query string | [optional] 
**remote_addr** | **str** | Remote request IP address | [optional] 
**remote_city** | **str** | Remote client city (available only if GeoIP lookup is enabled) | [optional] 
**remote_country** | **str** | Remote client country (available only if GeoIP lookup is enabled) | [optional] 
**remote_host** | **str** | Remote client  host | [optional] 
**remote_lat** | **str** | Remote client latitude (available only if GeoIP lookup is enabled) | [optional] 
**remote_lon** | **str** | Remote client longitude (available only if GeoIP lookup is enabled) | [optional] 
**remote_user** | **str** | User issuing the request | [optional] 
**remote_user_agent** | **str** | Remote client user agent | [optional] 
**resources** | **str** | Name of the resources (layers, processes, ...) specified as part of the request | [optional] 
**resources_list** | **str** | Name of the resources (layers, processes, ...) specified as part of the request | [optional] 
**response_content_type** | **str** | Content type of the response | [optional] 
**response_length** | **int** | Size of the response in bytes | [optional] 
**response_status** | **str** | HTTP status of the response | [optional] 
**service** | **str** | OGC service in use (available only for OGC requests) | [optional] 
**start_time** | **str** | Request start time | [optional] 
**status** | **str** | Status of the request (WAITING, RUNNING, CANCELLING, FAILED, FINISHED, CANCELLED, INTERRUPTED) | [optional] 
**sub_operation** | **str** | The OGC sub operations, for the cases in which it applies (e.g., for WFS-T it can be Insert/Delete/Update) | [optional] 
**total_time** | **int** | Total request time in milliseconds | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


