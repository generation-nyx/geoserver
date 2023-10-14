# swagger_client.GwcMemoryCacheStatisticsApi

All URIs are relative to *http://geoserver:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_get**](GwcMemoryCacheStatisticsApi.md#statistics_get) | **GET** /statistics | Returns XML or JSON response with memory cache statistics


# **statistics_get**
> statistics_get()

Returns XML or JSON response with memory cache statistics

When appended with .json or .xml will respond with memory caches statistics in the requested format if the blobstore used is an instance of MemoryBlobStore.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcMemoryCacheStatisticsApi()

try:
    # Returns XML or JSON response with memory cache statistics
    api_instance.statistics_get()
except ApiException as e:
    print("Exception when calling GwcMemoryCacheStatisticsApi->statistics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

