# swagger_client.DataStoresApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clean_all_mongo_schemas**](DataStoresApi.md#clean_all_mongo_schemas) | **POST** /workspaces/{workspaceName}/appschemastores/{storeName}/cleanSchemas | Cleans all MongoDB internal stores Schemas for an App-Schema store.
[**clean_mongo_schema**](DataStoresApi.md#clean_mongo_schema) | **POST** /workspaces/{workspaceName}/appschemastores/{storeName}/datastores/{internalStoreId}/cleanSchemas | Cleans a MongoDB internal store Schemas for an App-Schema store.
[**delete_data_store_upload**](DataStoresApi.md#delete_data_store_upload) | **DELETE** /workspaces/{workspaceName}/datastores/{storeName}/{method}.{format} | 
[**delete_datastore**](DataStoresApi.md#delete_datastore) | **DELETE** /workspaces/{workspaceName}/datastores/{storeName} | Delete data store
[**deletedatastores**](DataStoresApi.md#deletedatastores) | **DELETE** /workspaces/{workspaceName}/datastores | 
[**get_data_store**](DataStoresApi.md#get_data_store) | **GET** /workspaces/{workspaceName}/datastores/{storeName} | Retrieve a particular data store from a workspace
[**get_data_store_upload**](DataStoresApi.md#get_data_store_upload) | **GET** /workspaces/{workspaceName}/datastores/{storeName}/{method}.{format} | 
[**get_datastores**](DataStoresApi.md#get_datastores) | **GET** /workspaces/{workspaceName}/datastores | Get a list of data stores
[**post_data_store_reset**](DataStoresApi.md#post_data_store_reset) | **POST** /workspaces/{workspaceName}/datastores/{storeName}/reset | Reset the caches related to this specific data store.
[**post_data_store_upload**](DataStoresApi.md#post_data_store_upload) | **POST** /workspaces/{workspaceName}/datastores/{storeName}/{method}.{format} | 
[**post_datastore**](DataStoresApi.md#post_datastore) | **POST** /workspaces/{workspaceName}/datastores/{storeName} | 
[**post_datastores**](DataStoresApi.md#post_datastores) | **POST** /workspaces/{workspaceName}/datastores | Create a new data store
[**put_data_store_reset**](DataStoresApi.md#put_data_store_reset) | **PUT** /workspaces/{workspaceName}/datastores/{storeName}/reset | Reset the caches related to this specific data store.
[**put_data_store_upload**](DataStoresApi.md#put_data_store_upload) | **PUT** /workspaces/{workspaceName}/datastores/{storeName}/{method}.{format} | Uploads files to the data store, creating it if necessary
[**put_datastore**](DataStoresApi.md#put_datastore) | **PUT** /workspaces/{workspaceName}/datastores/{storeName} | Modify a data store.
[**putdatastores**](DataStoresApi.md#putdatastores) | **PUT** /workspaces/{workspaceName}/datastores | 
[**rebuild_all_mongo_schemas**](DataStoresApi.md#rebuild_all_mongo_schemas) | **POST** /workspaces/{workspaceName}/appschemastores/{storeName}/rebuildMongoSchemas | Rebuilds all MongoDB internal stores Schemas for an App-Schema store.
[**rebuild_mongo_schema**](DataStoresApi.md#rebuild_mongo_schema) | **POST** /workspaces/{workspaceName}/appschemastores/{storeName}/datastores/{internalStoreId}/rebuildMongoSchemas | Rebuilds a MongoDB internal store Schemas for an App-Schema store.


# **clean_all_mongo_schemas**
> clean_all_mongo_schemas(workspace_name, store_name)

Cleans all MongoDB internal stores Schemas for an App-Schema store.

Cleans all MongoDB internal stores Schemas for an App-Schema store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data stores.
store_name = 'store_name_example' # str | The name of the App-Schema store

try:
    # Cleans all MongoDB internal stores Schemas for an App-Schema store.
    api_instance.clean_all_mongo_schemas(workspace_name, store_name)
except ApiException as e:
    print("Exception when calling DataStoresApi->clean_all_mongo_schemas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data stores. | 
 **store_name** | **str**| The name of the App-Schema store | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clean_mongo_schema**
> clean_mongo_schema(workspace_name, store_name, internal_store_id)

Cleans a MongoDB internal store Schemas for an App-Schema store.

Cleans a MongoDB internal store Schemas for an App-Schema store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data stores.
store_name = 'store_name_example' # str | The name of the App-Schema store
internal_store_id = 'internal_store_id_example' # str | The store ID for the internal MongoDB store as specified on App-Schema Mappings.

try:
    # Cleans a MongoDB internal store Schemas for an App-Schema store.
    api_instance.clean_mongo_schema(workspace_name, store_name, internal_store_id)
except ApiException as e:
    print("Exception when calling DataStoresApi->clean_mongo_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data stores. | 
 **store_name** | **str**| The name of the App-Schema store | 
 **internal_store_id** | **str**| The store ID for the internal MongoDB store as specified on App-Schema Mappings. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_store_upload**
> delete_data_store_upload()



Invalid, only used for uploads

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()

try:
    api_instance.delete_data_store_upload()
except ApiException as e:
    print("Exception when calling DataStoresApi->delete_data_store_upload: %s\n" % e)
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

# **delete_datastore**
> delete_datastore(workspace_name, store_name, recurse=recurse)

Delete data store

Deletes a data store from the server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data store.
store_name = 'store_name_example' # str | The name of the data store to delete.
recurse = true # bool | The recurse controls recursive deletion. When set to true all resources contained in the store are also removed. The default value is \"false\". (optional)

try:
    # Delete data store
    api_instance.delete_datastore(workspace_name, store_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling DataStoresApi->delete_datastore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data store. | 
 **store_name** | **str**| The name of the data store to delete. | 
 **recurse** | **bool**| The recurse controls recursive deletion. When set to true all resources contained in the store are also removed. The default value is \&quot;false\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletedatastores**
> deletedatastores()



Invalid. Use /datastores/{datastore} instead.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()

try:
    api_instance.deletedatastores()
except ApiException as e:
    print("Exception when calling DataStoresApi->deletedatastores: %s\n" % e)
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

# **get_data_store**
> Datastore get_data_store(workspace_name, store_name, quiet_on_not_found=quiet_on_not_found)

Retrieve a particular data store from a workspace

Controls a particular data store in a given workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/datastores/{datastore}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data store.
store_name = 'store_name_example' # str | The name of the data store to retrieve.
quiet_on_not_found = true # bool | The quietOnNotFound parameter avoids logging an exception when the data store is not present. Note that 404 status code will still be returned. (optional)

try:
    # Retrieve a particular data store from a workspace
    api_response = api_instance.get_data_store(workspace_name, store_name, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->get_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data store. | 
 **store_name** | **str**| The name of the data store to retrieve. | 
 **quiet_on_not_found** | **bool**| The quietOnNotFound parameter avoids logging an exception when the data store is not present. Note that 404 status code will still be returned. | [optional] 

### Return type

[**Datastore**](Datastore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_store_upload**
> get_data_store_upload(workspace_name, store_name, method, format)



Deprecated. Retrieve the underlying files for the data store as a zip file with MIME type application/zip

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data store.
store_name = 'store_name_example' # str | The name of the store to be retrieved
method = 'method_example' # str | The upload method. Can be \"url\", \"file\", \"external\". Unused for GET
format = 'format_example' # str | The type of source data store (e.g., \"shp\"). Unused for GET

try:
    api_instance.get_data_store_upload(workspace_name, store_name, method, format)
except ApiException as e:
    print("Exception when calling DataStoresApi->get_data_store_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data store. | 
 **store_name** | **str**| The name of the store to be retrieved | 
 **method** | **str**| The upload method. Can be \&quot;url\&quot;, \&quot;file\&quot;, \&quot;external\&quot;. Unused for GET | 
 **format** | **str**| The type of source data store (e.g., \&quot;shp\&quot;). Unused for GET | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datastores**
> DataStoreResponse get_datastores(workspace_name)

Get a list of data stores

List all data stores in workspace ws. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/datastores.xml\" for XML)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data stores.

try:
    # Get a list of data stores
    api_response = api_instance.get_datastores(workspace_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->get_datastores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data stores. | 

### Return type

[**DataStoreResponse**](DataStoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_data_store_reset**
> post_data_store_reset(workspace_name, store_name)

Reset the caches related to this specific data store.

Resets caches for this data store. This operation is used to force GeoServer to drop caches associated to this data store, and reconnect to the vector source the next time it is needed by a request. This is useful as the store can keep state, such as a connection pool, and the structure of the feature types it's serving.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data store.
store_name = 'store_name_example' # str | The name of the data store to modify.

try:
    # Reset the caches related to this specific data store.
    api_instance.post_data_store_reset(workspace_name, store_name)
except ApiException as e:
    print("Exception when calling DataStoresApi->post_data_store_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data store. | 
 **store_name** | **str**| The name of the data store to modify. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_data_store_upload**
> post_data_store_upload()



Invalid, use PUT for uploads

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()

try:
    api_instance.post_data_store_upload()
except ApiException as e:
    print("Exception when calling DataStoresApi->post_data_store_upload: %s\n" % e)
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

# **post_datastore**
> post_datastore()



Invalid. Use PUT to edit a data store definition, or POST with /datastore to add a new definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()

try:
    api_instance.post_datastore()
except ApiException as e:
    print("Exception when calling DataStoresApi->post_datastore: %s\n" % e)
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

# **post_datastores**
> str post_datastores(workspace_name, data_store_body)

Create a new data store

Adds a new data store to the workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data stores.
data_store_body = swagger_client.Datastore() # Datastore | The data store body information to upload.  The contents of the connection parameters will differ depending on the type of data store being added.  - GeoPackage    Examples:   - application/xml:      ```     <dataStore>       <name>nyc</name>       <connectionParameters>         <database>file:///path/to/nyc.gpkg</database>         <dbtype>geopkg</dbtype>       </connectionParameters>     </dataStore>     ```    - application/json:      ```     {       \"dataStore\": {         \"name\": \"nyc\",         \"connectionParameters\": {           \"entry\": [             {\"@key\":\"database\",\"$\":\"file:///path/to/nyc.gpkg\"},             {\"@key\":\"dbtype\",\"$\":\"geopkg\"}           ]         }       }     }     ```    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as 'schema.name' or just 'name' | user | String | False | ` ` |   | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | ` ` |   | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | `3` |   | database | Database | user | File | True | ` ` |   | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | `1` |   | fetch size | number of records read with each interaction with the DBMS | user | Integer | False | `1000` |   | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | `20` |   | namespace | Namespace prefix | user | String | False | ` ` |   | max connections | maximum number of open connections | user | Integer | False | `10` |   | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | `True` |   | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | `300` |   | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | ` ` |   | validate connections | check connection is alive before using it | user | Boolean | False | `True` |   | dbtype | Type | program | String | True | `geopkg` |   | passwd | password used to login | user | String | False | ` ` |   | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | `False` |   | min connections | minimum number of pooled connections | user | Integer | False | `1` |   | Evictor run periodicity | number of seconds between idle object evictor runs (default, 300 seconds) | user | Integer | False | `300` |   | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | ` ` |   | user | user name to login as | user | String | False | ` ` |  - PostGIS    Examples:   - application/xml:      ```     <dataStore>       <name>nyc</name>       <connectionParameters>         <host>localhost</host>         <port>5432</port>         <database>nyc</database>         <user>bob</user>         <passwd>postgres</passwd>         <dbtype>postgis</dbtype>       </connectionParameters>     </dataStore>     ```    - application/json:      ```     {       \"dataStore\": {         \"name\": \"nyc\",         \"connectionParameters\": {           \"entry\": [             {\"@key\":\"host\",\"$\":\"localhost\"},             {\"@key\":\"port\",\"$\":\"5432\"},             {\"@key\":\"database\",\"$\":\"nyc\"},             {\"@key\":\"user\",\"$\":\"bob\"},             {\"@key\":\"passwd\",\"$\":\"postgres\"},             {\"@key\":\"dbtype\",\"$\":\"postgis\"}           ]         }       }     }     ```    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | `20` |   | validate connections | check connection is alive before using it | user | Boolean | False | `True` |   | port | Port | user | Integer | True | `5432` |   | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as 'schema.name' or just 'name' | user | String | False | ` ` |   | Support on the fly geometry simplification | When enabled, operations such as map rendering will pass a hint that will enable the usage of ST_Simplify | user | Boolean | False | `True` |   | create database | Creates the database if it does not exist yet | advanced | Boolean | False | `False` |   | create database params | Extra specifications appended to the CREATE DATABASE command | advanced | String | False | `` |   | dbtype | Type | program | String | True | `postgis` |   | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | `1` |   | namespace | Namespace prefix | user | String | False | ` ` |   | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | `300` |   | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | ` ` |   | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | `False` |   | min connections | minimum number of pooled connections | user | Integer | False | `1` |   | Max open prepared statements | Maximum number of prepared statements kept open and cached for each connection in the pool. Set to 0 to have unbounded caching, to -1 to disable caching | user | Integer | False | `50` |   | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | ` ` |   | passwd | password used to login | user | String | False | ` ` |   | encode functions | set to true to have a set of filter functions be translated directly in SQL. Due to differences in the type systems the result might not be the same as evaluating them in memory, including the SQL failing with errors while the in memory version works fine. However this allows us to push more of the filter into the database, increasing performance of the postgis table. | advanced | Boolean | False | `False` |   | host | Host | user | String | True | `localhost` |   | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | `3` |   | Loose bbox | Perform only primary filter on bbox | user | Boolean | False | `True` |   | Evictor run periodicity | number of seconds between idle object evictor runs (default, 300 seconds) | user | Integer | False | `300` |   | Estimated extends | Use the spatial index information to quickly get an estimate of the data bounds | user | Boolean | False | `True` |   | database | Database | user | String | False | ` ` |   | fetch size | number of records read with each interaction with the DBMS | user | Integer | False | `1000` |   | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | `True` |   | max connections | maximum number of open connections | user | Integer | False | `10` |   | preparedStatements | Use prepared statements | user | Boolean | False | `False` |   | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | ` ` |   | schema | Schema | user | String | False | `public` |   | user | user name to login as | user | String | True | ` ` |  - Shapefile    Examples:   - application/xml:      ```     <dataStore>       <name>nyc</name>       <connectionParameters>         <url>file:/path/to/nyc.shp</url>       </connectionParameters>     </dataStore>     ```    - application/json:      ```     {       \"dataStore\": {         \"name\": \"nyc\",         \"connectionParameters\": {           \"entry\": [             {\"@key\":\"url\",\"$\":\"file:/path/to/nyc.shp\"}           ]         }       }     }     ```    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | `True` |   | namespace | URI to the namespace | advanced | URI | False | ` ` |   | filetype | Discriminator for directory stores | program | String | False | `shapefile` |   | charset | character used to decode strings from the DBF file | advanced | Charset | False | `ISO-8859-1` |   | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | `True` |   | fstype | Enable using a setting of 'shape'. | advanced | String | False | `shape` |   | url | url to a .shp file | user | URL | True | ` ` |   | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | `True` |   | memory mapped buffer | enable/disable the use of memory-mapped IO | advanced | Boolean | False | `False` |   | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | `Pacific Standard Time` |  - Directory of spatial files (shapefiles)    Examples:   - application/xml:      ```     <dataStore>       <name>nyc</name>       <connectionParameters>         <url>file:/path/to/directory</url>       </connectionParameters>     </dataStore>     ```    - application/json:      ```     {       \"dataStore\": {         \"name\": \"nyc\",         \"connectionParameters\": {           \"entry\": [             {\"@key\":\"url\",\"$\":\"file:/path/to/directory\"}           ]         }       }     }     ```    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | `True` |   | namespace | URI to the namespace | advanced | URI | False | ` ` |   | filetype | Discriminator for directory stores | program | String | False | `shapefile` |   | charset | character used to decode strings from the DBF file | advanced | Charset | False | `ISO-8859-1` |   | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | `True` |   | fstype | Enable using a setting of 'shape'. | advanced | String | False | `shape` |   | url | url to a .shp file | user | URL | True | ` ` |   | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | `True` |   | memory mapped buffer | enable/disable the use of memory-mapped IO | advanced | Boolean | False | `False` |   | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | `Pacific Standard Time` |   - Web Feature Service    Examples:   - application/xml:      ```     <dataStore>       <name>nyc</name>       <connectionParameters>         <GET_CAPABILITIES_URL>http://localhost:8080/geoserver/wfs?request=GetCapabilities</GET_CAPABILITIES_URL>       </connectionParameters>     </dataStore>     ```    - application/json:      ```     {       \"dataStore\": {         \"name\": \"nyc\",         \"connectionParameters\": {           \"entry\": [             {\"@key\":\"GET_CAPABILITIES_URL\",\"$\":\"http://localhost:8080/geoserver/wfs?request=GetCapabilities\"}           ]         }       }     }     ```    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Protocol | Sets a preference for the HTTP protocol to use when requesting WFS functionality. Set this value to Boolean.TRUE for POST, Boolean.FALSE for GET or NULL for AUTO | user | Boolean | False | ` ` |   | WFS GetCapabilities URL | Represents a URL to the getCapabilities document or a server instance. | user | URL | False | ` ` |   | Buffer Size | This allows the user to specify a buffer size in features. This param has a default value of 10 features. | user | Integer | False | `10` |   | Filter compliance | Level of compliance to WFS specification (0-low,1-medium,2-high) | user | Integer | False | ` ` |   | EntityResolver | Sets the entity resolver used to expand XML entities | program | EntityResolver | False | `org.geotools.xml.PreventLocalEntityResolver@75e98519` |   | Time-out | This allows the user to specify a timeout in milliseconds. This param has a default value of 3000ms. | user | Integer | False | `3000` |   | GmlComplianceLevel | Optional OGC GML compliance level required. | user | Integer | False | `0` |   | Lenient | Indicates that datastore should do its best to create features from the provided data even if it does not accurately match the schema.  Errors will be logged but the parsing will continue if this is true.  Default is false | user | Boolean | False | `False` |   | Password | This allows the user to specify a username. This param should not be used without the USERNAME param. | user | String | False | ` ` |   | Use Default SRS | Use always the declared DefaultSRS for requests and reproject locally if necessary | advanced | Boolean | False | `False` |   | Namespace | Override the original WFS type name namespaces | advanced | String | False | ` ` |   | Username | This allows the user to specify a username. This param should not be used without the PASSWORD param. | user | String | False | ` ` |   | Axis Order Filter | Indicates axis order used by the remote WFS server for filters. It applies only to WFS 1.x.0 servers. Default is the same as AXIS_ORDER | advanced | String | False | ` ` |   | GmlCompatibleTypeNames | Use Gml Compatible TypeNames (replace : by _). | user | Boolean | False | `False` |   | Maximum features | Positive integer used as a hard limit for the number of Features to retrieve for each FeatureType. A value of zero or not providing this parameter means no limit. | user | Integer | False | `0` |   | Axis Order | Indicates axis order used by the remote WFS server in result coordinates. It applies only to WFS 1.x.0 servers. Default is Compliant | advanced | String | False | `Compliant` |   | WFS Strategy | Override WFS strategy with either cubwerx, ionic, mapserver, geoserver, strict, nonstrict or arcgis strategy. | user | String | False | `auto` |   | Try GZIP | Indicates that datastore should use gzip to transfer data if the server supports it. Default is true | user | Boolean | False | `True` |   | Encoding | This allows the user to specify the character encoding of the XML-Requests sent to the Server. Defaults to UTF-8 | user | String | False | `UTF-8` |   | Outputformat | This allows the user to specify an output format, different from the default one. | advanced | String | False | ` ` | 

try:
    # Create a new data store
    api_response = api_instance.post_datastores(workspace_name, data_store_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->post_datastores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data stores. | 
 **data_store_body** | [**Datastore**](Datastore.md)| The data store body information to upload.  The contents of the connection parameters will differ depending on the type of data store being added.  - GeoPackage    Examples:   - application/xml:      &#x60;&#x60;&#x60;     &lt;dataStore&gt;       &lt;name&gt;nyc&lt;/name&gt;       &lt;connectionParameters&gt;         &lt;database&gt;file:///path/to/nyc.gpkg&lt;/database&gt;         &lt;dbtype&gt;geopkg&lt;/dbtype&gt;       &lt;/connectionParameters&gt;     &lt;/dataStore&gt;     &#x60;&#x60;&#x60;    - application/json:      &#x60;&#x60;&#x60;     {       \&quot;dataStore\&quot;: {         \&quot;name\&quot;: \&quot;nyc\&quot;,         \&quot;connectionParameters\&quot;: {           \&quot;entry\&quot;: [             {\&quot;@key\&quot;:\&quot;database\&quot;,\&quot;$\&quot;:\&quot;file:///path/to/nyc.gpkg\&quot;},             {\&quot;@key\&quot;:\&quot;dbtype\&quot;,\&quot;$\&quot;:\&quot;geopkg\&quot;}           ]         }       }     }     &#x60;&#x60;&#x60;    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as &#39;schema.name&#39; or just &#39;name&#39; | user | String | False | &#x60; &#x60; |   | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | &#x60; &#x60; |   | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | &#x60;3&#x60; |   | database | Database | user | File | True | &#x60; &#x60; |   | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | &#x60;1&#x60; |   | fetch size | number of records read with each interaction with the DBMS | user | Integer | False | &#x60;1000&#x60; |   | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | &#x60;20&#x60; |   | namespace | Namespace prefix | user | String | False | &#x60; &#x60; |   | max connections | maximum number of open connections | user | Integer | False | &#x60;10&#x60; |   | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | &#x60;True&#x60; |   | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | &#x60;300&#x60; |   | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | &#x60; &#x60; |   | validate connections | check connection is alive before using it | user | Boolean | False | &#x60;True&#x60; |   | dbtype | Type | program | String | True | &#x60;geopkg&#x60; |   | passwd | password used to login | user | String | False | &#x60; &#x60; |   | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | &#x60;False&#x60; |   | min connections | minimum number of pooled connections | user | Integer | False | &#x60;1&#x60; |   | Evictor run periodicity | number of seconds between idle object evictor runs (default, 300 seconds) | user | Integer | False | &#x60;300&#x60; |   | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | &#x60; &#x60; |   | user | user name to login as | user | String | False | &#x60; &#x60; |  - PostGIS    Examples:   - application/xml:      &#x60;&#x60;&#x60;     &lt;dataStore&gt;       &lt;name&gt;nyc&lt;/name&gt;       &lt;connectionParameters&gt;         &lt;host&gt;localhost&lt;/host&gt;         &lt;port&gt;5432&lt;/port&gt;         &lt;database&gt;nyc&lt;/database&gt;         &lt;user&gt;bob&lt;/user&gt;         &lt;passwd&gt;postgres&lt;/passwd&gt;         &lt;dbtype&gt;postgis&lt;/dbtype&gt;       &lt;/connectionParameters&gt;     &lt;/dataStore&gt;     &#x60;&#x60;&#x60;    - application/json:      &#x60;&#x60;&#x60;     {       \&quot;dataStore\&quot;: {         \&quot;name\&quot;: \&quot;nyc\&quot;,         \&quot;connectionParameters\&quot;: {           \&quot;entry\&quot;: [             {\&quot;@key\&quot;:\&quot;host\&quot;,\&quot;$\&quot;:\&quot;localhost\&quot;},             {\&quot;@key\&quot;:\&quot;port\&quot;,\&quot;$\&quot;:\&quot;5432\&quot;},             {\&quot;@key\&quot;:\&quot;database\&quot;,\&quot;$\&quot;:\&quot;nyc\&quot;},             {\&quot;@key\&quot;:\&quot;user\&quot;,\&quot;$\&quot;:\&quot;bob\&quot;},             {\&quot;@key\&quot;:\&quot;passwd\&quot;,\&quot;$\&quot;:\&quot;postgres\&quot;},             {\&quot;@key\&quot;:\&quot;dbtype\&quot;,\&quot;$\&quot;:\&quot;postgis\&quot;}           ]         }       }     }     &#x60;&#x60;&#x60;    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | &#x60;20&#x60; |   | validate connections | check connection is alive before using it | user | Boolean | False | &#x60;True&#x60; |   | port | Port | user | Integer | True | &#x60;5432&#x60; |   | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as &#39;schema.name&#39; or just &#39;name&#39; | user | String | False | &#x60; &#x60; |   | Support on the fly geometry simplification | When enabled, operations such as map rendering will pass a hint that will enable the usage of ST_Simplify | user | Boolean | False | &#x60;True&#x60; |   | create database | Creates the database if it does not exist yet | advanced | Boolean | False | &#x60;False&#x60; |   | create database params | Extra specifications appended to the CREATE DATABASE command | advanced | String | False | &#x60;&#x60; |   | dbtype | Type | program | String | True | &#x60;postgis&#x60; |   | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | &#x60;1&#x60; |   | namespace | Namespace prefix | user | String | False | &#x60; &#x60; |   | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | &#x60;300&#x60; |   | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | &#x60; &#x60; |   | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | &#x60;False&#x60; |   | min connections | minimum number of pooled connections | user | Integer | False | &#x60;1&#x60; |   | Max open prepared statements | Maximum number of prepared statements kept open and cached for each connection in the pool. Set to 0 to have unbounded caching, to -1 to disable caching | user | Integer | False | &#x60;50&#x60; |   | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | &#x60; &#x60; |   | passwd | password used to login | user | String | False | &#x60; &#x60; |   | encode functions | set to true to have a set of filter functions be translated directly in SQL. Due to differences in the type systems the result might not be the same as evaluating them in memory, including the SQL failing with errors while the in memory version works fine. However this allows us to push more of the filter into the database, increasing performance of the postgis table. | advanced | Boolean | False | &#x60;False&#x60; |   | host | Host | user | String | True | &#x60;localhost&#x60; |   | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | &#x60;3&#x60; |   | Loose bbox | Perform only primary filter on bbox | user | Boolean | False | &#x60;True&#x60; |   | Evictor run periodicity | number of seconds between idle object evictor runs (default, 300 seconds) | user | Integer | False | &#x60;300&#x60; |   | Estimated extends | Use the spatial index information to quickly get an estimate of the data bounds | user | Boolean | False | &#x60;True&#x60; |   | database | Database | user | String | False | &#x60; &#x60; |   | fetch size | number of records read with each interaction with the DBMS | user | Integer | False | &#x60;1000&#x60; |   | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | &#x60;True&#x60; |   | max connections | maximum number of open connections | user | Integer | False | &#x60;10&#x60; |   | preparedStatements | Use prepared statements | user | Boolean | False | &#x60;False&#x60; |   | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | &#x60; &#x60; |   | schema | Schema | user | String | False | &#x60;public&#x60; |   | user | user name to login as | user | String | True | &#x60; &#x60; |  - Shapefile    Examples:   - application/xml:      &#x60;&#x60;&#x60;     &lt;dataStore&gt;       &lt;name&gt;nyc&lt;/name&gt;       &lt;connectionParameters&gt;         &lt;url&gt;file:/path/to/nyc.shp&lt;/url&gt;       &lt;/connectionParameters&gt;     &lt;/dataStore&gt;     &#x60;&#x60;&#x60;    - application/json:      &#x60;&#x60;&#x60;     {       \&quot;dataStore\&quot;: {         \&quot;name\&quot;: \&quot;nyc\&quot;,         \&quot;connectionParameters\&quot;: {           \&quot;entry\&quot;: [             {\&quot;@key\&quot;:\&quot;url\&quot;,\&quot;$\&quot;:\&quot;file:/path/to/nyc.shp\&quot;}           ]         }       }     }     &#x60;&#x60;&#x60;    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | &#x60;True&#x60; |   | namespace | URI to the namespace | advanced | URI | False | &#x60; &#x60; |   | filetype | Discriminator for directory stores | program | String | False | &#x60;shapefile&#x60; |   | charset | character used to decode strings from the DBF file | advanced | Charset | False | &#x60;ISO-8859-1&#x60; |   | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | &#x60;True&#x60; |   | fstype | Enable using a setting of &#39;shape&#39;. | advanced | String | False | &#x60;shape&#x60; |   | url | url to a .shp file | user | URL | True | &#x60; &#x60; |   | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | &#x60;True&#x60; |   | memory mapped buffer | enable/disable the use of memory-mapped IO | advanced | Boolean | False | &#x60;False&#x60; |   | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | &#x60;Pacific Standard Time&#x60; |  - Directory of spatial files (shapefiles)    Examples:   - application/xml:      &#x60;&#x60;&#x60;     &lt;dataStore&gt;       &lt;name&gt;nyc&lt;/name&gt;       &lt;connectionParameters&gt;         &lt;url&gt;file:/path/to/directory&lt;/url&gt;       &lt;/connectionParameters&gt;     &lt;/dataStore&gt;     &#x60;&#x60;&#x60;    - application/json:      &#x60;&#x60;&#x60;     {       \&quot;dataStore\&quot;: {         \&quot;name\&quot;: \&quot;nyc\&quot;,         \&quot;connectionParameters\&quot;: {           \&quot;entry\&quot;: [             {\&quot;@key\&quot;:\&quot;url\&quot;,\&quot;$\&quot;:\&quot;file:/path/to/directory\&quot;}           ]         }       }     }     &#x60;&#x60;&#x60;    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | &#x60;True&#x60; |   | namespace | URI to the namespace | advanced | URI | False | &#x60; &#x60; |   | filetype | Discriminator for directory stores | program | String | False | &#x60;shapefile&#x60; |   | charset | character used to decode strings from the DBF file | advanced | Charset | False | &#x60;ISO-8859-1&#x60; |   | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | &#x60;True&#x60; |   | fstype | Enable using a setting of &#39;shape&#39;. | advanced | String | False | &#x60;shape&#x60; |   | url | url to a .shp file | user | URL | True | &#x60; &#x60; |   | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | &#x60;True&#x60; |   | memory mapped buffer | enable/disable the use of memory-mapped IO | advanced | Boolean | False | &#x60;False&#x60; |   | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | &#x60;Pacific Standard Time&#x60; |   - Web Feature Service    Examples:   - application/xml:      &#x60;&#x60;&#x60;     &lt;dataStore&gt;       &lt;name&gt;nyc&lt;/name&gt;       &lt;connectionParameters&gt;         &lt;GET_CAPABILITIES_URL&gt;http://localhost:8080/geoserver/wfs?request&#x3D;GetCapabilities&lt;/GET_CAPABILITIES_URL&gt;       &lt;/connectionParameters&gt;     &lt;/dataStore&gt;     &#x60;&#x60;&#x60;    - application/json:      &#x60;&#x60;&#x60;     {       \&quot;dataStore\&quot;: {         \&quot;name\&quot;: \&quot;nyc\&quot;,         \&quot;connectionParameters\&quot;: {           \&quot;entry\&quot;: [             {\&quot;@key\&quot;:\&quot;GET_CAPABILITIES_URL\&quot;,\&quot;$\&quot;:\&quot;http://localhost:8080/geoserver/wfs?request&#x3D;GetCapabilities\&quot;}           ]         }       }     }     &#x60;&#x60;&#x60;    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Protocol | Sets a preference for the HTTP protocol to use when requesting WFS functionality. Set this value to Boolean.TRUE for POST, Boolean.FALSE for GET or NULL for AUTO | user | Boolean | False | &#x60; &#x60; |   | WFS GetCapabilities URL | Represents a URL to the getCapabilities document or a server instance. | user | URL | False | &#x60; &#x60; |   | Buffer Size | This allows the user to specify a buffer size in features. This param has a default value of 10 features. | user | Integer | False | &#x60;10&#x60; |   | Filter compliance | Level of compliance to WFS specification (0-low,1-medium,2-high) | user | Integer | False | &#x60; &#x60; |   | EntityResolver | Sets the entity resolver used to expand XML entities | program | EntityResolver | False | &#x60;org.geotools.xml.PreventLocalEntityResolver@75e98519&#x60; |   | Time-out | This allows the user to specify a timeout in milliseconds. This param has a default value of 3000ms. | user | Integer | False | &#x60;3000&#x60; |   | GmlComplianceLevel | Optional OGC GML compliance level required. | user | Integer | False | &#x60;0&#x60; |   | Lenient | Indicates that datastore should do its best to create features from the provided data even if it does not accurately match the schema.  Errors will be logged but the parsing will continue if this is true.  Default is false | user | Boolean | False | &#x60;False&#x60; |   | Password | This allows the user to specify a username. This param should not be used without the USERNAME param. | user | String | False | &#x60; &#x60; |   | Use Default SRS | Use always the declared DefaultSRS for requests and reproject locally if necessary | advanced | Boolean | False | &#x60;False&#x60; |   | Namespace | Override the original WFS type name namespaces | advanced | String | False | &#x60; &#x60; |   | Username | This allows the user to specify a username. This param should not be used without the PASSWORD param. | user | String | False | &#x60; &#x60; |   | Axis Order Filter | Indicates axis order used by the remote WFS server for filters. It applies only to WFS 1.x.0 servers. Default is the same as AXIS_ORDER | advanced | String | False | &#x60; &#x60; |   | GmlCompatibleTypeNames | Use Gml Compatible TypeNames (replace : by _). | user | Boolean | False | &#x60;False&#x60; |   | Maximum features | Positive integer used as a hard limit for the number of Features to retrieve for each FeatureType. A value of zero or not providing this parameter means no limit. | user | Integer | False | &#x60;0&#x60; |   | Axis Order | Indicates axis order used by the remote WFS server in result coordinates. It applies only to WFS 1.x.0 servers. Default is Compliant | advanced | String | False | &#x60;Compliant&#x60; |   | WFS Strategy | Override WFS strategy with either cubwerx, ionic, mapserver, geoserver, strict, nonstrict or arcgis strategy. | user | String | False | &#x60;auto&#x60; |   | Try GZIP | Indicates that datastore should use gzip to transfer data if the server supports it. Default is true | user | Boolean | False | &#x60;True&#x60; |   | Encoding | This allows the user to specify the character encoding of the XML-Requests sent to the Server. Defaults to UTF-8 | user | String | False | &#x60;UTF-8&#x60; |   | Outputformat | This allows the user to specify an output format, different from the default one. | advanced | String | False | &#x60; &#x60; |  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_data_store_reset**
> put_data_store_reset(workspace_name, store_name)

Reset the caches related to this specific data store.

Resets caches for this data store. This operation is used to force GeoServer to drop caches associated to this data store, and reconnect to the vector source the next time it is needed by a request. This is useful as the store can keep state, such as a connection pool, and the structure of the feature types it's serving.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data store.
store_name = 'store_name_example' # str | The name of the data store to modify.

try:
    # Reset the caches related to this specific data store.
    api_instance.put_data_store_reset(workspace_name, store_name)
except ApiException as e:
    print("Exception when calling DataStoresApi->put_data_store_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data store. | 
 **store_name** | **str**| The name of the data store to modify. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_data_store_upload**
> put_data_store_upload(workspace_name, store_name, method, format, configure=configure, target=target, update=update, charset=charset, filename=filename)

Uploads files to the data store, creating it if necessary

Creates or modifies a single data store by uploading spatial data or mapping configuration (in case an app-schema data store is targeted) files.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the coverage stores.
store_name = 'store_name_example' # str | The name of the store to be retrieved
method = 'method_example' # str | The upload method. Can be \"url\", \"file\", \"external\". \"file\" uploads a file from a local source. The body of the request is the file itself. \"url\" uploads a file from an remote source. The body of the request is a URL pointing to the file to upload. This URL must be visible from the server. \"external\" uses an existing file on the server. The body of the request is the absolute path to the existing file.
format = 'format_example' # str | The type of source data store (e.g., \"shp\").
configure = 'configure_example' # str | The configure parameter controls if a coverage/layer are configured upon file upload, in addition to creating the store. It can have a value of \"none\" to avoid configuring coverages. (optional)
target = 'target_example' # str | The type of target data store (e.g., \"shp\"). Same as format if not provided. (optional)
update = 'update_example' # str | The update mode. If \"overwrite\", will overwrite existing data. Otherwise, will append to existing data. (optional)
charset = 'charset_example' # str | The character set of the data. (optional)
filename = 'filename_example' # str | The filename parameter specifies the target file name for the file to be uploaded. This is important to avoid clashes with existing files. (optional)

try:
    # Uploads files to the data store, creating it if necessary
    api_instance.put_data_store_upload(workspace_name, store_name, method, format, configure=configure, target=target, update=update, charset=charset, filename=filename)
except ApiException as e:
    print("Exception when calling DataStoresApi->put_data_store_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the coverage stores. | 
 **store_name** | **str**| The name of the store to be retrieved | 
 **method** | **str**| The upload method. Can be \&quot;url\&quot;, \&quot;file\&quot;, \&quot;external\&quot;. \&quot;file\&quot; uploads a file from a local source. The body of the request is the file itself. \&quot;url\&quot; uploads a file from an remote source. The body of the request is a URL pointing to the file to upload. This URL must be visible from the server. \&quot;external\&quot; uses an existing file on the server. The body of the request is the absolute path to the existing file. | 
 **format** | **str**| The type of source data store (e.g., \&quot;shp\&quot;). | 
 **configure** | **str**| The configure parameter controls if a coverage/layer are configured upon file upload, in addition to creating the store. It can have a value of \&quot;none\&quot; to avoid configuring coverages. | [optional] 
 **target** | **str**| The type of target data store (e.g., \&quot;shp\&quot;). Same as format if not provided. | [optional] 
 **update** | **str**| The update mode. If \&quot;overwrite\&quot;, will overwrite existing data. Otherwise, will append to existing data. | [optional] 
 **charset** | **str**| The character set of the data. | [optional] 
 **filename** | **str**| The filename parameter specifies the target file name for the file to be uploaded. This is important to avoid clashes with existing files. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_datastore**
> put_datastore(workspace_name, store_name, data_store_body)

Modify a data store.

Modify data store ds. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/datastores/{ds}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data store.
store_name = 'store_name_example' # str | The name of the data store to modify.
data_store_body = swagger_client.Datastore() # Datastore | The updated data store definition. For a PUT, only values which should be changed need to be included. The connectionParameters map counts as a single value,  so if you change it all pre-existing connection parameters will be overwritten.  The contents of the connection parameters will differ depending on the type of data store being added.  - GeoPackage    Examples:   - application/xml:      ```     <dataStore>       <description>A data store</description>       <enabled>true</enabled>       <__default>true</__default>       <connectionParameters>         <database>file:///path/to/nyc.gpkg</database>       </connectionParameters>     </dataStore>     ```    - application/json:      ```     {       \"dataStore\": {         \"description\": \"A data store\",         \"enabled\": \"true\",         \"_default\": \"true\",         \"connectionParameters\": {           \"entry\": [             {\"@key\":\"database\",\"$\":\"file:///path/to/nyc.gpkg\"},           ]         }       }     }     ```    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as 'schema.name' or just 'name' | user | String | False | ` ` |   | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | ` ` |   | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | `3` |   | database | Database | user | File | True | ` ` |   | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | `1` |   | fetch size | number of records read with each interaction with the DBMS | user | Integer | False | `1000` |   | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | `20` |   | namespace | Namespace prefix | user | String | False | ` ` |   | max connections | maximum number of open connections | user | Integer | False | `10` |   | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | `True` |   | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | `300` |   | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | ` ` |   | validate connections | check connection is alive before using it | user | Boolean | False | `True` |   | dbtype | Type | program | String | True | `geopkg` |   | passwd | password used to login | user | String | False | ` ` |   | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | `False` |   | min connections | minimum number of pooled connections | user | Integer | False | `1` |   | Evictor run periodicity | number of seconds between idle object evictor runs (default, 300 seconds) | user | Integer | False | `300` |   | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | ` ` |   | user | user name to login as | user | String | False | ` ` |  - PostGIS    Examples:   - application/xml:      ```     <dataStore>       <description>A data store</description>       <enabled>true</enabled>       <__default>true</__default>       <connectionParameters>         <host>localhost</host>         <port>5432</port>         <database>nyc</database>         <user>bob</user>         <passwd>postgres</passwd>       </connectionParameters>     </dataStore>     ```    - application/json:      ```     {       \"dataStore\": {         \"description\": \"A data store\",         \"enabled\": \"true\",         \"_default\": \"true\",         \"connectionParameters\": {           \"entry\": [             {\"@key\":\"host\",\"$\":\"localhost\"},             {\"@key\":\"port\",\"$\":\"5432\"},             {\"@key\":\"database\",\"$\":\"nyc\"},             {\"@key\":\"user\",\"$\":\"bob\"},             {\"@key\":\"passwd\",\"$\":\"postgres\"},           ]         }       }     }     ```    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | `20` |   | validate connections | check connection is alive before using it | user | Boolean | False | `True` |   | port | Port | user | Integer | True | `5432` |   | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as 'schema.name' or just 'name' | user | String | False | ` ` |   | Support on the fly geometry simplification | When enabled, operations such as map rendering will pass a hint that will enable the usage of ST_Simplify | user | Boolean | False | `True` |   | create database | Creates the database if it does not exist yet | advanced | Boolean | False | `False` |   | create database params | Extra specifications appended to the CREATE DATABASE command | advanced | String | False | `` |   | dbtype | Type | program | String | True | `postgis` |   | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | `1` |   | namespace | Namespace prefix | user | String | False | ` ` |   | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | `300` |   | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | ` ` |   | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | `False` |   | min connections | minimum number of pooled connections | user | Integer | False | `1` |   | Max open prepared statements | Maximum number of prepared statements kept open and cached for each connection in the pool. Set to 0 to have unbounded caching, to -1 to disable caching | user | Integer | False | `50` |   | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | ` ` |   | passwd | password used to login | user | String | False | ` ` |   | encode functions | set to true to have a set of filter functions be translated directly in SQL. Due to differences in the type systems the result might not be the same as evaluating them in memory, including the SQL failing with errors while the in memory version works fine. However this allows us to push more of the filter into the database, increasing performance of the postgis table. | advanced | Boolean | False | `False` |   | host | Host | user | String | True | `localhost` |   | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | `3` |   | Loose bbox | Perform only primary filter on bbox | user | Boolean | False | `True` |   | Evictor run periodicity | number of seconds between idle object evictor runs (default, 300 seconds) | user | Integer | False | `300` |   | Estimated extends | Use the spatial index information to quickly get an estimate of the data bounds | user | Boolean | False | `True` |   | database | Database | user | String | False | ` ` |   | fetch size | number of records read with each interaction with the DBMS | user | Integer | False | `1000` |   | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | `True` |   | max connections | maximum number of open connections | user | Integer | False | `10` |   | preparedStatements | Use prepared statements | user | Boolean | False | `False` |   | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | ` ` |   | schema | Schema | user | String | False | `public` |   | user | user name to login as | user | String | True | ` ` |  - Shapefile    Examples:   - application/xml:      ```     <dataStore>       <description>A data store</description>       <enabled>true</enabled>       <__default>true</__default>       <connectionParameters>         <url>file:/path/to/nyc.shp</url>       </connectionParameters>     </dataStore>     ```    - application/json:      ```     {       \"dataStore\": {         \"description\": \"A data store\",         \"enabled\": \"true\",         \"_default\": \"true\",         \"connectionParameters\": {           \"entry\": [             {\"@key\":\"url\",\"$\":\"file:/path/to/nyc.shp\"}           ]         }       }     }     ```    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | `True` |   | namespace | URI to the namespace | advanced | URI | False | ` ` |   | filetype | Discriminator for directory stores | program | String | False | `shapefile` |   | charset | character used to decode strings from the DBF file | advanced | Charset | False | `ISO-8859-1` |   | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | `True` |   | fstype | Enable using a setting of 'shape'. | advanced | String | False | `shape` |   | url | url to a .shp file | user | URL | True | ` ` |   | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | `True` |   | memory mapped buffer | enable/disable the use of memory-mapped IO | advanced | Boolean | False | `False` |   | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | `Pacific Standard Time` |  - Directory of spatial files (shapefiles)    Examples:   - application/xml:      ```     <dataStore>       <description>A data store</description>       <enabled>true</enabled>       <__default>true</__default>       <connectionParameters>         <url>file:/path/to/directory</url>       </connectionParameters>     </dataStore>     ```    - application/json:      ```     {       \"dataStore\": {         \"description\": \"A data store\",         \"enabled\": \"true\",         \"_default\": \"true\",         \"connectionParameters\": {           \"entry\": [             {\"@key\":\"url\",\"$\":\"file:/path/to/directory\"}           ]         }       }     }     ```    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | `True` |   | namespace | URI to the namespace | advanced | URI | False | ` ` |   | filetype | Discriminator for directory stores | program | String | False | `shapefile` |   | charset | character used to decode strings from the DBF file | advanced | Charset | False | `ISO-8859-1` |   | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | `True` |   | fstype | Enable using a setting of 'shape'. | advanced | String | False | `shape` |   | url | url to a .shp file | user | URL | True | ` ` |   | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | `True` |   | memory mapped buffer | enable/disable the use of memory-mapped IO | advanced | Boolean | False | `False` |   | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | `Pacific Standard Time` |   - Web Feature Service    Examples:   - application/xml:      ```     <dataStore>       <description>A data store</description>       <enabled>true</enabled>       <__default>true</__default>       <connectionParameters>         <GET_CAPABILITIES_URL>http://localhost:8080/geoserver/wfs?request=GetCapabilities</GET_CAPABILITIES_URL>       </connectionParameters>     </dataStore>     ```    - application/json:      ```     {       \"dataStore\": {         \"description\": \"A data store\",         \"enabled\": \"true\",         \"_default\": \"true\",         \"connectionParameters\": {           \"entry\": [             {\"@key\":\"GET_CAPABILITIES_URL\",\"$\":\"http://localhost:8080/geoserver/wfs?request=GetCapabilities\"}           ]         }       }     }     ```    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Protocol | Sets a preference for the HTTP protocol to use when requesting WFS functionality. Set this value to Boolean.TRUE for POST, Boolean.FALSE for GET or NULL for AUTO | user | Boolean | False | ` ` |   | WFS GetCapabilities URL | Represents a URL to the getCapabilities document or a server instance. | user | URL | False | ` ` |   | Buffer Size | This allows the user to specify a buffer size in features. This param has a default value of 10 features. | user | Integer | False | `10` |   | Filter compliance | Level of compliance to WFS specification (0-low,1-medium,2-high) | user | Integer | False | ` ` |   | EntityResolver | Sets the entity resolver used to expand XML entities | program | EntityResolver | False | `org.geotools.xml.PreventLocalEntityResolver@75e98519` |   | Time-out | This allows the user to specify a timeout in milliseconds. This param has a default value of 3000ms. | user | Integer | False | `3000` |   | GmlComplianceLevel | Optional OGC GML compliance level required. | user | Integer | False | `0` |   | Lenient | Indicates that datastore should do its best to create features from the provided data even if it does not accurately match the schema.  Errors will be logged but the parsing will continue if this is true.  Default is false | user | Boolean | False | `False` |   | Password | This allows the user to specify a username. This param should not be used without the USERNAME param. | user | String | False | ` ` |   | Use Default SRS | Use always the declared DefaultSRS for requests and reproject locally if necessary | advanced | Boolean | False | `False` |   | Namespace | Override the original WFS type name namespaces | advanced | String | False | ` ` |   | Username | This allows the user to specify a username. This param should not be used without the PASSWORD param. | user | String | False | ` ` |   | Axis Order Filter | Indicates axis order used by the remote WFS server for filters. It applies only to WFS 1.x.0 servers. Default is the same as AXIS_ORDER | advanced | String | False | ` ` |   | GmlCompatibleTypeNames | Use Gml Compatible TypeNames (replace : by _). | user | Boolean | False | `False` |   | Maximum features | Positive integer used as a hard limit for the number of Features to retrieve for each FeatureType. A value of zero or not providing this parameter means no limit. | user | Integer | False | `0` |   | Axis Order | Indicates axis order used by the remote WFS server in result coordinates. It applies only to WFS 1.x.0 servers. Default is Compliant | advanced | String | False | `Compliant` |   | WFS Strategy | Override WFS strategy with either cubwerx, ionic, mapserver, geoserver, strict, nonstrict or arcgis strategy. | user | String | False | `auto` |   | Try GZIP | Indicates that datastore should use gzip to transfer data if the server supports it. Default is true | user | Boolean | False | `True` |   | Encoding | This allows the user to specify the character encoding of the XML-Requests sent to the Server. Defaults to UTF-8 | user | String | False | `UTF-8` |   | Outputformat | This allows the user to specify an output format, different from the default one. | advanced | String | False | ` ` | 

try:
    # Modify a data store.
    api_instance.put_datastore(workspace_name, store_name, data_store_body)
except ApiException as e:
    print("Exception when calling DataStoresApi->put_datastore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data store. | 
 **store_name** | **str**| The name of the data store to modify. | 
 **data_store_body** | [**Datastore**](Datastore.md)| The updated data store definition. For a PUT, only values which should be changed need to be included. The connectionParameters map counts as a single value,  so if you change it all pre-existing connection parameters will be overwritten.  The contents of the connection parameters will differ depending on the type of data store being added.  - GeoPackage    Examples:   - application/xml:      &#x60;&#x60;&#x60;     &lt;dataStore&gt;       &lt;description&gt;A data store&lt;/description&gt;       &lt;enabled&gt;true&lt;/enabled&gt;       &lt;__default&gt;true&lt;/__default&gt;       &lt;connectionParameters&gt;         &lt;database&gt;file:///path/to/nyc.gpkg&lt;/database&gt;       &lt;/connectionParameters&gt;     &lt;/dataStore&gt;     &#x60;&#x60;&#x60;    - application/json:      &#x60;&#x60;&#x60;     {       \&quot;dataStore\&quot;: {         \&quot;description\&quot;: \&quot;A data store\&quot;,         \&quot;enabled\&quot;: \&quot;true\&quot;,         \&quot;_default\&quot;: \&quot;true\&quot;,         \&quot;connectionParameters\&quot;: {           \&quot;entry\&quot;: [             {\&quot;@key\&quot;:\&quot;database\&quot;,\&quot;$\&quot;:\&quot;file:///path/to/nyc.gpkg\&quot;},           ]         }       }     }     &#x60;&#x60;&#x60;    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as &#39;schema.name&#39; or just &#39;name&#39; | user | String | False | &#x60; &#x60; |   | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | &#x60; &#x60; |   | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | &#x60;3&#x60; |   | database | Database | user | File | True | &#x60; &#x60; |   | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | &#x60;1&#x60; |   | fetch size | number of records read with each interaction with the DBMS | user | Integer | False | &#x60;1000&#x60; |   | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | &#x60;20&#x60; |   | namespace | Namespace prefix | user | String | False | &#x60; &#x60; |   | max connections | maximum number of open connections | user | Integer | False | &#x60;10&#x60; |   | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | &#x60;True&#x60; |   | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | &#x60;300&#x60; |   | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | &#x60; &#x60; |   | validate connections | check connection is alive before using it | user | Boolean | False | &#x60;True&#x60; |   | dbtype | Type | program | String | True | &#x60;geopkg&#x60; |   | passwd | password used to login | user | String | False | &#x60; &#x60; |   | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | &#x60;False&#x60; |   | min connections | minimum number of pooled connections | user | Integer | False | &#x60;1&#x60; |   | Evictor run periodicity | number of seconds between idle object evictor runs (default, 300 seconds) | user | Integer | False | &#x60;300&#x60; |   | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | &#x60; &#x60; |   | user | user name to login as | user | String | False | &#x60; &#x60; |  - PostGIS    Examples:   - application/xml:      &#x60;&#x60;&#x60;     &lt;dataStore&gt;       &lt;description&gt;A data store&lt;/description&gt;       &lt;enabled&gt;true&lt;/enabled&gt;       &lt;__default&gt;true&lt;/__default&gt;       &lt;connectionParameters&gt;         &lt;host&gt;localhost&lt;/host&gt;         &lt;port&gt;5432&lt;/port&gt;         &lt;database&gt;nyc&lt;/database&gt;         &lt;user&gt;bob&lt;/user&gt;         &lt;passwd&gt;postgres&lt;/passwd&gt;       &lt;/connectionParameters&gt;     &lt;/dataStore&gt;     &#x60;&#x60;&#x60;    - application/json:      &#x60;&#x60;&#x60;     {       \&quot;dataStore\&quot;: {         \&quot;description\&quot;: \&quot;A data store\&quot;,         \&quot;enabled\&quot;: \&quot;true\&quot;,         \&quot;_default\&quot;: \&quot;true\&quot;,         \&quot;connectionParameters\&quot;: {           \&quot;entry\&quot;: [             {\&quot;@key\&quot;:\&quot;host\&quot;,\&quot;$\&quot;:\&quot;localhost\&quot;},             {\&quot;@key\&quot;:\&quot;port\&quot;,\&quot;$\&quot;:\&quot;5432\&quot;},             {\&quot;@key\&quot;:\&quot;database\&quot;,\&quot;$\&quot;:\&quot;nyc\&quot;},             {\&quot;@key\&quot;:\&quot;user\&quot;,\&quot;$\&quot;:\&quot;bob\&quot;},             {\&quot;@key\&quot;:\&quot;passwd\&quot;,\&quot;$\&quot;:\&quot;postgres\&quot;},           ]         }       }     }     &#x60;&#x60;&#x60;    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Connection timeout | number of seconds the connection pool will wait before timing out attempting to get a new connection (default, 20 seconds) | user | Integer | False | &#x60;20&#x60; |   | validate connections | check connection is alive before using it | user | Boolean | False | &#x60;True&#x60; |   | port | Port | user | Integer | True | &#x60;5432&#x60; |   | Primary key metadata table | The optional table containing primary key structure and sequence associations. Can be expressed as &#39;schema.name&#39; or just &#39;name&#39; | user | String | False | &#x60; &#x60; |   | Support on the fly geometry simplification | When enabled, operations such as map rendering will pass a hint that will enable the usage of ST_Simplify | user | Boolean | False | &#x60;True&#x60; |   | create database | Creates the database if it does not exist yet | advanced | Boolean | False | &#x60;False&#x60; |   | create database params | Extra specifications appended to the CREATE DATABASE command | advanced | String | False | &#x60;&#x60; |   | dbtype | Type | program | String | True | &#x60;postgis&#x60; |   | Batch insert size | Number of records inserted in the same batch (default, 1). For optimal performance, set to 100. | user | Integer | False | &#x60;1&#x60; |   | namespace | Namespace prefix | user | String | False | &#x60; &#x60; |   | Max connection idle time | number of seconds a connection needs to stay idle for the evictor to consider closing it | user | Integer | False | &#x60;300&#x60; |   | Session startup SQL | SQL statement executed when the connection is grabbed from the pool | user | String | False | &#x60; &#x60; |   | Expose primary keys | Expose primary key columns as attributes of the feature type | user | Boolean | False | &#x60;False&#x60; |   | min connections | minimum number of pooled connections | user | Integer | False | &#x60;1&#x60; |   | Max open prepared statements | Maximum number of prepared statements kept open and cached for each connection in the pool. Set to 0 to have unbounded caching, to -1 to disable caching | user | Integer | False | &#x60;50&#x60; |   | Callback factory | Name of JDBCReaderCallbackFactory to enable on the data store | user | String | False | &#x60; &#x60; |   | passwd | password used to login | user | String | False | &#x60; &#x60; |   | encode functions | set to true to have a set of filter functions be translated directly in SQL. Due to differences in the type systems the result might not be the same as evaluating them in memory, including the SQL failing with errors while the in memory version works fine. However this allows us to push more of the filter into the database, increasing performance of the postgis table. | advanced | Boolean | False | &#x60;False&#x60; |   | host | Host | user | String | True | &#x60;localhost&#x60; |   | Evictor tests per run | number of connections checked by the idle connection evictor for each of its runs (defaults to 3) | user | Integer | False | &#x60;3&#x60; |   | Loose bbox | Perform only primary filter on bbox | user | Boolean | False | &#x60;True&#x60; |   | Evictor run periodicity | number of seconds between idle object evictor runs (default, 300 seconds) | user | Integer | False | &#x60;300&#x60; |   | Estimated extends | Use the spatial index information to quickly get an estimate of the data bounds | user | Boolean | False | &#x60;True&#x60; |   | database | Database | user | String | False | &#x60; &#x60; |   | fetch size | number of records read with each interaction with the DBMS | user | Integer | False | &#x60;1000&#x60; |   | Test while idle | Periodically test the connections are still valid also while idle in the pool | user | Boolean | False | &#x60;True&#x60; |   | max connections | maximum number of open connections | user | Integer | False | &#x60;10&#x60; |   | preparedStatements | Use prepared statements | user | Boolean | False | &#x60;False&#x60; |   | Session close-up SQL | SQL statement executed when the connection is released to the pool | user | String | False | &#x60; &#x60; |   | schema | Schema | user | String | False | &#x60;public&#x60; |   | user | user name to login as | user | String | True | &#x60; &#x60; |  - Shapefile    Examples:   - application/xml:      &#x60;&#x60;&#x60;     &lt;dataStore&gt;       &lt;description&gt;A data store&lt;/description&gt;       &lt;enabled&gt;true&lt;/enabled&gt;       &lt;__default&gt;true&lt;/__default&gt;       &lt;connectionParameters&gt;         &lt;url&gt;file:/path/to/nyc.shp&lt;/url&gt;       &lt;/connectionParameters&gt;     &lt;/dataStore&gt;     &#x60;&#x60;&#x60;    - application/json:      &#x60;&#x60;&#x60;     {       \&quot;dataStore\&quot;: {         \&quot;description\&quot;: \&quot;A data store\&quot;,         \&quot;enabled\&quot;: \&quot;true\&quot;,         \&quot;_default\&quot;: \&quot;true\&quot;,         \&quot;connectionParameters\&quot;: {           \&quot;entry\&quot;: [             {\&quot;@key\&quot;:\&quot;url\&quot;,\&quot;$\&quot;:\&quot;file:/path/to/nyc.shp\&quot;}           ]         }       }     }     &#x60;&#x60;&#x60;    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | &#x60;True&#x60; |   | namespace | URI to the namespace | advanced | URI | False | &#x60; &#x60; |   | filetype | Discriminator for directory stores | program | String | False | &#x60;shapefile&#x60; |   | charset | character used to decode strings from the DBF file | advanced | Charset | False | &#x60;ISO-8859-1&#x60; |   | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | &#x60;True&#x60; |   | fstype | Enable using a setting of &#39;shape&#39;. | advanced | String | False | &#x60;shape&#x60; |   | url | url to a .shp file | user | URL | True | &#x60; &#x60; |   | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | &#x60;True&#x60; |   | memory mapped buffer | enable/disable the use of memory-mapped IO | advanced | Boolean | False | &#x60;False&#x60; |   | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | &#x60;Pacific Standard Time&#x60; |  - Directory of spatial files (shapefiles)    Examples:   - application/xml:      &#x60;&#x60;&#x60;     &lt;dataStore&gt;       &lt;description&gt;A data store&lt;/description&gt;       &lt;enabled&gt;true&lt;/enabled&gt;       &lt;__default&gt;true&lt;/__default&gt;       &lt;connectionParameters&gt;         &lt;url&gt;file:/path/to/directory&lt;/url&gt;       &lt;/connectionParameters&gt;     &lt;/dataStore&gt;     &#x60;&#x60;&#x60;    - application/json:      &#x60;&#x60;&#x60;     {       \&quot;dataStore\&quot;: {         \&quot;description\&quot;: \&quot;A data store\&quot;,         \&quot;enabled\&quot;: \&quot;true\&quot;,         \&quot;_default\&quot;: \&quot;true\&quot;,         \&quot;connectionParameters\&quot;: {           \&quot;entry\&quot;: [             {\&quot;@key\&quot;:\&quot;url\&quot;,\&quot;$\&quot;:\&quot;file:/path/to/directory\&quot;}           ]         }       }     }     &#x60;&#x60;&#x60;    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | cache and reuse memory maps | only memory map a file one, then cache and reuse the map | advanced | Boolean | False | &#x60;True&#x60; |   | namespace | URI to the namespace | advanced | URI | False | &#x60; &#x60; |   | filetype | Discriminator for directory stores | program | String | False | &#x60;shapefile&#x60; |   | charset | character used to decode strings from the DBF file | advanced | Charset | False | &#x60;ISO-8859-1&#x60; |   | create spatial index | enable/disable the automatic creation of spatial index | advanced | Boolean | False | &#x60;True&#x60; |   | fstype | Enable using a setting of &#39;shape&#39;. | advanced | String | False | &#x60;shape&#x60; |   | url | url to a .shp file | user | URL | True | &#x60; &#x60; |   | enable spatial index | enable/disable the use of spatial index for local shapefiles | advanced | Boolean | False | &#x60;True&#x60; |   | memory mapped buffer | enable/disable the use of memory-mapped IO | advanced | Boolean | False | &#x60;False&#x60; |   | timezone | time zone used to read dates from the DBF file | advanced | TimeZone | False | &#x60;Pacific Standard Time&#x60; |   - Web Feature Service    Examples:   - application/xml:      &#x60;&#x60;&#x60;     &lt;dataStore&gt;       &lt;description&gt;A data store&lt;/description&gt;       &lt;enabled&gt;true&lt;/enabled&gt;       &lt;__default&gt;true&lt;/__default&gt;       &lt;connectionParameters&gt;         &lt;GET_CAPABILITIES_URL&gt;http://localhost:8080/geoserver/wfs?request&#x3D;GetCapabilities&lt;/GET_CAPABILITIES_URL&gt;       &lt;/connectionParameters&gt;     &lt;/dataStore&gt;     &#x60;&#x60;&#x60;    - application/json:      &#x60;&#x60;&#x60;     {       \&quot;dataStore\&quot;: {         \&quot;description\&quot;: \&quot;A data store\&quot;,         \&quot;enabled\&quot;: \&quot;true\&quot;,         \&quot;_default\&quot;: \&quot;true\&quot;,         \&quot;connectionParameters\&quot;: {           \&quot;entry\&quot;: [             {\&quot;@key\&quot;:\&quot;GET_CAPABILITIES_URL\&quot;,\&quot;$\&quot;:\&quot;http://localhost:8080/geoserver/wfs?request&#x3D;GetCapabilities\&quot;}           ]         }       }     }     &#x60;&#x60;&#x60;    Connection Parameters:    | key | description | level | type | required | default |   | --- | ----------- | ----- | ---- | -------- | ------- |   | Protocol | Sets a preference for the HTTP protocol to use when requesting WFS functionality. Set this value to Boolean.TRUE for POST, Boolean.FALSE for GET or NULL for AUTO | user | Boolean | False | &#x60; &#x60; |   | WFS GetCapabilities URL | Represents a URL to the getCapabilities document or a server instance. | user | URL | False | &#x60; &#x60; |   | Buffer Size | This allows the user to specify a buffer size in features. This param has a default value of 10 features. | user | Integer | False | &#x60;10&#x60; |   | Filter compliance | Level of compliance to WFS specification (0-low,1-medium,2-high) | user | Integer | False | &#x60; &#x60; |   | EntityResolver | Sets the entity resolver used to expand XML entities | program | EntityResolver | False | &#x60;org.geotools.xml.PreventLocalEntityResolver@75e98519&#x60; |   | Time-out | This allows the user to specify a timeout in milliseconds. This param has a default value of 3000ms. | user | Integer | False | &#x60;3000&#x60; |   | GmlComplianceLevel | Optional OGC GML compliance level required. | user | Integer | False | &#x60;0&#x60; |   | Lenient | Indicates that datastore should do its best to create features from the provided data even if it does not accurately match the schema.  Errors will be logged but the parsing will continue if this is true.  Default is false | user | Boolean | False | &#x60;False&#x60; |   | Password | This allows the user to specify a username. This param should not be used without the USERNAME param. | user | String | False | &#x60; &#x60; |   | Use Default SRS | Use always the declared DefaultSRS for requests and reproject locally if necessary | advanced | Boolean | False | &#x60;False&#x60; |   | Namespace | Override the original WFS type name namespaces | advanced | String | False | &#x60; &#x60; |   | Username | This allows the user to specify a username. This param should not be used without the PASSWORD param. | user | String | False | &#x60; &#x60; |   | Axis Order Filter | Indicates axis order used by the remote WFS server for filters. It applies only to WFS 1.x.0 servers. Default is the same as AXIS_ORDER | advanced | String | False | &#x60; &#x60; |   | GmlCompatibleTypeNames | Use Gml Compatible TypeNames (replace : by _). | user | Boolean | False | &#x60;False&#x60; |   | Maximum features | Positive integer used as a hard limit for the number of Features to retrieve for each FeatureType. A value of zero or not providing this parameter means no limit. | user | Integer | False | &#x60;0&#x60; |   | Axis Order | Indicates axis order used by the remote WFS server in result coordinates. It applies only to WFS 1.x.0 servers. Default is Compliant | advanced | String | False | &#x60;Compliant&#x60; |   | WFS Strategy | Override WFS strategy with either cubwerx, ionic, mapserver, geoserver, strict, nonstrict or arcgis strategy. | user | String | False | &#x60;auto&#x60; |   | Try GZIP | Indicates that datastore should use gzip to transfer data if the server supports it. Default is true | user | Boolean | False | &#x60;True&#x60; |   | Encoding | This allows the user to specify the character encoding of the XML-Requests sent to the Server. Defaults to UTF-8 | user | String | False | &#x60;UTF-8&#x60; |   | Outputformat | This allows the user to specify an output format, different from the default one. | advanced | String | False | &#x60; &#x60; |  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putdatastores**
> putdatastores()



Invalid. Use POST for adding a new data store, or PUT on /datastores/{datastore} to edit an existing data store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()

try:
    api_instance.putdatastores()
except ApiException as e:
    print("Exception when calling DataStoresApi->putdatastores: %s\n" % e)
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

# **rebuild_all_mongo_schemas**
> rebuild_all_mongo_schemas(workspace_name, store_name, ids=ids, max=max)

Rebuilds all MongoDB internal stores Schemas for an App-Schema store.

Rebuilds all MongoDB internal stores Schemas for an App-Schema store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data stores.
store_name = 'store_name_example' # str | The name of the App-Schema store
ids = 'ids_example' # str | Comma separated MongoDB object IDs for use in new generated schema. (optional)
max = 56 # int | Max number of objects for use in new generated schema. (optional)

try:
    # Rebuilds all MongoDB internal stores Schemas for an App-Schema store.
    api_instance.rebuild_all_mongo_schemas(workspace_name, store_name, ids=ids, max=max)
except ApiException as e:
    print("Exception when calling DataStoresApi->rebuild_all_mongo_schemas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data stores. | 
 **store_name** | **str**| The name of the App-Schema store | 
 **ids** | **str**| Comma separated MongoDB object IDs for use in new generated schema. | [optional] 
 **max** | **int**| Max number of objects for use in new generated schema. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild_mongo_schema**
> rebuild_mongo_schema(workspace_name, store_name, internal_store_id, ids=ids, max=max, schema=schema)

Rebuilds a MongoDB internal store Schemas for an App-Schema store.

Rebuilds a MongoDB internal store Schemas for an App-Schema store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
workspace_name = 'workspace_name_example' # str | The name of the workspace containing the data stores.
store_name = 'store_name_example' # str | The name of the App-Schema store
internal_store_id = 'internal_store_id_example' # str | The store ID for the internal MongoDB store as specified on App-Schema Mappings.
ids = 'ids_example' # str | Comma separated MongoDB object IDs for use in new generated schema. (optional)
max = 56 # int | Max number of objects for use in new generated schema. (optional)
schema = 'schema_example' # str | Name of schema to re-build. (optional)

try:
    # Rebuilds a MongoDB internal store Schemas for an App-Schema store.
    api_instance.rebuild_mongo_schema(workspace_name, store_name, internal_store_id, ids=ids, max=max, schema=schema)
except ApiException as e:
    print("Exception when calling DataStoresApi->rebuild_mongo_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace containing the data stores. | 
 **store_name** | **str**| The name of the App-Schema store | 
 **internal_store_id** | **str**| The store ID for the internal MongoDB store as specified on App-Schema Mappings. | 
 **ids** | **str**| Comma separated MongoDB object IDs for use in new generated schema. | [optional] 
 **max** | **int**| Max number of objects for use in new generated schema. | [optional] 
 **schema** | **str**| Name of schema to re-build. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

