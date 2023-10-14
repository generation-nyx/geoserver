# swagger_client.CoveragesApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_coverage**](CoveragesApi.md#delete_coverage) | **DELETE** /workspaces/{workspace}/coverages/{coverage} | 
[**delete_coverage_store**](CoveragesApi.md#delete_coverage_store) | **DELETE** /workspaces/{workspace}/coverages | 
[**delete_workspace_coverage**](CoveragesApi.md#delete_workspace_coverage) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
[**delete_workspace_coverage_store**](CoveragesApi.md#delete_workspace_coverage_store) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages | 
[**get_coverage**](CoveragesApi.md#get_coverage) | **GET** /workspaces/{workspace}/coverages/{coverage} | 
[**get_coverage_store**](CoveragesApi.md#get_coverage_store) | **GET** /workspaces/{workspace}/coverages | 
[**get_workspace_coverage**](CoveragesApi.md#get_workspace_coverage) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
[**get_workspace_coverage_store**](CoveragesApi.md#get_workspace_coverage_store) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages | 
[**post_coverage**](CoveragesApi.md#post_coverage) | **POST** /workspaces/{workspace}/coverages/{coverage} | 
[**post_coverage_reset**](CoveragesApi.md#post_coverage_reset) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/reset | Reset the caches related to this specific coverage.
[**post_coverage_store**](CoveragesApi.md#post_coverage_store) | **POST** /workspaces/{workspace}/coverages | 
[**post_workspace_coverage**](CoveragesApi.md#post_workspace_coverage) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
[**post_workspace_coverage_store**](CoveragesApi.md#post_workspace_coverage_store) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages | 
[**put_coverage**](CoveragesApi.md#put_coverage) | **PUT** /workspaces/{workspace}/coverages/{coverage} | 
[**put_coverage_reset**](CoveragesApi.md#put_coverage_reset) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/reset | Reset the caches related to this specific coverage.
[**put_coverage_store**](CoveragesApi.md#put_coverage_store) | **PUT** /workspaces/{workspace}/coverages | 
[**put_workspace_coverage**](CoveragesApi.md#put_workspace_coverage) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
[**put_workspace_coverage_store**](CoveragesApi.md#put_workspace_coverage_store) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages | 


# **delete_coverage**
> delete_coverage()



Invalid. Can only delete an individual coverage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()

try:
    api_instance.delete_coverage()
except ApiException as e:
    print("Exception when calling CoveragesApi->delete_coverage: %s\n" % e)
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

# **delete_coverage_store**
> delete_coverage_store()



Invalid. Can only delete an individual coverage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()

try:
    api_instance.delete_coverage_store()
except ApiException as e:
    print("Exception when calling CoveragesApi->delete_coverage_store: %s\n" % e)
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

# **delete_workspace_coverage**
> delete_workspace_coverage(workspace, store, coverage, recurse=recurse)



Delete a coverage (optionally recursively deleting layers).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage data store
coverage = 'coverage_example' # str | The name of the coverage
recurse = false # bool | The recurse controls recursive deletion. When set to true all stores containing the resource are also removed. (optional) (default to false)

try:
    api_instance.delete_workspace_coverage(workspace, store, coverage, recurse=recurse)
except ApiException as e:
    print("Exception when calling CoveragesApi->delete_workspace_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage data store | 
 **coverage** | **str**| The name of the coverage | 
 **recurse** | **bool**| The recurse controls recursive deletion. When set to true all stores containing the resource are also removed. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_coverage_store**
> delete_workspace_coverage_store()



Invalid. Can only delete an individual coverage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()

try:
    api_instance.delete_workspace_coverage_store()
except ApiException as e:
    print("Exception when calling CoveragesApi->delete_workspace_coverage_store: %s\n" % e)
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

# **get_coverage**
> InlineResponse2001 get_coverage(workspace, coverage, quiet_on_not_found=quiet_on_not_found)



Get an individual coverage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()
workspace = 'workspace_example' # str | The name of the workspace
coverage = 'coverage_example' # str | The name of the coverage
quiet_on_not_found = false # bool | The quietOnNotFound parameter avoids logging an Exception when the coverage is not present. Note that 404 status code will be returned anyway. (optional) (default to false)

try:
    api_response = api_instance.get_coverage(workspace, coverage, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->get_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **coverage** | **str**| The name of the coverage | 
 **quiet_on_not_found** | **bool**| The quietOnNotFound parameter avoids logging an Exception when the coverage is not present. Note that 404 status code will be returned anyway. | [optional] [default to false]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coverage_store**
> InlineResponse200 get_coverage_store(workspace, list=list)



Get the coverages available for the provided workspace. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()
workspace = 'workspace_example' # str | The name of the workspace
list = 'list_example' # str | If the list parameter value is equal to \"all\" all the coverages available in the data source (even the non-published ones) will be returned.  (optional)

try:
    api_response = api_instance.get_coverage_store(workspace, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->get_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **list** | **str**| If the list parameter value is equal to \&quot;all\&quot; all the coverages available in the data source (even the non-published ones) will be returned.  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_coverage**
> InlineResponse2001 get_workspace_coverage(workspace, store, coverage, quiet_on_not_found=quiet_on_not_found)



Get an individual coverage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage datastore
coverage = 'coverage_example' # str | The name of the coverage
quiet_on_not_found = false # bool | The quietOnNotFound parameter avoids logging an Exception when the coverage is not present. Note that 404 status code will be returned anyway. (optional) (default to false)

try:
    api_response = api_instance.get_workspace_coverage(workspace, store, coverage, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->get_workspace_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage datastore | 
 **coverage** | **str**| The name of the coverage | 
 **quiet_on_not_found** | **bool**| The quietOnNotFound parameter avoids logging an Exception when the coverage is not present. Note that 404 status code will be returned anyway. | [optional] [default to false]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_coverage_store**
> InlineResponse200 get_workspace_coverage_store(workspace, store, list=list)



Get the coverages available for the provided workspace and data store. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage data store
list = 'list_example' # str | If the list parameter value is equal to \"all\" all the coverages available in the data source (even the non-published ones) will be returned.  (optional)

try:
    api_response = api_instance.get_workspace_coverage_store(workspace, store, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->get_workspace_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage data store | 
 **list** | **str**| If the list parameter value is equal to \&quot;all\&quot; all the coverages available in the data source (even the non-published ones) will be returned.  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_coverage**
> post_coverage()



Invalid. Use POST on the coverages endpoint to add a new coverage, or PUT on an individual coverage to edit it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()

try:
    api_instance.post_coverage()
except ApiException as e:
    print("Exception when calling CoveragesApi->post_coverage: %s\n" % e)
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

# **post_coverage_reset**
> post_coverage_reset(workspace, store, coverage)

Reset the caches related to this specific coverage.

Resets raster caches for this coverage. This operation is used to force GeoServer to drop caches associated to this coverage, and reconnect to the raster source the next time it is needed by a request. This is useful as the readers often cache some information about the bounds, coordinate system and image structure that might have changed in the meantime. Warning, the band structure is stored as part of the coverage configuration and won't be modified by this call, in case of need it should be modified issuing a PUT request against the coverage resource itself.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage store.
store = 'store_example' # str | The name of the coverage store containing the target coverage.
coverage = 'coverage_example' # str | The name of the target coverage.

try:
    # Reset the caches related to this specific coverage.
    api_instance.post_coverage_reset(workspace, store, coverage)
except ApiException as e:
    print("Exception when calling CoveragesApi->post_coverage_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage store. | 
 **store** | **str**| The name of the coverage store containing the target coverage. | 
 **coverage** | **str**| The name of the target coverage. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_coverage_store**
> post_coverage_store(workspace, coverage)



Create a new coverage, the coverage definition needs to reference a store. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()
workspace = 'workspace_example' # str | The name of the workspace
coverage = swagger_client.CoverageInfo() # CoverageInfo | The body of the coverage to POST

try:
    api_instance.post_coverage_store(workspace, coverage)
except ApiException as e:
    print("Exception when calling CoveragesApi->post_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **coverage** | [**CoverageInfo**](CoverageInfo.md)| The body of the coverage to POST | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workspace_coverage**
> post_workspace_coverage()



Invalid. Use POST on the coverages endpoint to add a new coverage, or PUT on an individual coverage to edit it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()

try:
    api_instance.post_workspace_coverage()
except ApiException as e:
    print("Exception when calling CoveragesApi->post_workspace_coverage: %s\n" % e)
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

# **post_workspace_coverage_store**
> post_workspace_coverage_store(workspace, store, coverage)



Create a new coverage, the underlying data store must exist. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage data store
coverage = swagger_client.CoverageInfo() # CoverageInfo | The body of the coverage to POST

try:
    api_instance.post_workspace_coverage_store(workspace, store, coverage)
except ApiException as e:
    print("Exception when calling CoveragesApi->post_workspace_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage data store | 
 **coverage** | [**CoverageInfo**](CoverageInfo.md)| The body of the coverage to POST | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_coverage**
> put_coverage()



Invalid. Use POST for adding a new coverage, or PUT on an individual coverage to edit that type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()

try:
    api_instance.put_coverage()
except ApiException as e:
    print("Exception when calling CoveragesApi->put_coverage: %s\n" % e)
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

# **put_coverage_reset**
> put_coverage_reset(workspace, store, coverage)

Reset the caches related to this specific coverage.

Resets raster caches for this coverage. This operation is used to force GeoServer to drop caches associated to this coverage, and reconnect to the raster source the next time it is needed by a request. This is useful as the readers often cache some information about the bounds, coordinate system and image structure that might have changed in the meantime. Warning, the band structure is stored as part of the coverage configuration and won't be modified by this call, in case of need it should be modified issuing a PUT request against the coverage resource itself.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()
workspace = 'workspace_example' # str | The name of the workspace containing the coverage store.
store = 'store_example' # str | The name of the coverage store containing the target coverage.
coverage = 'coverage_example' # str | The name of the target coverage.

try:
    # Reset the caches related to this specific coverage.
    api_instance.put_coverage_reset(workspace, store, coverage)
except ApiException as e:
    print("Exception when calling CoveragesApi->put_coverage_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the coverage store. | 
 **store** | **str**| The name of the coverage store containing the target coverage. | 
 **coverage** | **str**| The name of the target coverage. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_coverage_store**
> put_coverage_store()



Invalid. Use POST for adding a new coverage, or PUT on an individual coverage to edit that type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()

try:
    api_instance.put_coverage_store()
except ApiException as e:
    print("Exception when calling CoveragesApi->put_coverage_store: %s\n" % e)
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

# **put_workspace_coverage**
> put_workspace_coverage(workspace, store, coverage, coverage2, calculate=calculate)



Update an individual coverage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage data store
coverage = 'coverage_example' # str | The name of the coverage
coverage2 = swagger_client.CoverageInfo() # CoverageInfo | The body of the coverage to PUT
calculate = ['calculate_example'] # list[str] | Comma-separated list of optional fields to calculate. Optional fields include: \"nativebbox\", \"latlonbbox\", \"dimensions\" (that is, bands). (optional)

try:
    api_instance.put_workspace_coverage(workspace, store, coverage, coverage2, calculate=calculate)
except ApiException as e:
    print("Exception when calling CoveragesApi->put_workspace_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage data store | 
 **coverage** | **str**| The name of the coverage | 
 **coverage2** | [**CoverageInfo**](CoverageInfo.md)| The body of the coverage to PUT | 
 **calculate** | [**list[str]**](str.md)| Comma-separated list of optional fields to calculate. Optional fields include: \&quot;nativebbox\&quot;, \&quot;latlonbbox\&quot;, \&quot;dimensions\&quot; (that is, bands). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, text/xml, application/json, text/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_workspace_coverage_store**
> put_workspace_coverage_store()



Invalid. Use POST for adding a new coverage, or PUT on an individual coverage to edit that type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoveragesApi()

try:
    api_instance.put_workspace_coverage_store()
except ApiException as e:
    print("Exception when calling CoveragesApi->put_workspace_coverage_store: %s\n" % e)
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

