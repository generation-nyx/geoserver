# swagger_client.GwcGridSetsApi

All URIs are relative to *http://geoserver:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gridset_delete**](GwcGridSetsApi.md#gridset_delete) | **DELETE** /gridsets/{gridsetName} | Delete configured gridset
[**gridset_get**](GwcGridSetsApi.md#gridset_get) | **GET** /gridsets/{gridsetName} | Retrieve a configured gridset
[**gridset_put**](GwcGridSetsApi.md#gridset_put) | **PUT** /gridsets/{gridsetName} | Create or update a configured gridset.
[**gridsets_get**](GwcGridSetsApi.md#gridsets_get) | **GET** /gridsets | Get a list of configured gridsets


# **gridset_delete**
> gridset_delete(gridset_name)

Delete configured gridset

Deletes a configured gridset from the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcGridSetsApi()
gridset_name = 'gridset_name_example' # str | The name of the gridset to delete.

try:
    # Delete configured gridset
    api_instance.gridset_delete(gridset_name)
except ApiException as e:
    print("Exception when calling GwcGridSetsApi->gridset_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gridset_name** | **str**| The name of the gridset to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridset_get**
> GridSet gridset_get(gridset_name)

Retrieve a configured gridset

Retrieves a single configured gridset definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcGridSetsApi()
gridset_name = 'gridset_name_example' # str | The name of the gridset to retrieve.

try:
    # Retrieve a configured gridset
    api_response = api_instance.gridset_get(gridset_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GwcGridSetsApi->gridset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gridset_name** | **str**| The name of the gridset to retrieve. | 

### Return type

[**GridSet**](GridSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridset_put**
> gridset_put(gridset_name, gridset_body)

Create or update a configured gridset.

Creates a new configured gridset on the server, or modifies an existing gridset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcGridSetsApi()
gridset_name = 'gridset_name_example' # str | The name of the gridset to add or update.
gridset_body = swagger_client.GridSet() # GridSet | The new gridset definition.

try:
    # Create or update a configured gridset.
    api_instance.gridset_put(gridset_name, gridset_body)
except ApiException as e:
    print("Exception when calling GwcGridSetsApi->gridset_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gridset_name** | **str**| The name of the gridset to add or update. | 
 **gridset_body** | [**GridSet**](GridSet.md)| The new gridset definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridsets_get**
> GridSets gridsets_get()

Get a list of configured gridsets

Displays a list of all configured gridsets on the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcGridSetsApi()

try:
    # Get a list of configured gridsets
    api_response = api_instance.gridsets_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GwcGridSetsApi->gridsets_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GridSets**](GridSets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

