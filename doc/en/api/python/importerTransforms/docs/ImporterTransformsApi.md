# swagger_client.ImporterTransformsApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_transform**](ImporterTransformsApi.md#delete_transform) | **DELETE** /imports/{importId}/tasks/{taskId}/transforms/{transformId} | Removes the transformation
[**get_transform**](ImporterTransformsApi.md#get_transform) | **GET** /imports/{importId}/tasks/{taskId}/transforms/{transformId} | Retrieve a transformation
[**get_transforms**](ImporterTransformsApi.md#get_transforms) | **GET** /imports/{importId}/tasks/{taskId}/transforms | Retrieve transformation list
[**post_transform**](ImporterTransformsApi.md#post_transform) | **POST** /imports/{importId}/tasks/{taskId}/transforms | Create a new transformation
[**put_transform**](ImporterTransformsApi.md#put_transform) | **PUT** /imports/{importId}/tasks/{taskId}/transforms/{transformId} | Modifies a transformation


# **delete_transform**
> delete_transform(import_id, task_id, transform_id)

Removes the transformation

Removes the transformation identified by {transformId} inside a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTransformsApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
transform_id = 'transform_id_example' # str | The ID of the transform

try:
    # Removes the transformation
    api_instance.delete_transform(import_id, task_id, transform_id)
except ApiException as e:
    print("Exception when calling ImporterTransformsApi->delete_transform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **transform_id** | **str**| The ID of the transform | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transform**
> Transform get_transform(import_id, task_id, transform_id, expand=expand)

Retrieve a transformation

Retrieve a transformation identified by {transformId} inside a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTransformsApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
transform_id = 'transform_id_example' # str | The ID of the transform
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \"self\" or \"none\", depending on the request. (optional)

try:
    # Retrieve a transformation
    api_response = api_instance.get_transform(import_id, task_id, transform_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTransformsApi->get_transform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **transform_id** | **str**| The ID of the transform | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \&quot;self\&quot; or \&quot;none\&quot;, depending on the request. | [optional] 

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transforms**
> Transforms get_transforms(import_id, task_id, expand=expand)

Retrieve transformation list

Retrieve the list of transformations of a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTransformsApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \"self\" or \"none\", depending on the request. (optional)

try:
    # Retrieve transformation list
    api_response = api_instance.get_transforms(import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTransformsApi->get_transforms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \&quot;self\&quot; or \&quot;none\&quot;, depending on the request. | [optional] 

### Return type

[**Transforms**](Transforms.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_transform**
> post_transform(import_id, task_id, transform_body, expand=expand)

Create a new transformation

Create a new transformation and append it inside a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTransformsApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
transform_body = swagger_client.Transform() # Transform | The transform to add.
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \"self\" or \"none\", depending on the request. (optional)

try:
    # Create a new transformation
    api_instance.post_transform(import_id, task_id, transform_body, expand=expand)
except ApiException as e:
    print("Exception when calling ImporterTransformsApi->post_transform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **transform_body** | [**Transform**](Transform.md)| The transform to add. | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \&quot;self\&quot; or \&quot;none\&quot;, depending on the request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_transform**
> Transform put_transform(import_id, task_id, transform_id, transform_body, expand=expand)

Modifies a transformation

Modifies the definition of a transformation identified by {transformId} inside a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTransformsApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
transform_id = 'transform_id_example' # str | The ID of the transform
transform_body = swagger_client.Transform() # Transform | The transform to add.
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \"self\" or \"none\", depending on the request. (optional)

try:
    # Modifies a transformation
    api_response = api_instance.put_transform(import_id, task_id, transform_id, transform_body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTransformsApi->put_transform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **transform_id** | **str**| The ID of the transform | 
 **transform_body** | [**Transform**](Transform.md)| The transform to add. | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \&quot;self\&quot; or \&quot;none\&quot;, depending on the request. | [optional] 

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

