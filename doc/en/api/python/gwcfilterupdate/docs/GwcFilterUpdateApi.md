# swagger_client.GwcFilterUpdateApi

All URIs are relative to *http://geoserver:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_update_post**](GwcFilterUpdateApi.md#filter_update_post) | **POST** /filter/{filterName}/update/{updateType} | Updates a given layer filter by way of xml or zip file.


# **filter_update_post**
> filter_update_post(filter_name, update_type, request_body)

Updates a given layer filter by way of xml or zip file.

Restfully updates the given filterName with parameters provided in the xml or zip

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcFilterUpdateApi()
filter_name = 'filter_name_example' # str | The name of the filter to update.
update_type = 'update_type_example' # str | One of 'zip' or 'xml'
request_body = swagger_client.RequestFilterUpdate() # RequestFilterUpdate | The parameters that are accepted by a given filter.

try:
    # Updates a given layer filter by way of xml or zip file.
    api_instance.filter_update_post(filter_name, update_type, request_body)
except ApiException as e:
    print("Exception when calling GwcFilterUpdateApi->filter_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| The name of the filter to update. | 
 **update_type** | **str**| One of &#39;zip&#39; or &#39;xml&#39; | 
 **request_body** | [**RequestFilterUpdate**](RequestFilterUpdate.md)| The parameters that are accepted by a given filter. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/zip
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

