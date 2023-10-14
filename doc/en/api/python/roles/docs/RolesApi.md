# swagger_client.RolesApi

All URIs are relative to *https://geoserver:8080/geoserver/rest/security*

Method | HTTP request | Description
------------- | ------------- | -------------
[**role_default_delete**](RolesApi.md#role_default_delete) | **DELETE** /roles/role/{role} | Delete a role
[**role_default_group_delete**](RolesApi.md#role_default_group_delete) | **DELETE** /roles/role/{role}/group/{group} | Disassociate a role from a group
[**role_default_group_post**](RolesApi.md#role_default_group_post) | **POST** /roles/role/{role}/group/{group} | Associate a role with a group
[**role_default_post**](RolesApi.md#role_default_post) | **POST** /roles/role/{role} | Add a role
[**role_default_user_delete**](RolesApi.md#role_default_user_delete) | **DELETE** /roles/role/{role}/user/{user} | Disassociate a role from a user
[**role_default_user_post**](RolesApi.md#role_default_user_post) | **POST** /roles/role/{role}/user/{user} | Associate a role with a user
[**role_delete**](RolesApi.md#role_delete) | **DELETE** /service/{serviceName}/role/{role} | Delete a role
[**role_group_delete**](RolesApi.md#role_group_delete) | **DELETE** /service/{serviceName}/roles/role/{role}/group/{group} | Disassociate a role from a group
[**role_group_post**](RolesApi.md#role_group_post) | **POST** /service/{serviceName}/roles/role/{role}/group/{group} | Associate a role with a group
[**role_post**](RolesApi.md#role_post) | **POST** /service/{serviceName}/role/{role} | Add a role
[**role_user_delete**](RolesApi.md#role_user_delete) | **DELETE** /service/{serviceName}/roles/role/{role}/user/{user} | Disassociate a role from a user
[**role_user_post**](RolesApi.md#role_user_post) | **POST** /service/{serviceName}/roles/role/{role}/user/{user} | Associate a role with a user
[**roles_default_get**](RolesApi.md#roles_default_get) | **GET** /roles | Query all roles
[**roles_default_group_get**](RolesApi.md#roles_default_group_get) | **GET** /roles/group/{group} | Query all roles for group
[**roles_default_user_get**](RolesApi.md#roles_default_user_get) | **GET** /roles/user/{user} | Query all roles for user
[**roles_get**](RolesApi.md#roles_get) | **GET** /roles/service/{serviceName}/roles/ | Query all roles
[**roles_group_get**](RolesApi.md#roles_group_get) | **GET** /roles/service/{serviceName}/group/{group} | Query all roles for group
[**roles_user_get**](RolesApi.md#roles_user_get) | **GET** /roles/service/{serviceName}/user/{user} | Query all roles for user


# **role_default_delete**
> role_default_delete(role)

Delete a role

Delete a role in the default role service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role = 'role_example' # str | the name of the role

try:
    # Delete a role
    api_instance.role_default_delete(role)
except ApiException as e:
    print("Exception when calling RolesApi->role_default_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| the name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_default_group_delete**
> role_default_group_delete(role, group)

Disassociate a role from a group

Disassociate a role in the default role service with a group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role = 'role_example' # str | the name of the role
group = 'group_example' # str | the name of the group

try:
    # Disassociate a role from a group
    api_instance.role_default_group_delete(role, group)
except ApiException as e:
    print("Exception when calling RolesApi->role_default_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| the name of the role | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_default_group_post**
> role_default_group_post(role, group)

Associate a role with a group

Associate an existing role in the default role service with a group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role = 'role_example' # str | the name of the role
group = 'group_example' # str | the name of the group

try:
    # Associate a role with a group
    api_instance.role_default_group_post(role, group)
except ApiException as e:
    print("Exception when calling RolesApi->role_default_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| the name of the role | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_default_post**
> role_default_post(role)

Add a role

Add a role in the default role service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role = 'role_example' # str | the name of the role

try:
    # Add a role
    api_instance.role_default_post(role)
except ApiException as e:
    print("Exception when calling RolesApi->role_default_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| the name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_default_user_delete**
> role_default_user_delete(role, user)

Disassociate a role from a user

Disassociate a role in the default role service with a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role = 'role_example' # str | the name of the role
user = 'user_example' # str | the name of the user

try:
    # Disassociate a role from a user
    api_instance.role_default_user_delete(role, user)
except ApiException as e:
    print("Exception when calling RolesApi->role_default_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| the name of the role | 
 **user** | **str**| the name of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_default_user_post**
> role_default_user_post(role, user)

Associate a role with a user

Associate an existing role in the default role service with a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role = 'role_example' # str | the name of the role
user = 'user_example' # str | the name of the user

try:
    # Associate a role with a user
    api_instance.role_default_user_post(role, user)
except ApiException as e:
    print("Exception when calling RolesApi->role_default_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| the name of the role | 
 **user** | **str**| the name of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_delete**
> role_delete(service_name, role)

Delete a role

Delete a role in a particular role service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
service_name = 'service_name_example' # str | the name of the role service
role = 'role_example' # str | the name of the role

try:
    # Delete a role
    api_instance.role_delete(service_name, role)
except ApiException as e:
    print("Exception when calling RolesApi->role_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the role service | 
 **role** | **str**| the name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_group_delete**
> role_group_delete(service_name, role, group)

Disassociate a role from a group

Disassociate a role in a particular role service with a group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
service_name = 'service_name_example' # str | the name of the role service
role = 'role_example' # str | the name of the role
group = 'group_example' # str | the name of the group

try:
    # Disassociate a role from a group
    api_instance.role_group_delete(service_name, role, group)
except ApiException as e:
    print("Exception when calling RolesApi->role_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the role service | 
 **role** | **str**| the name of the role | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_group_post**
> role_group_post(service_name, role, group)

Associate a role with a group

Associate an existing role in a particular role service with a group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
service_name = 'service_name_example' # str | the name of the role service
role = 'role_example' # str | the name of the role
group = 'group_example' # str | the name of the group

try:
    # Associate a role with a group
    api_instance.role_group_post(service_name, role, group)
except ApiException as e:
    print("Exception when calling RolesApi->role_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the role service | 
 **role** | **str**| the name of the role | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_post**
> role_post(service_name, role)

Add a role

Add a role in a particular role service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
service_name = 'service_name_example' # str | the name of the role service
role = 'role_example' # str | the name of the role

try:
    # Add a role
    api_instance.role_post(service_name, role)
except ApiException as e:
    print("Exception when calling RolesApi->role_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the role service | 
 **role** | **str**| the name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_user_delete**
> role_user_delete(service_name, role, user)

Disassociate a role from a user

Disassociate a role in a particular role service with a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
service_name = 'service_name_example' # str | the name of the role service
role = 'role_example' # str | the name of the role
user = 'user_example' # str | the name of the user

try:
    # Disassociate a role from a user
    api_instance.role_user_delete(service_name, role, user)
except ApiException as e:
    print("Exception when calling RolesApi->role_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the role service | 
 **role** | **str**| the name of the role | 
 **user** | **str**| the name of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_user_post**
> role_user_post(service_name, role, user)

Associate a role with a user

Associate an existing role in a particular role service with a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
service_name = 'service_name_example' # str | the name of the role service
role = 'role_example' # str | the name of the role
user = 'user_example' # str | the name of the user

try:
    # Associate a role with a user
    api_instance.role_user_post(service_name, role, user)
except ApiException as e:
    print("Exception when calling RolesApi->role_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the role service | 
 **role** | **str**| the name of the role | 
 **user** | **str**| the name of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_default_get**
> Roles roles_default_get()

Query all roles

Query all roles in the default role service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()

try:
    # Query all roles
    api_response = api_instance.roles_default_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->roles_default_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Roles**](Roles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_default_group_get**
> Roles roles_default_group_get(group)

Query all roles for group

Query all roles for the group in the default role service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
group = 'group_example' # str | the name of the group

try:
    # Query all roles for group
    api_response = api_instance.roles_default_group_get(group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->roles_default_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the name of the group | 

### Return type

[**Roles**](Roles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_default_user_get**
> Roles roles_default_user_get(user)

Query all roles for user

Query all roles for the user in the default role service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
user = 'user_example' # str | the name of the user

try:
    # Query all roles for user
    api_response = api_instance.roles_default_user_get(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->roles_default_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| the name of the user | 

### Return type

[**Roles**](Roles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_get**
> Roles roles_get(service_name)

Query all roles

Query all roles in a particular role service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
service_name = 'service_name_example' # str | the name of the role role service

try:
    # Query all roles
    api_response = api_instance.roles_get(service_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the role role service | 

### Return type

[**Roles**](Roles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_group_get**
> Roles roles_group_get(service_name, group)

Query all roles for group

Query all roles for the group in a particular role service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
service_name = 'service_name_example' # str | the name of the role role service
group = 'group_example' # str | the name of the group

try:
    # Query all roles for group
    api_response = api_instance.roles_group_get(service_name, group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->roles_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the role role service | 
 **group** | **str**| the name of the group | 

### Return type

[**Roles**](Roles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_user_get**
> Roles roles_user_get(service_name, user)

Query all roles for user

Query all roles for the user in a particular role service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
service_name = 'service_name_example' # str | the name of the role role service
user = 'user_example' # str | the name of the user

try:
    # Query all roles for user
    api_response = api_instance.roles_user_get(service_name, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->roles_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the role role service | 
 **user** | **str**| the name of the user | 

### Return type

[**Roles**](Roles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

