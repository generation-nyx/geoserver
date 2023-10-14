# swagger_client.MonitoringApi

All URIs are relative to *https://geoserver:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_monitor_request**](MonitoringApi.md#delete_monitor_request) | **DELETE** /monitor/requests/{request} | 
[**delete_monitor_requests**](MonitoringApi.md#delete_monitor_requests) | **DELETE** /monitor/requests | 
[**get_monitor_request**](MonitoringApi.md#get_monitor_request) | **GET** /monitor/requests/{request} | Get a list of requests
[**get_monitor_requests**](MonitoringApi.md#get_monitor_requests) | **GET** /monitor/requests | Get a list of requests
[**post_monitor_request**](MonitoringApi.md#post_monitor_request) | **POST** /monitor/requests/{request} | 
[**post_monitor_requests**](MonitoringApi.md#post_monitor_requests) | **POST** /monitor/requests | 
[**put_monitor_request**](MonitoringApi.md#put_monitor_request) | **PUT** /monitor/requests/{request} | 
[**put_monitor_requests**](MonitoringApi.md#put_monitor_requests) | **PUT** /monitor/requests | 


# **delete_monitor_request**
> delete_monitor_request()



Invalid. Cannot delete a specific request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitoringApi()

try:
    api_instance.delete_monitor_request()
except ApiException as e:
    print("Exception when calling MonitoringApi->delete_monitor_request: %s\n" % e)
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

# **delete_monitor_requests**
> delete_monitor_requests()



Clears all reqests

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitoringApi()

try:
    api_instance.delete_monitor_requests()
except ApiException as e:
    print("Exception when calling MonitoringApi->delete_monitor_requests: %s\n" % e)
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

# **get_monitor_request**
> Request get_monitor_request(request, fields=fields)

Get a list of requests

Returns a specific request, by identifier The HTML format returns all details of the request. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/request/1.xls\" for Excel). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitoringApi()
request = 'request_example' # str | The request identifier
fields = 'fields_example' # str | Comma separated list of fields to be returned (optional)

try:
    # Get a list of requests
    api_response = api_instance.get_monitor_request(request, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringApi->get_monitor_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **str**| The request identifier | 
 **fields** | **str**| Comma separated list of fields to be returned | [optional] 

### Return type

[**Request**](Request.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv, application/zip, application/vnd.ms-excel, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitor_requests**
> RequestList get_monitor_requests(_from=_from, to=to, filter=filter, order=order, offset=offset, count=count, live=live, fields=fields)

Get a list of requests

Returns a list of all requests known to the monitoring system. If no list of fields is specified, the full list will be returned, with the exception of Class, Body and Error fields. The HTML format return a summary of the requests, and links to the single request to gather details. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/requests.xls\" for Excel). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitoringApi()
_from = '_from_example' # str | Specifies an inclusive lower bound on the timestamp for the start of a request.  The timestamp must be expressed as an ISO can be specified to any desired precision (e..g, \"2010-07-23\", \"2010-07-23T16:16:44\")    (optional)
to = 'to_example' # str | Specifies an inclusive lower bound on the timestamp for the start of a request.  The timestamp must be expressed as an ISO can be specified to any desired precision (e..g, \"2010-07-23\", \"2010-07-23T16:16:44\")    (optional)
filter = 'filter_example' # str | Specifies generic filter against the available fields, in the form \"attributeName:OP:value\" where OP can be: - EQ: equals - NEQ: not equals - LT: less than - LTE: less than or equals - GT: greater than - GTE: greater than or equals - IN: in list (\"value\" must be a comma separated list of values  (optional)
order = 'order_example' # str | Specifies which request attribute to sort by, and optionally specifies the sort direction. The syntax is \"attribute[;ASC|DESC]\", where the sorting direction is optional  (optional)
offset = 56 # int | Specifies where in the result set records should be returned from (optional)
count = 56 # int | Specifies how many records should be returned. (optional)
live = true # bool | Specifies which requests to return based on status. If true, only returns live (RUNNING, WAITING, CANCELLING) requests. If false, only returns completed (FINISHED, FAILED) requests. If not specified, all requests are returned regardless of status.  (optional)
fields = 'fields_example' # str | Comma separated list of fields to be returned (optional)

try:
    # Get a list of requests
    api_response = api_instance.get_monitor_requests(_from=_from, to=to, filter=filter, order=order, offset=offset, count=count, live=live, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringApi->get_monitor_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Specifies an inclusive lower bound on the timestamp for the start of a request.  The timestamp must be expressed as an ISO can be specified to any desired precision (e..g, \&quot;2010-07-23\&quot;, \&quot;2010-07-23T16:16:44\&quot;)    | [optional] 
 **to** | **str**| Specifies an inclusive lower bound on the timestamp for the start of a request.  The timestamp must be expressed as an ISO can be specified to any desired precision (e..g, \&quot;2010-07-23\&quot;, \&quot;2010-07-23T16:16:44\&quot;)    | [optional] 
 **filter** | **str**| Specifies generic filter against the available fields, in the form \&quot;attributeName:OP:value\&quot; where OP can be: - EQ: equals - NEQ: not equals - LT: less than - LTE: less than or equals - GT: greater than - GTE: greater than or equals - IN: in list (\&quot;value\&quot; must be a comma separated list of values  | [optional] 
 **order** | **str**| Specifies which request attribute to sort by, and optionally specifies the sort direction. The syntax is \&quot;attribute[;ASC|DESC]\&quot;, where the sorting direction is optional  | [optional] 
 **offset** | **int**| Specifies where in the result set records should be returned from | [optional] 
 **count** | **int**| Specifies how many records should be returned. | [optional] 
 **live** | **bool**| Specifies which requests to return based on status. If true, only returns live (RUNNING, WAITING, CANCELLING) requests. If false, only returns completed (FINISHED, FAILED) requests. If not specified, all requests are returned regardless of status.  | [optional] 
 **fields** | **str**| Comma separated list of fields to be returned | [optional] 

### Return type

[**RequestList**](RequestList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv, application/zip, application/vnd.ms-excel, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_monitor_request**
> post_monitor_request()



This resource cannot be modified

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitoringApi()

try:
    api_instance.post_monitor_request()
except ApiException as e:
    print("Exception when calling MonitoringApi->post_monitor_request: %s\n" % e)
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

# **post_monitor_requests**
> post_monitor_requests()



Invalid. This resource cannot be modified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitoringApi()

try:
    api_instance.post_monitor_requests()
except ApiException as e:
    print("Exception when calling MonitoringApi->post_monitor_requests: %s\n" % e)
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

# **put_monitor_request**
> put_monitor_request()



This resource cannot be modified

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitoringApi()

try:
    api_instance.put_monitor_request()
except ApiException as e:
    print("Exception when calling MonitoringApi->put_monitor_request: %s\n" % e)
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

# **put_monitor_requests**
> put_monitor_requests()



Invalid. This resource cannot be modified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonitoringApi()

try:
    api_instance.put_monitor_requests()
except ApiException as e:
    print("Exception when calling MonitoringApi->put_monitor_requests: %s\n" % e)
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

