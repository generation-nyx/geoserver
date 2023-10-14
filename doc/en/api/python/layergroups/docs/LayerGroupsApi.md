# swagger_client.LayerGroupsApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_layergroup**](LayerGroupsApi.md#delete_layergroup) | **DELETE** /layergroups/{layergroupName} | Delete layer group
[**delete_layergroups**](LayerGroupsApi.md#delete_layergroups) | **DELETE** /layergroups | 
[**delete_workspace_layergroup**](LayerGroupsApi.md#delete_workspace_layergroup) | **DELETE** /workspaces/{workspace}/layergroups/{layergroup} | Delete layer group
[**delete_workspace_layergroups**](LayerGroupsApi.md#delete_workspace_layergroups) | **DELETE** /workspaces/{workspace}/layergroups | 
[**get_layergroup**](LayerGroupsApi.md#get_layergroup) | **GET** /layergroups/{layergroupName} | Retrieve a layer group
[**get_layergroups**](LayerGroupsApi.md#get_layergroups) | **GET** /layergroups | Get a list of layer groups
[**get_workspace_layergroup**](LayerGroupsApi.md#get_workspace_layergroup) | **GET** /workspaces/{workspace}/layergroups/{layergroup} | Retrieve a layer group
[**get_workspace_layergroups**](LayerGroupsApi.md#get_workspace_layergroups) | **GET** /workspaces/{workspace}/layergroups | Get a list of layer groups in a workspace
[**post_layergroup**](LayerGroupsApi.md#post_layergroup) | **POST** /layergroups/{layergroupName} | 
[**post_layergroups**](LayerGroupsApi.md#post_layergroups) | **POST** /layergroups | Add a new layer group
[**post_workspace_layergroup**](LayerGroupsApi.md#post_workspace_layergroup) | **POST** /workspaces/{workspace}/layergroups/{layergroup} | 
[**post_workspace_layergroups**](LayerGroupsApi.md#post_workspace_layergroups) | **POST** /workspaces/{workspace}/layergroups | Add a new layer group
[**put_layergroup**](LayerGroupsApi.md#put_layergroup) | **PUT** /layergroups/{layergroupName} | Modify a layer group.
[**put_layergroups**](LayerGroupsApi.md#put_layergroups) | **PUT** /layergroups | 
[**put_workspace_layergroup**](LayerGroupsApi.md#put_workspace_layergroup) | **PUT** /workspaces/{workspace}/layergroups/{layergroup} | Modify a layer group.
[**put_workspace_layergroups**](LayerGroupsApi.md#put_workspace_layergroups) | **PUT** /workspaces/{workspace}/layergroups | 


# **delete_layergroup**
> delete_layergroup(layergroup_name)

Delete layer group

Deletes a layer group from the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()
layergroup_name = 'layergroup_name_example' # str | The name of the layer group to delete.

try:
    # Delete layer group
    api_instance.delete_layergroup(layergroup_name)
except ApiException as e:
    print("Exception when calling LayerGroupsApi->delete_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layergroup_name** | **str**| The name of the layer group to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_layergroups**
> delete_layergroups()



Invalid. Use /layergroups/{layergroup} instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()

try:
    api_instance.delete_layergroups()
except ApiException as e:
    print("Exception when calling LayerGroupsApi->delete_layergroups: %s\n" % e)
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

# **delete_workspace_layergroup**
> delete_workspace_layergroup(layergroup, workspace)

Delete layer group

Deletes a layer group from the server in the given workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()
layergroup = 'layergroup_example' # str | The name of the layer group to delete.
workspace = 'workspace_example' # str | The name of the workspace

try:
    # Delete layer group
    api_instance.delete_workspace_layergroup(layergroup, workspace)
except ApiException as e:
    print("Exception when calling LayerGroupsApi->delete_workspace_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layergroup** | **str**| The name of the layer group to delete. | 
 **workspace** | **str**| The name of the workspace | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_layergroups**
> delete_workspace_layergroups()



Invalid. Use /workspaces/{workspace}/layergroups/{layergroup} instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()

try:
    api_instance.delete_workspace_layergroups()
except ApiException as e:
    print("Exception when calling LayerGroupsApi->delete_workspace_layergroups: %s\n" % e)
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

# **get_layergroup**
> Layergroup get_layergroup(layergroup_name)

Retrieve a layer group

Retrieves a single layer group definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layergroups/{layergroup}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()
layergroup_name = 'layergroup_name_example' # str | The name of the layer group to retrieve.

try:
    # Retrieve a layer group
    api_response = api_instance.get_layergroup(layergroup_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerGroupsApi->get_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layergroup_name** | **str**| The name of the layer group to retrieve. | 

### Return type

[**Layergroup**](Layergroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layergroups**
> LayergroupResponse get_layergroups()

Get a list of layer groups

Displays a list of all layer groups on the server not otherwise in a workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layergroups.xml\" for XML)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()

try:
    # Get a list of layer groups
    api_response = api_instance.get_layergroups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerGroupsApi->get_layergroups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LayergroupResponse**](LayergroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_layergroup**
> Layergroup get_workspace_layergroup(workspace, layergroup)

Retrieve a layer group

Retrieves a single layer group definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/layergroups/{layergroup}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()
workspace = 'workspace_example' # str | The name of the workspace
layergroup = 'layergroup_example' # str | The name of the layer group to retrieve.

try:
    # Retrieve a layer group
    api_response = api_instance.get_workspace_layergroup(workspace, layergroup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerGroupsApi->get_workspace_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **layergroup** | **str**| The name of the layer group to retrieve. | 

### Return type

[**Layergroup**](Layergroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_layergroups**
> LayergroupResponse get_workspace_layergroups(workspace)

Get a list of layer groups in a workspace

Displays a list of all layer groups in a given workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layergroups.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()
workspace = 'workspace_example' # str | The name of the workspace

try:
    # Get a list of layer groups in a workspace
    api_response = api_instance.get_workspace_layergroups(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerGroupsApi->get_workspace_layergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 

### Return type

[**LayergroupResponse**](LayergroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_layergroup**
> post_layergroup()



Invalid. Use PUT to edit a layer group definition, or POST with /layergroups to add a new definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()

try:
    api_instance.post_layergroup()
except ApiException as e:
    print("Exception when calling LayerGroupsApi->post_layergroup: %s\n" % e)
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

# **post_layergroups**
> str post_layergroups(layergroup_body)

Add a new layer group

Adds a new layer group entry to the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()
layergroup_body = swagger_client.Layergroup() # Layergroup | The layer group body information to upload.

try:
    # Add a new layer group
    api_response = api_instance.post_layergroups(layergroup_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerGroupsApi->post_layergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layergroup_body** | [**Layergroup**](Layergroup.md)| The layer group body information to upload. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workspace_layergroup**
> post_workspace_layergroup()



Invalid. Use PUT to edit a layer group definition, or POST with /workspaces/{workspace}/layergroups to add a new definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()

try:
    api_instance.post_workspace_layergroup()
except ApiException as e:
    print("Exception when calling LayerGroupsApi->post_workspace_layergroup: %s\n" % e)
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

# **post_workspace_layergroups**
> str post_workspace_layergroups(layergroup_body)

Add a new layer group

Adds a new layer group entry to the server in the specified workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()
layergroup_body = swagger_client.Layergroup() # Layergroup | The layer group body information to upload.

try:
    # Add a new layer group
    api_response = api_instance.post_workspace_layergroups(layergroup_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayerGroupsApi->post_workspace_layergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layergroup_body** | [**Layergroup**](Layergroup.md)| The layer group body information to upload. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_layergroup**
> put_layergroup(layergroup_name, layergroup_body)

Modify a layer group.

Modifies an existing layer group on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layergroups/{layergroup}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()
layergroup_name = 'layergroup_name_example' # str | The name of the layer group to modify.
layergroup_body = swagger_client.Layergroup() # Layergroup | The updated layer group definition.

try:
    # Modify a layer group.
    api_instance.put_layergroup(layergroup_name, layergroup_body)
except ApiException as e:
    print("Exception when calling LayerGroupsApi->put_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layergroup_name** | **str**| The name of the layer group to modify. | 
 **layergroup_body** | [**Layergroup**](Layergroup.md)| The updated layer group definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_layergroups**
> put_layergroups()



Invalid. Use POST for adding a new layer group, or PUT on /layergroups/{layergroup} to edit an existing layer group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()

try:
    api_instance.put_layergroups()
except ApiException as e:
    print("Exception when calling LayerGroupsApi->put_layergroups: %s\n" % e)
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

# **put_workspace_layergroup**
> put_workspace_layergroup(workspace, layergroup, layergroup_body)

Modify a layer group.

Modifies an existing layer group on the server in the given workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/layergroups/{layergroup}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()
workspace = 'workspace_example' # str | The name of the workspace
layergroup = 'layergroup_example' # str | The name of the layer group to modify.
layergroup_body = swagger_client.Layergroup() # Layergroup | The updated layer group definition.

try:
    # Modify a layer group.
    api_instance.put_workspace_layergroup(workspace, layergroup, layergroup_body)
except ApiException as e:
    print("Exception when calling LayerGroupsApi->put_workspace_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **layergroup** | **str**| The name of the layer group to modify. | 
 **layergroup_body** | [**Layergroup**](Layergroup.md)| The updated layer group definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_workspace_layergroups**
> put_workspace_layergroups()



Invalid. Use POST for adding a new layer group to a workspace, or PUT on /workspaces/{workspace}/layergroups/{layergroup} to edit an existing layer group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayerGroupsApi()

try:
    api_instance.put_workspace_layergroups()
except ApiException as e:
    print("Exception when calling LayerGroupsApi->put_workspace_layergroups: %s\n" % e)
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

