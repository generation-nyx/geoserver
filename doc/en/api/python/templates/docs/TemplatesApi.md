# swagger_client.TemplatesApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**template_coverage_delete**](TemplatesApi.md#template_coverage_delete) | **DELETE** /workspaces/{workspace}/coveragestore/{store}/coverages/{coverage}/templates/{template}.ftl | Delete a template.
[**template_coverage_get**](TemplatesApi.md#template_coverage_get) | **GET** /workspaces/{workspace}/coveragestore/{store}/coverages/{coverage}/templates/{template}.ftl | Return a template for a coverage
[**template_coverage_post**](TemplatesApi.md#template_coverage_post) | **POST** /workspaces/{workspace}/coveragestore/{store}/coverages/{coverage}/templates/{template}.ftl | 
[**template_coverage_put**](TemplatesApi.md#template_coverage_put) | **PUT** /workspaces/{workspace}/coveragestore/{store}/coverages/{coverage}/templates/{template}.ftl | Insert or update a template
[**template_data_store_cs_delete**](TemplatesApi.md#template_data_store_cs_delete) | **DELETE** /workspaces/{workspace}/coveragestore/{store}/templates/{template}.ftl | Delete a template.
[**template_data_store_cs_get**](TemplatesApi.md#template_data_store_cs_get) | **GET** /workspaces/{workspace}/coveragestore/{store}/templates/{template}.ftl | Return a template for a coverage store
[**template_data_store_cs_post**](TemplatesApi.md#template_data_store_cs_post) | **POST** /workspaces/{workspace}/coveragestore/{store}/templates/{template}.ftl | 
[**template_data_store_cs_put**](TemplatesApi.md#template_data_store_cs_put) | **PUT** /workspaces/{workspace}/coveragestore/{store}/templates/{template}.ftl | Insert or update a template
[**template_data_store_delete**](TemplatesApi.md#template_data_store_delete) | **DELETE** /workspaces/{workspace}/datastores/{store}/templates/{template}.ftl | Delete a template.
[**template_data_store_ft_delete**](TemplatesApi.md#template_data_store_ft_delete) | **DELETE** /workspaces/{workspace}/datastores/{store}/featuretypes/{type}/templates/{template}.ftl | Delete a template.
[**template_data_store_ft_get**](TemplatesApi.md#template_data_store_ft_get) | **GET** /workspaces/{workspace}/datastores/{store}/featuretypes/{type}/templates/{template}.ftl | Return a template for a feature type.
[**template_data_store_ft_post**](TemplatesApi.md#template_data_store_ft_post) | **POST** /workspaces/{workspace}/datastores/{store}/featuretypes/{type}/templates/{template}.ftl | 
[**template_data_store_ft_put**](TemplatesApi.md#template_data_store_ft_put) | **PUT** /workspaces/{workspace}/datastores/{store}/featuretypes/{type}/templates/{template}.ftl | Insert or update a template
[**template_data_store_get**](TemplatesApi.md#template_data_store_get) | **GET** /workspaces/{workspace}/datastores/{store}/templates/{template}.ftl | Return a template for a data store
[**template_data_store_post**](TemplatesApi.md#template_data_store_post) | **POST** /workspaces/{workspace}/datastores/{store}/templates/{template}.ftl | 
[**template_data_store_put**](TemplatesApi.md#template_data_store_put) | **PUT** /workspaces/{workspace}/datastores/{store}/templates/{template}.ftl | Insert or update a template
[**template_delete**](TemplatesApi.md#template_delete) | **DELETE** /templates/{template}.ftl | Delete a template.
[**template_get**](TemplatesApi.md#template_get) | **GET** /templates/{template}.ftl | Return a template
[**template_post**](TemplatesApi.md#template_post) | **POST** /templates/{template}.ftl | 
[**template_put**](TemplatesApi.md#template_put) | **PUT** /templates/{template}.ftl | Insert or update a template
[**template_workspace_delete**](TemplatesApi.md#template_workspace_delete) | **DELETE** /workspaces/{workspace}/templates/{template}.ftl | Delete a template.
[**template_workspace_get**](TemplatesApi.md#template_workspace_get) | **GET** /workspaces/{workspace}/templates/{template}.ftl | Return a template for workspace
[**template_workspace_post**](TemplatesApi.md#template_workspace_post) | **POST** /workspaces/{workspace}/templates/{template}.ftl | 
[**template_workspace_put**](TemplatesApi.md#template_workspace_put) | **PUT** /workspaces/{workspace}/templates/{template}.ftl | Insert or update a template
[**templates_coverage_delete**](TemplatesApi.md#templates_coverage_delete) | **DELETE** /workspaces/{workspace}/coveragestore/{store}/coverages/{coverage}/templates | 
[**templates_coverage_get**](TemplatesApi.md#templates_coverage_get) | **GET** /workspaces/{workspace}/coveragestore/{store}/coverages/{coverage}/templates | List of templates for a coverage
[**templates_coverage_post**](TemplatesApi.md#templates_coverage_post) | **POST** /workspaces/{workspace}/coveragestore/{store}/coverages/{coverage}/templates | 
[**templates_coverage_put**](TemplatesApi.md#templates_coverage_put) | **PUT** /workspaces/{workspace}/coveragestore/{store}/coverages/{coverage}/templates | 
[**templates_data_store_cs_delete**](TemplatesApi.md#templates_data_store_cs_delete) | **DELETE** /workspaces/{workspace}/coveragestore/{store}/templates | 
[**templates_data_store_cs_get**](TemplatesApi.md#templates_data_store_cs_get) | **GET** /workspaces/{workspace}/coveragestore/{store}/templates | List of templates for a coverage store
[**templates_data_store_cs_post**](TemplatesApi.md#templates_data_store_cs_post) | **POST** /workspaces/{workspace}/coveragestore/{store}/templates | 
[**templates_data_store_cs_put**](TemplatesApi.md#templates_data_store_cs_put) | **PUT** /workspaces/{workspace}/coveragestore/{store}/templates | 
[**templates_data_store_delete**](TemplatesApi.md#templates_data_store_delete) | **DELETE** /workspaces/{workspace}/datastores/{store}/templates | 
[**templates_data_store_ft_delete**](TemplatesApi.md#templates_data_store_ft_delete) | **DELETE** /workspaces/{workspace}/datastores/{store}/featuretypes/{type}/templates | 
[**templates_data_store_ft_get**](TemplatesApi.md#templates_data_store_ft_get) | **GET** /workspaces/{workspace}/datastores/{store}/featuretypes/{type}/templates | List of templates for a feature type.
[**templates_data_store_ft_post**](TemplatesApi.md#templates_data_store_ft_post) | **POST** /workspaces/{workspace}/datastores/{store}/featuretypes/{type}/templates | 
[**templates_data_store_ft_put**](TemplatesApi.md#templates_data_store_ft_put) | **PUT** /workspaces/{workspace}/datastores/{store}/featuretypes/{type}/templates | 
[**templates_data_store_get**](TemplatesApi.md#templates_data_store_get) | **GET** /workspaces/{workspace}/datastores/{store}/templates | List of templates for a data store
[**templates_data_store_post**](TemplatesApi.md#templates_data_store_post) | **POST** /workspaces/{workspace}/datastores/{store}/templates | 
[**templates_data_store_put**](TemplatesApi.md#templates_data_store_put) | **PUT** /workspaces/{workspace}/datastores/{store}/templates | 
[**templates_delete**](TemplatesApi.md#templates_delete) | **DELETE** /templates | 
[**templates_get**](TemplatesApi.md#templates_get) | **GET** /templates | List of templates for the server
[**templates_post**](TemplatesApi.md#templates_post) | **POST** /templates | 
[**templates_put**](TemplatesApi.md#templates_put) | **PUT** /templates | 
[**templates_workspace_delete**](TemplatesApi.md#templates_workspace_delete) | **DELETE** /workspaces/{workspace}/templates | 
[**templates_workspace_get**](TemplatesApi.md#templates_workspace_get) | **GET** /workspaces/{workspace}/templates | List of templates for workspace
[**templates_workspace_post**](TemplatesApi.md#templates_workspace_post) | **POST** /workspaces/{workspace}/templates | 
[**templates_workspace_put**](TemplatesApi.md#templates_workspace_put) | **PUT** /workspaces/{workspace}/templates | 


# **template_coverage_delete**
> template_coverage_delete(workspace, store, coverage, template)

Delete a template.

Deletes a single template registered for use by a coverage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
coverage = 'coverage_example' # str | The coverage name
template = 'template_example' # str | The template name

try:
    # Delete a template.
    api_instance.template_coverage_delete(workspace, store, coverage, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_coverage_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **coverage** | **str**| The coverage name | 
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_coverage_get**
> Templates template_coverage_get(workspace, store, coverage, template)

Return a template for a coverage

Displays a single template registered for use by a coverage (example for GetFeatureInfo WMS operation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
coverage = 'coverage_example' # str | The coverage name
template = 'template_example' # str | The template name

try:
    # Return a template for a coverage
    api_response = api_instance.template_coverage_get(workspace, store, coverage, template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_coverage_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **coverage** | **str**| The coverage name | 
 **template** | **str**| The template name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_coverage_post**
> template_coverage_post(workspace, store, coverage, template)



Invalid. Use PUT to insert a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
coverage = 'coverage_example' # str | The coverage name
template = 'template_example' # str | The template name

try:
    api_instance.template_coverage_post(workspace, store, coverage, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_coverage_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **coverage** | **str**| The coverage name | 
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_coverage_put**
> template_coverage_put(workspace, store, coverage, template)

Insert or update a template

Inserts or updates a single template registered for use by a coverage (example for GetFeatureInfo WMS operation). Overwrites any existing template with the same name and location.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
coverage = 'coverage_example' # str | The coverage name
template = 'template_example' # str | The template content to upload

try:
    # Insert or update a template
    api_instance.template_coverage_put(workspace, store, coverage, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_coverage_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **coverage** | **str**| The coverage name | 
 **template** | **str**| The template content to upload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_cs_delete**
> template_data_store_cs_delete(workspace, store, template)

Delete a template.

Deletes a single template registered for use by all layers generated by a coverage store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
template = 'template_example' # str | The template name

try:
    # Delete a template.
    api_instance.template_data_store_cs_delete(workspace, store, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_cs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_cs_get**
> Templates template_data_store_cs_get(workspace, store, template)

Return a template for a coverage store

Displays a single template registered for use by all layers generated by a coverage store (example for GetFeatureInfo WMS operation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
template = 'template_example' # str | The template name

try:
    # Return a template for a coverage store
    api_response = api_instance.template_data_store_cs_get(workspace, store, template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_cs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **template** | **str**| The template name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_cs_post**
> template_data_store_cs_post(workspace, store, template)



Invalid. Use PUT to insert a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
template = 'template_example' # str | The template name

try:
    api_instance.template_data_store_cs_post(workspace, store, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_cs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_cs_put**
> template_data_store_cs_put(workspace, store, template)

Insert or update a template

Inserts or updates a single template registered for use by all layers generated by a coverage store (example for GetFeatureInfo WMS operation). Overwrites any existing template with the same name and location.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
template = 'template_example' # str | The template content to upload

try:
    # Insert or update a template
    api_instance.template_data_store_cs_put(workspace, store, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_cs_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **template** | **str**| The template content to upload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_delete**
> template_data_store_delete(workspace, store, template)

Delete a template.

Deletes a single template registered for use by all layers generated by a data store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
template = 'template_example' # str | The template name

try:
    # Delete a template.
    api_instance.template_data_store_delete(workspace, store, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_ft_delete**
> template_data_store_ft_delete(workspace, store, type, template)

Delete a template.

Deletes a single template registered for use by a feature type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
type = 'type_example' # str | The feature type name
template = 'template_example' # str | The template name

try:
    # Delete a template.
    api_instance.template_data_store_ft_delete(workspace, store, type, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_ft_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **type** | **str**| The feature type name | 
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_ft_get**
> Templates template_data_store_ft_get(workspace, store, type, template)

Return a template for a feature type.

Displays a single template registered for use by a feature type (example for GetFeatureInfo WMS operation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
type = 'type_example' # str | The feature type name
template = 'template_example' # str | The template name

try:
    # Return a template for a feature type.
    api_response = api_instance.template_data_store_ft_get(workspace, store, type, template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_ft_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **type** | **str**| The feature type name | 
 **template** | **str**| The template name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_ft_post**
> template_data_store_ft_post(workspace, store, type, template)



Invalid. Use PUT to insert a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
type = 'type_example' # str | The feature type name
template = 'template_example' # str | The template name

try:
    api_instance.template_data_store_ft_post(workspace, store, type, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_ft_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **type** | **str**| The feature type name | 
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_ft_put**
> template_data_store_ft_put(workspace, store, type, template)

Insert or update a template

Inserts or updates a single template registered for use by a feature type (example for GetFeatureInfo WMS operation). Overwrites any existing template with the same name and location.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
type = 'type_example' # str | The feature type name
template = 'template_example' # str | The template content to upload

try:
    # Insert or update a template
    api_instance.template_data_store_ft_put(workspace, store, type, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_ft_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **type** | **str**| The feature type name | 
 **template** | **str**| The template content to upload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_get**
> Templates template_data_store_get(workspace, store, template)

Return a template for a data store

Displays a single template registered for use by all layers generated by a data store (example for GetFeatureInfo WMS operation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
template = 'template_example' # str | The template name

try:
    # Return a template for a data store
    api_response = api_instance.template_data_store_get(workspace, store, template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **template** | **str**| The template name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_post**
> template_data_store_post(workspace, store, template)



Invalid. Use PUT to insert a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
template = 'template_example' # str | The template name

try:
    api_instance.template_data_store_post(workspace, store, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_data_store_put**
> template_data_store_put(workspace, store, template)

Insert or update a template

Inserts or updates a single template registered for use by all layers generated by a data store (example for GetFeatureInfo WMS operation). Overwrites any existing template with the same name and location.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
template = 'template_example' # str | The template content to upload

try:
    # Insert or update a template
    api_instance.template_data_store_put(workspace, store, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_data_store_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **template** | **str**| The template content to upload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_delete**
> template_delete(template)

Delete a template.

Deletes a single template registered for use on the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
template = 'template_example' # str | The template name

try:
    # Delete a template.
    api_instance.template_delete(template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_get**
> Templates template_get(template)

Return a template

Displays a single template registered for use on the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
template = 'template_example' # str | The template name

try:
    # Return a template
    api_response = api_instance.template_get(template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**| The template name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_post**
> template_post(template)



Invalid. Use PUT to insert a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
template = 'template_example' # str | The template name

try:
    api_instance.template_post(template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_put**
> template_put(template)

Insert or update a template

Inserts or updates a single template registered for use on the server. Overwrites any existing template with the same name and location.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
template = 'template_example' # str | The template content to upload

try:
    # Insert or update a template
    api_instance.template_put(template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**| The template content to upload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_workspace_delete**
> template_workspace_delete(workspace, template)

Delete a template.

Deletes a single template registered for use in a workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
template = 'template_example' # str | The template name

try:
    # Delete a template.
    api_instance.template_workspace_delete(workspace, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_workspace_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_workspace_get**
> Templates template_workspace_get(workspace, template)

Return a template for workspace

Displays a single template registered for use in a workspace (example for GetFeatureInfo WMS operation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
template = 'template_example' # str | The template name

try:
    # Return a template for workspace
    api_response = api_instance.template_workspace_get(workspace, template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_workspace_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **template** | **str**| The template name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_workspace_post**
> template_workspace_post(workspace, template)



Invalid. Use PUT to insert a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
template = 'template_example' # str | The template name

try:
    api_instance.template_workspace_post(workspace, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_workspace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **template** | **str**| The template name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **template_workspace_put**
> template_workspace_put(workspace, template)

Insert or update a template

Inserts or updates a single template registered for use in a workspace (example for GetFeatureInfo WMS operation). Overwrites any existing template with the same name and location.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
template = 'template_example' # str | The template content to upload

try:
    # Insert or update a template
    api_instance.template_workspace_put(workspace, template)
except ApiException as e:
    print("Exception when calling TemplatesApi->template_workspace_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **template** | **str**| The template content to upload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_coverage_delete**
> templates_coverage_delete(workspace, store, coverage)



Invalid. Delete from `/{template}` to remove a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
coverage = 'coverage_example' # str | The coverage name

try:
    api_instance.templates_coverage_delete(workspace, store, coverage)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_coverage_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **coverage** | **str**| The coverage name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_coverage_get**
> Templates templates_coverage_get(workspace, store, coverage)

List of templates for a coverage

Displays a list of templates registered for use by a coverage (example for GetFeatureInfo WMS operation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
coverage = 'coverage_example' # str | The coverage name

try:
    # List of templates for a coverage
    api_response = api_instance.templates_coverage_get(workspace, store, coverage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_coverage_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **coverage** | **str**| The coverage name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_coverage_post**
> templates_coverage_post(workspace, store, coverage)



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
coverage = 'coverage_example' # str | The coverage name

try:
    api_instance.templates_coverage_post(workspace, store, coverage)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_coverage_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **coverage** | **str**| The coverage name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_coverage_put**
> templates_coverage_put(workspace, store, coverage)



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
coverage = 'coverage_example' # str | The coverage name

try:
    api_instance.templates_coverage_put(workspace, store, coverage)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_coverage_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **coverage** | **str**| The coverage name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_cs_delete**
> templates_data_store_cs_delete(workspace, store)



Invalid. Delete from `/{template}` to remove a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name

try:
    api_instance.templates_data_store_cs_delete(workspace, store)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_cs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_cs_get**
> Templates templates_data_store_cs_get(workspace, store)

List of templates for a coverage store

Displays a list of templates registered for use by all layers generated by a coverage store (example for GetFeatureInfo WMS operation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name

try:
    # List of templates for a coverage store
    api_response = api_instance.templates_data_store_cs_get(workspace, store)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_cs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_cs_post**
> templates_data_store_cs_post(workspace, store)



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name

try:
    api_instance.templates_data_store_cs_post(workspace, store)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_cs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_cs_put**
> templates_data_store_cs_put(workspace, store)



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name

try:
    api_instance.templates_data_store_cs_put(workspace, store)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_cs_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_delete**
> templates_data_store_delete(workspace, store)



Invalid. Delete from `/{template}` to remove a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name

try:
    api_instance.templates_data_store_delete(workspace, store)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_ft_delete**
> templates_data_store_ft_delete(workspace, store, type)



Invalid. Delete from `/{template}` to remove a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
type = 'type_example' # str | The feature type name

try:
    api_instance.templates_data_store_ft_delete(workspace, store, type)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_ft_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **type** | **str**| The feature type name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_ft_get**
> Templates templates_data_store_ft_get(workspace, store, type)

List of templates for a feature type.

Displays a list of templates registered for use by feature type (example for GetFeatureInfo WMS operation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
type = 'type_example' # str | The feature type name

try:
    # List of templates for a feature type.
    api_response = api_instance.templates_data_store_ft_get(workspace, store, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_ft_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **type** | **str**| The feature type name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_ft_post**
> templates_data_store_ft_post(workspace, store, type)



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
type = 'type_example' # str | The feature type name

try:
    api_instance.templates_data_store_ft_post(workspace, store, type)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_ft_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **type** | **str**| The feature type name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_ft_put**
> templates_data_store_ft_put(workspace, store, type)



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name
type = 'type_example' # str | The feature type name

try:
    api_instance.templates_data_store_ft_put(workspace, store, type)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_ft_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 
 **type** | **str**| The feature type name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_get**
> Templates templates_data_store_get(workspace, store)

List of templates for a data store

Displays a list of templates registered for use by all layers generated by a data store (example for GetFeatureInfo WMS operation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name

try:
    # List of templates for a data store
    api_response = api_instance.templates_data_store_get(workspace, store)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_post**
> templates_data_store_post(workspace, store)



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name

try:
    api_instance.templates_data_store_post(workspace, store)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_data_store_put**
> templates_data_store_put(workspace, store)



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name
store = 'store_example' # str | The store name

try:
    api_instance.templates_data_store_put(workspace, store)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_data_store_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 
 **store** | **str**| The store name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_delete**
> templates_delete()



Invalid. Delete from `/{template}` to remove a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()

try:
    api_instance.templates_delete()
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_delete: %s\n" % e)
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

# **templates_get**
> Templates templates_get()

List of templates for the server

Displays a list of templates registered for use on the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()

try:
    # List of templates for the server
    api_response = api_instance.templates_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_post**
> templates_post()



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()

try:
    api_instance.templates_post()
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_post: %s\n" % e)
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

# **templates_put**
> templates_put()



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()

try:
    api_instance.templates_put()
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_put: %s\n" % e)
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

# **templates_workspace_delete**
> templates_workspace_delete(workspace)



Invalid. Delete from `/{template}` to remove a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.templates_workspace_delete(workspace)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_workspace_delete: %s\n" % e)
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

# **templates_workspace_get**
> Templates templates_workspace_get(workspace)

List of templates for workspace

Displays a list of templates registered for use in a workspace (example for GetFeatureInfo WMS operation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    # List of templates for workspace
    api_response = api_instance.templates_workspace_get(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_workspace_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**Templates**](Templates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_workspace_post**
> templates_workspace_post(workspace)



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.templates_workspace_post(workspace)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_workspace_post: %s\n" % e)
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

# **templates_workspace_put**
> templates_workspace_put(workspace)



Invalid. PUT to `/{template}` to edit a template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TemplatesApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.templates_workspace_put(workspace)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_workspace_put: %s\n" % e)
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

