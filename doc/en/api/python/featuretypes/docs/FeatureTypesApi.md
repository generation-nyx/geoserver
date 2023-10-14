# swagger_client.FeatureTypesApi

All URIs are relative to *http://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_feature_type**](FeatureTypesApi.md#delete_feature_type) | **DELETE** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes/{featureTypeName} | 
[**delete_feature_type_0**](FeatureTypesApi.md#delete_feature_type_0) | **DELETE** /workspaces/{workspaceName}/featuretypes/{featureTypeName} | 
[**delete_feature_types**](FeatureTypesApi.md#delete_feature_types) | **DELETE** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes | 
[**delete_feature_types_0**](FeatureTypesApi.md#delete_feature_types_0) | **DELETE** /workspaces/{workspaceName}/featuretypes | 
[**get_feature_type**](FeatureTypesApi.md#get_feature_type) | **GET** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes/{featureTypeName} | 
[**get_feature_type_0**](FeatureTypesApi.md#get_feature_type_0) | **GET** /workspaces/{workspaceName}/featuretypes/{featureTypeName} | 
[**get_feature_types**](FeatureTypesApi.md#get_feature_types) | **GET** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes | 
[**get_feature_types_0**](FeatureTypesApi.md#get_feature_types_0) | **GET** /workspaces/{workspaceName}/featuretypes | 
[**post_feature_type**](FeatureTypesApi.md#post_feature_type) | **POST** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes/{featureTypeName} | 
[**post_feature_type_0**](FeatureTypesApi.md#post_feature_type_0) | **POST** /workspaces/{workspaceName}/featuretypes/{featureTypeName} | 
[**post_feature_type_reset**](FeatureTypesApi.md#post_feature_type_reset) | **POST** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes/{featureTypeName}/reset | Reset the caches related to this specific feature type
[**post_feature_type_reset_0**](FeatureTypesApi.md#post_feature_type_reset_0) | **POST** /workspaces/{workspaceName}/featuretypes/{featureTypeName}/reset | Reset the caches related to this specific feature type
[**post_feature_types**](FeatureTypesApi.md#post_feature_types) | **POST** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes | 
[**post_feature_types_0**](FeatureTypesApi.md#post_feature_types_0) | **POST** /workspaces/{workspaceName}/featuretypes | 
[**put_feature_type**](FeatureTypesApi.md#put_feature_type) | **PUT** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes/{featureTypeName} | 
[**put_feature_type_0**](FeatureTypesApi.md#put_feature_type_0) | **PUT** /workspaces/{workspaceName}/featuretypes/{featureTypeName} | 
[**put_feature_type_reset**](FeatureTypesApi.md#put_feature_type_reset) | **PUT** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes/{featureTypeName}/reset | Reset the caches related to this specific feature type.
[**put_feature_type_reset_0**](FeatureTypesApi.md#put_feature_type_reset_0) | **PUT** /workspaces/{workspaceName}/featuretypes/{featureTypeName}/reset | Reset the caches related to this specific feature type.
[**put_feature_types**](FeatureTypesApi.md#put_feature_types) | **PUT** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes | 
[**put_feature_types_0**](FeatureTypesApi.md#put_feature_types_0) | **PUT** /workspaces/{workspaceName}/featuretypes | 


# **delete_feature_type**
> delete_feature_type(workspace_name, store_name, feature_type_name, recurse=recurse)



Delete a feature type (optionally recursively deleting layers).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
store_name = 'store_name_example' # str | The name of the datastore
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
recurse = false # bool | Recursively deletes all layers referenced by the specified featuretype. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layers reference the featuretype. (optional) (default to false)

try:
    api_instance.delete_feature_type(workspace_name, store_name, feature_type_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->delete_feature_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **store_name** | **str**| The name of the datastore | 
 **feature_type_name** | **str**| The name of the feature type | 
 **recurse** | **bool**| Recursively deletes all layers referenced by the specified featuretype. Allowed values for this parameter are true or false. The default value is false. A request with &#39;recurse&#x3D;false&#39; will fail if any layers reference the featuretype. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_type_0**
> delete_feature_type_0(workspace_name, feature_type_name, recurse=recurse)



Delete a feature type in the default data store for the workspace (optionally recursively deleting layers).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
recurse = false # bool | Recursively deletes all layers referenced by the specified featuretype. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layers reference the featuretype. (optional) (default to false)

try:
    api_instance.delete_feature_type_0(workspace_name, feature_type_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->delete_feature_type_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **feature_type_name** | **str**| The name of the feature type | 
 **recurse** | **bool**| Recursively deletes all layers referenced by the specified featuretype. Allowed values for this parameter are true or false. The default value is false. A request with &#39;recurse&#x3D;false&#39; will fail if any layers reference the featuretype. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_types**
> delete_feature_types()



Invalid.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.delete_feature_types()
except ApiException as e:
    print("Exception when calling FeatureTypesApi->delete_feature_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_types_0**
> delete_feature_types_0()



Invalid.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.delete_feature_types_0()
except ApiException as e:
    print("Exception when calling FeatureTypesApi->delete_feature_types_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_type**
> InlineResponse2001 get_feature_type(workspace_name, store_name, feature_type_name, quiet_on_not_found=quiet_on_not_found)



Get an individual feature type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
store_name = 'store_name_example' # str | The name of the datastore
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
quiet_on_not_found = false # bool | Prevents logging an Exception when the feature type is not present. Note that 404 status code will be returned anyway. Defaults to \"false\". (optional) (default to false)

try:
    api_response = api_instance.get_feature_type(workspace_name, store_name, feature_type_name, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->get_feature_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **store_name** | **str**| The name of the datastore | 
 **feature_type_name** | **str**| The name of the feature type | 
 **quiet_on_not_found** | **bool**| Prevents logging an Exception when the feature type is not present. Note that 404 status code will be returned anyway. Defaults to \&quot;false\&quot;. | [optional] [default to false]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_type_0**
> InlineResponse2001 get_feature_type_0(workspace_name, feature_type_name, quiet_on_not_found=quiet_on_not_found)



Get an individual feature type in the default data store for the workspace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
quiet_on_not_found = false # bool | Prevents logging an Exception when the feature type is not present. Note that 404 status code will be returned anyway. Defaults to \"false\". (optional) (default to false)

try:
    api_response = api_instance.get_feature_type_0(workspace_name, feature_type_name, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->get_feature_type_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **feature_type_name** | **str**| The name of the feature type | 
 **quiet_on_not_found** | **bool**| Prevents logging an Exception when the feature type is not present. Note that 404 status code will be returned anyway. Defaults to \&quot;false\&quot;. | [optional] [default to false]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_types**
> InlineResponse200 get_feature_types(workspace_name, store_name, list=list)



Get a list of feature types for the workspace and datastore. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/featuretypes.xml\" for XML) 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
store_name = 'store_name_example' # str | The name of the datastore
list = 'list_example' # str | The list parameter is used to control the category of feature types that are returned. Must be one of \"configured\", \"available\", \"available_with_geom\", \"all\"  (optional)

try:
    api_response = api_instance.get_feature_types(workspace_name, store_name, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->get_feature_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **store_name** | **str**| The name of the datastore | 
 **list** | **str**| The list parameter is used to control the category of feature types that are returned. Must be one of \&quot;configured\&quot;, \&quot;available\&quot;, \&quot;available_with_geom\&quot;, \&quot;all\&quot;  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_types_0**
> InlineResponse200 get_feature_types_0(workspace_name, list=list)



Get a list of all feature types for all datastores in the workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/featuretypes.xml\" for XML) 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
list = 'list_example' # str | The list parameter is used to control the category of feature types that are returned. Must be one of \"configured\", \"available\", \"available_with_geom\", \"all\"  (optional)

try:
    api_response = api_instance.get_feature_types_0(workspace_name, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->get_feature_types_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **list** | **str**| The list parameter is used to control the category of feature types that are returned. Must be one of \&quot;configured\&quot;, \&quot;available\&quot;, \&quot;available_with_geom\&quot;, \&quot;all\&quot;  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feature_type**
> post_feature_type()



Invalid. Use POST on the /featuretypes endpoint to add a new feature type, or PUT on an individual feature type to edit that type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.post_feature_type()
except ApiException as e:
    print("Exception when calling FeatureTypesApi->post_feature_type: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feature_type_0**
> post_feature_type_0()



Invalid. Use POST on the /featuretypes endpoint to add a new feature type, or PUT on an individual feature type to edit that type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.post_feature_type_0()
except ApiException as e:
    print("Exception when calling FeatureTypesApi->post_feature_type_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feature_type_reset**
> post_feature_type_reset(workspace_name, store_name, feature_type_name)

Reset the caches related to this specific feature type

Resets caches for this feature type. This operation is used to force GeoServer to drop cached feature type structures, and eventually re-compute them the next time it is needed by a request. This is useful as both GeoServer and the underlying data store can keep state information about a feature type attributes. Warning, if an explicit list of attributes is configured in the feature type, to support attribute selection, renaming, data type conversion and calculation of new attributes, the reset itself won't change such configuration, an explicit PUT on the feature type resource is required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data store.
store_name = 'store_name_example' # str | The name of the data store.
feature_type_name = 'feature_type_name_example' # str | The name of the feature type

try:
    # Reset the caches related to this specific feature type
    api_instance.post_feature_type_reset(workspace_name, store_name, feature_type_name)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->post_feature_type_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data store. | 
 **store_name** | **str**| The name of the data store. | 
 **feature_type_name** | **str**| The name of the feature type | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feature_type_reset_0**
> post_feature_type_reset_0(workspace_name, feature_type_name)

Reset the caches related to this specific feature type

Resets caches for this feature type. This operation is used to force GeoServer to drop cached feature type structures, and eventually re-compute them the next time it is needed by a request. This is useful as both GeoServer and the underlying data store can keep state information about a feature type attributes. Warning, if an explicit list of attributes is configured in the feature type, to support attribute selection, renaming, data type conversion and calculation of new attributes, the reset itself won't change such configuration, an explicit PUT on the feature type resource is required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data store.
feature_type_name = 'feature_type_name_example' # str | The name of the feature type

try:
    # Reset the caches related to this specific feature type
    api_instance.post_feature_type_reset_0(workspace_name, feature_type_name)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->post_feature_type_reset_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data store. | 
 **feature_type_name** | **str**| The name of the feature type | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feature_types**
> post_feature_types(workspace_name, store_name, feature_type)



Create a new feature type. Note -  when creating a new feature type via POST, if no underlying dataset with the specified name exists an attempt will be made to create it. This will work only in cases where the underlying data format supports the creation of new types (such as a database). When creating a feature type in this manner the client should include all attribute information in the feature type representation. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
store_name = 'store_name_example' # str | The name of the datastore
feature_type = swagger_client.FeatureTypeInfo() # FeatureTypeInfo | The body of the feature type to POST

try:
    api_instance.post_feature_types(workspace_name, store_name, feature_type)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->post_feature_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **store_name** | **str**| The name of the datastore | 
 **feature_type** | [**FeatureTypeInfo**](FeatureTypeInfo.md)| The body of the feature type to POST | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feature_types_0**
> post_feature_types_0(workspace_name, feature_type)



Create a new feature type, the feature type definition needs to reference a store. Note -  when creating a new feature type via POST, if no underlying dataset with the specified name exists an attempt will be made to create it. This will work only in cases where the underlying data format supports the creation of new types (such as a database). When creating a feature type in this manner the client should include all attribute information in the feature type representation. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
feature_type = swagger_client.FeatureTypeInfo() # FeatureTypeInfo | The body of the feature type to POST

try:
    api_instance.post_feature_types_0(workspace_name, feature_type)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->post_feature_types_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **feature_type** | [**FeatureTypeInfo**](FeatureTypeInfo.md)| The body of the feature type to POST | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_feature_type**
> put_feature_type(workspace_name, store_name, feature_type_name, feature_type, recalculate=recalculate)



Update an individual feature type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
store_name = 'store_name_example' # str | The name of the datastore
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
feature_type = swagger_client.FeatureTypeInfo() # FeatureTypeInfo | The body of the feature type to POST
recalculate = ['recalculate_example'] # list[str] | Specifies whether to recalculate properties for a feature type. Some properties of feature types are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter 'recalculate=' is useful avoid slow recalculation when operating against large datasets as 'recalculate=' avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter 'recalculate=nativebbox' is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - 'recalculate=nativebbox,latlonbbox' can be used after a bulk import to recalculate both the native bounding box and the lat/lon bounding box. Finally, 'recalculate=attributes' can be  used to reset the attributes and reload them from the original vector source. Pay attention to its usage, if attributes were explicity configured to perform attribute selection, renaming, and other transformations, such configuration will be lost, resetting the feature type to the list of attributes found in the vector data source. (optional)

try:
    api_instance.put_feature_type(workspace_name, store_name, feature_type_name, feature_type, recalculate=recalculate)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->put_feature_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **store_name** | **str**| The name of the datastore | 
 **feature_type_name** | **str**| The name of the feature type | 
 **feature_type** | [**FeatureTypeInfo**](FeatureTypeInfo.md)| The body of the feature type to POST | 
 **recalculate** | [**list[str]**](str.md)| Specifies whether to recalculate properties for a feature type. Some properties of feature types are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter &#39;recalculate&#x3D;&#39; is useful avoid slow recalculation when operating against large datasets as &#39;recalculate&#x3D;&#39; avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter &#39;recalculate&#x3D;nativebbox&#39; is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - &#39;recalculate&#x3D;nativebbox,latlonbbox&#39; can be used after a bulk import to recalculate both the native bounding box and the lat/lon bounding box. Finally, &#39;recalculate&#x3D;attributes&#39; can be  used to reset the attributes and reload them from the original vector source. Pay attention to its usage, if attributes were explicity configured to perform attribute selection, renaming, and other transformations, such configuration will be lost, resetting the feature type to the list of attributes found in the vector data source. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xml, text/xml, application/json, text/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_feature_type_0**
> put_feature_type_0(workspace_name, feature_type_name, feature_type, recalculate=recalculate)



Update an individual feature type in the default data store for the workspace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
feature_type = swagger_client.FeatureTypeInfo() # FeatureTypeInfo | The body of the feature type to POST
recalculate = ['recalculate_example'] # list[str] | Specifies whether to recalculate any bounding boxes for a feature type. Some properties of feature types are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter 'recalculate=' is useful avoid slow recalculation when operating against large datasets as 'recalculate=' avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter 'recalculate=nativebbox' is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - 'recalculate=nativebbox,latlonbbox' can be used after a bulk import to recalculate both the native bounding box and the lat/lon bounding box. (optional)

try:
    api_instance.put_feature_type_0(workspace_name, feature_type_name, feature_type, recalculate=recalculate)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->put_feature_type_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **feature_type_name** | **str**| The name of the feature type | 
 **feature_type** | [**FeatureTypeInfo**](FeatureTypeInfo.md)| The body of the feature type to POST | 
 **recalculate** | [**list[str]**](str.md)| Specifies whether to recalculate any bounding boxes for a feature type. Some properties of feature types are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter &#39;recalculate&#x3D;&#39; is useful avoid slow recalculation when operating against large datasets as &#39;recalculate&#x3D;&#39; avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter &#39;recalculate&#x3D;nativebbox&#39; is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - &#39;recalculate&#x3D;nativebbox,latlonbbox&#39; can be used after a bulk import to recalculate both the native bounding box and the lat/lon bounding box. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xml, text/xml, application/json, text/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_feature_type_reset**
> put_feature_type_reset(workspace_name, store_name, feature_type_name)

Reset the caches related to this specific feature type.

Resets caches for this feature type. This operation is used to force GeoServer to drop cached feature type structures, and eventually re-compute them the next time it is needed by a request. This is useful as both GeoServer and the underlying data store can keep state information about a feature type attributes. Warning, if an explicit list of attributes is configured in the feature type, to support attribute selection, renaming, data type conversion and calculation of new attributes, the reset itself won't change such configuration, an explicit PUT on the feature type resource is required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data store.
store_name = 'store_name_example' # str | The name of the data store.
feature_type_name = 'feature_type_name_example' # str | The name of the feature type

try:
    # Reset the caches related to this specific feature type.
    api_instance.put_feature_type_reset(workspace_name, store_name, feature_type_name)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->put_feature_type_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data store. | 
 **store_name** | **str**| The name of the data store. | 
 **feature_type_name** | **str**| The name of the feature type | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_feature_type_reset_0**
> put_feature_type_reset_0(workspace_name, feature_type_name)

Reset the caches related to this specific feature type.

Resets caches for this feature type. This operation is used to force GeoServer to drop cached feature type structures, and eventually re-compute them the next time it is needed by a request. This is useful as both GeoServer and the underlying data store can keep state information about a feature type attributes. Warning, if an explicit list of attributes is configured in the feature type, to support attribute selection, renaming, data type conversion and calculation of new attributes, the reset itself won't change such configuration, an explicit PUT on the feature type resource is required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data store.
feature_type_name = 'feature_type_name_example' # str | The name of the feature type

try:
    # Reset the caches related to this specific feature type.
    api_instance.put_feature_type_reset_0(workspace_name, feature_type_name)
except ApiException as e:
    print("Exception when calling FeatureTypesApi->put_feature_type_reset_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data store. | 
 **feature_type_name** | **str**| The name of the feature type | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_feature_types**
> put_feature_types()



Invalid. Use POST for adding a new feature type, or PUT on an individual feature type to edit that type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.put_feature_types()
except ApiException as e:
    print("Exception when calling FeatureTypesApi->put_feature_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_feature_types_0**
> put_feature_types_0()



Invalid. Use POST for adding a new feature type, or PUT on an individual feature type to edit that type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.FeatureTypesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.put_feature_types_0()
except ApiException as e:
    print("Exception when calling FeatureTypesApi->put_feature_types_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

