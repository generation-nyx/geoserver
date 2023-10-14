# swagger_client.WMTSLayersApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_wmts_store_layer**](WMTSLayersApi.md#delete_wmts_store_layer) | **DELETE** /workspaces/{workspace}/wmtslayers/{wmtslayer} | 
[**delete_wmts_store_layers**](WMTSLayersApi.md#delete_wmts_store_layers) | **DELETE** /workspaces/{workspace}/wmtslayers | 
[**delete_wmts_store_store_layer**](WMTSLayersApi.md#delete_wmts_store_store_layer) | **DELETE** /workspaces/{workspace}/wmtsstores/{wmtsstore}/layers/{wmtslayer} | 
[**delete_wmts_store_store_layers**](WMTSLayersApi.md#delete_wmts_store_store_layers) | **DELETE** /workspaces/{workspace}/wmtsstores/{wmtsstore}/layers | 
[**get_wmts_store_layer**](WMTSLayersApi.md#get_wmts_store_layer) | **GET** /workspaces/{workspace}/wmtslayers/{wmtslayer} | 
[**get_wmts_store_layers**](WMTSLayersApi.md#get_wmts_store_layers) | **GET** /workspaces/{workspace}/wmtslayers | 
[**get_wmts_store_store_layer**](WMTSLayersApi.md#get_wmts_store_store_layer) | **GET** /workspaces/{workspace}/wmtsstores/{wmtsstore}/layers/{wmtslayer} | 
[**get_wmts_store_store_layers**](WMTSLayersApi.md#get_wmts_store_store_layers) | **GET** /workspaces/{workspace}/wmtsstores/{wmtsstore}/layers | 
[**post_wmts_store_layer**](WMTSLayersApi.md#post_wmts_store_layer) | **POST** /workspaces/{workspace}/wmtslayers/{wmtslayer} | 
[**post_wmts_store_layers**](WMTSLayersApi.md#post_wmts_store_layers) | **POST** /workspaces/{workspace}/wmtslayers | 
[**post_wmts_store_store_layer**](WMTSLayersApi.md#post_wmts_store_store_layer) | **POST** /workspaces/{workspace}/wmtsstores/{wmtsstore}/layers/{wmtslayer} | 
[**post_wmts_store_store_layers**](WMTSLayersApi.md#post_wmts_store_store_layers) | **POST** /workspaces/{workspace}/wmtsstores/{wmtsstore}/layers | 
[**put_wmts_store_layer**](WMTSLayersApi.md#put_wmts_store_layer) | **PUT** /workspaces/{workspace}/wmtslayers/{wmtslayer} | 
[**put_wmts_store_layers**](WMTSLayersApi.md#put_wmts_store_layers) | **PUT** /workspaces/{workspace}/wmtslayers | 
[**put_wmts_store_store_layer**](WMTSLayersApi.md#put_wmts_store_store_layer) | **PUT** /workspaces/{workspace}/wmtsstores/{wmtsstore}/layers/{wmtslayer} | 
[**put_wmts_store_store_layers**](WMTSLayersApi.md#put_wmts_store_store_layers) | **PUT** /workspaces/{workspace}/wmtsstores/{wmtsstore}/layers | 


# **delete_wmts_store_layer**
> delete_wmts_store_layer(workspace, wmtslayer, recurse=recurse)



Deletes a layer from the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()
workspace = 'workspace_example' # str | Name of the workspace
wmtslayer = 'wmtslayer_example' # str | Name of the layer to be deleted
recurse = false # bool | Recursively deletes all layers referenced by the specified wmtslayer. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layers reference the wmtslayer. (optional) (default to false)

try:
    api_instance.delete_wmts_store_layer(workspace, wmtslayer, recurse=recurse)
except ApiException as e:
    print("Exception when calling WMTSLayersApi->delete_wmts_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmtslayer** | **str**| Name of the layer to be deleted | 
 **recurse** | **bool**| Recursively deletes all layers referenced by the specified wmtslayer. Allowed values for this parameter are true or false. The default value is false. A request with &#39;recurse&#x3D;false&#39; will fail if any layers reference the wmtslayer. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wmts_store_layers**
> delete_wmts_store_layers()



Invalid. Can only delete an individual layer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()

try:
    api_instance.delete_wmts_store_layers()
except ApiException as e:
    print("Exception when calling WMTSLayersApi->delete_wmts_store_layers: %s\n" % e)
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

# **delete_wmts_store_store_layer**
> delete_wmts_store_store_layer(workspace, wmtsstore, wmtslayer, recurse=recurse)



Deletes a layer from the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()
workspace = 'workspace_example' # str | Name of the workspace
wmtsstore = 'wmtsstore_example' # str | Name of the store
wmtslayer = 'wmtslayer_example' # str | Name of the layer to be deleted
recurse = false # bool | Recursively deletes all layers referenced by the specified wmtslayer. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layers reference the wmtslayer. (optional) (default to false)

try:
    api_instance.delete_wmts_store_store_layer(workspace, wmtsstore, wmtslayer, recurse=recurse)
except ApiException as e:
    print("Exception when calling WMTSLayersApi->delete_wmts_store_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmtsstore** | **str**| Name of the store | 
 **wmtslayer** | **str**| Name of the layer to be deleted | 
 **recurse** | **bool**| Recursively deletes all layers referenced by the specified wmtslayer. Allowed values for this parameter are true or false. The default value is false. A request with &#39;recurse&#x3D;false&#39; will fail if any layers reference the wmtslayer. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wmts_store_store_layers**
> delete_wmts_store_store_layers()



Invalid. Can only delete an individual layer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()

try:
    api_instance.delete_wmts_store_store_layers()
except ApiException as e:
    print("Exception when calling WMTSLayersApi->delete_wmts_store_store_layers: %s\n" % e)
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

# **get_wmts_store_layer**
> WMTSStoreLayerInfo get_wmts_store_layer(workspace, wmtslayer, quiet_on_not_found=quiet_on_not_found)



Retrieves an individual WMTS layer. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/wmtslayers/{wmtslayer}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()
workspace = 'workspace_example' # str | Name of the workspace
wmtslayer = 'wmtslayer_example' # str | Name of the layer
quiet_on_not_found = true # bool | When set to \"true\", will not log an exception when the style is not present. The 404 status code will still be returned. Allowable values are \"true\" or \"false\" (default). (optional)

try:
    api_response = api_instance.get_wmts_store_layer(workspace, wmtslayer, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WMTSLayersApi->get_wmts_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmtslayer** | **str**| Name of the layer | 
 **quiet_on_not_found** | **bool**| When set to \&quot;true\&quot;, will not log an exception when the style is not present. The 404 status code will still be returned. Allowable values are \&quot;true\&quot; or \&quot;false\&quot; (default). | [optional] 

### Return type

[**WMTSStoreLayerInfo**](WMTSStoreLayerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmts_store_layers**
> WMTSStoreLayersList get_wmts_store_layers(workspace, list=list)



Retrieves the WMTS layers available on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/wmtslayers\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()
workspace = 'workspace_example' # str | Name of the workspace
list = 'configured' # str | Set \"list=available\" to see all possible layers in the store, not just ones currently published (optional) (default to configured)

try:
    api_response = api_instance.get_wmts_store_layers(workspace, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WMTSLayersApi->get_wmts_store_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **list** | **str**| Set \&quot;list&#x3D;available\&quot; to see all possible layers in the store, not just ones currently published | [optional] [default to configured]

### Return type

[**WMTSStoreLayersList**](WMTSStoreLayersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmts_store_store_layer**
> WMTSStoreLayerInfo get_wmts_store_store_layer(workspace, wmtsstore, wtmslayer, quiet_on_not_found=quiet_on_not_found)



Retrieves an individual WMTS store layer for a given store. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/wmtsstores/{wmtsstore}/wmtslayers/{wmtslayer}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()
workspace = 'workspace_example' # str | Name of the workspace
wmtsstore = 'wmtsstore_example' # str | Name of the store
wtmslayer = 'wtmslayer_example' # str | Name of the layer
quiet_on_not_found = true # bool | When set to \"true\", will not log an exception when the style is not present. The 404 status code will still be returned. Allowable values are \"true\" or \"false\" (default). (optional)

try:
    api_response = api_instance.get_wmts_store_store_layer(workspace, wmtsstore, wtmslayer, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WMTSLayersApi->get_wmts_store_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmtsstore** | **str**| Name of the store | 
 **wtmslayer** | **str**| Name of the layer | 
 **quiet_on_not_found** | **bool**| When set to \&quot;true\&quot;, will not log an exception when the style is not present. The 404 status code will still be returned. Allowable values are \&quot;true\&quot; or \&quot;false\&quot; (default). | [optional] 

### Return type

[**WMTSStoreLayerInfo**](WMTSStoreLayerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmts_store_store_layers**
> WMTSStoreLayersList get_wmts_store_store_layers(workspace, wmtsstore, list=list)



Retrieves the WMTS store layers available in the given store. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/wmtsstores/{wmtsstore}/wmtslayers.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()
workspace = 'workspace_example' # str | Name of the workspace
wmtsstore = 'wmtsstore_example' # str | Name of the store
list = 'configured' # str | Set \"list=available\" to see all possible layers in the store, not just ones currently published (optional) (default to configured)

try:
    api_response = api_instance.get_wmts_store_store_layers(workspace, wmtsstore, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WMTSLayersApi->get_wmts_store_store_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmtsstore** | **str**| Name of the store | 
 **list** | **str**| Set \&quot;list&#x3D;available\&quot; to see all possible layers in the store, not just ones currently published | [optional] [default to configured]

### Return type

[**WMTSStoreLayersList**](WMTSStoreLayersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wmts_store_layer**
> post_wmts_store_layer()



Invalid. Use PUT to edit a layer, or POST on the /wmtslayers endpoint to add a new layer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()

try:
    api_instance.post_wmts_store_layer()
except ApiException as e:
    print("Exception when calling WMTSLayersApi->post_wmts_store_layer: %s\n" % e)
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

# **post_wmts_store_layers**
> post_wmts_store_layers(workspace, wmts_store_layer_body)



Publishes a new WMTS store layer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()
workspace = 'workspace_example' # str | Name of the workspace
wmts_store_layer_body = swagger_client.WMTSStoreLayerInfo() # WMTSStoreLayerInfo | Body of the WMTS store layer

try:
    api_instance.post_wmts_store_layers(workspace, wmts_store_layer_body)
except ApiException as e:
    print("Exception when calling WMTSLayersApi->post_wmts_store_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmts_store_layer_body** | [**WMTSStoreLayerInfo**](WMTSStoreLayerInfo.md)| Body of the WMTS store layer | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wmts_store_store_layer**
> post_wmts_store_store_layer()



Invalid. Use PUT to edit a layer, or POST on the /wmtslayers endpoint to add a new layer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()

try:
    api_instance.post_wmts_store_store_layer()
except ApiException as e:
    print("Exception when calling WMTSLayersApi->post_wmts_store_store_layer: %s\n" % e)
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

# **post_wmts_store_store_layers**
> post_wmts_store_store_layers(workspace, wmtsstore, wmts_store_layer_body)



Publishes a new WMTS store layer in the given store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()
workspace = 'workspace_example' # str | Name of the workspace
wmtsstore = 'wmtsstore_example' # str | Name of the data store
wmts_store_layer_body = swagger_client.WMTSStoreLayerInfo() # WMTSStoreLayerInfo | Body of the WMTS store layer

try:
    api_instance.post_wmts_store_store_layers(workspace, wmtsstore, wmts_store_layer_body)
except ApiException as e:
    print("Exception when calling WMTSLayersApi->post_wmts_store_store_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmtsstore** | **str**| Name of the data store | 
 **wmts_store_layer_body** | [**WMTSStoreLayerInfo**](WMTSStoreLayerInfo.md)| Body of the WMTS store layer | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wmts_store_layer**
> put_wmts_store_layer(workspace, wmtslayer, wmts_store_layer_body, calculate=calculate)



Edits an existing WMTS store layer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()
workspace = 'workspace_example' # str | Name of the workspace
wmtslayer = 'wmtslayer_example' # str | Name of the layer to be edited
wmts_store_layer_body = swagger_client.WMTSStoreLayerInfo() # WMTSStoreLayerInfo | Body of the WMTS store layer
calculate = ['calculate_example'] # list[str] | Specifies whether to recalculate any bounding boxes for a wmtWMTSs layer. Some properties are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter 'recalculate=' is useful avoid slow recalculation when operating against large datasets as 'recalculate=' avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter 'recalculate=nativebbox' is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - 'recalculate=nativebbox,latlonbbox' can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. (optional)

try:
    api_instance.put_wmts_store_layer(workspace, wmtslayer, wmts_store_layer_body, calculate=calculate)
except ApiException as e:
    print("Exception when calling WMTSLayersApi->put_wmts_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmtslayer** | **str**| Name of the layer to be edited | 
 **wmts_store_layer_body** | [**WMTSStoreLayerInfo**](WMTSStoreLayerInfo.md)| Body of the WMTS store layer | 
 **calculate** | [**list[str]**](str.md)| Specifies whether to recalculate any bounding boxes for a wmtWMTSs layer. Some properties are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter &#39;recalculate&#x3D;&#39; is useful avoid slow recalculation when operating against large datasets as &#39;recalculate&#x3D;&#39; avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter &#39;recalculate&#x3D;nativebbox&#39; is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - &#39;recalculate&#x3D;nativebbox,latlonbbox&#39; can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wmts_store_layers**
> put_wmts_store_layers()



Invalid. Use POST for adding a new layer, or PUT on an individual layer to edit it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()

try:
    api_instance.put_wmts_store_layers()
except ApiException as e:
    print("Exception when calling WMTSLayersApi->put_wmts_store_layers: %s\n" % e)
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

# **put_wmts_store_store_layer**
> put_wmts_store_store_layer(workspace, wmtsstore, wmtslayer, wmts_store_layer_body, calculate=calculate)



Edits an existing WMTS store layer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()
workspace = 'workspace_example' # str | Name of the workspace
wmtsstore = 'wmtsstore_example' # str | Name of the store
wmtslayer = 'wmtslayer_example' # str | Name of the layer to be edited
wmts_store_layer_body = swagger_client.WMTSStoreLayerInfo() # WMTSStoreLayerInfo | Body of the WMTS store layer
calculate = ['calculate_example'] # list[str] | Specifies whether to recalculate any bounding boxes for a wmts layer. Some properties are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter 'recalculate=' is useful avoid slow recalculation when operating against large datasets as 'recalculate=' avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter 'recalculate=nativebbox' is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - 'recalculate=nativebbox,latlonbbox' can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. (optional)

try:
    api_instance.put_wmts_store_store_layer(workspace, wmtsstore, wmtslayer, wmts_store_layer_body, calculate=calculate)
except ApiException as e:
    print("Exception when calling WMTSLayersApi->put_wmts_store_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmtsstore** | **str**| Name of the store | 
 **wmtslayer** | **str**| Name of the layer to be edited | 
 **wmts_store_layer_body** | [**WMTSStoreLayerInfo**](WMTSStoreLayerInfo.md)| Body of the WMTS store layer | 
 **calculate** | [**list[str]**](str.md)| Specifies whether to recalculate any bounding boxes for a wmts layer. Some properties are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter &#39;recalculate&#x3D;&#39; is useful avoid slow recalculation when operating against large datasets as &#39;recalculate&#x3D;&#39; avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter &#39;recalculate&#x3D;nativebbox&#39; is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - &#39;recalculate&#x3D;nativebbox,latlonbbox&#39; can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wmts_store_store_layers**
> put_wmts_store_store_layers()



Invalid. Use POST for adding a new layer, or PUT on an individual layer to edit it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WMTSLayersApi()

try:
    api_instance.put_wmts_store_store_layers()
except ApiException as e:
    print("Exception when calling WMTSLayersApi->put_wmts_store_store_layers: %s\n" % e)
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

