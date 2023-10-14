# swagger_client.LoggingApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logging**](LoggingApi.md#get_logging) | **GET** /logging | Get logging configuration of GeoServer
[**put_logging**](LoggingApi.md#put_logging) | **PUT** /logging | Update logging


# **get_logging**
> Logging get_logging()

Get logging configuration of GeoServer

Displays a list of all logging settings on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/logging.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoggingApi()

try:
    # Get logging configuration of GeoServer
    api_response = api_instance.get_logging()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggingApi->get_logging: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Logging**](Logging.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_logging**
> put_logging(logging_body)

Update logging

Updates logging settings on the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoggingApi()
logging_body = swagger_client.Logging() # Logging | The logging information to upload.

try:
    # Update logging
    api_instance.put_logging(logging_body)
except ApiException as e:
    print("Exception when calling LoggingApi->put_logging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logging_body** | [**Logging**](Logging.md)| The logging information to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

