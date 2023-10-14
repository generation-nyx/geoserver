# swagger_client.MetadataApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_delete**](MetadataApi.md#metadata_delete) | **DELETE** /metadata | Delete all custom metadata
[**metadata_fix_get**](MetadataApi.md#metadata_fix_get) | **GET** /metadata/fix | Fix all custom metadata
[**metadata_import_post**](MetadataApi.md#metadata_import_post) | **POST** /metadata/import | Bulk import from geonetwork and/or template linking.
[**metadata_native_to_custom_get**](MetadataApi.md#metadata_native_to_custom_get) | **GET** /metadata/nativeToCustom | Perform native-to-custom mapping for all layers.
[**metadata_native_to_custom_post**](MetadataApi.md#metadata_native_to_custom_post) | **POST** /metadata/nativeToCustom | Perform native-to-custom mapping for selected layers.


# **metadata_delete**
> metadata_delete()

Delete all custom metadata

Remove ALL custom metadata from ALL layers. All template links are removed. Used for testing and debugging.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    # Delete all custom metadata
    api_instance.metadata_delete()
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_delete: %s\n" % e)
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

# **metadata_fix_get**
> metadata_fix_get()

Fix all custom metadata

Calls routine operations that may fix corrupted custom metadata in all layers. Used for testing and debugging.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    # Fix all custom metadata
    api_instance.metadata_fix_get()
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_fix_get: %s\n" % e)
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

# **metadata_import_post**
> metadata_import_post()

Bulk import from geonetwork and/or template linking.

Will perform a bulk import and/or template linking for every layer specified in CSV file. CSV file must be of form \"prefix:layername; [geonetwork-id] [; template-1 [;template-2 ... ] ]\" Existing template links will be removed first.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    # Bulk import from geonetwork and/or template linking.
    api_instance.metadata_import_post()
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_import_post: %s\n" % e)
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

# **metadata_native_to_custom_get**
> metadata_native_to_custom_get()

Perform native-to-custom mapping for all layers.

With respect to your custom-to-native mapping file (see general documentation), this operation will perform an opposite synchronization from native fields to custom fields.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    # Perform native-to-custom mapping for all layers.
    api_instance.metadata_native_to_custom_get()
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_native_to_custom_get: %s\n" % e)
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

# **metadata_native_to_custom_post**
> metadata_native_to_custom_post()

Perform native-to-custom mapping for selected layers.

With respect to your custom-to-native mapping file (see metadata module documentation), this operation will perform an opposite synchronization from native fields to custom fields. Your body must be a list layers, where each row is of the form \"prefix:layername\".

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    # Perform native-to-custom mapping for selected layers.
    api_instance.metadata_native_to_custom_post()
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_native_to_custom_post: %s\n" % e)
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

