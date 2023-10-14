# swagger_client.UserGroupApi

All URIs are relative to *https://geoserver:8080/geoserver/rest/security*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_default_delete**](UserGroupApi.md#group_default_delete) | **DELETE** /usergroup/group/{group} | Delete a group
[**group_default_post**](UserGroupApi.md#group_default_post) | **POST** /usergroup/group/{group} | Add a group
[**group_default_user_get**](UserGroupApi.md#group_default_user_get) | **GET** /usergroup/group/{group}/users | Query all users for a group
[**group_delete**](UserGroupApi.md#group_delete) | **DELETE** /usergroup/service/{serviceName}/group/{group} | Delete a group
[**group_post**](UserGroupApi.md#group_post) | **POST** /usergroup/service/{serviceName}/group/{group} | Add a group
[**group_user_get**](UserGroupApi.md#group_user_get) | **GET** /usergroup/service/{serviceName}/group/{group}/users | Query all users for a group
[**groups_default_get**](UserGroupApi.md#groups_default_get) | **GET** /usergroup/groups/ | Query all groups
[**groups_get**](UserGroupApi.md#groups_get) | **GET** /usergroup/service/{serviceName}/groups/ | Query all groups
[**user_default_delete**](UserGroupApi.md#user_default_delete) | **DELETE** /usergroup/user/{user} | Delete a user
[**user_default_group_get**](UserGroupApi.md#user_default_group_get) | **GET** /usergroup/user/{user}/groups | Query all groups for a user
[**user_default_post**](UserGroupApi.md#user_default_post) | **POST** /usergroup/user/{user} | Modify a user
[**user_delete**](UserGroupApi.md#user_delete) | **DELETE** /usergroup/service/{serviceName}/user/{user} | Delete a user
[**user_group_default_delete**](UserGroupApi.md#user_group_default_delete) | **DELETE** /usergroup/user/{user}/group/{group} | Unassociate a user from a group
[**user_group_default_post**](UserGroupApi.md#user_group_default_post) | **POST** /usergroup/user/{user}/group/{group} | Associate a user with a group
[**user_group_delete**](UserGroupApi.md#user_group_delete) | **DELETE** /usergroup/service/{serviceName}/user/{user}/group/{group} | Unassociate a user from a group
[**user_group_get**](UserGroupApi.md#user_group_get) | **GET** /usergroup/service/{serviceName}/user/{user}/groups | Query all groups for a user
[**user_group_post**](UserGroupApi.md#user_group_post) | **POST** /usergroup/service/{serviceName}/user/{user}/group/{group} | Associate a user with a group
[**user_post**](UserGroupApi.md#user_post) | **POST** /usergroup/service/{serviceName}/user/{user} | Modify a user
[**users_default_get**](UserGroupApi.md#users_default_get) | **GET** /usergroup/users/ | Query all users
[**users_default_post**](UserGroupApi.md#users_default_post) | **POST** /usergroup/users/ | Add a new user
[**users_get**](UserGroupApi.md#users_get) | **GET** /usergroup/service/{serviceName}/users/ | Query all users
[**users_post**](UserGroupApi.md#users_post) | **POST** /usergroup/service/{serviceName}/users/ | Add a new user


# **group_default_delete**
> group_default_delete(group)

Delete a group

Delete a group in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
group = 'group_example' # str | the name of the group

try:
    # Delete a group
    api_instance.group_default_delete(group)
except ApiException as e:
    print("Exception when calling UserGroupApi->group_default_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_default_post**
> group_default_post(group)

Add a group

Add a group in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
group = 'group_example' # str | the name of the group

try:
    # Add a group
    api_instance.group_default_post(group)
except ApiException as e:
    print("Exception when calling UserGroupApi->group_default_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_default_user_get**
> Users group_default_user_get(group)

Query all users for a group

Query all users for a group in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
group = 'group_example' # str | the name of the group

try:
    # Query all users for a group
    api_response = api_instance.group_default_user_get(group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->group_default_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the name of the group | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_delete**
> group_delete(service_name, group)

Delete a group

Delete a group in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the user/group service
group = 'group_example' # str | the name of the group

try:
    # Delete a group
    api_instance.group_delete(service_name, group)
except ApiException as e:
    print("Exception when calling UserGroupApi->group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_post**
> group_post(service_name, group)

Add a group

Add a group in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the user/group service
group = 'group_example' # str | the name of the group

try:
    # Add a group
    api_instance.group_post(service_name, group)
except ApiException as e:
    print("Exception when calling UserGroupApi->group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_user_get**
> Users group_user_get(service_name, group)

Query all users for a group

Query all users for a group in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the user/group service
group = 'group_example' # str | the name of the group

try:
    # Query all users for a group
    api_response = api_instance.group_user_get(service_name, group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->group_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **group** | **str**| the name of the group | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_default_get**
> Groups groups_default_get()

Query all groups

Query all groups in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()

try:
    # Query all groups
    api_response = api_instance.groups_default_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->groups_default_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Groups**](Groups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get**
> Groups groups_get(service_name)

Query all groups

Query all groups in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the group group service

try:
    # Query all groups
    api_response = api_instance.groups_get(service_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the group group service | 

### Return type

[**Groups**](Groups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_default_delete**
> user_default_delete(user)

Delete a user

Delete a user in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
user = 'user_example' # str | the name of the user

try:
    # Delete a user
    api_instance.user_default_delete(user)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_default_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| the name of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_default_group_get**
> Groups user_default_group_get(user)

Query all groups for a user

Query all groups for a user in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
user = 'user_example' # str | the name of the user

try:
    # Query all groups for a user
    api_response = api_instance.user_default_group_get(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_default_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| the name of the user | 

### Return type

[**Groups**](Groups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_default_post**
> user_default_post(user, user_default_post_body)

Modify a user

Modify a user in the default user/group service, unspecified fields remain unchanged.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
user = 'user_example' # str | the name of the user
user_default_post_body = swagger_client.User() # User | the new user's details

try:
    # Modify a user
    api_instance.user_default_post(user, user_default_post_body)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_default_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| the name of the user | 
 **user_default_post_body** | [**User**](User.md)| the new user&#39;s details | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete**
> user_delete(service_name, user)

Delete a user

Delete a user in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the user/group service
user = 'user_example' # str | the name of the user

try:
    # Delete a user
    api_instance.user_delete(service_name, user)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **user** | **str**| the name of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_default_delete**
> user_group_default_delete(user, group)

Unassociate a user from a group

Unassociate a user from a group in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
user = 'user_example' # str | the name of the user
group = 'group_example' # str | the name of the group

try:
    # Unassociate a user from a group
    api_instance.user_group_default_delete(user, group)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_group_default_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| the name of the user | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_default_post**
> user_group_default_post(user, group)

Associate a user with a group

Associate a user with a group in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
user = 'user_example' # str | the name of the user
group = 'group_example' # str | the name of the group

try:
    # Associate a user with a group
    api_instance.user_group_default_post(user, group)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_group_default_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| the name of the user | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_delete**
> user_group_delete(service_name, user, group)

Unassociate a user from a group

Unassociate a user from a group in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the user/group service
user = 'user_example' # str | the name of the user
group = 'group_example' # str | the name of the group

try:
    # Unassociate a user from a group
    api_instance.user_group_delete(service_name, user, group)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **user** | **str**| the name of the user | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_get**
> Groups user_group_get(service_name, user)

Query all groups for a user

Query all groups for a user in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the user/group service
user = 'user_example' # str | the name of the user

try:
    # Query all groups for a user
    api_response = api_instance.user_group_get(service_name, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **user** | **str**| the name of the user | 

### Return type

[**Groups**](Groups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_post**
> user_group_post(service_name, user, group)

Associate a user with a group

Associate a user with a group in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the user/group service
user = 'user_example' # str | the name of the user
group = 'group_example' # str | the name of the group

try:
    # Associate a user with a group
    api_instance.user_group_post(service_name, user, group)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **user** | **str**| the name of the user | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_post**
> user_post(service_name, user, user_post_body)

Modify a user

Modify a user in a particular user/group service, unspecified fields remain unchanged.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the user/group service
user = 'user_example' # str | the name of the user
user_post_body = swagger_client.User() # User | the new user's details

try:
    # Modify a user
    api_instance.user_post(service_name, user, user_post_body)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **user** | **str**| the name of the user | 
 **user_post_body** | [**User**](User.md)| the new user&#39;s details | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_default_get**
> Users users_default_get()

Query all users

Query all users in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()

try:
    # Query all users
    api_response = api_instance.users_default_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->users_default_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_default_post**
> users_default_post(users_default_post_body)

Add a new user

Add a new user to the default user/group service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
users_default_post_body = swagger_client.User() # User | the new user's details

try:
    # Add a new user
    api_instance.users_default_post(users_default_post_body)
except ApiException as e:
    print("Exception when calling UserGroupApi->users_default_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_default_post_body** | [**User**](User.md)| the new user&#39;s details | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> Users users_get(service_name)

Query all users

Query all users in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the user/group service

try:
    # Query all users
    api_response = api_instance.users_get(service_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> users_post(service_name, users_post_body)

Add a new user

Add a new user to a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupApi()
service_name = 'service_name_example' # str | the name of the user/group service
users_post_body = swagger_client.User() # User | the new user's details

try:
    # Add a new user
    api_instance.users_post(service_name, users_post_body)
except ApiException as e:
    print("Exception when calling UserGroupApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **users_post_body** | [**User**](User.md)| the new user&#39;s details | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

