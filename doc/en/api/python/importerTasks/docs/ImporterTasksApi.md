# swagger_client.ImporterTasksApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_task**](ImporterTasksApi.md#delete_task) | **DELETE** /imports/{importId}/tasks/{taskId} | Remove task with id {taskId} within import with id {importId}
[**get_task**](ImporterTasksApi.md#get_task) | **GET** /imports/{importId}/tasks/{taskId} | Retrieve task with id {taskId} within import with id {importId}
[**get_task_layer**](ImporterTasksApi.md#get_task_layer) | **GET** /imports/{importId}/tasks/{taskId}/layer | Retrieve the layer of a task with id {taskId} within import with id {importId}
[**get_task_progress**](ImporterTasksApi.md#get_task_progress) | **GET** /imports/{importId}/tasks/{taskId}/progress | Retrieve the current state and import progress of a task with id {taskId} within import with id {importId}
[**get_task_target**](ImporterTasksApi.md#get_task_target) | **GET** /imports/{importId}/tasks/{taskId}/target | Retrieve the store of a task with id {taskId} within import with id {importId}
[**get_tasks**](ImporterTasksApi.md#get_tasks) | **GET** /imports/{importId}/tasks | Retrieve all tasks for import with id {importId}
[**post_task**](ImporterTasksApi.md#post_task) | **POST** /imports/{importId}/tasks | Create a new task
[**put_task**](ImporterTasksApi.md#put_task) | **PUT** /imports/{importId}/tasks/{taskId} | Modify task with id {taskId} within import with id {importId}
[**put_task_file**](ImporterTasksApi.md#put_task_file) | **PUT** /imports/{importId}/tasks/{filename} | Create a new task
[**put_task_layer**](ImporterTasksApi.md#put_task_layer) | **PUT** /imports/{importId}/tasks/{taskId}/layer | Modify the target layer for a task with id {taskId} within import with id {importId}
[**put_task_target**](ImporterTasksApi.md#put_task_target) | **PUT** /imports/{importId}/tasks/{taskId}/target | Modify the target store for a task with id {taskId} within import with id {importId}


# **delete_task**
> delete_task(import_id, task_id)

Remove task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task

try:
    # Remove task with id {taskId} within import with id {importId}
    api_instance.delete_task(import_id, task_id)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> Task get_task(import_id, task_id, expand=expand)

Retrieve task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Retrieve task with id {taskId} within import with id {importId}
    api_response = api_instance.get_task(import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_layer**
> Layer get_task_layer(import_id, task_id, expand=expand)

Retrieve the layer of a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Retrieve the layer of a task with id {taskId} within import with id {importId}
    api_response = api_instance.get_task_layer(import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->get_task_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**Layer**](Layer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_progress**
> Progress get_task_progress(import_id, task_id)

Retrieve the current state and import progress of a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task

try:
    # Retrieve the current state and import progress of a task with id {taskId} within import with id {importId}
    api_response = api_instance.get_task_progress(import_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->get_task_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 

### Return type

[**Progress**](Progress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/htm

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_target**
> Store get_task_target(import_id, task_id, expand=expand)

Retrieve the store of a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Retrieve the store of a task with id {taskId} within import with id {importId}
    api_response = api_instance.get_task_target(import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->get_task_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**Store**](Store.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> Tasks get_tasks(import_id, expand=expand)

Retrieve all tasks for import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
expand = 'none' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to none)

try:
    # Retrieve all tasks for import with id {importId}
    api_response = api_instance.get_tasks(import_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to none]

### Return type

[**Tasks**](Tasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_task**
> Task post_task(import_id, task_body, expand=expand)

Create a new task

A new task can be created by issuing a POST to imports/<importId>/tasks as a \"Content-type: multipart/form-data\" multipart encoded data as defined by RFC 2388. One or more file can be uploaded this way, and a task will be created for importing them. In case the file being uploaded is a zip file, it will be unzipped on the server side and treated as a directory of files. Alternatively, a new task can be created by issuing a POST as a \"Content-type: application/x-www-form-urlencoded\" form url encoded data containing a url paramerter with the location of the uploaded file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
task_body = swagger_client.Task() # Task | The task to create or modify
expand = 'none' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to none)

try:
    # Create a new task
    api_response = api_instance.post_task(import_id, task_body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->post_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_body** | [**Task**](Task.md)| The task to create or modify | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to none]

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json, text/htm

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task**
> Task put_task(import_id, task_id, task_body, expand=expand)

Modify task with id {taskId} within import with id {importId}

A PUT request over an existing task can be used to update its representation. The representation can be partial, and just contains the elements that need to be updated. The updateMode of a task normally starts as \"CREATE\", that is, create the target resource if missing. Other possible values are \"REPLACE\", that is, delete the existing features in the target layer and replace them with the task source ones, or \"APPEND\", to just add the features from the task source into an existing layer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
task_body = swagger_client.Task() # Task | The task to create or modify
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Modify task with id {taskId} within import with id {importId}
    api_response = api_instance.put_task(import_id, task_id, task_body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->put_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **task_body** | [**Task**](Task.md)| The task to create or modify | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task_file**
> Tasks put_task_file(import_id, filename, file_body, expand=expand)

Create a new task

A new task can be created by issuing a PUT containing the raw file content to this endpoint. The name of the uploaded file will be {filename}. The location of the uploaded file will be the top level directory associated with the import, or the \"uploads\" directory in the data directory if no directory is associated with the current import.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
filename = 'filename_example' # str | The filename
file_body = 'B' # str | The file contents to upload.
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Create a new task
    api_response = api_instance.put_task_file(import_id, filename, file_body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->put_task_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **filename** | **str**| The filename | 
 **file_body** | **str**| The file contents to upload. | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**Tasks**](Tasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: \\*/*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task_layer**
> Task put_task_layer(import_id, task_id, layer_body, expand=expand)

Modify the target layer for a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
layer_body = swagger_client.Layer() # Layer | The layer to modify
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Modify the target layer for a task with id {taskId} within import with id {importId}
    api_response = api_instance.put_task_layer(import_id, task_id, layer_body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->put_task_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **layer_body** | [**Layer**](Layer.md)| The layer to modify | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task_target**
> put_task_target(import_id, task_id, target_body)

Modify the target store for a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterTasksApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
target_body = swagger_client.Store() # Store | The store to modify

try:
    # Modify the target store for a task with id {taskId} within import with id {importId}
    api_instance.put_task_target(import_id, task_id, target_body)
except ApiException as e:
    print("Exception when calling ImporterTasksApi->put_task_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **target_body** | [**Store**](Store.md)| The store to modify | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

