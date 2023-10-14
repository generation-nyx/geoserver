# swagger_client.ImporterDataApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_import_data_file**](ImporterDataApi.md#delete_import_data_file) | **DELETE** /imports/{importId}/data/files/{filename} | Remove a specific file with id {filename} from the import with id {importId}. Only applies to file/directory imports.
[**delete_task_data_file**](ImporterDataApi.md#delete_task_data_file) | **DELETE** /imports/{importId}/tasks/{taskId}/data/files/{filename} | Remove a specific file with id {filename} from the task with id {taskId} within import with id {importId}. Only applies to file/directory imports.
[**get_data**](ImporterDataApi.md#get_data) | **GET** /imports/{importId}/data | Retrieve the database connection parameters for an import with id {importId}. Only applies to database imports.
[**get_data_file**](ImporterDataApi.md#get_data_file) | **GET** /imports/{importId}/data/files/{filename} | Retrieve information about the file with id {fileId} from the data of an import with id {importId}. Only applies to file/directory imports.
[**get_data_files**](ImporterDataApi.md#get_data_files) | **GET** /imports/{importId}/data/files | Retrieve the list of files for an import with id {importId}. Only applies to file/directory imports.
[**get_task_data**](ImporterDataApi.md#get_task_data) | **GET** /imports/{importId}/tasks/{taskId}/data | Retrieve the table description for a task with id {taskId} within import with id {importId}. Only applies to database imports.
[**get_task_data_file**](ImporterDataApi.md#get_task_data_file) | **GET** /imports/{importId}/tasks/{taskId}/data/files/{filename} | Retrieve information about the file with id {fileId} from the data of a task with id {taskId} within import with id {importId}. Only applies to file/directory imports.
[**get_task_data_files**](ImporterDataApi.md#get_task_data_files) | **GET** /imports/{importId}/tasks/{taskId}/data/files | Retrieve the list of files for a task with id {taskId} within import with id {importId}. Only applies to file/directory imports.


# **delete_import_data_file**
> delete_import_data_file()

Remove a specific file with id {filename} from the import with id {importId}. Only applies to file/directory imports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterDataApi()

try:
    # Remove a specific file with id {filename} from the import with id {importId}. Only applies to file/directory imports.
    api_instance.delete_import_data_file()
except ApiException as e:
    print("Exception when calling ImporterDataApi->delete_import_data_file: %s\n" % e)
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

# **delete_task_data_file**
> delete_task_data_file()

Remove a specific file with id {filename} from the task with id {taskId} within import with id {importId}. Only applies to file/directory imports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterDataApi()

try:
    # Remove a specific file with id {filename} from the task with id {taskId} within import with id {importId}. Only applies to file/directory imports.
    api_instance.delete_task_data_file()
except ApiException as e:
    print("Exception when calling ImporterDataApi->delete_task_data_file: %s\n" % e)
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

# **get_data**
> Database get_data(import_id, expand=expand)

Retrieve the database connection parameters for an import with id {importId}. Only applies to database imports.

Get import data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterDataApi()
import_id = 'import_id_example' # str | The ID of the import
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Retrieve the database connection parameters for an import with id {importId}. Only applies to database imports.
    api_response = api_instance.get_data(import_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterDataApi->get_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**Database**](Database.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_file**
> File get_data_file(import_id, filename, expand=expand)

Retrieve information about the file with id {fileId} from the data of an import with id {importId}. Only applies to file/directory imports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterDataApi()
import_id = 'import_id_example' # str | The ID of the import
filename = 'filename_example' # str | The filename
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Retrieve information about the file with id {fileId} from the data of an import with id {importId}. Only applies to file/directory imports.
    api_response = api_instance.get_data_file(import_id, filename, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterDataApi->get_data_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **filename** | **str**| The filename | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_files**
> Directory get_data_files(import_id, expand=expand)

Retrieve the list of files for an import with id {importId}. Only applies to file/directory imports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterDataApi()
import_id = 'import_id_example' # str | The ID of the import
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Retrieve the list of files for an import with id {importId}. Only applies to file/directory imports.
    api_response = api_instance.get_data_files(import_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterDataApi->get_data_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**Directory**](Directory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_data**
> Table get_task_data(import_id, task_id, expand=expand)

Retrieve the table description for a task with id {taskId} within import with id {importId}. Only applies to database imports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterDataApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Retrieve the table description for a task with id {taskId} within import with id {importId}. Only applies to database imports.
    api_response = api_instance.get_task_data(import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterDataApi->get_task_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**Table**](Table.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_data_file**
> File get_task_data_file(import_id, task_id, filename, expand=expand)

Retrieve information about the file with id {fileId} from the data of a task with id {taskId} within import with id {importId}. Only applies to file/directory imports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterDataApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
filename = 'filename_example' # str | The filename
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Retrieve information about the file with id {fileId} from the data of a task with id {taskId} within import with id {importId}. Only applies to file/directory imports.
    api_response = api_instance.get_task_data_file(import_id, task_id, filename, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterDataApi->get_task_data_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **filename** | **str**| The filename | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_data_files**
> Directory get_task_data_files(import_id, task_id, expand=expand)

Retrieve the list of files for a task with id {taskId} within import with id {importId}. Only applies to file/directory imports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImporterDataApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'self' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional) (default to self)

try:
    # Retrieve the list of files for a task with id {taskId} within import with id {importId}. Only applies to file/directory imports.
    api_response = api_instance.get_task_data_files(import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterDataApi->get_task_data_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#39;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] [default to self]

### Return type

[**Directory**](Directory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

