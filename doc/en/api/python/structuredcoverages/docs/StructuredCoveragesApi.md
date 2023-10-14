# swagger_client.StructuredCoveragesApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_coverage_stores**](StructuredCoveragesApi.md#delete_coverage_stores) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | 
[**delete_structured_coverage_granule**](StructuredCoveragesApi.md#delete_structured_coverage_granule) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | 
[**delete_structured_coverage_granules**](StructuredCoveragesApi.md#delete_structured_coverage_granules) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | 
[**get_structured_coverage_granule**](StructuredCoveragesApi.md#get_structured_coverage_granule) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | Get the attributes of a particular granule
[**get_structured_coverage_granules**](StructuredCoveragesApi.md#get_structured_coverage_granules) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | Get the attributes associated to the granules
[**get_structured_coverage_index**](StructuredCoveragesApi.md#get_structured_coverage_index) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | Get the information schema attached to the granules
[**post_structured_coverage_granule**](StructuredCoveragesApi.md#post_structured_coverage_granule) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | 
[**post_structured_coverage_granules**](StructuredCoveragesApi.md#post_structured_coverage_granules) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | 
[**post_structured_coverage_index**](StructuredCoveragesApi.md#post_structured_coverage_index) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | 
[**put_structured_coverage_granule**](StructuredCoveragesApi.md#put_structured_coverage_granule) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | 
[**put_structured_coverage_granules**](StructuredCoveragesApi.md#put_structured_coverage_granules) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | 
[**put_structured_coverage_index**](StructuredCoveragesApi.md#put_structured_coverage_index) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | 


# **delete_coverage_stores**
> delete_coverage_stores()



Invalid, the index cannot be created or modified

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()

try:
    api_instance.delete_coverage_stores()
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->delete_coverage_stores: %s\n" % e)
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

# **delete_structured_coverage_granule**
> delete_structured_coverage_granule(workspace, store, coverage, granule_id, purge=purge, update_b_box=update_b_box)



Allows removing the specified granule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage = 'coverage_example' # str | The name of the coverage to be retrieved
granule_id = 'granule_id_example' # str | The granule ID
purge = 'purge_example' # str | The purge parameter specifies if and how the underlying raster data source is deleted. Allowable values for this parameter are \"none\", \"metadata\" and \"all\". When set to \"none\" data and auxiliary files are preserved, only the registration in the mosaic is removed When set to \"metadata\" delete only auxiliary files and metadata (e.g. NetCDF sidecar indexes). It’s recommended when data files (such as granules) should not be deleted from disk. Finally, when set to \"all\" both data and auxiliary files are removed. (optional)
update_b_box = NULL # object | When set to \"true\", triggers re-calculation of the layer native bbox. Defaults to \"false\". (optional)

try:
    api_instance.delete_structured_coverage_granule(workspace, store, coverage, granule_id, purge=purge, update_b_box=update_b_box)
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->delete_structured_coverage_granule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the worskpace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **coverage** | **str**| The name of the coverage to be retrieved | 
 **granule_id** | **str**| The granule ID | 
 **purge** | **str**| The purge parameter specifies if and how the underlying raster data source is deleted. Allowable values for this parameter are \&quot;none\&quot;, \&quot;metadata\&quot; and \&quot;all\&quot;. When set to \&quot;none\&quot; data and auxiliary files are preserved, only the registration in the mosaic is removed When set to \&quot;metadata\&quot; delete only auxiliary files and metadata (e.g. NetCDF sidecar indexes). It’s recommended when data files (such as granules) should not be deleted from disk. Finally, when set to \&quot;all\&quot; both data and auxiliary files are removed. | [optional] 
 **update_b_box** | [**object**](.md)| When set to \&quot;true\&quot;, triggers re-calculation of the layer native bbox. Defaults to \&quot;false\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_structured_coverage_granules**
> delete_structured_coverage_granules(workspace, store, coverage, filter=filter, purge=purge, update_b_box=update_b_box)



Allows removing one or more granules from the index

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage = 'coverage_example' # str | The name of the coverage to be retrieved
filter = 'filter_example' # str | A CQL filter to reduce the returned granules (optional)
purge = 'purge_example' # str | The purge parameter specifies if and how the underlying raster data source is deleted. Allowable values for this parameter are \"none\", \"metadata\" and \"all\". When set to \"none\" data and auxiliary files are preserved, only the registration in the mosaic is removed When set to \"metadata\" delete only auxiliary files and metadata (e.g. NetCDF sidecar indexes). It’s recommended when data files (such as granules) should not be deleted from disk. Finally, when set to \"all\" both data and auxiliary files are removed. (optional)
update_b_box = NULL # object | When set to \"true\", triggers re-calculation of the layer native bbox. Defaults to \"false\". (optional)

try:
    api_instance.delete_structured_coverage_granules(workspace, store, coverage, filter=filter, purge=purge, update_b_box=update_b_box)
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->delete_structured_coverage_granules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the worskpace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **coverage** | **str**| The name of the coverage to be retrieved | 
 **filter** | **str**| A CQL filter to reduce the returned granules | [optional] 
 **purge** | **str**| The purge parameter specifies if and how the underlying raster data source is deleted. Allowable values for this parameter are \&quot;none\&quot;, \&quot;metadata\&quot; and \&quot;all\&quot;. When set to \&quot;none\&quot; data and auxiliary files are preserved, only the registration in the mosaic is removed When set to \&quot;metadata\&quot; delete only auxiliary files and metadata (e.g. NetCDF sidecar indexes). It’s recommended when data files (such as granules) should not be deleted from disk. Finally, when set to \&quot;all\&quot; both data and auxiliary files are removed. | [optional] 
 **update_b_box** | [**object**](.md)| When set to \&quot;true\&quot;, triggers re-calculation of the layer native bbox. Defaults to \&quot;false\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_structured_coverage_granule**
> get_structured_coverage_granule(workspace, store, coverage, granule_id)

Get the attributes of a particular granule

Displays a list of all the attributes associated to a particular coverage's granule. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/index.xml\" for XML). Defaults to XML representation. The XML output is actually WFS 1.0 GML, while the JSON output is GeoJSON

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage = 'coverage_example' # str | The name of the coverage to be retrieved
granule_id = 'granule_id_example' # str | The granule ID

try:
    # Get the attributes of a particular granule
    api_instance.get_structured_coverage_granule(workspace, store, coverage, granule_id)
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->get_structured_coverage_granule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the worskpace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **coverage** | **str**| The name of the coverage to be retrieved | 
 **granule_id** | **str**| The granule ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_structured_coverage_granules**
> get_structured_coverage_granules(workspace, store, coverage, filter=filter, offset=offset, limit=limit)

Get the attributes associated to the granules

Displays a list of all the attributes associated to a particular coverage's granules. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/index.xml\" for XML). Defaults to XML representation. The XML output is actually WFS 1.0 GML, while the JSON output is GeoJSON 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage = 'coverage_example' # str | The name of the coverage to be retrieved
filter = 'filter_example' # str | A CQL filter to reduce the returned granules (optional)
offset = 0 # int | Used for paging, the start of the current page (optional) (default to 0)
limit = 56 # int | Used for paging, the number of items to be returned (optional)

try:
    # Get the attributes associated to the granules
    api_instance.get_structured_coverage_granules(workspace, store, coverage, filter=filter, offset=offset, limit=limit)
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->get_structured_coverage_granules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the worskpace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **coverage** | **str**| The name of the coverage to be retrieved | 
 **filter** | **str**| A CQL filter to reduce the returned granules | [optional] 
 **offset** | **int**| Used for paging, the start of the current page | [optional] [default to 0]
 **limit** | **int**| Used for paging, the number of items to be returned | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_structured_coverage_index**
> Schema get_structured_coverage_index(workspace, store, coverage)

Get the information schema attached to the granules

Displays a list of all the attributes associated to a particular coverage's granules. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/index.xml\" for XML). Defaults to XML representation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage = 'coverage_example' # str | The name of the coverage to be retrieved

try:
    # Get the information schema attached to the granules
    api_response = api_instance.get_structured_coverage_index(workspace, store, coverage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->get_structured_coverage_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the worskpace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **coverage** | **str**| The name of the coverage to be retrieved | 

### Return type

[**Schema**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_structured_coverage_granule**
> post_structured_coverage_granule()



Invalid, the granules cannot harvested here, use a POST request on /workspaces/{workspace}/coveragestores/{store}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()

try:
    api_instance.post_structured_coverage_granule()
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->post_structured_coverage_granule: %s\n" % e)
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

# **post_structured_coverage_granules**
> post_structured_coverage_granules()



Invalid, the granules cannot harvested here, use a POST request on /workspaces/{workspace}/coveragestores/{store}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()

try:
    api_instance.post_structured_coverage_granules()
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->post_structured_coverage_granules: %s\n" % e)
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

# **post_structured_coverage_index**
> post_structured_coverage_index()



Invalid, the index cannot be created or modified

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()

try:
    api_instance.post_structured_coverage_index()
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->post_structured_coverage_index: %s\n" % e)
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

# **put_structured_coverage_granule**
> put_structured_coverage_granule()



Invalid, the granules cannot harvested here, use a POST request on /workspaces/{workspace}/coveragestores/{store}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()

try:
    api_instance.put_structured_coverage_granule()
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->put_structured_coverage_granule: %s\n" % e)
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

# **put_structured_coverage_granules**
> put_structured_coverage_granules()



Invalid, the granules cannot harvested here, use a POST request on /workspaces/{workspace}/coveragestores/{store}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()

try:
    api_instance.put_structured_coverage_granules()
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->put_structured_coverage_granules: %s\n" % e)
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

# **put_structured_coverage_index**
> put_structured_coverage_index()



Invalid, the index cannot be created or modified

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructuredCoveragesApi()

try:
    api_instance.put_structured_coverage_index()
except ApiException as e:
    print("Exception when calling StructuredCoveragesApi->put_structured_coverage_index: %s\n" % e)
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

