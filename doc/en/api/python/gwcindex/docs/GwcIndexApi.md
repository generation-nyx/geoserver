# swagger_client.GwcIndexApi

All URIs are relative to *http://geoserver:8080/geoserver/gwc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_get**](GwcIndexApi.md#index_get) | **GET** /rest | Returns the HTML user interface


# **index_get**
> index_get()

Returns the HTML user interface

Returns the HTML for the front facing ui homepage for GeoWebCache.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcIndexApi()

try:
    # Returns the HTML user interface
    api_instance.index_get()
except ApiException as e:
    print("Exception when calling GwcIndexApi->index_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

