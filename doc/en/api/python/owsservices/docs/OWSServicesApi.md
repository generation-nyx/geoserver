# swagger_client.OWSServicesApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_oseo_settings**](OWSServicesApi.md#delete_oseo_settings) | **DELETE** /services/oseo/settings | 
[**delete_wcs_settings**](OWSServicesApi.md#delete_wcs_settings) | **DELETE** /services/wcs/settings | 
[**delete_wcs_workspace_settings**](OWSServicesApi.md#delete_wcs_workspace_settings) | **DELETE** /services/wcs/workspaces/{workspace}/settings | 
[**delete_wfs_settings**](OWSServicesApi.md#delete_wfs_settings) | **DELETE** /services/wfs/settings | 
[**delete_wfs_workspace_settings**](OWSServicesApi.md#delete_wfs_workspace_settings) | **DELETE** /services/wfs/workspaces/{workspace}/settings | 
[**delete_wms_settings**](OWSServicesApi.md#delete_wms_settings) | **DELETE** /services/wms/settings | 
[**delete_wms_workspace_settings**](OWSServicesApi.md#delete_wms_workspace_settings) | **DELETE** /services/wms/workspaces/{workspace}/settings | 
[**delete_wmts_settings**](OWSServicesApi.md#delete_wmts_settings) | **DELETE** /services/wmts/settings | 
[**delete_wmts_workspace_settings**](OWSServicesApi.md#delete_wmts_workspace_settings) | **DELETE** /services/wmts/workspaces/{workspace}/settings | 
[**get_oseo_settings**](OWSServicesApi.md#get_oseo_settings) | **GET** /services/oseo/settings | 
[**get_wcs_settings**](OWSServicesApi.md#get_wcs_settings) | **GET** /services/wcs/settings | 
[**get_wcs_workspace_settings**](OWSServicesApi.md#get_wcs_workspace_settings) | **GET** /services/wcs/workspaces/{workspace}/settings | 
[**get_wfs_settings**](OWSServicesApi.md#get_wfs_settings) | **GET** /services/wfs/settings | 
[**get_wfs_workspace_settings**](OWSServicesApi.md#get_wfs_workspace_settings) | **GET** /services/wfs/workspaces/{workspace}/settings | 
[**get_wms_settings**](OWSServicesApi.md#get_wms_settings) | **GET** /services/wms/settings | 
[**get_wms_workspace_settings**](OWSServicesApi.md#get_wms_workspace_settings) | **GET** /services/wms/workspaces/{workspace}/settings | 
[**get_wmts_settings**](OWSServicesApi.md#get_wmts_settings) | **GET** /services/wmts/settings | 
[**get_wmts_workspace_settings**](OWSServicesApi.md#get_wmts_workspace_settings) | **GET** /services/wmts/workspaces/{workspace}/settings | 
[**post_oseo_settings**](OWSServicesApi.md#post_oseo_settings) | **POST** /services/oseo/settings | 
[**post_wcs_settings**](OWSServicesApi.md#post_wcs_settings) | **POST** /services/wcs/settings | 
[**post_wcs_workspace_settings**](OWSServicesApi.md#post_wcs_workspace_settings) | **POST** /services/wcs/workspaces/{workspace}/settings | 
[**post_wfs_settings**](OWSServicesApi.md#post_wfs_settings) | **POST** /services/wfs/settings | 
[**post_wfs_workspace_settings**](OWSServicesApi.md#post_wfs_workspace_settings) | **POST** /services/wfs/workspaces/{workspace}/settings | 
[**post_wms_settings**](OWSServicesApi.md#post_wms_settings) | **POST** /services/wms/settings | 
[**post_wms_workspace_settings**](OWSServicesApi.md#post_wms_workspace_settings) | **POST** /services/wms/workspaces/{workspace}/settings | 
[**post_wmts_settings**](OWSServicesApi.md#post_wmts_settings) | **POST** /services/wmts/settings | 
[**post_wmts_workspace_settings**](OWSServicesApi.md#post_wmts_workspace_settings) | **POST** /services/wmts/workspaces/{workspace}/settings | 
[**put_oseo_settings**](OWSServicesApi.md#put_oseo_settings) | **PUT** /services/oseo/settings | 
[**put_wcs_settings**](OWSServicesApi.md#put_wcs_settings) | **PUT** /services/wcs/settings | 
[**put_wcs_workspace_settings**](OWSServicesApi.md#put_wcs_workspace_settings) | **PUT** /services/wcs/workspaces/{workspace}/settings | 
[**put_wfs_settings**](OWSServicesApi.md#put_wfs_settings) | **PUT** /services/wfs/settings | 
[**put_wfs_workspace_settings**](OWSServicesApi.md#put_wfs_workspace_settings) | **PUT** /services/wfs/workspaces/{workspace}/settings | 
[**put_wms_settings**](OWSServicesApi.md#put_wms_settings) | **PUT** /services/wms/settings | 
[**put_wms_workspace_settings**](OWSServicesApi.md#put_wms_workspace_settings) | **PUT** /services/wms/workspaces/{workspace}/settings | 
[**put_wmts_settings**](OWSServicesApi.md#put_wmts_settings) | **PUT** /services/wmts/settings | 
[**put_wmts_workspace_settings**](OWSServicesApi.md#put_wmts_workspace_settings) | **PUT** /services/wmts/workspaces/{workspace}/settings | 


# **delete_oseo_settings**
> delete_oseo_settings()



Invalid. Use PUT to edit settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_instance.delete_oseo_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->delete_oseo_settings: %s\n" % e)
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

# **delete_wcs_settings**
> delete_wcs_settings()



Invalid. Use PUT to edit settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_instance.delete_wcs_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->delete_wcs_settings: %s\n" % e)
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

# **delete_wcs_workspace_settings**
> delete_wcs_workspace_settings(workspace)



Deletes a workspace-specific WCS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_wcs_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling OWSServicesApi->delete_wcs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wfs_settings**
> delete_wfs_settings()



Invalid. Use PUT to edit settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_instance.delete_wfs_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->delete_wfs_settings: %s\n" % e)
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

# **delete_wfs_workspace_settings**
> delete_wfs_workspace_settings(workspace)



Deletes a workspace-specific WFS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_wfs_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling OWSServicesApi->delete_wfs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wms_settings**
> delete_wms_settings()



Invalid. Use PUT to edit settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_instance.delete_wms_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->delete_wms_settings: %s\n" % e)
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

# **delete_wms_workspace_settings**
> delete_wms_workspace_settings(workspace)



Deletes a workspace-specific WMS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_wms_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling OWSServicesApi->delete_wms_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wmts_settings**
> delete_wmts_settings()



Invalid. Use PUT to edit settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_instance.delete_wmts_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->delete_wmts_settings: %s\n" % e)
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

# **delete_wmts_workspace_settings**
> delete_wmts_workspace_settings(workspace)



Deletes a workspace-specific WMTS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_wmts_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling OWSServicesApi->delete_wmts_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oseo_settings**
> WFSInfo get_oseo_settings()



Retrieves Open Search for Earth Observation Service settings globally for the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_response = api_instance.get_oseo_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OWSServicesApi->get_oseo_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WFSInfo**](WFSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wcs_settings**
> WCSInfo get_wcs_settings()



Retrieves Web Coverage Service settings globally for the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_response = api_instance.get_wcs_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OWSServicesApi->get_wcs_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WCSInfo**](WCSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wcs_workspace_settings**
> WCSInfo get_wcs_workspace_settings(workspace)



Retrieves Web Coverage Service settings for a given workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_wcs_workspace_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OWSServicesApi->get_wcs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WCSInfo**](WCSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wfs_settings**
> WFSInfo get_wfs_settings()



Retrieves Web Feature Service settings globally for the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_response = api_instance.get_wfs_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OWSServicesApi->get_wfs_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WFSInfo**](WFSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wfs_workspace_settings**
> WFSInfo get_wfs_workspace_settings(workspace)



Retrieves Web Feature Service settings for a given workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_wfs_workspace_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OWSServicesApi->get_wfs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WFSInfo**](WFSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wms_settings**
> WMSInfo get_wms_settings()



Retrieves Web Map Service settings globally for the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_response = api_instance.get_wms_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OWSServicesApi->get_wms_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WMSInfo**](WMSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wms_workspace_settings**
> WMSInfo get_wms_workspace_settings(workspace)



Retrieves Web Map Service settings for a given workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_wms_workspace_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OWSServicesApi->get_wms_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WMSInfo**](WMSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmts_settings**
> WMTSInfo get_wmts_settings()



Retrieves Web Map Tile Service settings globally for the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_response = api_instance.get_wmts_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OWSServicesApi->get_wmts_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WMTSInfo**](WMTSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmts_workspace_settings**
> WMTSInfo get_wmts_workspace_settings(workspace)



Retrieves Web Map Tile Service settings for a given workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_wmts_workspace_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OWSServicesApi->get_wmts_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WMTSInfo**](WMTSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_oseo_settings**
> post_oseo_settings()



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_instance.post_oseo_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->post_oseo_settings: %s\n" % e)
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

# **post_wcs_settings**
> post_wcs_settings()



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_instance.post_wcs_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->post_wcs_settings: %s\n" % e)
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

# **post_wcs_workspace_settings**
> post_wcs_workspace_settings(workspace)



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.post_wcs_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling OWSServicesApi->post_wcs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wfs_settings**
> post_wfs_settings()



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_instance.post_wfs_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->post_wfs_settings: %s\n" % e)
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

# **post_wfs_workspace_settings**
> post_wfs_workspace_settings(workspace)



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.post_wfs_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling OWSServicesApi->post_wfs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wms_settings**
> post_wms_settings()



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_instance.post_wms_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->post_wms_settings: %s\n" % e)
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

# **post_wms_workspace_settings**
> post_wms_workspace_settings(workspace)



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.post_wms_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling OWSServicesApi->post_wms_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wmts_settings**
> post_wmts_settings()



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()

try:
    api_instance.post_wmts_settings()
except ApiException as e:
    print("Exception when calling OWSServicesApi->post_wmts_settings: %s\n" % e)
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

# **post_wmts_workspace_settings**
> post_wmts_workspace_settings(workspace)



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.post_wmts_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling OWSServicesApi->post_wmts_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_oseo_settings**
> put_oseo_settings(oseo_settings_body)



Edits a global OSEO setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
oseo_settings_body = swagger_client.WFSInfo() # WFSInfo | Body of the OSEO settings

try:
    api_instance.put_oseo_settings(oseo_settings_body)
except ApiException as e:
    print("Exception when calling OWSServicesApi->put_oseo_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oseo_settings_body** | [**WFSInfo**](WFSInfo.md)| Body of the OSEO settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wcs_settings**
> put_wcs_settings(wcs_settings_body)



Edits a global WCS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
wcs_settings_body = swagger_client.WCSInfo() # WCSInfo | Body of the WCS settings

try:
    api_instance.put_wcs_settings(wcs_settings_body)
except ApiException as e:
    print("Exception when calling OWSServicesApi->put_wcs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wcs_settings_body** | [**WCSInfo**](WCSInfo.md)| Body of the WCS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wcs_workspace_settings**
> put_wcs_workspace_settings(workspace, wcs_settings_body)



Edits a workspace-specific WCS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name
wcs_settings_body = swagger_client.WCSInfo() # WCSInfo | Body of the WCS settings

try:
    api_instance.put_wcs_workspace_settings(workspace, wcs_settings_body)
except ApiException as e:
    print("Exception when calling OWSServicesApi->put_wcs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **wcs_settings_body** | [**WCSInfo**](WCSInfo.md)| Body of the WCS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wfs_settings**
> put_wfs_settings(wfs_settings_body)



Edits a global WFS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
wfs_settings_body = swagger_client.WFSInfo() # WFSInfo | Body of the WFS settings

try:
    api_instance.put_wfs_settings(wfs_settings_body)
except ApiException as e:
    print("Exception when calling OWSServicesApi->put_wfs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfs_settings_body** | [**WFSInfo**](WFSInfo.md)| Body of the WFS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wfs_workspace_settings**
> put_wfs_workspace_settings(workspace, wfs_settings_body)



Edits a workspace-specific WFS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name
wfs_settings_body = swagger_client.WFSInfo() # WFSInfo | Body of the WFS settings layer

try:
    api_instance.put_wfs_workspace_settings(workspace, wfs_settings_body)
except ApiException as e:
    print("Exception when calling OWSServicesApi->put_wfs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **wfs_settings_body** | [**WFSInfo**](WFSInfo.md)| Body of the WFS settings layer | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wms_settings**
> put_wms_settings(wms_settings_body)



Edits a global WMS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
wms_settings_body = swagger_client.WMSInfo() # WMSInfo | Body of the WMS settings

try:
    api_instance.put_wms_settings(wms_settings_body)
except ApiException as e:
    print("Exception when calling OWSServicesApi->put_wms_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wms_settings_body** | [**WMSInfo**](WMSInfo.md)| Body of the WMS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wms_workspace_settings**
> put_wms_workspace_settings(workspace, wms_settings_body)



Edits a workspace-specific WMS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name
wms_settings_body = swagger_client.WMSInfo() # WMSInfo | Body of the WMS settings

try:
    api_instance.put_wms_workspace_settings(workspace, wms_settings_body)
except ApiException as e:
    print("Exception when calling OWSServicesApi->put_wms_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **wms_settings_body** | [**WMSInfo**](WMSInfo.md)| Body of the WMS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wmts_settings**
> put_wmts_settings(wmts_settings_body)



Edits a global WMTS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
wmts_settings_body = swagger_client.WMTSInfo() # WMTSInfo | Body of the WMTS settings

try:
    api_instance.put_wmts_settings(wmts_settings_body)
except ApiException as e:
    print("Exception when calling OWSServicesApi->put_wmts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wmts_settings_body** | [**WMTSInfo**](WMTSInfo.md)| Body of the WMTS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wmts_workspace_settings**
> put_wmts_workspace_settings(workspace, wmts_settings_body)



Edits a workspace-specific WMTS setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OWSServicesApi()
workspace = 'workspace_example' # str | The workspace name
wmts_settings_body = swagger_client.WMTSInfo() # WMTSInfo | Body of the WMTS settings

try:
    api_instance.put_wmts_workspace_settings(workspace, wmts_settings_body)
except ApiException as e:
    print("Exception when calling OWSServicesApi->put_wmts_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **wmts_settings_body** | [**WMTSInfo**](WMTSInfo.md)| Body of the WMTS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

