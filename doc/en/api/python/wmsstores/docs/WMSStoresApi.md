# swagger_client.WMSStoresApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_wms_store**](WMSStoresApi.md#delete_wms_store) | **DELETE** /workspaces/{workspace}/wmsstores/{store} | Delete WMS store
[**delete_wms_stores**](WMSStoresApi.md#delete_wms_stores) | **DELETE** /workspaces/{workspace}/wmsstores | 
[**get_wms_store**](WMSStoresApi.md#get_wms_store) | **GET** /workspaces/{workspace}/wmsstores/{store} | Retrieve a WMS store in a given workspace
[**get_wms_stores**](WMSStoresApi.md#get_wms_stores) | **GET** /workspaces/{workspace}/wmsstores | Get a list of WMS stores
[**post_wms_store**](WMSStoresApi.md#post_wms_store) | **POST** /workspaces/{workspace}/wmsstores/{store} | 
[**post_wms_stores**](WMSStoresApi.md#post_wms_stores) | **POST** /workspaces/{workspace}/wmsstores | Add a new WMS store
[**put_wms_store**](WMSStoresApi.md#put_wms_store) | **PUT** /workspaces/{workspace}/wmsstores/{store} | Modify a single WMS store.
[**put_wms_stores**](WMSStoresApi.md#put_wms_stores) | **PUT** /workspaces/{workspace}/wmsstores | 


# **delete_wms_store**
> delete_wms_store(workspace, store, recurse=recurse)

Delete WMS store

Deletes a WMS store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMSStoresApi()
workspace = 'workspace_example' # str | Name of the workspace containing the WMS store.
store = 'store_example' # str | Name of the WMS store
recurse = false # bool | When set to true all resources contained in the store are also removed. (optional) (default to false)

try:
    # Delete WMS store
    api_instance.delete_wms_store(workspace, store, recurse=recurse)
except ApiException as e:
    print("Exception when calling WMSStoresApi->delete_wms_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace containing the WMS store. | 
 **store** | **str**| Name of the WMS store | 
 **recurse** | **bool**| When set to true all resources contained in the store are also removed. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wms_stores**
> delete_wms_stores()



Invalid. Use /workspaces/{workspace}/wmsstores/{wmsstore} instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMSStoresApi()

try:
    api_instance.delete_wms_stores()
except ApiException as e:
    print("Exception when calling WMSStoresApi->delete_wms_stores: %s\n" % e)
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

# **get_wms_store**
> WMSStoreInfo get_wms_store(workspace, store, quiet_on_not_found=quiet_on_not_found)

Retrieve a WMS store in a given workspace

Displays a representation of the WMS store. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/wmsstores/{store}.xml\" for XML). Defaults to HTML representation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMSStoresApi()
workspace = 'workspace_example' # str | The name of the workspace containing the WMS store.
store = 'store_example' # str | The name of the store to be retrieved
quiet_on_not_found = true # bool | When set to true, avoids to log an Exception when the WMS store is not present. Note that 404 status code will be returned anyway. (optional)

try:
    # Retrieve a WMS store in a given workspace
    api_response = api_instance.get_wms_store(workspace, store, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WMSStoresApi->get_wms_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the WMS store. | 
 **store** | **str**| The name of the store to be retrieved | 
 **quiet_on_not_found** | **bool**| When set to true, avoids to log an Exception when the WMS store is not present. Note that 404 status code will be returned anyway. | [optional] 

### Return type

[**WMSStoreInfo**](WMSStoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wms_stores**
> WMSStoresList get_wms_stores()

Get a list of WMS stores

Displays a list of all WMS stores on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/rest/workspaces/{workspace}/wmsstores.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMSStoresApi()

try:
    # Get a list of WMS stores
    api_response = api_instance.get_wms_stores()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WMSStoresApi->get_wms_stores: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WMSStoresList**](WMSStoresList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wms_store**
> post_wms_store()



Invalid. Use POST on /workspaces/{workspace}/WMSstores for adding a new WMS store, or PUT on /workspaces/{workspace}/WMSstores/{store} to edit/upload an existing WMS store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMSStoresApi()

try:
    api_instance.post_wms_store()
except ApiException as e:
    print("Exception when calling WMSStoresApi->post_wms_store: %s\n" % e)
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

# **post_wms_stores**
> post_wms_stores(workspace, wms_store_body)

Add a new WMS store

Adds a new WMS store entry to the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMSStoresApi()
workspace = 'workspace_example' # str | Name of the worskpace containing the WMS store.
wms_store_body = swagger_client.WMSStoreInfo() # WMSStoreInfo | WMS store body information to upload.  Examples: - application/xml:    ```   <wmsStore>     <name>remote</name>     <capabilitiesUrl>http://demo.geoserver.org/geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities</capabilitiesUrl>   </wmsStore>   ```  - application/json:    ```   {     \"wmsStore\": {       \"name\": \"remote\",       \"capabilitiesUrl\": \"http://demo.geoserver.org/geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities\"     }   }   ``` 

try:
    # Add a new WMS store
    api_instance.post_wms_stores(workspace, wms_store_body)
except ApiException as e:
    print("Exception when calling WMSStoresApi->post_wms_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the worskpace containing the WMS store. | 
 **wms_store_body** | [**WMSStoreInfo**](WMSStoreInfo.md)| WMS store body information to upload.  Examples: - application/xml:    &#x60;&#x60;&#x60;   &lt;wmsStore&gt;     &lt;name&gt;remote&lt;/name&gt;     &lt;capabilitiesUrl&gt;http://demo.geoserver.org/geoserver/wms?SERVICE&#x3D;WMS&amp;VERSION&#x3D;1.1.1&amp;REQUEST&#x3D;GetCapabilities&lt;/capabilitiesUrl&gt;   &lt;/wmsStore&gt;   &#x60;&#x60;&#x60;  - application/json:    &#x60;&#x60;&#x60;   {     \&quot;wmsStore\&quot;: {       \&quot;name\&quot;: \&quot;remote\&quot;,       \&quot;capabilitiesUrl\&quot;: \&quot;http://demo.geoserver.org/geoserver/wms?SERVICE&#x3D;WMS&amp;VERSION&#x3D;1.1.1&amp;REQUEST&#x3D;GetCapabilities\&quot;     }   }   &#x60;&#x60;&#x60;  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wms_store**
> put_wms_store(workspace, store, wms_store_body)

Modify a single WMS store.

Modifies a single WMS store. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"{store}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMSStoresApi()
workspace = 'workspace_example' # str | The name of the worskpace containing the WMS stores.
store = 'store_example' # str | The name of the store to be retrieved
wms_store_body = swagger_client.WMSStoreInfo() # WMSStoreInfo | WMS store body information to upload. For a PUT, only values which should be changed need to be included.  Examples: - application/xml:    ```   <wmsStore>     <description>A wms store</description>     <enabled>true</enabled>     <__default>true</__default>     <capabilitiesUrl>http://demo.geoserver.org/geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities</capabilitiesUrl>     <user>admin</user>     <password>geoserver</password>     <maxConnections>6</maxConnections>     <readTimeout>60</readTimeout>     <connectTimeout>30</connectTimeout>   </wmsStore>   ```  - application/json:    ```   {     \"wmsStore\": {       \"description\": \"A wms store\",       \"enabled\": \"true\",       \"_default\": \"true\",       \"capabilitiesUrl\": \"http://demo.geoserver.org/geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities\",       \"user\": \"admin\",       \"password\": \"geoserver\",       \"maxConnections\": \"6\",       \"readTimeout\": \"60\",       \"connectTimeout\": \"30\"     }   }   ``` 

try:
    # Modify a single WMS store.
    api_instance.put_wms_store(workspace, store, wms_store_body)
except ApiException as e:
    print("Exception when calling WMSStoresApi->put_wms_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the worskpace containing the WMS stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **wms_store_body** | [**WMSStoreInfo**](WMSStoreInfo.md)| WMS store body information to upload. For a PUT, only values which should be changed need to be included.  Examples: - application/xml:    &#x60;&#x60;&#x60;   &lt;wmsStore&gt;     &lt;description&gt;A wms store&lt;/description&gt;     &lt;enabled&gt;true&lt;/enabled&gt;     &lt;__default&gt;true&lt;/__default&gt;     &lt;capabilitiesUrl&gt;http://demo.geoserver.org/geoserver/wms?SERVICE&#x3D;WMS&amp;VERSION&#x3D;1.1.1&amp;REQUEST&#x3D;GetCapabilities&lt;/capabilitiesUrl&gt;     &lt;user&gt;admin&lt;/user&gt;     &lt;password&gt;geoserver&lt;/password&gt;     &lt;maxConnections&gt;6&lt;/maxConnections&gt;     &lt;readTimeout&gt;60&lt;/readTimeout&gt;     &lt;connectTimeout&gt;30&lt;/connectTimeout&gt;   &lt;/wmsStore&gt;   &#x60;&#x60;&#x60;  - application/json:    &#x60;&#x60;&#x60;   {     \&quot;wmsStore\&quot;: {       \&quot;description\&quot;: \&quot;A wms store\&quot;,       \&quot;enabled\&quot;: \&quot;true\&quot;,       \&quot;_default\&quot;: \&quot;true\&quot;,       \&quot;capabilitiesUrl\&quot;: \&quot;http://demo.geoserver.org/geoserver/wms?SERVICE&#x3D;WMS&amp;VERSION&#x3D;1.1.1&amp;REQUEST&#x3D;GetCapabilities\&quot;,       \&quot;user\&quot;: \&quot;admin\&quot;,       \&quot;password\&quot;: \&quot;geoserver\&quot;,       \&quot;maxConnections\&quot;: \&quot;6\&quot;,       \&quot;readTimeout\&quot;: \&quot;60\&quot;,       \&quot;connectTimeout\&quot;: \&quot;30\&quot;     }   }   &#x60;&#x60;&#x60;  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wms_stores**
> put_wms_stores()



Invalid. Use POST for adding a new WMS store, or PUT on /workspaces/{workspace}/wmsstores/{wmsstore} to edit an existing WMS store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMSStoresApi()

try:
    api_instance.put_wms_stores()
except ApiException as e:
    print("Exception when calling WMSStoresApi->put_wms_stores: %s\n" % e)
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

