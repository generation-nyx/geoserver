# swagger_client.ResourceApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_delete**](ResourceApi.md#resource_delete) | **DELETE** /resource/{pathToResource} | 
[**resource_get**](ResourceApi.md#resource_get) | **GET** /resource/{pathToResource} | 
[**resource_head**](ResourceApi.md#resource_head) | **HEAD** /resource/{pathToResource} | 
[**resource_post**](ResourceApi.md#resource_post) | **POST** /resource/{pathToResource} | 
[**resource_put**](ResourceApi.md#resource_put) | **PUT** /resource/{pathToResource} | 


# **resource_delete**
> resource_delete(path_to_resource)



Delete a resource (recursively if directory)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourceApi()
path_to_resource = 'path_to_resource_example' # str | The full path to the resource. Required, but may be empty; a request to `/resource` references the top level resource directory.

try:
    api_instance.resource_delete(path_to_resource)
except ApiException as e:
    print("Exception when calling ResourceApi->resource_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_to_resource** | **str**| The full path to the resource. Required, but may be empty; a request to &#x60;/resource&#x60; references the top level resource directory. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_get**
> resource_get(path_to_resource, operation=operation, format=format)



Download a resource, list contents of directory, or show formatted resource metadata.  Response content depends upon parameters.  With `operation=default`, if the request is made against a non-directory resource, the content of the resource is returned.  For example, `/resource/styles/default_point.sld?operation=default`  ``` <?xml version=\"1.0\" encoding=\"UTF-8\"?> <StyledLayerDescriptor version=\"1.0.0\"   xsi:schemaLocation=\"http://www.opengis.net/sld StyledLayerDescriptor.xsd\"   xmlns=\"http://www.opengis.net/sld\"   xmlns:ogc=\"http://www.opengis.net/ogc\"   xmlns:xlink=\"http://www.w3.org/1999/xlink\"   xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">   <!-- a Named Layer is the basic building block of an SLD document -->   <NamedLayer>     <Name>default_point</Name>     <UserStyle>     <!-- Styles can have names, titles and abstracts -->       <Title>Default Point</Title>       <Abstract>A sample style that draws a point</Abstract>       <!-- FeatureTypeStyles describe how to render different features -->       <!-- A FeatureTypeStyle for rendering points -->       <FeatureTypeStyle>         <Rule>           <Name>rule1</Name>           <Title>Red Square</Title>           <Abstract>A 6 pixel square with a red fill and no stroke</Abstract>             <PointSymbolizer>               <Graphic>                 <Mark>                   <WellKnownName>square</WellKnownName>                   <Fill>                     <CssParameter name=\"fill\">#FF0000</CssParameter>                   </Fill>                 </Mark>               <Size>6</Size>             </Graphic>           </PointSymbolizer>         </Rule>       </FeatureTypeStyle>     </UserStyle>   </NamedLayer> </StyledLayerDescriptor> ```  If the request is made against a directory resource, a \"ResourceDirectory\" response is returned, containing information about the directory and its children. Examples:  - `http://localhost:8080/geoserver/rest/resource/logs?operation=default&format=xml`   ```   <ResourceDirectory>     <name>logs</name>     <parent>       <path>/</path>       <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/\" rel=\"alternate\" type=\"application/xml\"/>     </parent>     <lastModified>2017-09-15 18:50:54.0 UTC</lastModified>     <children>       <child>         <name>DEFAULT_LOGGING.xml</name>         <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/logs/DEFAULT_LOGGING.xml\" rel=\"alternate\" type=\"application/octet-stream\"/>       </child>       <child>         <name>geoserver.log</name>         <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/logs/geoserver.log\" rel=\"alternate\" type=\"application/octet-stream\"/>       </child>       <child>         <name>geoserver.log.1</name>         <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/logs/geoserver.log.1\" rel=\"alternate\" type=\"application/octet-stream\"/>       </child>       <child>         <name>geoserver.log.2</name>         <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/logs/geoserver.log.2\" rel=\"alternate\" type=\"application/octet-stream\"/>       </child>       <child>         <name>GEOSERVER_DEVELOPER_LOGGING.xml</name>         <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/logs/GEOSERVER_DEVELOPER_LOGGING.xml\" rel=\"alternate\" type=\"application/octet-stream\"/>       </child>       <child>         <name>GEOTOOLS_DEVELOPER_LOGGING.xml</name>         <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/logs/GEOTOOLS_DEVELOPER_LOGGING.xml\" rel=\"alternate\" type=\"application/octet-stream\"/>       </child>       <child>         <name>PRODUCTION_LOGGING.xml</name>         <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/logs/PRODUCTION_LOGGING.xml\" rel=\"alternate\" type=\"application/octet-stream\"/>       </child>       <child>         <name>QUIET_LOGGING.xml</name>         <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/logs/QUIET_LOGGING.xml\" rel=\"alternate\" type=\"application/octet-stream\"/>       </child>       <child>         <name>TEST_LOGGING.xml</name>         <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/logs/TEST_LOGGING.xml\" rel=\"alternate\" type=\"application/octet-stream\"/>       </child>       <child>         <name>VERBOSE_LOGGING.xml</name>         <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/logs/VERBOSE_LOGGING.xml\" rel=\"alternate\" type=\"application/octet-stream\"/>       </child>     </children>   </ResourceDirectory>   ```  - `http://localhost:8080/geoserver/rest/resource/logs?operation=default&format=json`   ```   {\"ResourceDirectory\":{\"name\":\"logs\",\"parent\":{\"path\":\"/\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/\",\"rel\":\"alternate\",\"type\":\"application/json\"}},\"lastModified\":\"2017-09-15 18:50:54.0 UTC\",\"children\":{\"child\":[{\"name\":\"DEFAULT_LOGGING.xml\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/logs/DEFAULT_LOGGING.xml\",\"rel\":\"alternate\",\"type\":\"application/octet-stream\"}},{\"name\":\"geoserver.log\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/logs/geoserver.log\",\"rel\":\"alternate\",\"type\":\"application/octet-stream\"}},{\"name\":\"geoserver.log.1\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/logs/geoserver.log.1\",\"rel\":\"alternate\",\"type\":\"application/octet-stream\"}},{\"name\":\"geoserver.log.2\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/logs/geoserver.log.2\",\"rel\":\"alternate\",\"type\":\"application/octet-stream\"}},{\"name\":\"GEOSERVER_DEVELOPER_LOGGING.xml\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/logs/GEOSERVER_DEVELOPER_LOGGING.xml\",\"rel\":\"alternate\",\"type\":\"application/octet-stream\"}},{\"name\":\"GEOTOOLS_DEVELOPER_LOGGING.xml\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/logs/GEOTOOLS_DEVELOPER_LOGGING.xml\",\"rel\":\"alternate\",\"type\":\"application/octet-stream\"}},{\"name\":\"PRODUCTION_LOGGING.xml\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/logs/PRODUCTION_LOGGING.xml\",\"rel\":\"alternate\",\"type\":\"application/octet-stream\"}},{\"name\":\"QUIET_LOGGING.xml\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/logs/QUIET_LOGGING.xml\",\"rel\":\"alternate\",\"type\":\"application/octet-stream\"}},{\"name\":\"TEST_LOGGING.xml\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/logs/TEST_LOGGING.xml\",\"rel\":\"alternate\",\"type\":\"application/octet-stream\"}},{\"name\":\"VERBOSE_LOGGING.xml\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/logs/VERBOSE_LOGGING.xml\",\"rel\":\"alternate\",\"type\":\"application/octet-stream\"}}]}}}   ```  With `operation=metadata`, a \"ResourceMetadata\" object is returned. If the resource is a directory, this metadata object will not list the children of the directory. Examples:  - `http://localhost:8080/geoserver/rest/resource/styles/default_point.sld?operation=metadata&format=xml`   ```   <ResourceMetadata>     <name>default_point.sld</name>     <parent>       <path>/styles</path>       <atom:link xmlns:atom=\"http://www.w3.org/2005/Atom\" href=\"http://localhost:8080/geoserver/rest/resource/styles\" rel=\"alternate\" type=\"application/xml\"/>     </parent>     <lastModified>2017-01-18 19:02:38.0 UTC</lastModified>     <type>resource</type>   </ResourceMetadata>   ``` - `http://localhost:8080/geoserver/rest/resource/styles/default_point.sld?operation=metadata&format=json`   ```   {\"ResourceMetadata\":{\"name\":\"default_point.sld\",\"parent\":{\"path\":\"/styles\",\"link\":{\"href\":\"http://localhost:8080/geoserver/rest/resource/styles\",\"rel\":\"alternate\",\"type\":\"application/json\"}},\"lastModified\":\"2017-01-18 19:02:38.0 UTC\",\"type\":\"resource\"}}   ``` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourceApi()
path_to_resource = 'path_to_resource_example' # str | The full path to the resource. Required, but may be empty; a request to `/resource` references the top level resource directory.
operation = 'default' # str | The type of GET operation. `default` returns a list of the contained resources in the case of a directory resource, or the actual resource contents in the case of a resource resource.`metadata` requests a metadata summary of the resource. (optional) (default to default)
format = 'html' # str | The format of the response. Only applicable for the `metadata` operation, or for a directory resource. (optional) (default to html)

try:
    api_instance.resource_get(path_to_resource, operation=operation, format=format)
except ApiException as e:
    print("Exception when calling ResourceApi->resource_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_to_resource** | **str**| The full path to the resource. Required, but may be empty; a request to &#x60;/resource&#x60; references the top level resource directory. | 
 **operation** | **str**| The type of GET operation. &#x60;default&#x60; returns a list of the contained resources in the case of a directory resource, or the actual resource contents in the case of a resource resource.&#x60;metadata&#x60; requests a metadata summary of the resource. | [optional] [default to default]
 **format** | **str**| The format of the response. Only applicable for the &#x60;metadata&#x60; operation, or for a directory resource. | [optional] [default to html]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/plain, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_head**
> resource_head(path_to_resource)



Show resource metadata in HTTP headers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourceApi()
path_to_resource = 'path_to_resource_example' # str | The full path to the resource. Required, but may be empty; a request to `/resource` references the top level resource directory.

try:
    api_instance.resource_head(path_to_resource)
except ApiException as e:
    print("Exception when calling ResourceApi->resource_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_to_resource** | **str**| The full path to the resource. Required, but may be empty; a request to &#x60;/resource&#x60; references the top level resource directory. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_post**
> resource_post(path_to_resource)



Invalid. Use PUT to create a resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourceApi()
path_to_resource = 'path_to_resource_example' # str | The full path to the resource. Required, but may be empty; a request to `/resource` references the top level resource directory.

try:
    api_instance.resource_post(path_to_resource)
except ApiException as e:
    print("Exception when calling ResourceApi->resource_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_to_resource** | **str**| The full path to the resource. Required, but may be empty; a request to &#x60;/resource&#x60; references the top level resource directory. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_put**
> resource_put(path_to_resource, operation=operation, resource_body=resource_body)



Upload/move/copy a resource, create directories on the fly (overwrite if exists). For move/copy operations, place source path in body. Copying is not supported for directories.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourceApi()
path_to_resource = 'path_to_resource_example' # str | The full path to the resource. Required, but may be empty; a request to `/resource` references the top level resource directory.
operation = 'default' # str | The type of PUT operation. `default` creates a new resource or alters an existing resource. `move` moves the resource to a new location. `copy` duplicates the resource to a new location (optional) (default to default)
resource_body = 'B' # str | The content of the resource to upload. In the case of a `move` or `copy` operation, this is instead the path to the source resource to move/copy from. (optional)

try:
    api_instance.resource_put(path_to_resource, operation=operation, resource_body=resource_body)
except ApiException as e:
    print("Exception when calling ResourceApi->resource_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_to_resource** | **str**| The full path to the resource. Required, but may be empty; a request to &#x60;/resource&#x60; references the top level resource directory. | 
 **operation** | **str**| The type of PUT operation. &#x60;default&#x60; creates a new resource or alters an existing resource. &#x60;move&#x60; moves the resource to a new location. &#x60;copy&#x60; duplicates the resource to a new location | [optional] [default to default]
 **resource_body** | **str**| The content of the resource to upload. In the case of a &#x60;move&#x60; or &#x60;copy&#x60; operation, this is instead the path to the source resource to move/copy from. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

