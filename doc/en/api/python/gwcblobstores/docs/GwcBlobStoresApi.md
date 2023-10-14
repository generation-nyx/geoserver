# swagger_client.GwcBlobStoresApi

All URIs are relative to *http://geoserver:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blobstore_delete**](GwcBlobStoresApi.md#blobstore_delete) | **DELETE** /blobstores/{blobstoreName} | Delete configured blobstore
[**blobstore_get**](GwcBlobStoresApi.md#blobstore_get) | **GET** /blobstores/{blobstoreName} | Retrieve a configured blobstore
[**blobstore_put**](GwcBlobStoresApi.md#blobstore_put) | **PUT** /blobstores/{blobstoreName} | Create or update a configured blobstore.
[**blobstores_get**](GwcBlobStoresApi.md#blobstores_get) | **GET** /blobstores | Get a list of configured blobstores


# **blobstore_delete**
> blobstore_delete(blobstore_name)

Delete configured blobstore

Deletes a configured blobstore from the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcBlobStoresApi()
blobstore_name = 'blobstore_name_example' # str | The name of the blobstore to delete.

try:
    # Delete configured blobstore
    api_instance.blobstore_delete(blobstore_name)
except ApiException as e:
    print("Exception when calling GwcBlobStoresApi->blobstore_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blobstore_name** | **str**| The name of the blobstore to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobstore_get**
> BlobStore blobstore_get(blobstore_name)

Retrieve a configured blobstore

Retrieves a single configured blobstore definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcBlobStoresApi()
blobstore_name = 'blobstore_name_example' # str | The name of the blobstore to retrieve.

try:
    # Retrieve a configured blobstore
    api_response = api_instance.blobstore_get(blobstore_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GwcBlobStoresApi->blobstore_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blobstore_name** | **str**| The name of the blobstore to retrieve. | 

### Return type

[**BlobStore**](BlobStore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobstore_put**
> blobstore_put(blobstore_name, blobstore_body)

Create or update a configured blobstore.

Creates a new configured blobstore on the server, or modifies an existing blobstore.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcBlobStoresApi()
blobstore_name = 'blobstore_name_example' # str | The name of the blobstore to add or update.
blobstore_body = swagger_client.BlobStore() # BlobStore | The new blobstore definition.

try:
    # Create or update a configured blobstore.
    api_instance.blobstore_put(blobstore_name, blobstore_body)
except ApiException as e:
    print("Exception when calling GwcBlobStoresApi->blobstore_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blobstore_name** | **str**| The name of the blobstore to add or update. | 
 **blobstore_body** | [**BlobStore**](BlobStore.md)| The new blobstore definition. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobstores_get**
> BlobStores blobstores_get()

Get a list of configured blobstores

Displays a list of all configured blobstores on the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GwcBlobStoresApi()

try:
    # Get a list of configured blobstores
    api_response = api_instance.blobstores_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GwcBlobStoresApi->blobstores_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlobStores**](BlobStores.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

