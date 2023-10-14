# swagger_client.ReloadApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_reload**](ReloadApi.md#delete_reload) | **DELETE** /reload | 
[**delete_reset**](ReloadApi.md#delete_reset) | **DELETE** /reset | 
[**get_reload**](ReloadApi.md#get_reload) | **GET** /reload | 
[**get_reset**](ReloadApi.md#get_reset) | **GET** /reset | 
[**post_reload**](ReloadApi.md#post_reload) | **POST** /reload | Reload the configuration from disk, and reset all caches.
[**post_reset**](ReloadApi.md#post_reset) | **POST** /reset | Reset all store, raster, and schema caches.
[**put_reload**](ReloadApi.md#put_reload) | **PUT** /reload | Reload the configuration from disk, and reset all caches.
[**put_reset**](ReloadApi.md#put_reset) | **PUT** /reset | Reset all store, raster, and schema caches.


# **delete_reload**
> delete_reload()



Invalid. Use PUT or POST to reload the catalog and configuation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReloadApi()

try:
    api_instance.delete_reload()
except ApiException as e:
    print("Exception when calling ReloadApi->delete_reload: %s\n" % e)
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

# **delete_reset**
> delete_reset()



Invalid. Use PUT or POST to reset the caches.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReloadApi()

try:
    api_instance.delete_reset()
except ApiException as e:
    print("Exception when calling ReloadApi->delete_reset: %s\n" % e)
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

# **get_reload**
> get_reload()



Invalid. Use PUT or POST to reload the catalog and configuation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReloadApi()

try:
    api_instance.get_reload()
except ApiException as e:
    print("Exception when calling ReloadApi->get_reload: %s\n" % e)
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

# **get_reset**
> get_reset()



Invalid. Use PUT or POST to reset the caches.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReloadApi()

try:
    api_instance.get_reset()
except ApiException as e:
    print("Exception when calling ReloadApi->get_reset: %s\n" % e)
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

# **post_reload**
> post_reload()

Reload the configuration from disk, and reset all caches.

Reloads the GeoServer catalog and configuration from disk. This operation is used in cases where an external tool has modified the on-disk configuration. This operation will also force GeoServer to drop any internal caches and reconnect to all data stores.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReloadApi()

try:
    # Reload the configuration from disk, and reset all caches.
    api_instance.post_reload()
except ApiException as e:
    print("Exception when calling ReloadApi->post_reload: %s\n" % e)
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

# **post_reset**
> post_reset()

Reset all store, raster, and schema caches.

Resets all store, raster, and schema caches. This operation is used to force GeoServer to drop all caches and store connections and reconnect to each of them the next time they are needed by a request. This is useful in case the stores themselves cache some information about the data structures they manage that may have changed in the meantime.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReloadApi()

try:
    # Reset all store, raster, and schema caches.
    api_instance.post_reset()
except ApiException as e:
    print("Exception when calling ReloadApi->post_reset: %s\n" % e)
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

# **put_reload**
> put_reload()

Reload the configuration from disk, and reset all caches.

Reloads the GeoServer catalog and configuration from disk. This operation is used in cases where an external tool has modified the on-disk configuration. This operation will also force GeoServer to drop any internal caches and reconnect to all data stores.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReloadApi()

try:
    # Reload the configuration from disk, and reset all caches.
    api_instance.put_reload()
except ApiException as e:
    print("Exception when calling ReloadApi->put_reload: %s\n" % e)
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

# **put_reset**
> put_reset()

Reset all store, raster, and schema caches.

Resets all store, raster, and schema caches. This operation is used to force GeoServer to drop all caches and store connections and reconnect to each of them the next time they are needed by a request. This is useful in case the stores themselves cache some information about the data structures they manage that may have changed in the meantime.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReloadApi()

try:
    # Reset all store, raster, and schema caches.
    api_instance.put_reset()
except ApiException as e:
    print("Exception when calling ReloadApi->put_reset: %s\n" % e)
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

