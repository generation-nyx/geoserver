# swagger_client.SystemStatusApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_monitor_requests**](SystemStatusApi.md#get_monitor_requests) | **GET** /about/system-status | Get a list of requests


# **get_monitor_requests**
> Metrics get_monitor_requests()

Get a list of requests

Returns a list of system-level information. Major operating systems (Linux, Windows and MacOX) are supported out of the box. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemStatusApi()

try:
    # Get a list of requests
    api_response = api_instance.get_monitor_requests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemStatusApi->get_monitor_requests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Metrics**](Metrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

