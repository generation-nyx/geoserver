# swagger_client.GwcMassTruncateApi

All URIs are relative to *http://geoserver:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**masstruncate_get**](GwcMassTruncateApi.md#masstruncate_get) | **GET** /masstruncate | Returns available request types for truncation
[**masstruncate_post**](GwcMassTruncateApi.md#masstruncate_post) | **POST** /masstruncate | Issue a mass truncate request


# **masstruncate_get**
> masstruncate_get()

Returns available request types for truncation

Returns xml containing the request type capabilities for mass truncation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcMassTruncateApi()

try:
    # Returns available request types for truncation
    api_instance.masstruncate_get()
except ApiException as e:
    print("Exception when calling GwcMassTruncateApi->masstruncate_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **masstruncate_post**
> masstruncate_post(request_type, layer=layer)

Issue a mass truncate request

Issues a mass truncate request based on the request type parameter. truncateLayer, will clear all caches associated with a named layer, including all permutations of gridset, parameter filter values, and image formats.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcMassTruncateApi()
request_type = 'request_type_example' # str | The requestType parameter is used to control which cached tiles to truncate.
layer = 'layer_example' # str | The layername to truncate (optional)

try:
    # Issue a mass truncate request
    api_instance.masstruncate_post(request_type, layer=layer)
except ApiException as e:
    print("Exception when calling GwcMassTruncateApi->masstruncate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_type** | **str**| The requestType parameter is used to control which cached tiles to truncate. | 
 **layer** | **str**| The layername to truncate | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

