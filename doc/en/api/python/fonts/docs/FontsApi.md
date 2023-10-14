# swagger_client.FontsApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_fonts**](FontsApi.md#delete_fonts) | **DELETE** /fonts | 
[**get_fonts**](FontsApi.md#get_fonts) | **GET** /fonts | Get a list of fonts
[**post_fonts**](FontsApi.md#post_fonts) | **POST** /fonts | 
[**put_fonts**](FontsApi.md#put_fonts) | **PUT** /fonts | 


# **delete_fonts**
> delete_fonts()



Invalid. Fonts cannot be deleted through the REST API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FontsApi()

try:
    api_instance.delete_fonts()
except ApiException as e:
    print("Exception when calling FontsApi->delete_fonts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fonts**
> FontList get_fonts()

Get a list of fonts

Displays a list of all fonts on the server. You must use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/fonts.xml\" for XML)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FontsApi()

try:
    # Get a list of fonts
    api_response = api_instance.get_fonts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FontsApi->get_fonts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FontList**](FontList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_fonts**
> post_fonts()



Invalid. Fonts cannot be added through the REST API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FontsApi()

try:
    api_instance.post_fonts()
except ApiException as e:
    print("Exception when calling FontsApi->post_fonts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_fonts**
> put_fonts()



Invalid. Fonts cannot be updated through the REST API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FontsApi()

try:
    api_instance.put_fonts()
except ApiException as e:
    print("Exception when calling FontsApi->put_fonts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

