# swagger_client.SecurityApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_acl_layer**](SecurityApi.md#delete_acl_layer) | **DELETE** /rest/security/acl/layers/{rule} | Delete layer rule.
[**delete_acl_layers**](SecurityApi.md#delete_acl_layers) | **DELETE** /rest/security/acl/layers | Delete layer rule(s)
[**delete_acl_service**](SecurityApi.md#delete_acl_service) | **DELETE** /rest/security/acl/services/{rule} | Delete service rule.
[**delete_acl_services**](SecurityApi.md#delete_acl_services) | **DELETE** /rest/security/acl/services | Delete service rule(s)
[**delete_aclrest_rule**](SecurityApi.md#delete_aclrest_rule) | **DELETE** /rest/security/acl/rest/{rule} | Delete REST access rule
[**delete_aclrest_rules**](SecurityApi.md#delete_aclrest_rules) | **DELETE** /rest/security/acl/rest | Delete REST access rule(s)
[**delete_catalog_mode**](SecurityApi.md#delete_catalog_mode) | **DELETE** /rest/security/acl/catalog | 
[**delete_master_pw**](SecurityApi.md#delete_master_pw) | **DELETE** /rest/security/masterpw | 
[**delete_self_password**](SecurityApi.md#delete_self_password) | **DELETE** /rest/security/self/password | 
[**get_acl_layer**](SecurityApi.md#get_acl_layer) | **GET** /rest/security/acl/layers/{rule} | 
[**get_acl_layers**](SecurityApi.md#get_acl_layers) | **GET** /rest/security/acl/layers | Get layer rules
[**get_acl_service**](SecurityApi.md#get_acl_service) | **GET** /rest/security/acl/services/{rule} | 
[**get_acl_services**](SecurityApi.md#get_acl_services) | **GET** /rest/security/acl/services | Get service rules
[**get_aclrest_rule**](SecurityApi.md#get_aclrest_rule) | **GET** /rest/security/acl/rest/{rule} | 
[**get_aclrest_rules**](SecurityApi.md#get_aclrest_rules) | **GET** /rest/security/acl/rest | Get REST rules
[**get_catalog_mode**](SecurityApi.md#get_catalog_mode) | **GET** /rest/security/acl/catalog | 
[**get_master_pw**](SecurityApi.md#get_master_pw) | **GET** /rest/security/masterpw | Get keystore password
[**get_self_password**](SecurityApi.md#get_self_password) | **GET** /rest/security/self/password | 
[**post_acl_layer**](SecurityApi.md#post_acl_layer) | **POST** /rest/security/acl/layers/{rule} | 
[**post_acl_layers**](SecurityApi.md#post_acl_layers) | **POST** /rest/security/acl/layers | Add layer rule(s)
[**post_acl_service**](SecurityApi.md#post_acl_service) | **POST** /rest/security/acl/services/{rule} | 
[**post_acl_services**](SecurityApi.md#post_acl_services) | **POST** /rest/security/acl/services | Add service rule(s)
[**post_aclrest_rule**](SecurityApi.md#post_aclrest_rule) | **POST** /rest/security/acl/rest/{rule} | 
[**post_aclrest_rules**](SecurityApi.md#post_aclrest_rules) | **POST** /rest/security/acl/rest | Add REST access rule(s)
[**post_catalog_mode**](SecurityApi.md#post_catalog_mode) | **POST** /rest/security/acl/catalog | 
[**post_master_pw**](SecurityApi.md#post_master_pw) | **POST** /rest/security/masterpw | 
[**post_self_password**](SecurityApi.md#post_self_password) | **POST** /rest/security/self/password | 
[**put_acl_layer**](SecurityApi.md#put_acl_layer) | **PUT** /rest/security/acl/layers/{rule} | 
[**put_acl_layers**](SecurityApi.md#put_acl_layers) | **PUT** /rest/security/acl/layers | Edit layer rule(s)
[**put_acl_service**](SecurityApi.md#put_acl_service) | **PUT** /rest/security/acl/services/{rule} | 
[**put_acl_services**](SecurityApi.md#put_acl_services) | **PUT** /rest/security/acl/services | Edit service rule(s)
[**put_aclrest_rule**](SecurityApi.md#put_aclrest_rule) | **PUT** /rest/security/acl/rest/{rule} | 
[**put_aclrest_rules**](SecurityApi.md#put_aclrest_rules) | **PUT** /rest/security/acl/rest | Edit REST access rule(s)
[**put_master_pw**](SecurityApi.md#put_master_pw) | **PUT** /rest/security/masterpw | Update keystore password
[**put_self_password**](SecurityApi.md#put_self_password) | **PUT** /rest/security/self/password | Update password
[**rest_security_acl_catalog_put**](SecurityApi.md#rest_security_acl_catalog_put) | **PUT** /rest/security/acl/catalog | Update catalog mode


# **delete_acl_layer**
> delete_acl_layer(rule)

Delete layer rule.

Deletes specific layer-based rule(s). The {rule} must specified in the last part of the URL and of the form \\<workspace\\>.\\<layer\\>.[r|w|a] 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r  

try:
    # Delete layer rule.
    api_instance.delete_acl_layer(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->delete_acl_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r   | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_acl_layers**
> delete_acl_layers()

Delete layer rule(s)

Deletes one or more layer-based rules in the list of security rules. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    # Delete layer rule(s)
    api_instance.delete_acl_layers()
except ApiException as e:
    print("Exception when calling SecurityApi->delete_acl_layers: %s\n" % e)
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

# **delete_acl_service**
> delete_acl_service(rule)

Delete service rule.

Deletes specific service-based rule(s). The {rule} must be specified as the last part of the URL and must be of the form \\<service\\>.\\<operation\\> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r  

try:
    # Delete service rule.
    api_instance.delete_acl_service(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->delete_acl_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r   | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_acl_services**
> delete_acl_services()

Delete service rule(s)

Deletes one or more service-based rules in the list of security rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    # Delete service rule(s)
    api_instance.delete_acl_services()
except ApiException as e:
    print("Exception when calling SecurityApi->delete_acl_services: %s\n" % e)
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

# **delete_aclrest_rule**
> delete_aclrest_rule(rule)

Delete REST access rule

Deletes specific REST access rule(s). The {rule} must specified as the last part of the URL and must be of the form \\<URL Ant pattern\\>:\\<comma separated list of HTTP methods\\> 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The REST rule, specified as \\<URL Ant pattern\\>;\\<comma separated list of HTTP methods\\>. Examples are  - /**;GET - /**;POST,DELETE,PUT 

try:
    # Delete REST access rule
    api_instance.delete_aclrest_rule(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->delete_aclrest_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The REST rule, specified as \\&lt;URL Ant pattern\\&gt;;\\&lt;comma separated list of HTTP methods\\&gt;. Examples are  - /**;GET - /**;POST,DELETE,PUT  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aclrest_rules**
> delete_aclrest_rules()

Delete REST access rule(s)

Deletes one or more service-based rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    # Delete REST access rule(s)
    api_instance.delete_aclrest_rules()
except ApiException as e:
    print("Exception when calling SecurityApi->delete_aclrest_rules: %s\n" % e)
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

# **delete_catalog_mode**
> delete_catalog_mode()



Invalid. Use PUT to change catalog mode.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    api_instance.delete_catalog_mode()
except ApiException as e:
    print("Exception when calling SecurityApi->delete_catalog_mode: %s\n" % e)
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

# **delete_master_pw**
> delete_master_pw()



Invalid. Use PUT to change keystore password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    api_instance.delete_master_pw()
except ApiException as e:
    print("Exception when calling SecurityApi->delete_master_pw: %s\n" % e)
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

# **delete_self_password**
> delete_self_password()



Invalid. Use PUT to change password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    api_instance.delete_self_password()
except ApiException as e:
    print("Exception when calling SecurityApi->delete_self_password: %s\n" % e)
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

# **get_acl_layer**
> get_acl_layer(rule)



Has no effect. Endpoint that includes a specific rule is only used with DELETE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r  

try:
    api_instance.get_acl_layer(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->get_acl_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r   | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acl_layers**
> ACLLayers get_acl_layers()

Get layer rules

Displays the current layer-based security rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    # Get layer rules
    api_response = api_instance.get_acl_layers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_acl_layers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ACLLayers**](ACLLayers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acl_service**
> get_acl_service(rule)



Has no effect. Endpoint that includes a specific rule is only used with DELETE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r  

try:
    api_instance.get_acl_service(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->get_acl_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r   | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acl_services**
> ACLServices get_acl_services()

Get service rules

Displays the current service-based security rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    # Get service rules
    api_response = api_instance.get_acl_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_acl_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ACLServices**](ACLServices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aclrest_rule**
> get_aclrest_rule(rule)



Has no effect. Endpoint that includes a specific rule is only used with DELETE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The REST rule, specified as \\<URL Ant pattern\\>;\\<comma separated list of HTTP methods\\>. Examples are  - /**;GET - /**;POST,DELETE,PUT 

try:
    api_instance.get_aclrest_rule(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->get_aclrest_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The REST rule, specified as \\&lt;URL Ant pattern\\&gt;;\\&lt;comma separated list of HTTP methods\\&gt;. Examples are  - /**;GET - /**;POST,DELETE,PUT  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aclrest_rules**
> ACLREST get_aclrest_rules()

Get REST rules

Displays the current REST access rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    # Get REST rules
    api_response = api_instance.get_aclrest_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_aclrest_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ACLREST**](ACLREST.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_mode**
> CatalogMode get_catalog_mode()



Gets the catalog mode, which specifies how GeoServer will advertise secured layers and behave when a secured layer is accessed without the necessary privileges.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    api_response = api_instance.get_catalog_mode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_catalog_mode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CatalogMode**](CatalogMode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_master_pw**
> MasterPW get_master_pw()

Get keystore password

Displays the keystore password. HTTPS is strongly suggested, otherwise password will be sent in plain text. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/settings.xml\" for XML). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    # Get keystore password
    api_response = api_instance.get_master_pw()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_master_pw: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MasterPW**](MasterPW.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_password**
> get_self_password()



Invalid. Use PUT to change password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    api_instance.get_self_password()
except ApiException as e:
    print("Exception when calling SecurityApi->get_self_password: %s\n" % e)
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

# **post_acl_layer**
> post_acl_layer(rule)



Has no effect. Endpoint that includes a specific rule is only used with DELETE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r  

try:
    api_instance.post_acl_layer(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->post_acl_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r   | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_acl_layers**
> post_acl_layers(acl_layers_body)

Add layer rule(s)

Adds one or more new layer-based rules to the list of security rules. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
acl_layers_body = swagger_client.ACLLayers() # ACLLayers | The new rules to upload.

try:
    # Add layer rule(s)
    api_instance.post_acl_layers(acl_layers_body)
except ApiException as e:
    print("Exception when calling SecurityApi->post_acl_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_layers_body** | [**ACLLayers**](ACLLayers.md)| The new rules to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_acl_service**
> post_acl_service(rule)



Has no effect. Endpoint that includes a specific rule is only used with DELETE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r  

try:
    api_instance.post_acl_service(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->post_acl_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r   | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_acl_services**
> post_acl_services(acl_services_body)

Add service rule(s)

Adds one or more new service-based rules to the list of security rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
acl_services_body = swagger_client.ACLServices() # ACLServices | The new rules to upload.

try:
    # Add service rule(s)
    api_instance.post_acl_services(acl_services_body)
except ApiException as e:
    print("Exception when calling SecurityApi->post_acl_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_services_body** | [**ACLServices**](ACLServices.md)| The new rules to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_aclrest_rule**
> post_aclrest_rule(rule)



Has no effect. Endpoint that includes a specific rule is only used with DELETE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The REST rule, specified as \\<URL Ant pattern\\>;\\<comma separated list of HTTP methods\\>. Examples are  - /**;GET - /**;POST,DELETE,PUT 

try:
    api_instance.post_aclrest_rule(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->post_aclrest_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The REST rule, specified as \\&lt;URL Ant pattern\\&gt;;\\&lt;comma separated list of HTTP methods\\&gt;. Examples are  - /**;GET - /**;POST,DELETE,PUT  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_aclrest_rules**
> post_aclrest_rules(aclrest_body)

Add REST access rule(s)

Adds one or more new REST access rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
aclrest_body = swagger_client.ACLREST() # ACLREST | The new rules to upload.

try:
    # Add REST access rule(s)
    api_instance.post_aclrest_rules(aclrest_body)
except ApiException as e:
    print("Exception when calling SecurityApi->post_aclrest_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclrest_body** | [**ACLREST**](ACLREST.md)| The new rules to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_catalog_mode**
> post_catalog_mode()



Invalid. Use PUT to change catalog mode.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    api_instance.post_catalog_mode()
except ApiException as e:
    print("Exception when calling SecurityApi->post_catalog_mode: %s\n" % e)
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

# **post_master_pw**
> post_master_pw()



Invalid. Use PUT to change keystore password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    api_instance.post_master_pw()
except ApiException as e:
    print("Exception when calling SecurityApi->post_master_pw: %s\n" % e)
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

# **post_self_password**
> post_self_password()



Invalid. Use PUT to change password

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()

try:
    api_instance.post_self_password()
except ApiException as e:
    print("Exception when calling SecurityApi->post_self_password: %s\n" % e)
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

# **put_acl_layer**
> put_acl_layer(rule)



Has no effect. Endpoint that includes a specific rule is only used with DELETE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r  

try:
    api_instance.put_acl_layer(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->put_acl_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r   | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_acl_layers**
> put_acl_layers(acl_layers_body)

Edit layer rule(s)

Edits one or more layer-based rules in the list of security rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
acl_layers_body = swagger_client.ACLLayers() # ACLLayers | The altered rules to upload.

try:
    # Edit layer rule(s)
    api_instance.put_acl_layers(acl_layers_body)
except ApiException as e:
    print("Exception when calling SecurityApi->put_acl_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_layers_body** | [**ACLLayers**](ACLLayers.md)| The altered rules to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_acl_service**
> put_acl_service(rule)



Has no effect. Endpoint that includes a specific rule is only used with DELETE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r  

try:
    api_instance.put_acl_service(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->put_acl_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The specified rule, as the last part in the URI, e.g. /security/acl/layers/\\*.\\*.r   | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_acl_services**
> put_acl_services(acl_services_body)

Edit service rule(s)

Edits one or more service-based rules in the list of security rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
acl_services_body = swagger_client.ACLServices() # ACLServices | The altered rules to upload.

try:
    # Edit service rule(s)
    api_instance.put_acl_services(acl_services_body)
except ApiException as e:
    print("Exception when calling SecurityApi->put_acl_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_services_body** | [**ACLServices**](ACLServices.md)| The altered rules to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_aclrest_rule**
> put_aclrest_rule(rule)



Has no effect. Endpoint that includes a specific rule is only used with DELETE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
rule = 'rule_example' # str | The REST rule, specified as \\<URL Ant pattern\\>;\\<comma separated list of HTTP methods\\>. Examples are  - /**;GET - /**;POST,DELETE,PUT 

try:
    api_instance.put_aclrest_rule(rule)
except ApiException as e:
    print("Exception when calling SecurityApi->put_aclrest_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The REST rule, specified as \\&lt;URL Ant pattern\\&gt;;\\&lt;comma separated list of HTTP methods\\&gt;. Examples are  - /**;GET - /**;POST,DELETE,PUT  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_aclrest_rules**
> put_aclrest_rules(aclrest_body)

Edit REST access rule(s)

Edits one or more REST access rules.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
aclrest_body = swagger_client.ACLREST() # ACLREST | The altered rules to upload.

try:
    # Edit REST access rule(s)
    api_instance.put_aclrest_rules(aclrest_body)
except ApiException as e:
    print("Exception when calling SecurityApi->put_aclrest_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aclrest_body** | [**ACLREST**](ACLREST.md)| The altered rules to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_master_pw**
> put_master_pw(master_pw_body)

Update keystore password

Changes keystore password. Must supply current keystore password. HTTPS is strongly suggested, otherwise password will be sent in plain text.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
master_pw_body = swagger_client.UpdateMasterPW() # UpdateMasterPW | The old and new keystore password information to upload.

try:
    # Update keystore password
    api_instance.put_master_pw(master_pw_body)
except ApiException as e:
    print("Exception when calling SecurityApi->put_master_pw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **master_pw_body** | [**UpdateMasterPW**](UpdateMasterPW.md)| The old and new keystore password information to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_self_password**
> put_self_password(self_password_body)

Update password

Updates the password for the account used to issue the request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
self_password_body = swagger_client.SelfPassword() # SelfPassword | The catalog mode information to upload.

try:
    # Update password
    api_instance.put_self_password(self_password_body)
except ApiException as e:
    print("Exception when calling SecurityApi->put_self_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_password_body** | [**SelfPassword**](SelfPassword.md)| The catalog mode information to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_security_acl_catalog_put**
> rest_security_acl_catalog_put(catalog_mode_body)

Update catalog mode

Changes catalog mode. The mode must be one of HIDE, MIXED, or CHALLENGE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecurityApi()
catalog_mode_body = swagger_client.CatalogMode() # CatalogMode | The catalog mode information to upload.

try:
    # Update catalog mode
    api_instance.rest_security_acl_catalog_put(catalog_mode_body)
except ApiException as e:
    print("Exception when calling SecurityApi->rest_security_acl_catalog_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_mode_body** | [**CatalogMode**](CatalogMode.md)| The catalog mode information to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

