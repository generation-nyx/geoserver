# swagger_client.LayersApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**layers_delete**](LayersApi.md#layers_delete) | **DELETE** /layers | 
[**layers_get**](LayersApi.md#layers_get) | **GET** /layers | Get a list of layers
[**layers_name_delete**](LayersApi.md#layers_name_delete) | **DELETE** /layers/{layerName} | Delete layer
[**layers_name_get**](LayersApi.md#layers_name_get) | **GET** /layers/{layerName} | Retrieve a layer
[**layers_name_post**](LayersApi.md#layers_name_post) | **POST** /layers/{layerName} | 
[**layers_name_put**](LayersApi.md#layers_name_put) | **PUT** /layers/{layerName} | Modify a layer.
[**layers_name_workspace_delete**](LayersApi.md#layers_name_workspace_delete) | **DELETE** /workspaces/{workspaceName}/layers/{layerName} | Delete layer
[**layers_name_workspace_get**](LayersApi.md#layers_name_workspace_get) | **GET** /workspaces/{workspaceName}/layers/{layerName} | Retrieve a layer
[**layers_name_workspace_post**](LayersApi.md#layers_name_workspace_post) | **POST** /workspaces/{workspaceName}/layers/{layerName} | 
[**layers_name_workspace_put**](LayersApi.md#layers_name_workspace_put) | **PUT** /workspaces/{workspaceName}/layers/{layerName} | Modify a layer.
[**layers_post**](LayersApi.md#layers_post) | **POST** /layers | 
[**layers_put**](LayersApi.md#layers_put) | **PUT** /layers | 
[**layers_workspace_delete**](LayersApi.md#layers_workspace_delete) | **DELETE** /workspaces/{workspaceName}/layers | 
[**layers_workspace_get**](LayersApi.md#layers_workspace_get) | **GET** /workspaces/{workspaceName}/layers | Get a list of layers in a workspace.
[**layers_workspace_post**](LayersApi.md#layers_workspace_post) | **POST** /workspaces/{workspaceName}/layers | 
[**layers_workspace_put**](LayersApi.md#layers_workspace_put) | **PUT** /workspaces/{workspaceName}/layers | 


# **layers_delete**
> layers_delete()



Invalid.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()

try:
    api_instance.layers_delete()
except ApiException as e:
    print("Exception when calling LayersApi->layers_delete: %s\n" % e)
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

# **layers_get**
> Layers layers_get()

Get a list of layers

Displays a list of all layers on the server. You must use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layers.xml\" for XML)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()

try:
    # Get a list of layers
    api_response = api_instance.layers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayersApi->layers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Layers**](Layers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_name_delete**
> layers_name_delete(layer_name, recurse=recurse)

Delete layer

Deletes a layer from the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()
layer_name = 'layer_name_example' # str | The name of the layer to delete.
recurse = false # bool | Recursively removes the layer from all layer groups which reference it. If this results in an empty layer group, also delete the layer group. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layer groups reference the layer. (optional) (default to false)

try:
    # Delete layer
    api_instance.layers_name_delete(layer_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling LayersApi->layers_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_name** | **str**| The name of the layer to delete. | 
 **recurse** | **bool**| Recursively removes the layer from all layer groups which reference it. If this results in an empty layer group, also delete the layer group. Allowed values for this parameter are true or false. The default value is false. A request with &#39;recurse&#x3D;false&#39; will fail if any layer groups reference the layer. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_name_get**
> Layer layers_name_get(layer_name)

Retrieve a layer

Retrieves a single layer definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layers/{layer}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()
layer_name = 'layer_name_example' # str | The name of the layer to retrieve.

try:
    # Retrieve a layer
    api_response = api_instance.layers_name_get(layer_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayersApi->layers_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_name** | **str**| The name of the layer to retrieve. | 

### Return type

[**Layer**](Layer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_name_post**
> layers_name_post()



Invalid. To create a new layer, instead POST to one of `/workspaces/{workspaceName}/coveragestores/{coveragestoreName}/coverages`, `/workspaces/{workspaceName}/datastores/{datastoreName}/featuretypes`, `/workspaces/{workspaceName}/wmsstores/{wmsstoreName}/wmslayers`, or `/workspaces/{workspaceName}/wmtsstores/{wmststoreName}/wmtslayers`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()

try:
    api_instance.layers_name_post()
except ApiException as e:
    print("Exception when calling LayersApi->layers_name_post: %s\n" % e)
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

# **layers_name_put**
> layers_name_put(layer_name, layer_body)

Modify a layer.

Modifies an existing layer on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layers/{layer}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()
layer_name = 'layer_name_example' # str | The name of the layer to modify.
layer_body = swagger_client.Layer() # Layer | The updated layer definition.

try:
    # Modify a layer.
    api_instance.layers_name_put(layer_name, layer_body)
except ApiException as e:
    print("Exception when calling LayersApi->layers_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_name** | **str**| The name of the layer to modify. | 
 **layer_body** | [**Layer**](Layer.md)| The updated layer definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_name_workspace_delete**
> layers_name_workspace_delete(workspace_name, layer_name, recurse=recurse)

Delete layer

Deletes a layer from the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()
workspace_name = NULL # object | The name of the workspace the layer is in.
layer_name = 'layer_name_example' # str | The name of the layer to delete.
recurse = false # bool | Recursively removes the layer from all layer groups which reference it. If this results in an empty layer group, also delete the layer group. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layer groups reference the layer. (optional) (default to false)

try:
    # Delete layer
    api_instance.layers_name_workspace_delete(workspace_name, layer_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling LayersApi->layers_name_workspace_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | [**object**](.md)| The name of the workspace the layer is in. | 
 **layer_name** | **str**| The name of the layer to delete. | 
 **recurse** | **bool**| Recursively removes the layer from all layer groups which reference it. If this results in an empty layer group, also delete the layer group. Allowed values for this parameter are true or false. The default value is false. A request with &#39;recurse&#x3D;false&#39; will fail if any layer groups reference the layer. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_name_workspace_get**
> Layer layers_name_workspace_get(workspace_name, layer_name)

Retrieve a layer

Retrieves a single layer definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layers/{layer}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace the layer is in.
layer_name = 'layer_name_example' # str | The name of the layer to retrieve.

try:
    # Retrieve a layer
    api_response = api_instance.layers_name_workspace_get(workspace_name, layer_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayersApi->layers_name_workspace_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace the layer is in. | 
 **layer_name** | **str**| The name of the layer to retrieve. | 

### Return type

[**Layer**](Layer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_name_workspace_post**
> layers_name_workspace_post()



Invalid. To create a new layer, instead POST to one of `/workspaces/{workspaceName}/coveragestores/{coveragestoreName}/coverages`, `/workspaces/{workspaceName}/datastores/{datastoreName}/featuretypes`, `/workspaces/{workspaceName}/wmsstores/{wmsstoreName}/wmslayers`, or `/workspaces/{workspaceName}/wmtsstores/{wmststoreName}/wmtslayers`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()

try:
    api_instance.layers_name_workspace_post()
except ApiException as e:
    print("Exception when calling LayersApi->layers_name_workspace_post: %s\n" % e)
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

# **layers_name_workspace_put**
> layers_name_workspace_put(workspace_name, layer_name, layer_body)

Modify a layer.

Modifies an existing layer on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layers/{layer}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()
workspace_name = NULL # object | The name of the workspace the layer is in.
layer_name = 'layer_name_example' # str | The name of the layer to modify.
layer_body = swagger_client.Layer() # Layer | The updated layer definition.

try:
    # Modify a layer.
    api_instance.layers_name_workspace_put(workspace_name, layer_name, layer_body)
except ApiException as e:
    print("Exception when calling LayersApi->layers_name_workspace_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | [**object**](.md)| The name of the workspace the layer is in. | 
 **layer_name** | **str**| The name of the layer to modify. | 
 **layer_body** | [**Layer**](Layer.md)| The updated layer definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_post**
> layers_post()



Invalid. To create a new layer, instead POST to one of `/workspaces/{workspaceName}/coveragestores/{coveragestoreName}/coverages`, `/workspaces/{workspaceName}/datastores/{datastoreName}/featuretypes`, `/workspaces/{workspaceName}/wmsstores/{wmsstoreName}/wmslayers`, or `/workspaces/{workspaceName}/wmtsstores/{wmststoreName}/wmtslayers`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()

try:
    api_instance.layers_post()
except ApiException as e:
    print("Exception when calling LayersApi->layers_post: %s\n" % e)
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

# **layers_put**
> layers_put()



Invalid. To edit a layer, use PUT on an individual layer instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()

try:
    api_instance.layers_put()
except ApiException as e:
    print("Exception when calling LayersApi->layers_put: %s\n" % e)
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

# **layers_workspace_delete**
> layers_workspace_delete()



Invalid.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()

try:
    api_instance.layers_workspace_delete()
except ApiException as e:
    print("Exception when calling LayersApi->layers_workspace_delete: %s\n" % e)
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

# **layers_workspace_get**
> Layers layers_workspace_get(workspace_name)

Get a list of layers in a workspace.

Displays a list of all layers in the provided workspace. You must use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layers.xml\" for XML)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace to list layers in

try:
    # Get a list of layers in a workspace.
    api_response = api_instance.layers_workspace_get(workspace_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayersApi->layers_workspace_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace to list layers in | 

### Return type

[**Layers**](Layers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_workspace_post**
> layers_workspace_post()



Invalid. To create a new layer, instead POST to one of `/workspaces/{workspaceName}/coveragestores/{coveragestoreName}/coverages`, `/workspaces/{workspaceName}/datastores/{datastoreName}/featuretypes`, `/workspaces/{workspaceName}/wmsstores/{wmsstoreName}/wmslayers`, or `/workspaces/{workspaceName}/wmtsstores/{wmststoreName}/wmtslayers`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()

try:
    api_instance.layers_workspace_post()
except ApiException as e:
    print("Exception when calling LayersApi->layers_workspace_post: %s\n" % e)
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

# **layers_workspace_put**
> layers_workspace_put()



Invalid. To edit a layer, use PUT on an individual layer instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LayersApi()

try:
    api_instance.layers_workspace_put()
except ApiException as e:
    print("Exception when calling LayersApi->layers_workspace_put: %s\n" % e)
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

