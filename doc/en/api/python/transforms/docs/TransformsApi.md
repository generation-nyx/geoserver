# swagger_client.TransformsApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tranform**](TransformsApi.md#delete_tranform) | **DELETE** /services/wfs/transforms/{transform} | Delete transformation
[**delete_transform**](TransformsApi.md#delete_transform) | **DELETE** /services/wfs/transforms | 
[**get_transform**](TransformsApi.md#get_transform) | **GET** /services/wfs/transforms/{transform} | Retrieve a transformation.
[**get_transforms**](TransformsApi.md#get_transforms) | **GET** /services/wfs/transforms | List available transformations.
[**post_tranform**](TransformsApi.md#post_tranform) | **POST** /services/wfs/transforms/{transform} | 
[**post_transform**](TransformsApi.md#post_transform) | **POST** /services/wfs/transforms | Add a new transform
[**put_tranform**](TransformsApi.md#put_tranform) | **PUT** /services/wfs/transforms/{transform} | Modify a single transform
[**put_transform**](TransformsApi.md#put_transform) | **PUT** /services/wfs/transforms | 


# **delete_tranform**
> delete_tranform(transform)

Delete transformation

Deletes a transformation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransformsApi()
transform = 'transform_example' # str | Name of the transformation.

try:
    # Delete transformation
    api_instance.delete_tranform(transform)
except ApiException as e:
    print("Exception when calling TransformsApi->delete_tranform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform** | **str**| Name of the transformation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transform**
> delete_transform()



Invalid.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransformsApi()

try:
    api_instance.delete_transform()
except ApiException as e:
    print("Exception when calling TransformsApi->delete_transform: %s\n" % e)
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

# **get_transform**
> Transform get_transform(transform)

Retrieve a transformation.

Retrieves a single transformation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransformsApi()
transform = 'transform_example' # str | Name of the transformation.

try:
    # Retrieve a transformation.
    api_response = api_instance.get_transform(transform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransformsApi->get_transform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform** | **str**| Name of the transformation. | 

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/xslt+xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transforms**
> TransformList get_transforms()

List available transformations.

Displays a list of all the transforms information available on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/styles.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransformsApi()

try:
    # List available transformations.
    api_response = api_instance.get_transforms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransformsApi->get_transforms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransformList**](TransformList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tranform**
> post_tranform()



Invalid.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransformsApi()

try:
    api_instance.post_tranform()
except ApiException as e:
    print("Exception when calling TransformsApi->post_tranform: %s\n" % e)
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

# **post_transform**
> post_transform(transform_body, name=name, source_format=source_format, output_format=output_format, output_mime_type=output_mime_type, file_extension=file_extension)

Add a new transform

Adds a new transform to the server. If the content type used is application/xml the server will assume a <transform> definition is being posted, and the XSLT will have to be uploaded separately using a PUT request with content type application/xslt+xml against the transformation resource. If the content type used is application/xslt+xml the server will assume the XSLT itself is being posted, and the name, sourceFormat, outputFormat, outputMimeType query parameters will be used to fill in the transform configuration instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransformsApi()
transform_body = swagger_client.Transform() # Transform | Transform body to upload.
name = 'name_example' # str | Name of the transformation. (optional)
source_format = 'source_format_example' # str | Source format of the transformation. (optional)
output_format = 'output_format_example' # str | Output format of the transformation. (optional)
output_mime_type = 'output_mime_type_example' # str | Output mime type of the transformation. (optional)
file_extension = 'file_extension_example' # str | The extension of the file generated by the transformation. (optional)

try:
    # Add a new transform
    api_instance.post_transform(transform_body, name=name, source_format=source_format, output_format=output_format, output_mime_type=output_mime_type, file_extension=file_extension)
except ApiException as e:
    print("Exception when calling TransformsApi->post_transform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform_body** | [**Transform**](Transform.md)| Transform body to upload. | 
 **name** | **str**| Name of the transformation. | [optional] 
 **source_format** | **str**| Source format of the transformation. | [optional] 
 **output_format** | **str**| Output format of the transformation. | [optional] 
 **output_mime_type** | **str**| Output mime type of the transformation. | [optional] 
 **file_extension** | **str**| The extension of the file generated by the transformation. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/xslt+xml, application/json, text/html
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tranform**
> put_tranform(transform_body, transform)

Modify a single transform

Modifies a single transform.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransformsApi()
transform_body = swagger_client.Transform() # Transform | Transform body to upload.
transform = 'transform_example' # str | Name of the transformation.

try:
    # Modify a single transform
    api_instance.put_tranform(transform_body, transform)
except ApiException as e:
    print("Exception when calling TransformsApi->put_tranform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transform_body** | [**Transform**](Transform.md)| Transform body to upload. | 
 **transform** | **str**| Name of the transformation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json, application/xslt+xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_transform**
> put_transform()



Invalid. Use POST for adding a new transformation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransformsApi()

try:
    api_instance.put_transform()
except ApiException as e:
    print("Exception when calling TransformsApi->put_transform: %s\n" % e)
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

