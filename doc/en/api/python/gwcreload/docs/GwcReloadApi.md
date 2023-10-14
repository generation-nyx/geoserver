# swagger_client.GwcReloadApi

All URIs are relative to *http://geoserver:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reload_post**](GwcReloadApi.md#reload_post) | **POST** /reload | Reloads GWC settings/


# **reload_post**
> reload_post(configuration_name=configuration_name)

Reloads GWC settings/

Reloads the GeoWebCache settings after making changes to the configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcReloadApi()
configuration_name = 'configuration_name_example' # str | The string value of the configuration ie. \"reload_configuration=1\" (optional)

try:
    # Reloads GWC settings/
    api_instance.reload_post(configuration_name=configuration_name)
except ApiException as e:
    print("Exception when calling GwcReloadApi->reload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_name** | **str**| The string value of the configuration ie. \&quot;reload_configuration&#x3D;1\&quot; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

