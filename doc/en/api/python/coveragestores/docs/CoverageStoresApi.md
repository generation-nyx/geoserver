# swagger_client.CoverageStoresApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_coverage_store**](CoverageStoresApi.md#delete_coverage_store) | **DELETE** /workspaces/{workspace}/coveragestores/{store} | Delete coverage store
[**delete_coverage_store_upload**](CoverageStoresApi.md#delete_coverage_store_upload) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/{method}.{format} | 
[**delete_coverage_stores**](CoverageStoresApi.md#delete_coverage_stores) | **DELETE** /workspaces/{workspace}/coveragestores | 
[**get_coverage_store**](CoverageStoresApi.md#get_coverage_store) | **GET** /workspaces/{workspace}/coveragestores/{store} | Get a coverage store named {store} in the {workspace} workspace
[**get_coverage_store_upload**](CoverageStoresApi.md#get_coverage_store_upload) | **GET** /workspaces/{workspace}/coveragestores/{store}/{method}.{format} | 
[**get_coverage_stores**](CoverageStoresApi.md#get_coverage_stores) | **GET** /workspaces/{workspace}/coveragestores | Get a list of all coverage stores in {workspace}
[**post_coverage_store**](CoverageStoresApi.md#post_coverage_store) | **POST** /workspaces/{workspace}/coveragestores/{store} | 
[**post_coverage_store_reset**](CoverageStoresApi.md#post_coverage_store_reset) | **POST** /workspaces/{workspace}/coveragestores/{store}/reset | Reset the caches related to this specific coverage store.
[**post_coverage_store_upload**](CoverageStoresApi.md#post_coverage_store_upload) | **POST** /workspaces/{workspace}/coveragestores/{store}/{method}.{format} | 
[**post_coverage_stores**](CoverageStoresApi.md#post_coverage_stores) | **POST** /workspaces/{workspace}/coveragestores | Add a new coverage store
[**put_coverage_store**](CoverageStoresApi.md#put_coverage_store) | **PUT** /workspaces/{workspace}/coveragestores/{store} | Modify a single coverage store.
[**put_coverage_store_reset**](CoverageStoresApi.md#put_coverage_store_reset) | **PUT** /workspaces/{workspace}/coveragestores/{store}/reset | Reset the caches related to this specific coverage store.
[**put_coverage_store_upload**](CoverageStoresApi.md#put_coverage_store_upload) | **PUT** /workspaces/{workspace}/coveragestores/{store}/{method}.{format} | Creates or overwrites the files for a coverage store
[**put_coverage_stores**](CoverageStoresApi.md#put_coverage_stores) | **PUT** /workspaces/{workspace}/coveragestores | 


# **delete_coverage_store**
> delete_coverage_store(workspace, store, purge=purge, recurse=recurse)

Delete coverage store

Deletes a coverage store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
purge = 'purge_example' # str | The purge parameter specifies if and how the underlying raster data source is deleted. Allowable values for this parameter are \"none\", \"metadata\", \"all\". When set to \"none\" data and auxiliary files are preserved. When set to \"metadata\" delete only auxiliary files and metadata. It’s recommended when data files (such as granules) should not be deleted from disk. Finally, when set to \"all\" both data and auxiliary files are removed. (optional)
recurse = true # bool | The recurse controls recursive deletion. When set to true all resources contained in the store are also removed. The default value is \"false\". (optional)

try:
    # Delete coverage store
    api_instance.delete_coverage_store(workspace, store, purge=purge, recurse=recurse)
except ApiException as e:
    print("Exception when calling CoverageStoresApi->delete_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **purge** | **str**| The purge parameter specifies if and how the underlying raster data source is deleted. Allowable values for this parameter are \&quot;none\&quot;, \&quot;metadata\&quot;, \&quot;all\&quot;. When set to \&quot;none\&quot; data and auxiliary files are preserved. When set to \&quot;metadata\&quot; delete only auxiliary files and metadata. It’s recommended when data files (such as granules) should not be deleted from disk. Finally, when set to \&quot;all\&quot; both data and auxiliary files are removed. | [optional] 
 **recurse** | **bool**| The recurse controls recursive deletion. When set to true all resources contained in the store are also removed. The default value is \&quot;false\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coverage_store_upload**
> delete_coverage_store_upload()



Invalid, only used for uploads

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()

try:
    api_instance.delete_coverage_store_upload()
except ApiException as e:
    print("Exception when calling CoverageStoresApi->delete_coverage_store_upload: %s\n" % e)
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

# **delete_coverage_stores**
> delete_coverage_stores()



Invalid. Use /coverage/{style} instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()

try:
    api_instance.delete_coverage_stores()
except ApiException as e:
    print("Exception when calling CoverageStoresApi->delete_coverage_stores: %s\n" % e)
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

# **get_coverage_store**
> CoverageStoreInfo get_coverage_store(workspace, store, quiet_on_not_found=quiet_on_not_found)

Get a coverage store named {store} in the {workspace} workspace

Displays a representation of the coverage store. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/{store}.xml\" for XML). Defaults to HTML representation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
quiet_on_not_found = true # bool | When set to true, avoids logging an Exception when the coverage store is not present. Note that 404 status code will be returned anyway. (optional)

try:
    # Get a coverage store named {store} in the {workspace} workspace
    api_response = api_instance.get_coverage_store(workspace, store, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoverageStoresApi->get_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **quiet_on_not_found** | **bool**| When set to true, avoids logging an Exception when the coverage store is not present. Note that 404 status code will be returned anyway. | [optional] 

### Return type

[**CoverageStoreInfo**](CoverageStoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coverage_store_upload**
> get_coverage_store_upload()



Invalid, only used for uploads

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()

try:
    api_instance.get_coverage_store_upload()
except ApiException as e:
    print("Exception when calling CoverageStoresApi->get_coverage_store_upload: %s\n" % e)
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

# **get_coverage_stores**
> CoverageStoreList get_coverage_stores(workspace)

Get a list of all coverage stores in {workspace}

Displays a list of all styles on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/coveragestores.xml\" for XML). Defaults to HTML representation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage stores.

try:
    # Get a list of all coverage stores in {workspace}
    api_response = api_instance.get_coverage_stores(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoverageStoresApi->get_coverage_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage stores. | 

### Return type

[**CoverageStoreList**](CoverageStoreList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_coverage_store**
> post_coverage_store()



Invalid. Use POST on /workspaces/{workspace}/coveragestores for adding a new coverage store, or PUT on /workspaces/{workspace}/coveragestores/{store} to edit/upload an existing coverage store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()

try:
    api_instance.post_coverage_store()
except ApiException as e:
    print("Exception when calling CoverageStoresApi->post_coverage_store: %s\n" % e)
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

# **post_coverage_store_reset**
> post_coverage_store_reset(workspace, store)

Reset the caches related to this specific coverage store.

Resets raster caches for this coverage store. This operation is used to force GeoServer to drop caches associated to this coverage store, and reconnect to the raster source the next time it is needed by a request. This is useful as the readers often cache some information about the bounds, coordinate system and image structure that might have changed in the meantime.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage store.
store = 'store_example' # str | The name of the coverage store to modify.

try:
    # Reset the caches related to this specific coverage store.
    api_instance.post_coverage_store_reset(workspace, store)
except ApiException as e:
    print("Exception when calling CoverageStoresApi->post_coverage_store_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage store. | 
 **store** | **str**| The name of the coverage store to modify. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_coverage_store_upload**
> post_coverage_store_upload(workspace, store, method, format, filename=filename, update_b_box=update_b_box)



Used to harvest new granules in a writable structured grid coverage reader (e.g., image mosaic). Attempting to harvest a file into any other reader will result in a HTTP 405, method not allowed. Multiple granules can be uploaded by wrapping them in a ZIP file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
method = 'method_example' # str | The upload method. Can be \"url\", \"file\", \"external\", \"remote\". \"file\" uploads a file from a local source. The body of the request is the file itself. \"url\" uploads a file from a remote source. The body of the request is a URL pointing to the file to upload. This URL must be visible from the server. \"external\" uses an existing file on the server. The body of the request is the absolute path to the existing file. \"remote\" uses a direct reference to a remote url, i.e. a file on a cloud storage. No data copy will occur. The body of the request is a URL pointing to the remote dataset.
format = 'format_example' # str | The type of target coverage store (e.g., \"imagemosaic\")
filename = 'filename_example' # str | The filename parameter specifies the target file name for a file that needs to be harvested as part of a mosaic. This is important to avoid clashes and to make sure the right dimension values are available in the name for multidimensional mosaics to work. Only used if method=\"file\". (optional)
update_b_box = true # bool | When set to \"true\", triggers re-calculation of the layer native bbox. Defaults to \"false\". (optional)

try:
    api_instance.post_coverage_store_upload(workspace, store, method, format, filename=filename, update_b_box=update_b_box)
except ApiException as e:
    print("Exception when calling CoverageStoresApi->post_coverage_store_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **method** | **str**| The upload method. Can be \&quot;url\&quot;, \&quot;file\&quot;, \&quot;external\&quot;, \&quot;remote\&quot;. \&quot;file\&quot; uploads a file from a local source. The body of the request is the file itself. \&quot;url\&quot; uploads a file from a remote source. The body of the request is a URL pointing to the file to upload. This URL must be visible from the server. \&quot;external\&quot; uses an existing file on the server. The body of the request is the absolute path to the existing file. \&quot;remote\&quot; uses a direct reference to a remote url, i.e. a file on a cloud storage. No data copy will occur. The body of the request is a URL pointing to the remote dataset. | 
 **format** | **str**| The type of target coverage store (e.g., \&quot;imagemosaic\&quot;) | 
 **filename** | **str**| The filename parameter specifies the target file name for a file that needs to be harvested as part of a mosaic. This is important to avoid clashes and to make sure the right dimension values are available in the name for multidimensional mosaics to work. Only used if method&#x3D;\&quot;file\&quot;. | [optional] 
 **update_b_box** | **bool**| When set to \&quot;true\&quot;, triggers re-calculation of the layer native bbox. Defaults to \&quot;false\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_coverage_stores**
> str post_coverage_stores(workspace, coverage_store_body)

Add a new coverage store

Adds a new coverage store entry to the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage stores.
coverage_store_body = swagger_client.CoverageStoreInfo() # CoverageStoreInfo | The coverage store body information to upload.  Examples: - application/xml:    ```   <coverageStore>     <name>nyc</name>     <url>file:/path/to/file.tiff</url>   </coverageStore>   ```  - application/json:    ```   {     \"coverageStore\": {       \"name\": \"nyc\",       \"url\": \"file:/path/to/file.tiff\"     }   }   ``` 

try:
    # Add a new coverage store
    api_response = api_instance.post_coverage_stores(workspace, coverage_store_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoverageStoresApi->post_coverage_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage stores. | 
 **coverage_store_body** | [**CoverageStoreInfo**](CoverageStoreInfo.md)| The coverage store body information to upload.  Examples: - application/xml:    &#x60;&#x60;&#x60;   &lt;coverageStore&gt;     &lt;name&gt;nyc&lt;/name&gt;     &lt;url&gt;file:/path/to/file.tiff&lt;/url&gt;   &lt;/coverageStore&gt;   &#x60;&#x60;&#x60;  - application/json:    &#x60;&#x60;&#x60;   {     \&quot;coverageStore\&quot;: {       \&quot;name\&quot;: \&quot;nyc\&quot;,       \&quot;url\&quot;: \&quot;file:/path/to/file.tiff\&quot;     }   }   &#x60;&#x60;&#x60;  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_coverage_store**
> put_coverage_store(workspace, store, coverage_store_body)

Modify a single coverage store.

Modifies a single coverage store. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"{store}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage_store_body = swagger_client.CoverageStoreInfo() # CoverageStoreInfo | The coverage store body information to upload. For a PUT, only values which should be changed need to be included.  Examples: - application/xml:    ```   <coverageStore>     <description>A coverage store</description>     <enabled>true</enabled>     <__default>true</__default>     <url>file:/path/to/file.tiff</url>   </coverageStore>   ```  - application/json:    ```   {     \"coverageStore\": {       \"description\": \"A coverage store\",       \"enabled\": \"true\",       \"_default\": \"true\",       \"url\": \"file:/path/to/file.tiff\"     }   }   ``` 

try:
    # Modify a single coverage store.
    api_instance.put_coverage_store(workspace, store, coverage_store_body)
except ApiException as e:
    print("Exception when calling CoverageStoresApi->put_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **coverage_store_body** | [**CoverageStoreInfo**](CoverageStoreInfo.md)| The coverage store body information to upload. For a PUT, only values which should be changed need to be included.  Examples: - application/xml:    &#x60;&#x60;&#x60;   &lt;coverageStore&gt;     &lt;description&gt;A coverage store&lt;/description&gt;     &lt;enabled&gt;true&lt;/enabled&gt;     &lt;__default&gt;true&lt;/__default&gt;     &lt;url&gt;file:/path/to/file.tiff&lt;/url&gt;   &lt;/coverageStore&gt;   &#x60;&#x60;&#x60;  - application/json:    &#x60;&#x60;&#x60;   {     \&quot;coverageStore\&quot;: {       \&quot;description\&quot;: \&quot;A coverage store\&quot;,       \&quot;enabled\&quot;: \&quot;true\&quot;,       \&quot;_default\&quot;: \&quot;true\&quot;,       \&quot;url\&quot;: \&quot;file:/path/to/file.tiff\&quot;     }   }   &#x60;&#x60;&#x60;  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_coverage_store_reset**
> put_coverage_store_reset(workspace, store)

Reset the caches related to this specific coverage store.

Resets raster caches for this coverage store. This operation is used to force GeoServer to drop caches associated to this coverage store, and reconnect to the raster source the next time it is needed by a request. This is useful as the readers often cache some information about the bounds, coordinate system and image structure that might have changed in the meantime.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage store.
store = 'store_example' # str | The name of the coverage store to modify.

try:
    # Reset the caches related to this specific coverage store.
    api_instance.put_coverage_store_reset(workspace, store)
except ApiException as e:
    print("Exception when calling CoverageStoresApi->put_coverage_store_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage store. | 
 **store** | **str**| The name of the coverage store to modify. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_coverage_store_upload**
> put_coverage_store_upload(workspace, store, method, format, configure=configure, use_jai_imageread=use_jai_imageread, coverage_name=coverage_name, filename=filename)

Creates or overwrites the files for a coverage store

Creates or modified a single coverage store by uploading its raster data files. Multi-file stores like mosaic can be created by uploading a zip file and setting the content type to \"application/zip\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
method = 'method_example' # str | The upload method. Can be \"url\", \"file\", \"external\", \"remote\". \"file\" uploads a file from a local source. The body of the request is the file itself. \"url\" uploads a file from a remote source. The body of the request is a URL pointing to the file to upload. This URL must be visible from the server. \"external\" uses an existing file on the server. The body of the request is the absolute path to the existing file. \"remote\" uses a direct reference to a remote url, i.e. a file on a cloud storage. No data copy will occur. The body of the request is a URL pointing to the remote dataset.
format = 'format_example' # str | The type of target coverage store (e.g., \"imagemosaic\")
configure = 'configure_example' # str | The configure parameter controls if a coverage/layer are configured upon file upload, in addition to creating the store. It can have a value of \"none\" to avoid configuring coverages. (optional)
use_jai_imageread = 'use_jai_imageread_example' # str | Whether to use deferred loading while configuring the coverage/layer. (optional)
coverage_name = 'coverage_name_example' # str | Name of the newly created coverage/layer. (optional)
filename = 'filename_example' # str | The filename parameter specifies the target file name for a file that needs to be harvested as part of a mosaic. This is important to avoid clashes and to make sure the right dimension values are available in the name for multidimensional mosaics to work. Only used if method=\"file\". (optional)

try:
    # Creates or overwrites the files for a coverage store
    api_instance.put_coverage_store_upload(workspace, store, method, format, configure=configure, use_jai_imageread=use_jai_imageread, coverage_name=coverage_name, filename=filename)
except ApiException as e:
    print("Exception when calling CoverageStoresApi->put_coverage_store_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **method** | **str**| The upload method. Can be \&quot;url\&quot;, \&quot;file\&quot;, \&quot;external\&quot;, \&quot;remote\&quot;. \&quot;file\&quot; uploads a file from a local source. The body of the request is the file itself. \&quot;url\&quot; uploads a file from a remote source. The body of the request is a URL pointing to the file to upload. This URL must be visible from the server. \&quot;external\&quot; uses an existing file on the server. The body of the request is the absolute path to the existing file. \&quot;remote\&quot; uses a direct reference to a remote url, i.e. a file on a cloud storage. No data copy will occur. The body of the request is a URL pointing to the remote dataset. | 
 **format** | **str**| The type of target coverage store (e.g., \&quot;imagemosaic\&quot;) | 
 **configure** | **str**| The configure parameter controls if a coverage/layer are configured upon file upload, in addition to creating the store. It can have a value of \&quot;none\&quot; to avoid configuring coverages. | [optional] 
 **use_jai_imageread** | **str**| Whether to use deferred loading while configuring the coverage/layer. | [optional] 
 **coverage_name** | **str**| Name of the newly created coverage/layer. | [optional] 
 **filename** | **str**| The filename parameter specifies the target file name for a file that needs to be harvested as part of a mosaic. This is important to avoid clashes and to make sure the right dimension values are available in the name for multidimensional mosaics to work. Only used if method&#x3D;\&quot;file\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_coverage_stores**
> put_coverage_stores()



Invalid. Use POST for adding a new coverage store, or PUT on /coveragestores/{store} to edit/upload an existing coverage store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoverageStoresApi()

try:
    api_instance.put_coverage_stores()
except ApiException as e:
    print("Exception when calling CoverageStoresApi->put_coverage_stores: %s\n" % e)
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

