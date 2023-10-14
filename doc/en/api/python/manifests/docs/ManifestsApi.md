# swagger_client.ManifestsApi

All URIs are relative to *http://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**about_status_get**](ManifestsApi.md#about_status_get) | **GET** /about/status | 
[**about_version_get**](ManifestsApi.md#about_version_get) | **GET** /about/version | 
[**get_manifest**](ManifestsApi.md#get_manifest) | **GET** /about/manifest | 


# **about_status_get**
> Status about_status_get(manifest=manifest, key=key, value=value)



This endpoint shows the status details of all installed and configured modules. Status details always include human readable name, and module name. Optional details include version, availability, status message, and links to documentation.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/about/manifest.xml\" for XML). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManifestsApi(swagger_client.ApiClient(configuration))
manifest = 'manifest_example' # str | The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions.  (optional)
key = 'key_example' # str | Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.   (optional)
value = 'value_example' # str | Only return manifest entries that have this value for the provided key parameter.            (optional)

try:
    api_response = api_instance.about_status_get(manifest=manifest, key=key, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestsApi->about_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest** | **str**| The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions.  | [optional] 
 **key** | **str**| Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.   | [optional] 
 **value** | **str**| Only return manifest entries that have this value for the provided key parameter.            | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **about_version_get**
> about_version_get(manifest=manifest, key=key, value=value)



'This endpoint shows only the details for the high-level components: GeoServer, GeoTools, and GeoWebCache.'  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/about/manifest.xml\" for XML).' 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManifestsApi(swagger_client.ApiClient(configuration))
manifest = 'manifest_example' # str | The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions.  (optional)
key = 'key_example' # str | Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.   (optional)
value = 'value_example' # str | Only return manifest entries that have this value for the provided key parameter.            (optional)

try:
    api_instance.about_version_get(manifest=manifest, key=key, value=value)
except ApiException as e:
    print("Exception when calling ManifestsApi->about_version_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest** | **str**| The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions.  | [optional] 
 **key** | **str**| Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.   | [optional] 
 **value** | **str**| Only return manifest entries that have this value for the provided key parameter.            | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest**
> Manifest get_manifest(manifest=manifest, key=key, value=value)



This endpoint retrieves details on all loaded JARs. All the GeoServer manifest JARs are marked with the property GeoServerModule and classified by type, so you can use filtering capabilities to search for a set of manifests using regular expressions (see the manifest parameter) or a type category (see the key and value parameter).  The available types are core, extension, or community. To filter modules by a particular type, append a request with key=GeoServerModule&value={type}  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/about/manifest.xml\" for XML).  The model is very simple and is shared between the version and the resource requests to parse both requests. You can customize the results adding a properties file called manifest.properties into the root of the data directory. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManifestsApi(swagger_client.ApiClient(configuration))
manifest = 'manifest_example' # str | The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions.  (optional)
key = 'key_example' # str | Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.   (optional)
value = 'value_example' # str | Only return manifest entries that have this value for the provided key parameter.            (optional)

try:
    api_response = api_instance.get_manifest(manifest=manifest, key=key, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestsApi->get_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest** | **str**| The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions.  | [optional] 
 **key** | **str**| Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.   | [optional] 
 **value** | **str**| Only return manifest entries that have this value for the provided key parameter.            | [optional] 

### Return type

[**Manifest**](Manifest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

