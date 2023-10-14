# swagger_client.StylesApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_layer_styles**](StylesApi.md#delete_layer_styles) | **DELETE** /rest/layers/{layer}/styles | 
[**delete_style**](StylesApi.md#delete_style) | **DELETE** /styles/{style} | Delete style
[**delete_styles**](StylesApi.md#delete_styles) | **DELETE** /styles | 
[**delete_workspace_style**](StylesApi.md#delete_workspace_style) | **DELETE** /rest/workspaces/{workspace}/styles/{style} | Delete style in a given workspace
[**delete_workspace_styles**](StylesApi.md#delete_workspace_styles) | **DELETE** /workspaces/{workspace}/styles | 
[**get_layer_styles**](StylesApi.md#get_layer_styles) | **GET** /rest/layers/{layer}/styles | Get a list of layer alternate styles
[**get_style**](StylesApi.md#get_style) | **GET** /styles/{style} | Retrieve a style
[**get_styles**](StylesApi.md#get_styles) | **GET** /styles | Get a list of styles
[**get_workspace_style**](StylesApi.md#get_workspace_style) | **GET** /rest/workspaces/{workspace}/styles/{style} | Retrieve a style from a given workspace
[**get_workspace_styles**](StylesApi.md#get_workspace_styles) | **GET** /workspaces/{workspace}/styles | Get a list of styles in a given workspace
[**post_layer_styles**](StylesApi.md#post_layer_styles) | **POST** /rest/layers/{layer}/styles | Add a new style
[**post_style**](StylesApi.md#post_style) | **POST** /styles/{style} | 
[**post_styles**](StylesApi.md#post_styles) | **POST** /styles | Add a new style
[**post_workspace_style**](StylesApi.md#post_workspace_style) | **POST** /rest/workspaces/{workspace}/styles/{style} | 
[**post_workspace_styles**](StylesApi.md#post_workspace_styles) | **POST** /workspaces/{workspace}/styles | Add a new style to a given workspace
[**put_layer_styles**](StylesApi.md#put_layer_styles) | **PUT** /rest/layers/{layer}/styles | 
[**put_style**](StylesApi.md#put_style) | **PUT** /styles/{style} | Modify a single style
[**put_styles**](StylesApi.md#put_styles) | **PUT** /styles | 
[**put_workspace_style**](StylesApi.md#put_workspace_style) | **PUT** /rest/workspaces/{workspace}/styles/{style} | Modify a single style in a given workspace
[**put_workspace_styles**](StylesApi.md#put_workspace_styles) | **PUT** /workspaces/{workspace}/styles | 


# **delete_layer_styles**
> delete_layer_styles(layer)



Invalid.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
layer = 'layer_example' # str | Name of the layer to manage styles for

try:
    api_instance.delete_layer_styles(layer)
except ApiException as e:
    print("Exception when calling StylesApi->delete_layer_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer** | **str**| Name of the layer to manage styles for | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_style**
> delete_style(style, purge=purge, recurse=recurse)

Delete style

Deletes a style.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
style = 'style_example' # str | Name of the style to delete.
purge = false # bool | Specifies whether the underlying file containing the style should be deleted on disk. (optional) (default to false)
recurse = false # bool | Removes references to the specified style in existing layers. (optional) (default to false)

try:
    # Delete style
    api_instance.delete_style(style, purge=purge, recurse=recurse)
except ApiException as e:
    print("Exception when calling StylesApi->delete_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **style** | **str**| Name of the style to delete. | 
 **purge** | **bool**| Specifies whether the underlying file containing the style should be deleted on disk. | [optional] [default to false]
 **recurse** | **bool**| Removes references to the specified style in existing layers. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_styles**
> delete_styles()



Invalid. Use /styles/{style} instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()

try:
    api_instance.delete_styles()
except ApiException as e:
    print("Exception when calling StylesApi->delete_styles: %s\n" % e)
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

# **delete_workspace_style**
> delete_workspace_style(workspace, style, purge=purge, recurse=recurse)

Delete style in a given workspace

Deletes a style in a given workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
workspace = 'workspace_example' # str | Name of the workspace for style definitions
style = 'style_example' # str | Name of the style to delete.
purge = false # bool | Specifies whether the underlying file containing the style should be deleted on disk. (optional) (default to false)
recurse = false # bool | Removes references to the specified style in existing layers. (optional) (default to false)

try:
    # Delete style in a given workspace
    api_instance.delete_workspace_style(workspace, style, purge=purge, recurse=recurse)
except ApiException as e:
    print("Exception when calling StylesApi->delete_workspace_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace for style definitions | 
 **style** | **str**| Name of the style to delete. | 
 **purge** | **bool**| Specifies whether the underlying file containing the style should be deleted on disk. | [optional] [default to false]
 **recurse** | **bool**| Removes references to the specified style in existing layers. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_styles**
> delete_workspace_styles(workspace)



Invalid. Use /workspaces/{workspace}/styles/{style} instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
workspace = 'workspace_example' # str | Name of workspace

try:
    api_instance.delete_workspace_styles(workspace)
except ApiException as e:
    print("Exception when calling StylesApi->delete_workspace_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of workspace | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layer_styles**
> StyleList get_layer_styles(layer)

Get a list of layer alternate styles

Displays a list of all alternate styles for a given layer. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layers/{layer}/styles.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
layer = 'layer_example' # str | Name of the layer to manage styles for

try:
    # Get a list of layer alternate styles
    api_response = api_instance.get_layer_styles(layer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->get_layer_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer** | **str**| Name of the layer to manage styles for | 

### Return type

[**StyleList**](StyleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_style**
> Style get_style(style)

Retrieve a style

Retrieves a single style. Used to both request the style info and the style definition body, depending on the media type requested. The media type can be specified either by using the \"Accept:\" header or by appending an extension to the endpoint. For example, a style info can be requested in XML format using \"/styles/{style}.xml\" or \"Accept: application/xml\". (Also available: \"{style}.json\", \"Accept: application/json\" \"{style}.html\", and \"Accept: text/html\").  The style definition body can be requested by either appending the file extension of the style file (e.g., \"{style}.sld\" or \"{style}.css\") or by specifying the correct media type for the style definition in the \"Accept\" header. Be aware that by default, if extension is specified, it will override media type. For example if you use SLD 1.1.0 style and specify .sld extension (which provides SLD 1.0.0 result), but use application/vnd.ogc.se+xml media type (which provides SLD 1.1.0 result), response still will be presented in sld version 1.0.0 Below are common style formats and the corresponding media types that can be used in the Accept header to request the style definition body.  - application/vnd.ogc.sld+xml for SLD 1.0.0 SLDs - application/vnd.ogc.se+xml for SLD 1.1.0 SLDs - application/vnd.geoserver.geocss+css for css styles - application/vnd.geoserver.ysld+yaml for ysld styles - application/vnd.geoserver.mbstyle+json for mb styles 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
style = 'style_example' # str | Name of the style to retrieve.

try:
    # Retrieve a style
    api_response = api_instance.get_style(style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->get_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **style** | **str**| Name of the style to retrieve. | 

### Return type

[**Style**](Style.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, application/vnd.ogc.sld+xml, application/vnd.ogc.se+xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_styles**
> StyleList get_styles()

Get a list of styles

Displays a list of all styles on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/styles.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()

try:
    # Get a list of styles
    api_response = api_instance.get_styles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->get_styles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StyleList**](StyleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_style**
> StyleWorkspace get_workspace_style(workspace, style)

Retrieve a style from a given workspace

Retrieves a single style. Used to both request the style info and the style definition body, depending on the media type requested. The media type can be specified either by using the \"Accept:\" header or by appending an extension to the endpoint. For example, a style info can be requested in XML format using \"/styles/{style}.xml\" or \"Accept: application/xml\". (Also available: \"{style}.json\", \"Accept: application/json\" \"{style}.html\", and \"Accept: text/html\").  The style definition body can be requested by either appending the file extension of the style file (e.g., \"{style}.sld\" or \"{style}.css\") or by specifying the correct media type for the style definition in the \"Accept\" header. Be aware that by default, if extension is specified, it will override media type. For example if you use SLD 1.1.0 style and specify .sld extension (which provides SLD 1.0.0 result), but use application/vnd.ogc.se+xml media type (which provides SLD 1.1.0 result), response still will be presented in sld version 1.0.0 Below are common style formats and the corresponding media types that can be used in the Accept header to request the style definition body.  - application/vnd.ogc.sld+xml for SLD 1.0.0 SLDs - application/vnd.ogc.se+xml for SLD 1.1.0 SLDs - application/vnd.geoserver.geocss+css for css styles - application/vnd.geoserver.ysld+yaml for ysld styles - application/vnd.geoserver.mbstyle+json for mb styles 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
workspace = 'workspace_example' # str | Name of the workspace for style definitions
style = 'style_example' # str | Name of the style to retrieve.

try:
    # Retrieve a style from a given workspace
    api_response = api_instance.get_workspace_style(workspace, style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->get_workspace_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace for style definitions | 
 **style** | **str**| Name of the style to retrieve. | 

### Return type

[**StyleWorkspace**](StyleWorkspace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, application/vnd.ogc.sld+xml, application/vnd.ogc.se+xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_styles**
> StyleList get_workspace_styles(workspace)

Get a list of styles in a given workspace

Displays a list of all styles in a given workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/styles.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
workspace = 'workspace_example' # str | Name of workspace

try:
    # Get a list of styles in a given workspace
    api_response = api_instance.get_workspace_styles(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->get_workspace_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of workspace | 

### Return type

[**StyleList**](StyleList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_layer_styles**
> post_layer_styles(layer, style_body, default=default)

Add a new style

Adds a new style entry to the layer. The style named in styleBody must already exist, and will not be altered by this request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
layer = 'layer_example' # str | Name of the layer to manage styles for
style_body = swagger_client.StyleInfoPost() # StyleInfoPost | Style body information naming an existing style to add to the layer
default = false # bool | Whether to make this the default style for the layer. (optional) (default to false)

try:
    # Add a new style
    api_instance.post_layer_styles(layer, style_body, default=default)
except ApiException as e:
    print("Exception when calling StylesApi->post_layer_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer** | **str**| Name of the layer to manage styles for | 
 **style_body** | [**StyleInfoPost**](StyleInfoPost.md)| Style body information naming an existing style to add to the layer | 
 **default** | **bool**| Whether to make this the default style for the layer. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_style**
> post_style(style)



Invalid. Use PUT to edit a style, or POST with /styles to add a new style.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
style = 'style_example' # str | Name of the style to retrieve.

try:
    api_instance.post_style(style)
except ApiException as e:
    print("Exception when calling StylesApi->post_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **style** | **str**| Name of the style to retrieve. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_styles**
> post_styles(style_body, name=name, content_type=content_type)

Add a new style

Adds a new style entry to the server.  Using POST with the `application/xml` or `application/json` content only adds the style info to the catalog and does not upload style content. PUT to `/styles/{style}` to upload the style in this case.  Use POST with a style file (`application/vnd.ogc.sld+xml` or `application/vnd.ogc.se+xml` for SLD; additional style types are added by extensions) to generate a style info and upload the style all at once. Then separately PUT the style info at `/styles/{style}` to make any desired changes to the generated catalog entry. You can also use POST with a ZIP file to upload a SLD 1.0 (`application/vnd.ogc.sld+xml`) file and any associated icon files, and then separately PUT the style info at /styles/{style}. POST with a ZIP file does not support any other style types. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
style_body = swagger_client.StyleInfoPost() # StyleInfoPost |  The style body of a request JSON or XML style uploads follow the schema. For example:    - application/xml:           ```     <style>       <name>roads_style</name>       <filename>roads.sld</filename>     </style>     ```    - application/json:         ```     {       \"style\": {          \"name\": \"roads_style\",          \"filename\": \"roads.sld\"       }     }     ```  Otherwise, the style body is an actual style:    - application/zip:         ```     <ZIP file containing SLD and icons>     ```          - application/vnd.ogc.sld+xml:      ```     <?xml version=\"1.0\" encoding=\"UTF-8\"?>     <StyledLayerDescriptor version=\"1.0.0\"       xsi:schemaLocation=\"http://www.opengis.net/sld StyledLayerDescriptor.xsd\"       xmlns=\"http://www.opengis.net/sld\"       xmlns:ogc=\"http://www.opengis.net/ogc\"       xmlns:xlink=\"http://www.w3.org/1999/xlink\"       xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">       <!-- a Named Layer is the basic building block of an SLD document -->       <NamedLayer>         <Name>default_line</Name>         <UserStyle>         <!-- Styles can have names, titles and abstracts -->           <Title>Default Line</Title>           <Abstract>A sample style that draws a line</Abstract>           <!-- FeatureTypeStyles describe how to render different features -->           <!-- A FeatureTypeStyle for rendering lines -->           <FeatureTypeStyle>             <Rule>               <Name>rule1</Name>               <Title>Blue Line</Title>               <Abstract>A solid blue line with a 1 pixel width</Abstract>               <LineSymbolizer>                 <Stroke>                   <CssParameter name=\"stroke\">#0000FF</CssParameter>                 </Stroke>               </LineSymbolizer>             </Rule>           </FeatureTypeStyle>         </UserStyle>       </NamedLayer>     </StyledLayerDescriptor>     ``` 
name = 'name_example' # str | The name of the style. Used only when POSTing a style file or ZIP bundle, to determine the name of the style in the catalog. Generated from the filename if not provided. (optional)
content_type = 'content_type_example' # str | Content-Type of the style file. Used to determine style encoding when POSTing a style file (e.g. SLD or SE). (optional)

try:
    # Add a new style
    api_instance.post_styles(style_body, name=name, content_type=content_type)
except ApiException as e:
    print("Exception when calling StylesApi->post_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **style_body** | [**StyleInfoPost**](StyleInfoPost.md)|  The style body of a request JSON or XML style uploads follow the schema. For example:    - application/xml:           &#x60;&#x60;&#x60;     &lt;style&gt;       &lt;name&gt;roads_style&lt;/name&gt;       &lt;filename&gt;roads.sld&lt;/filename&gt;     &lt;/style&gt;     &#x60;&#x60;&#x60;    - application/json:         &#x60;&#x60;&#x60;     {       \&quot;style\&quot;: {          \&quot;name\&quot;: \&quot;roads_style\&quot;,          \&quot;filename\&quot;: \&quot;roads.sld\&quot;       }     }     &#x60;&#x60;&#x60;  Otherwise, the style body is an actual style:    - application/zip:         &#x60;&#x60;&#x60;     &lt;ZIP file containing SLD and icons&gt;     &#x60;&#x60;&#x60;          - application/vnd.ogc.sld+xml:      &#x60;&#x60;&#x60;     &lt;?xml version&#x3D;\&quot;1.0\&quot; encoding&#x3D;\&quot;UTF-8\&quot;?&gt;     &lt;StyledLayerDescriptor version&#x3D;\&quot;1.0.0\&quot;       xsi:schemaLocation&#x3D;\&quot;http://www.opengis.net/sld StyledLayerDescriptor.xsd\&quot;       xmlns&#x3D;\&quot;http://www.opengis.net/sld\&quot;       xmlns:ogc&#x3D;\&quot;http://www.opengis.net/ogc\&quot;       xmlns:xlink&#x3D;\&quot;http://www.w3.org/1999/xlink\&quot;       xmlns:xsi&#x3D;\&quot;http://www.w3.org/2001/XMLSchema-instance\&quot;&gt;       &lt;!-- a Named Layer is the basic building block of an SLD document --&gt;       &lt;NamedLayer&gt;         &lt;Name&gt;default_line&lt;/Name&gt;         &lt;UserStyle&gt;         &lt;!-- Styles can have names, titles and abstracts --&gt;           &lt;Title&gt;Default Line&lt;/Title&gt;           &lt;Abstract&gt;A sample style that draws a line&lt;/Abstract&gt;           &lt;!-- FeatureTypeStyles describe how to render different features --&gt;           &lt;!-- A FeatureTypeStyle for rendering lines --&gt;           &lt;FeatureTypeStyle&gt;             &lt;Rule&gt;               &lt;Name&gt;rule1&lt;/Name&gt;               &lt;Title&gt;Blue Line&lt;/Title&gt;               &lt;Abstract&gt;A solid blue line with a 1 pixel width&lt;/Abstract&gt;               &lt;LineSymbolizer&gt;                 &lt;Stroke&gt;                   &lt;CssParameter name&#x3D;\&quot;stroke\&quot;&gt;#0000FF&lt;/CssParameter&gt;                 &lt;/Stroke&gt;               &lt;/LineSymbolizer&gt;             &lt;/Rule&gt;           &lt;/FeatureTypeStyle&gt;         &lt;/UserStyle&gt;       &lt;/NamedLayer&gt;     &lt;/StyledLayerDescriptor&gt;     &#x60;&#x60;&#x60;  | 
 **name** | **str**| The name of the style. Used only when POSTing a style file or ZIP bundle, to determine the name of the style in the catalog. Generated from the filename if not provided. | [optional] 
 **content_type** | **str**| Content-Type of the style file. Used to determine style encoding when POSTing a style file (e.g. SLD or SE). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json, application/zip, text/xml, text/json, application/vnd.ogc.sld+xml, application/vnd.ogc.se+xml, application/vnd.geoserver.geocss+css, application/vnd.geoserver.ysld+yaml, application/vnd.geoserver.mbstyle+json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workspace_style**
> post_workspace_style(workspace, style)



Invalid. Use PUT to edit a style, or POST with /workspaces/{workspace}/styles to add a new style.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
workspace = 'workspace_example' # str | Name of the workspace for style definitions
style = 'style_example' # str | Name of the style to retrieve.

try:
    api_instance.post_workspace_style(workspace, style)
except ApiException as e:
    print("Exception when calling StylesApi->post_workspace_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace for style definitions | 
 **style** | **str**| Name of the style to retrieve. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workspace_styles**
> post_workspace_styles(workspace, style_body, name=name, content_type=content_type)

Add a new style to a given workspace

Adds a new style entry to the server.  Using POST with the `application/xml` or `application/json` content only adds the style info to the catalog and does not upload style content. PUT to `/workspaces/{workspace}/styles/{style}` to upload the style in this case.  Use POST with a style file (`application/vnd.ogc.sld+xml` or `application/vnd.ogc.sld+xml` for SLD; additional style types are added by extensions) to generate a style info and upload the style all at once. Then separately PUT the style info at `/workspaces/{workspace}/styles/{style}` to make any desired changes to the generated catalog entry. You can also use POST with a ZIP file to upload a SLD 1.0 (`application/vnd.ogc.sld+xml`) file and any associated icon files, and then separately PUT the style info at /workspaces/{workspace}/styles/{style}. POST with a ZIP file does not support any other style types. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
workspace = 'workspace_example' # str | Name of workspace
style_body = swagger_client.StyleInfoPost() # StyleInfoPost |  The style body of a request JSON or XML style uploads follow the schema. For example:    - application/xml:           ```     <style>       <name>roads_style</name>       <filename>roads.sld</filename>     </style>     ```    - application/json:         ```     {       \"style\": {          \"name\": \"roads_style\",          \"filename\": \"roads.sld\"       }     }     ```  Otherwise, the style body is an actual style:    - application/zip:         ```     <ZIP file containing SLD and icons>     ```          - application/vnd.ogc.sld+xml:      ```     <?xml version=\"1.0\" encoding=\"UTF-8\"?>     <StyledLayerDescriptor version=\"1.0.0\"       xsi:schemaLocation=\"http://www.opengis.net/sld StyledLayerDescriptor.xsd\"       xmlns=\"http://www.opengis.net/sld\"       xmlns:ogc=\"http://www.opengis.net/ogc\"       xmlns:xlink=\"http://www.w3.org/1999/xlink\"       xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">       <!-- a Named Layer is the basic building block of an SLD document -->       <NamedLayer>         <Name>default_line</Name>         <UserStyle>         <!-- Styles can have names, titles and abstracts -->           <Title>Default Line</Title>           <Abstract>A sample style that draws a line</Abstract>           <!-- FeatureTypeStyles describe how to render different features -->           <!-- A FeatureTypeStyle for rendering lines -->           <FeatureTypeStyle>             <Rule>               <Name>rule1</Name>               <Title>Blue Line</Title>               <Abstract>A solid blue line with a 1 pixel width</Abstract>               <LineSymbolizer>                 <Stroke>                   <CssParameter name=\"stroke\">#0000FF</CssParameter>                 </Stroke>               </LineSymbolizer>             </Rule>           </FeatureTypeStyle>         </UserStyle>       </NamedLayer>     </StyledLayerDescriptor>     ``` 
name = 'name_example' # str | The name of the style. Used only when POSTing a style file or ZIP bundle, to determine the name of the style in the catalog. Generated from the filename if not provided. (optional)
content_type = 'content_type_example' # str | Content-Type of the style file. Used to determine style encoding when POSTing a style file (e.g. SLD or SE). (optional)

try:
    # Add a new style to a given workspace
    api_instance.post_workspace_styles(workspace, style_body, name=name, content_type=content_type)
except ApiException as e:
    print("Exception when calling StylesApi->post_workspace_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of workspace | 
 **style_body** | [**StyleInfoPost**](StyleInfoPost.md)|  The style body of a request JSON or XML style uploads follow the schema. For example:    - application/xml:           &#x60;&#x60;&#x60;     &lt;style&gt;       &lt;name&gt;roads_style&lt;/name&gt;       &lt;filename&gt;roads.sld&lt;/filename&gt;     &lt;/style&gt;     &#x60;&#x60;&#x60;    - application/json:         &#x60;&#x60;&#x60;     {       \&quot;style\&quot;: {          \&quot;name\&quot;: \&quot;roads_style\&quot;,          \&quot;filename\&quot;: \&quot;roads.sld\&quot;       }     }     &#x60;&#x60;&#x60;  Otherwise, the style body is an actual style:    - application/zip:         &#x60;&#x60;&#x60;     &lt;ZIP file containing SLD and icons&gt;     &#x60;&#x60;&#x60;          - application/vnd.ogc.sld+xml:      &#x60;&#x60;&#x60;     &lt;?xml version&#x3D;\&quot;1.0\&quot; encoding&#x3D;\&quot;UTF-8\&quot;?&gt;     &lt;StyledLayerDescriptor version&#x3D;\&quot;1.0.0\&quot;       xsi:schemaLocation&#x3D;\&quot;http://www.opengis.net/sld StyledLayerDescriptor.xsd\&quot;       xmlns&#x3D;\&quot;http://www.opengis.net/sld\&quot;       xmlns:ogc&#x3D;\&quot;http://www.opengis.net/ogc\&quot;       xmlns:xlink&#x3D;\&quot;http://www.w3.org/1999/xlink\&quot;       xmlns:xsi&#x3D;\&quot;http://www.w3.org/2001/XMLSchema-instance\&quot;&gt;       &lt;!-- a Named Layer is the basic building block of an SLD document --&gt;       &lt;NamedLayer&gt;         &lt;Name&gt;default_line&lt;/Name&gt;         &lt;UserStyle&gt;         &lt;!-- Styles can have names, titles and abstracts --&gt;           &lt;Title&gt;Default Line&lt;/Title&gt;           &lt;Abstract&gt;A sample style that draws a line&lt;/Abstract&gt;           &lt;!-- FeatureTypeStyles describe how to render different features --&gt;           &lt;!-- A FeatureTypeStyle for rendering lines --&gt;           &lt;FeatureTypeStyle&gt;             &lt;Rule&gt;               &lt;Name&gt;rule1&lt;/Name&gt;               &lt;Title&gt;Blue Line&lt;/Title&gt;               &lt;Abstract&gt;A solid blue line with a 1 pixel width&lt;/Abstract&gt;               &lt;LineSymbolizer&gt;                 &lt;Stroke&gt;                   &lt;CssParameter name&#x3D;\&quot;stroke\&quot;&gt;#0000FF&lt;/CssParameter&gt;                 &lt;/Stroke&gt;               &lt;/LineSymbolizer&gt;             &lt;/Rule&gt;           &lt;/FeatureTypeStyle&gt;         &lt;/UserStyle&gt;       &lt;/NamedLayer&gt;     &lt;/StyledLayerDescriptor&gt;     &#x60;&#x60;&#x60;  | 
 **name** | **str**| The name of the style. Used only when POSTing a style file or ZIP bundle, to determine the name of the style in the catalog. Generated from the filename if not provided. | [optional] 
 **content_type** | **str**| Content-Type of the style file. Used to determine style encoding when POSTing a style file (e.g. SLD or SE). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json, application/zip, text/html, text/json, application/vnd.ogc.sld+xml, application/vnd.ogc.se+xml, application/vnd.geoserver.geocss+css, application/vnd.geoserver.ysld+yaml, application/vnd.geoserver.mbstyle+json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_layer_styles**
> put_layer_styles(layer)



Invalid. Use POST to modify the styles for a layer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
layer = 'layer_example' # str | Name of the layer to manage styles for

try:
    api_instance.put_layer_styles(layer)
except ApiException as e:
    print("Exception when calling StylesApi->put_layer_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer** | **str**| Name of the layer to manage styles for | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_style**
> put_style(style_body, style, raw=raw)

Modify a single style

Modifies a single style.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example `/styles/{style}.xml` for XML).  Using PUT with the `application/xml` or `application/json` content modifies the style info in the catalog and does not alter the style content. Using PUT with any other format will modify the content of the style. You can also use PUT with a ZIP file to upload a SLD 1.0 (`application/vnd.ogc.sld+xml`) file and any associated icon files 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
style_body = swagger_client.StyleInfoPost() # StyleInfoPost |  The style body of a request. For a PUT, only values which should be changed need to be included. JSON or XML style uploads follow the schema, and alter the style configuration. For example:    - application/xml:           ```     <style>       <name>roads_style</name>       <languageVersion>         <version>1.0.0</version>       </languageVersion>       <filename>roads.sld</filename>       <legend>         <width>32</width>         <height>32</height>         <format>image/png; charset=UTF-8</format>         <onlineResource>legend.png</onlineResource>       </legend>     </style>     ```    - application/json:         ```     {       \"style\": {          \"name\": \"roads_style\",          \"languageVersion\": {           \"version\": \"1.0.0\"         },         \"filename\": \"roads.sld\",         \"legend\": {           \"format\": \"image/png; charset=UTF-8\",           \"height\": 32,           \"width\": 32,           \"onlineResource\": \"grass_fill.png\"         }       }     }     ```  Otherwise, the style body is an actual style:    - application/zip:           ```       <ZIP file containing SLD and icons>       ```          - application/vnd.ogc.sld+xml:      ```     <?xml version=\"1.0\" encoding=\"UTF-8\"?>     <StyledLayerDescriptor version=\"1.0.0\"       xsi:schemaLocation=\"http://www.opengis.net/sld StyledLayerDescriptor.xsd\"       xmlns=\"http://www.opengis.net/sld\"       xmlns:ogc=\"http://www.opengis.net/ogc\"       xmlns:xlink=\"http://www.w3.org/1999/xlink\"       xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">       <!-- a Named Layer is the basic building block of an SLD document -->       <NamedLayer>         <Name>default_line</Name>         <UserStyle>         <!-- Styles can have names, titles and abstracts -->           <Title>Default Line</Title>           <Abstract>A sample style that draws a line</Abstract>           <!-- FeatureTypeStyles describe how to render different features -->           <!-- A FeatureTypeStyle for rendering lines -->           <FeatureTypeStyle>             <Rule>               <Name>rule1</Name>               <Title>Blue Line</Title>               <Abstract>A solid blue line with a 1 pixel width</Abstract>               <LineSymbolizer>                 <Stroke>                   <CssParameter name=\"stroke\">#0000FF</CssParameter>                 </Stroke>               </LineSymbolizer>             </Rule>           </FeatureTypeStyle>         </UserStyle>       </NamedLayer>     </StyledLayerDescriptor>     ``` 
style = 'style_example' # str | Name of the style to edit.
raw = false # bool | When set to \"true\", will forgo parsing and encoding of the uploaded style content, and instead the style will be streamed directly to the GeoServer configuration. Use this setting if the content and formatting of the style is to be preserved exactly. May result in an invalid and unusable style if the payload is malformed. Allowable values are \"true\" or \"false\" (default). Only used when uploading a style file. (optional) (default to false)

try:
    # Modify a single style
    api_instance.put_style(style_body, style, raw=raw)
except ApiException as e:
    print("Exception when calling StylesApi->put_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **style_body** | [**StyleInfoPost**](StyleInfoPost.md)|  The style body of a request. For a PUT, only values which should be changed need to be included. JSON or XML style uploads follow the schema, and alter the style configuration. For example:    - application/xml:           &#x60;&#x60;&#x60;     &lt;style&gt;       &lt;name&gt;roads_style&lt;/name&gt;       &lt;languageVersion&gt;         &lt;version&gt;1.0.0&lt;/version&gt;       &lt;/languageVersion&gt;       &lt;filename&gt;roads.sld&lt;/filename&gt;       &lt;legend&gt;         &lt;width&gt;32&lt;/width&gt;         &lt;height&gt;32&lt;/height&gt;         &lt;format&gt;image/png; charset&#x3D;UTF-8&lt;/format&gt;         &lt;onlineResource&gt;legend.png&lt;/onlineResource&gt;       &lt;/legend&gt;     &lt;/style&gt;     &#x60;&#x60;&#x60;    - application/json:         &#x60;&#x60;&#x60;     {       \&quot;style\&quot;: {          \&quot;name\&quot;: \&quot;roads_style\&quot;,          \&quot;languageVersion\&quot;: {           \&quot;version\&quot;: \&quot;1.0.0\&quot;         },         \&quot;filename\&quot;: \&quot;roads.sld\&quot;,         \&quot;legend\&quot;: {           \&quot;format\&quot;: \&quot;image/png; charset&#x3D;UTF-8\&quot;,           \&quot;height\&quot;: 32,           \&quot;width\&quot;: 32,           \&quot;onlineResource\&quot;: \&quot;grass_fill.png\&quot;         }       }     }     &#x60;&#x60;&#x60;  Otherwise, the style body is an actual style:    - application/zip:           &#x60;&#x60;&#x60;       &lt;ZIP file containing SLD and icons&gt;       &#x60;&#x60;&#x60;          - application/vnd.ogc.sld+xml:      &#x60;&#x60;&#x60;     &lt;?xml version&#x3D;\&quot;1.0\&quot; encoding&#x3D;\&quot;UTF-8\&quot;?&gt;     &lt;StyledLayerDescriptor version&#x3D;\&quot;1.0.0\&quot;       xsi:schemaLocation&#x3D;\&quot;http://www.opengis.net/sld StyledLayerDescriptor.xsd\&quot;       xmlns&#x3D;\&quot;http://www.opengis.net/sld\&quot;       xmlns:ogc&#x3D;\&quot;http://www.opengis.net/ogc\&quot;       xmlns:xlink&#x3D;\&quot;http://www.w3.org/1999/xlink\&quot;       xmlns:xsi&#x3D;\&quot;http://www.w3.org/2001/XMLSchema-instance\&quot;&gt;       &lt;!-- a Named Layer is the basic building block of an SLD document --&gt;       &lt;NamedLayer&gt;         &lt;Name&gt;default_line&lt;/Name&gt;         &lt;UserStyle&gt;         &lt;!-- Styles can have names, titles and abstracts --&gt;           &lt;Title&gt;Default Line&lt;/Title&gt;           &lt;Abstract&gt;A sample style that draws a line&lt;/Abstract&gt;           &lt;!-- FeatureTypeStyles describe how to render different features --&gt;           &lt;!-- A FeatureTypeStyle for rendering lines --&gt;           &lt;FeatureTypeStyle&gt;             &lt;Rule&gt;               &lt;Name&gt;rule1&lt;/Name&gt;               &lt;Title&gt;Blue Line&lt;/Title&gt;               &lt;Abstract&gt;A solid blue line with a 1 pixel width&lt;/Abstract&gt;               &lt;LineSymbolizer&gt;                 &lt;Stroke&gt;                   &lt;CssParameter name&#x3D;\&quot;stroke\&quot;&gt;#0000FF&lt;/CssParameter&gt;                 &lt;/Stroke&gt;               &lt;/LineSymbolizer&gt;             &lt;/Rule&gt;           &lt;/FeatureTypeStyle&gt;         &lt;/UserStyle&gt;       &lt;/NamedLayer&gt;     &lt;/StyledLayerDescriptor&gt;     &#x60;&#x60;&#x60;  | 
 **style** | **str**| Name of the style to edit. | 
 **raw** | **bool**| When set to \&quot;true\&quot;, will forgo parsing and encoding of the uploaded style content, and instead the style will be streamed directly to the GeoServer configuration. Use this setting if the content and formatting of the style is to be preserved exactly. May result in an invalid and unusable style if the payload is malformed. Allowable values are \&quot;true\&quot; or \&quot;false\&quot; (default). Only used when uploading a style file. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/zip, text/xml, application/xml, text/json, application/vnd.ogc.sld+xml, application/vnd.ogc.se+xml, application/vnd.geoserver.geocss+css, application/vnd.geoserver.mbstyle+json, application/vnd.geoserver.ysld+yaml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_styles**
> put_styles()



Invalid. Use POST for adding a new style, or use PUT with /styles/{style} to edit/upload an existing style.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()

try:
    api_instance.put_styles()
except ApiException as e:
    print("Exception when calling StylesApi->put_styles: %s\n" % e)
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

# **put_workspace_style**
> put_workspace_style(style_body, workspace, style, raw=raw)

Modify a single style in a given workspace

Modifies a single style in a given workspace.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example `/workspaces/{workspace}/styles/{style}.xml` for XML).  Using PUT with the `application/xml` or `application/json` content modifies the style info in the catalog and does not alter the style content. Using PUT with any other format will modify the content of the style. You can also use PUT with a ZIP file to upload a SLD 1.0 (`application/vnd.ogc.sld+xml`) file and any associated icon files 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
style_body = swagger_client.StyleInfoPost() # StyleInfoPost |  The style body of a request. For a PUT, only values which should be changed need to be included. JSON or XML style uploads follow the schema, and alter the style configuration. For example:    - application/xml:           ```     <style>       <name>roads_style</name>       <languageVersion>         <version>1.0.0</version>       </languageVersion>       <filename>roads.sld</filename>       <legend>         <width>32</width>         <height>32</height>         <format>image/png; charset=UTF-8</format>         <onlineResource>legend.png</onlineResource>       </legend>     </style>     ```    - application/json:         ```     {       \"style\": {          \"name\": \"roads_style\",          \"languageVersion\": {           \"version\": \"1.0.0\"         },         \"filename\": \"roads.sld\",         \"legend\": {           \"format\": \"image/png; charset=UTF-8\",           \"height\": 32,           \"width\": 32,           \"onlineResource\": \"grass_fill.png\"         }       }     }     ```  Otherwise, the style body is an actual style:    - application/zip:           ```       <ZIP file containing SLD and icons>       ```          - application/vnd.ogc.sld+xml:      ```     <?xml version=\"1.0\" encoding=\"UTF-8\"?>     <StyledLayerDescriptor version=\"1.0.0\"       xsi:schemaLocation=\"http://www.opengis.net/sld StyledLayerDescriptor.xsd\"       xmlns=\"http://www.opengis.net/sld\"       xmlns:ogc=\"http://www.opengis.net/ogc\"       xmlns:xlink=\"http://www.w3.org/1999/xlink\"       xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">       <!-- a Named Layer is the basic building block of an SLD document -->       <NamedLayer>         <Name>default_line</Name>         <UserStyle>         <!-- Styles can have names, titles and abstracts -->           <Title>Default Line</Title>           <Abstract>A sample style that draws a line</Abstract>           <!-- FeatureTypeStyles describe how to render different features -->           <!-- A FeatureTypeStyle for rendering lines -->           <FeatureTypeStyle>             <Rule>               <Name>rule1</Name>               <Title>Blue Line</Title>               <Abstract>A solid blue line with a 1 pixel width</Abstract>               <LineSymbolizer>                 <Stroke>                   <CssParameter name=\"stroke\">#0000FF</CssParameter>                 </Stroke>               </LineSymbolizer>             </Rule>           </FeatureTypeStyle>         </UserStyle>       </NamedLayer>     </StyledLayerDescriptor>     ``` 
workspace = 'workspace_example' # str | Name of the workspace for style definitions
style = 'style_example' # str | Name of the style to retrieve.
raw = true # bool | When set to \"true\", will forgo parsing and encoding of the uploaded style content, and instead the style will be streamed directly to the GeoServer configuration. Use this setting if the content and formatting of the style is to be preserved exactly. May result in an invalid and unusable style if the payload is malformed. Allowable values are \"true\" or \"false\" (default). Only used when uploading a style file. (optional)

try:
    # Modify a single style in a given workspace
    api_instance.put_workspace_style(style_body, workspace, style, raw=raw)
except ApiException as e:
    print("Exception when calling StylesApi->put_workspace_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **style_body** | [**StyleInfoPost**](StyleInfoPost.md)|  The style body of a request. For a PUT, only values which should be changed need to be included. JSON or XML style uploads follow the schema, and alter the style configuration. For example:    - application/xml:           &#x60;&#x60;&#x60;     &lt;style&gt;       &lt;name&gt;roads_style&lt;/name&gt;       &lt;languageVersion&gt;         &lt;version&gt;1.0.0&lt;/version&gt;       &lt;/languageVersion&gt;       &lt;filename&gt;roads.sld&lt;/filename&gt;       &lt;legend&gt;         &lt;width&gt;32&lt;/width&gt;         &lt;height&gt;32&lt;/height&gt;         &lt;format&gt;image/png; charset&#x3D;UTF-8&lt;/format&gt;         &lt;onlineResource&gt;legend.png&lt;/onlineResource&gt;       &lt;/legend&gt;     &lt;/style&gt;     &#x60;&#x60;&#x60;    - application/json:         &#x60;&#x60;&#x60;     {       \&quot;style\&quot;: {          \&quot;name\&quot;: \&quot;roads_style\&quot;,          \&quot;languageVersion\&quot;: {           \&quot;version\&quot;: \&quot;1.0.0\&quot;         },         \&quot;filename\&quot;: \&quot;roads.sld\&quot;,         \&quot;legend\&quot;: {           \&quot;format\&quot;: \&quot;image/png; charset&#x3D;UTF-8\&quot;,           \&quot;height\&quot;: 32,           \&quot;width\&quot;: 32,           \&quot;onlineResource\&quot;: \&quot;grass_fill.png\&quot;         }       }     }     &#x60;&#x60;&#x60;  Otherwise, the style body is an actual style:    - application/zip:           &#x60;&#x60;&#x60;       &lt;ZIP file containing SLD and icons&gt;       &#x60;&#x60;&#x60;          - application/vnd.ogc.sld+xml:      &#x60;&#x60;&#x60;     &lt;?xml version&#x3D;\&quot;1.0\&quot; encoding&#x3D;\&quot;UTF-8\&quot;?&gt;     &lt;StyledLayerDescriptor version&#x3D;\&quot;1.0.0\&quot;       xsi:schemaLocation&#x3D;\&quot;http://www.opengis.net/sld StyledLayerDescriptor.xsd\&quot;       xmlns&#x3D;\&quot;http://www.opengis.net/sld\&quot;       xmlns:ogc&#x3D;\&quot;http://www.opengis.net/ogc\&quot;       xmlns:xlink&#x3D;\&quot;http://www.w3.org/1999/xlink\&quot;       xmlns:xsi&#x3D;\&quot;http://www.w3.org/2001/XMLSchema-instance\&quot;&gt;       &lt;!-- a Named Layer is the basic building block of an SLD document --&gt;       &lt;NamedLayer&gt;         &lt;Name&gt;default_line&lt;/Name&gt;         &lt;UserStyle&gt;         &lt;!-- Styles can have names, titles and abstracts --&gt;           &lt;Title&gt;Default Line&lt;/Title&gt;           &lt;Abstract&gt;A sample style that draws a line&lt;/Abstract&gt;           &lt;!-- FeatureTypeStyles describe how to render different features --&gt;           &lt;!-- A FeatureTypeStyle for rendering lines --&gt;           &lt;FeatureTypeStyle&gt;             &lt;Rule&gt;               &lt;Name&gt;rule1&lt;/Name&gt;               &lt;Title&gt;Blue Line&lt;/Title&gt;               &lt;Abstract&gt;A solid blue line with a 1 pixel width&lt;/Abstract&gt;               &lt;LineSymbolizer&gt;                 &lt;Stroke&gt;                   &lt;CssParameter name&#x3D;\&quot;stroke\&quot;&gt;#0000FF&lt;/CssParameter&gt;                 &lt;/Stroke&gt;               &lt;/LineSymbolizer&gt;             &lt;/Rule&gt;           &lt;/FeatureTypeStyle&gt;         &lt;/UserStyle&gt;       &lt;/NamedLayer&gt;     &lt;/StyledLayerDescriptor&gt;     &#x60;&#x60;&#x60;  | 
 **workspace** | **str**| Name of the workspace for style definitions | 
 **style** | **str**| Name of the style to retrieve. | 
 **raw** | **bool**| When set to \&quot;true\&quot;, will forgo parsing and encoding of the uploaded style content, and instead the style will be streamed directly to the GeoServer configuration. Use this setting if the content and formatting of the style is to be preserved exactly. May result in an invalid and unusable style if the payload is malformed. Allowable values are \&quot;true\&quot; or \&quot;false\&quot; (default). Only used when uploading a style file. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/zip, text/xml, application/xml, text/json, application/vnd.ogc.sld+xml, application/vnd.ogc.se+xml, application/vnd.geoserver.geocss+css, application/vnd.geoserver.ysld+yaml, application/vnd.geoserver.mbstyle+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_workspace_styles**
> put_workspace_styles(workspace)



Invalid. Use POST for adding a new style, or use PUT with /workspaces/{workspace}/styles/{style} to edit/upload an existing style.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StylesApi()
workspace = 'workspace_example' # str | Name of workspace

try:
    api_instance.put_workspace_styles(workspace)
except ApiException as e:
    print("Exception when calling StylesApi->put_workspace_styles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of workspace | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

