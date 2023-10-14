# swagger_client.WorkspacesApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspaceName} | 
[**delete_workspaces**](WorkspacesApi.md#delete_workspaces) | **DELETE** /workspaces | 
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspaceName} | Retrieve a layer group
[**get_workspaces**](WorkspacesApi.md#get_workspaces) | **GET** /workspaces | Get a list of workspaces
[**post_workspace**](WorkspacesApi.md#post_workspace) | **POST** /workspaces/{workspaceName} | 
[**post_workspaces**](WorkspacesApi.md#post_workspaces) | **POST** /workspaces | add a new workspace to GeoServer
[**put_workspace**](WorkspacesApi.md#put_workspace) | **PUT** /workspaces/{workspaceName} | Update a workspace
[**put_workspaces**](WorkspacesApi.md#put_workspaces) | **PUT** /workspaces | 


# **delete_workspace**
> delete_workspace(workspace_name, recurse=recurse)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_name = 'workspace_name_example' # str | name of workspace
recurse = true # bool | delete workspace contents (default false) (optional)

try:
    api_instance.delete_workspace(workspace_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| name of workspace | 
 **recurse** | **bool**| delete workspace contents (default false) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspaces**
> delete_workspaces()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()

try:
    api_instance.delete_workspaces()
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspaces: %s\n" % e)
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

# **get_workspace**
> WorkspaceResponse get_workspace(workspace_name, quiet_on_not_found=quiet_on_not_found)

Retrieve a layer group

Retrieves a single workspace definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_name = 'workspace_name_example' # str | the name of the workspace to fetch
quiet_on_not_found = true # bool | The quietOnNotFound parameter avoids logging an exception when the workspace is not present. Note that 404 status code will still be returned. (optional)

try:
    # Retrieve a layer group
    api_response = api_instance.get_workspace(workspace_name, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| the name of the workspace to fetch | 
 **quiet_on_not_found** | **bool**| The quietOnNotFound parameter avoids logging an exception when the workspace is not present. Note that 404 status code will still be returned. | [optional] 

### Return type

[**WorkspaceResponse**](WorkspaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces**
> WorkspacesResponse get_workspaces()

Get a list of workspaces

Displays a list of all workspaces on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces.xml\" for XML)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()

try:
    # Get a list of workspaces
    api_response = api_instance.get_workspaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkspacesResponse**](WorkspacesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workspace**
> post_workspace()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()

try:
    api_instance.post_workspace()
except ApiException as e:
    print("Exception when calling WorkspacesApi->post_workspace: %s\n" % e)
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

# **post_workspaces**
> str post_workspaces(workspace_body, default=default)

add a new workspace to GeoServer

Adds a new workspace to the server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_body = swagger_client.Workspace() # Workspace | The layer group body information to upload.
default = false # bool | New workspace will be the used as the default. Allowed values are true or false,  The default value is false. (optional) (default to false)

try:
    # add a new workspace to GeoServer
    api_response = api_instance.post_workspaces(workspace_body, default=default)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->post_workspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_body** | [**Workspace**](Workspace.md)| The layer group body information to upload. | 
 **default** | **bool**| New workspace will be the used as the default. Allowed values are true or false,  The default value is false. | [optional] [default to false]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: text/html, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_workspace**
> put_workspace(workspace_name, workspace_body)

Update a workspace

takes the body of the post and modifies the workspace from it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace_name = 'workspace_name_example' # str | name of workspace
workspace_body = swagger_client.Workspace() # Workspace | The layer group body information to upload.

try:
    # Update a workspace
    api_instance.put_workspace(workspace_name, workspace_body)
except ApiException as e:
    print("Exception when calling WorkspacesApi->put_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| name of workspace | 
 **workspace_body** | [**Workspace**](Workspace.md)| The layer group body information to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_workspaces**
> put_workspaces()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()

try:
    api_instance.put_workspaces()
except ApiException as e:
    print("Exception when calling WorkspacesApi->put_workspaces: %s\n" % e)
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

