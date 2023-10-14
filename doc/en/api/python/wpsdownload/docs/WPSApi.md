# swagger_client.WPSApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_download_service_configuration**](WPSApi.md#get_download_service_configuration) | **GET** /services/wps/download | 
[**get_download_service_configuration_0**](WPSApi.md#get_download_service_configuration_0) | **PUT** /services/wps/download | 


# **get_download_service_configuration**
> DownloadServiceConfiguration get_download_service_configuration()



Retrieves the WPS Download configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WPSApi()

try:
    api_response = api_instance.get_download_service_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WPSApi->get_download_service_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DownloadServiceConfiguration**](DownloadServiceConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_service_configuration_0**
> get_download_service_configuration_0(get_download_service_configuration_body)



Retrieves the WPS Download configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WPSApi()
get_download_service_configuration_body = swagger_client.DownloadServiceConfiguration() # DownloadServiceConfiguration | Body of the WPS download configuration

try:
    api_instance.get_download_service_configuration_0(get_download_service_configuration_body)
except ApiException as e:
    print("Exception when calling WPSApi->get_download_service_configuration_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_download_service_configuration_body** | [**DownloadServiceConfiguration**](DownloadServiceConfiguration.md)| Body of the WPS download configuration | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

