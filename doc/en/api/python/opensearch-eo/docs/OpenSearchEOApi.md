# swagger_client.OpenSearchEOApi

All URIs are relative to *https://geoserver:8080/geoserver/rest/oseo/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_collection_delete**](OpenSearchEOApi.md#collections_collection_delete) | **DELETE** /collections/{collection} | 
[**collections_collection_get**](OpenSearchEOApi.md#collections_collection_get) | **GET** /collections/{collection} | 
[**collections_collection_layer_delete**](OpenSearchEOApi.md#collections_collection_layer_delete) | **DELETE** /collections/{collection}/layer | 
[**collections_collection_layer_get**](OpenSearchEOApi.md#collections_collection_layer_get) | **GET** /collections/{collection}/layer | 
[**collections_collection_layer_put**](OpenSearchEOApi.md#collections_collection_layer_put) | **PUT** /collections/{collection}/layer | 
[**collections_collection_layers_get**](OpenSearchEOApi.md#collections_collection_layers_get) | **GET** /collections/{collection}/layers | 
[**collections_collection_layers_layer_delete**](OpenSearchEOApi.md#collections_collection_layers_layer_delete) | **DELETE** /collections/{collection}/layers/{layer} | 
[**collections_collection_layers_layer_get**](OpenSearchEOApi.md#collections_collection_layers_layer_get) | **GET** /collections/{collection}/layers/{layer} | 
[**collections_collection_layers_layer_put**](OpenSearchEOApi.md#collections_collection_layers_layer_put) | **PUT** /collections/{collection}/layers/{layer} | 
[**collections_collection_metadata_delete**](OpenSearchEOApi.md#collections_collection_metadata_delete) | **DELETE** /collections/{collection}/metadata | 
[**collections_collection_metadata_get**](OpenSearchEOApi.md#collections_collection_metadata_get) | **GET** /collections/{collection}/metadata | 
[**collections_collection_metadata_put**](OpenSearchEOApi.md#collections_collection_metadata_put) | **PUT** /collections/{collection}/metadata | 
[**collections_collection_ogc_links_delete**](OpenSearchEOApi.md#collections_collection_ogc_links_delete) | **DELETE** /collections/{collection}/ogcLinks | 
[**collections_collection_ogc_links_get**](OpenSearchEOApi.md#collections_collection_ogc_links_get) | **GET** /collections/{collection}/ogcLinks | 
[**collections_collection_ogc_links_put**](OpenSearchEOApi.md#collections_collection_ogc_links_put) | **PUT** /collections/{collection}/ogcLinks | 
[**collections_collection_products_get**](OpenSearchEOApi.md#collections_collection_products_get) | **GET** /collections/{collection}/products | 
[**collections_collection_products_post**](OpenSearchEOApi.md#collections_collection_products_post) | **POST** /collections/{collection}/products | 
[**collections_collection_products_product_delete**](OpenSearchEOApi.md#collections_collection_products_product_delete) | **DELETE** /collections/{collection}/products/{product} | 
[**collections_collection_products_product_get**](OpenSearchEOApi.md#collections_collection_products_product_get) | **GET** /collections/{collection}/products/{product} | 
[**collections_collection_products_product_granules_delete**](OpenSearchEOApi.md#collections_collection_products_product_granules_delete) | **DELETE** /collections/{collection}/products/{product}/granules | 
[**collections_collection_products_product_granules_get**](OpenSearchEOApi.md#collections_collection_products_product_granules_get) | **GET** /collections/{collection}/products/{product}/granules | 
[**collections_collection_products_product_granules_put**](OpenSearchEOApi.md#collections_collection_products_product_granules_put) | **PUT** /collections/{collection}/products/{product}/granules | 
[**collections_collection_products_product_metadata_delete**](OpenSearchEOApi.md#collections_collection_products_product_metadata_delete) | **DELETE** /collections/{collection}/products/{product}/metadata | 
[**collections_collection_products_product_metadata_get**](OpenSearchEOApi.md#collections_collection_products_product_metadata_get) | **GET** /collections/{collection}/products/{product}/metadata | 
[**collections_collection_products_product_metadata_put**](OpenSearchEOApi.md#collections_collection_products_product_metadata_put) | **PUT** /collections/{collection}/products/{product}/metadata | 
[**collections_collection_products_product_ogc_links_delete**](OpenSearchEOApi.md#collections_collection_products_product_ogc_links_delete) | **DELETE** /collections/{collection}/products/{product}/ogcLinks | 
[**collections_collection_products_product_ogc_links_get**](OpenSearchEOApi.md#collections_collection_products_product_ogc_links_get) | **GET** /collections/{collection}/products/{product}/ogcLinks | 
[**collections_collection_products_product_ogc_links_put**](OpenSearchEOApi.md#collections_collection_products_product_ogc_links_put) | **PUT** /collections/{collection}/products/{product}/ogcLinks | 
[**collections_collection_products_product_put**](OpenSearchEOApi.md#collections_collection_products_product_put) | **PUT** /collections/{collection}/products/{product} | 
[**collections_collection_products_product_thumbnail_delete**](OpenSearchEOApi.md#collections_collection_products_product_thumbnail_delete) | **DELETE** /collections/{collection}/products/{product}/thumbnail | 
[**collections_collection_products_product_thumbnail_get**](OpenSearchEOApi.md#collections_collection_products_product_thumbnail_get) | **GET** /collections/{collection}/products/{product}/thumbnail | 
[**collections_collection_products_product_thumbnail_put**](OpenSearchEOApi.md#collections_collection_products_product_thumbnail_put) | **PUT** /collections/{collection}/products/{product}/thumbnail | 
[**collections_collection_put**](OpenSearchEOApi.md#collections_collection_put) | **PUT** /collections/{collection} | 
[**collections_collection_thumbnail_delete**](OpenSearchEOApi.md#collections_collection_thumbnail_delete) | **DELETE** /collections/{collection}/thumbnail | 
[**collections_collection_thumbnail_get**](OpenSearchEOApi.md#collections_collection_thumbnail_get) | **GET** /collections/{collection}/thumbnail | 
[**collections_collection_thumbnail_put**](OpenSearchEOApi.md#collections_collection_thumbnail_put) | **PUT** /collections/{collection}/thumbnail | 
[**collections_get**](OpenSearchEOApi.md#collections_get) | **GET** /collections | 
[**collections_post**](OpenSearchEOApi.md#collections_post) | **POST** /collections | 


# **collections_collection_delete**
> collections_collection_delete(collection, keep_metadata=keep_metadata)



Deletes a collection and everything inside it

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
keep_metadata = true # bool | When present and set to true, makes GeoServer un-publish the collection (removal of OGC links, removal of associated layer) without removing the metadata. The collection remains searchable. (optional)

try:
    api_instance.collections_collection_delete(collection, keep_metadata=keep_metadata)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **keep_metadata** | **bool**| When present and set to true, makes GeoServer un-publish the collection (removal of OGC links, removal of associated layer) without removing the metadata. The collection remains searchable. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_get**
> collections_collection_get(collection)



Retrieves a collection search attributes and its ogc links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_get(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_layer_delete**
> collections_collection_layer_delete(collection)



Removes the mosaic configuration, store, layer and style associated to this collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_layer_delete(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_layer_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_layer_get**
> collections_collection_layer_get(collection)



Returns the current publishing configuration for the layer (or 404 if no configuration is currently in use)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_layer_get(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_layer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_layer_put**
> collections_collection_layer_put(collection)



Removes the previous publshing configuration and replaces with a new one, creating along the mosaic configuration, store, layer and style as described

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_layer_put(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_layer_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_layers_get**
> collections_collection_layers_get(collection)



Returns the list of collection layers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_layers_get(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_layers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_layers_layer_delete**
> collections_collection_layers_layer_delete(collection, layer)



Removes the collection layer configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
layer = 'layer_example' # str | Identifier of the layer

try:
    api_instance.collections_collection_layers_layer_delete(collection, layer)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_layers_layer_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **layer** | **str**| Identifier of the layer | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_layers_layer_get**
> collections_collection_layers_layer_get(collection, layer)



Returns the list of collection layers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
layer = 'layer_example' # str | Identifier of the layer

try:
    api_instance.collections_collection_layers_layer_get(collection, layer)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_layers_layer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **layer** | **str**| Identifier of the layer | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_layers_layer_put**
> collections_collection_layers_layer_put(collection, layer)



Updates/creates a collection layer publishing configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
layer = 'layer_example' # str | Identifier of the layer

try:
    api_instance.collections_collection_layers_layer_put(collection, layer)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_layers_layer_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **layer** | **str**| Identifier of the layer | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_metadata_delete**
> collections_collection_metadata_delete(collection)



Removes the product metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_metadata_delete(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_metadata_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_metadata_get**
> collections_collection_metadata_get(collection)



Returns the ISO metadata of this collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_metadata_get(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_metadata_put**
> collections_collection_metadata_put(collection)



Updates/creates a collection ISO metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_metadata_put(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_metadata_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_ogc_links_delete**
> collections_collection_ogc_links_delete(collection)



Removes the collection OGC links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_ogc_links_delete(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_ogc_links_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_ogc_links_get**
> collections_collection_ogc_links_get(collection)



Returns the list of OGC links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_ogc_links_get(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_ogc_links_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_ogc_links_put**
> collections_collection_ogc_links_put(collection)



Updates/creates a collection OGC links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_ogc_links_put(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_ogc_links_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_get**
> collections_collection_products_get(collection, offset=offset, limit=limit)



Returns a paged list of all available products

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
offset = 0 # int | First element for paged responses (optional) (default to 0)
limit = 10 # int | Number of elements in page (optional) (default to 10)

try:
    api_instance.collections_collection_products_get(collection, offset=offset, limit=limit)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **offset** | **int**| First element for paged responses | [optional] [default to 0]
 **limit** | **int**| Number of elements in page | [optional] [default to 10]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_post**
> collections_collection_products_post(collection)



Creates a new product via its search attributes and ogc links. The zip format accepts  a set of files creating the collection in a single shot, and will contain the following files:  * product.json: the list of searchable attributes and eventual OGC links * description.html: the HTML description for the product * metadata.xml: the O&M metadata for the collection * thumbnail.png: the product thumbnail (can also have jpeg or jpg extension) * owsLinks.json: the list of OWS links, in the same JSON format as the associated resource  * granules.json: the list of granules, in the same JSON format as the associated resource The JSON format is the same as the one returned by a GET on an existing product, the \"*Href\" properties should be omitted 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_products_post(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/zip
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_delete**
> collections_collection_products_product_delete(collection, product, keep_metadata=keep_metadata)



Deletes a product and everything inside it

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product
keep_metadata = true # bool | When present and set to true, makes GeoServer un-publish the product (removal of OGC links, direct download location and granule references) without removing the metadata. The product remains searchable. (optional)

try:
    api_instance.collections_collection_products_product_delete(collection, product, keep_metadata=keep_metadata)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 
 **keep_metadata** | **bool**| When present and set to true, makes GeoServer un-publish the product (removal of OGC links, direct download location and granule references) without removing the metadata. The product remains searchable. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_get**
> collections_collection_products_product_get(collection, product)



Retrieves a product search attributes, ogc links and granules. The response contains cross links to ogcLinks/metadata/thumbnail/granules sub-resources, when the same JSON is used to create a new collection the associated can be omitted, or if everything needs to be put in the JSON, the associated representations can be inlined instead (the thumbnail image can be BASE64 encoded). A creation with ZIP is recommend. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_get(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_granules_delete**
> collections_collection_products_product_granules_delete(collection, product)



Removes the product OGC links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_granules_delete(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_granules_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_granules_get**
> collections_collection_products_product_granules_get(collection, product)



Returns the list of a product granules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_granules_get(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_granules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_granules_put**
> collections_collection_products_product_granules_put(collection, product)



Updates/creates a product granules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_granules_put(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_granules_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_metadata_delete**
> collections_collection_products_product_metadata_delete(collection, product)



Removes the product metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_metadata_delete(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_metadata_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_metadata_get**
> collections_collection_products_product_metadata_get(collection, product)



Returns the O&M metadata of this product

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_metadata_get(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_metadata_put**
> collections_collection_products_product_metadata_put(collection, product)



Updates/creates a product O&M metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_metadata_put(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_metadata_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_ogc_links_delete**
> collections_collection_products_product_ogc_links_delete(collection, product)



Removes the product OGC links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_ogc_links_delete(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_ogc_links_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_ogc_links_get**
> collections_collection_products_product_ogc_links_get(collection, product)



Returns the list of a product OGC links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_ogc_links_get(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_ogc_links_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_ogc_links_put**
> collections_collection_products_product_ogc_links_put(collection, product)



Updates/creates a products OGC links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_ogc_links_put(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_ogc_links_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_put**
> collections_collection_products_product_put(collection, product)



Updates a product search attributes and OGC links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_put(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_thumbnail_delete**
> collections_collection_products_product_thumbnail_delete(collection, product)



Removes the product thumbnail

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_thumbnail_delete(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_thumbnail_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_thumbnail_get**
> collections_collection_products_product_thumbnail_get(collection, product)



Returns the thumbnail of this product

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_thumbnail_get(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_thumbnail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_products_product_thumbnail_put**
> collections_collection_products_product_thumbnail_put(collection, product)



Updates/creates a product thumbnail

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection
product = 'product_example' # str | Identifier of the product

try:
    api_instance.collections_collection_products_product_thumbnail_put(collection, product)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_products_product_thumbnail_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 
 **product** | **str**| Identifier of the product | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: image/png, image/jpeg
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_put**
> collections_collection_put(collection)



Updates a collection search attributes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_put(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_thumbnail_delete**
> collections_collection_thumbnail_delete(collection)



Removes the collection thumbnail

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_thumbnail_delete(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_thumbnail_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_thumbnail_get**
> collections_collection_thumbnail_get(collection)



Returns the thumbnail of this collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_thumbnail_get(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_thumbnail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collection_thumbnail_put**
> collections_collection_thumbnail_put(collection)



Updates/creates a collection thumbnail

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
collection = 'collection_example' # str | Identifier of the collection

try:
    api_instance.collections_collection_thumbnail_put(collection)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_collection_thumbnail_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Identifier of the collection | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: image/png, image/jpeg
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get**
> collections_get(offset=offset, limit=limit)



Retrieves a list of all available collections (names and links)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
offset = 56 # int | First element for paged responses (optional)
limit = 56 # int | Number of elements in page (optional)

try:
    api_instance.collections_get(offset=offset, limit=limit)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| First element for paged responses | [optional] 
 **limit** | **int**| Number of elements in page | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_post**
> collections_post(ogc_publish=ogc_publish, workspace=workspace, layer=layer)



Creates a new collection via its search attributes and ogc links.  The zip format accepts a set of files creating the collection in a single shot, and will contain the following files:  * collection.json: the list of searchable attributes, the format is the same as the one returned by a GET on a collection, the \"*HRef\" properties should be omitted.  * description.html: the HTML description for the collection * metadata.xml: the ISO metadata for the collection * thumbnail.png: the collection thumbnail (ignored at the time of writing) * owsLinks.json: the list of OWS links, in the same JSON format as the associated resource A creation with ZIP is recommend for speed and consistency sake. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OpenSearchEOApi()
ogc_publish = true # bool | When set to true, instructs GeoServer to automatically publish the collection as a layer in the location GeoServer (optional)
workspace = 'workspace_example' # str | workspace where the collection will be published (if missing the default workspace will be used) (optional)
layer = 'layer_example' # str | layer name used when publishing the collection (if missing the collection name will be used) (optional)

try:
    api_instance.collections_post(ogc_publish=ogc_publish, workspace=workspace, layer=layer)
except ApiException as e:
    print("Exception when calling OpenSearchEOApi->collections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ogc_publish** | **bool**| When set to true, instructs GeoServer to automatically publish the collection as a layer in the location GeoServer | [optional] 
 **workspace** | **str**| workspace where the collection will be published (if missing the default workspace will be used) | [optional] 
 **layer** | **str**| layer name used when publishing the collection (if missing the collection name will be used) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/zip
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

