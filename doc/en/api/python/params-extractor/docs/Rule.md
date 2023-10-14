# Rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | identifier of the rule | [optional] 
**activated** | **bool** | Whether or not the parameter echoing is active | [optional] 
**position** | **int** | The position of the URL base path element to be selected | [optional] 
**parameter** | **str** | The name of the parameter produced by this rule | [optional] 
**transform** | **str** | Expression that defines the value of the parameter, use {PARAMETER} as a placeholder for the selected path element | [optional] 
**match** | **str** | Regex match expression with groups, for example ^(?:/[^/]*){3}(/([^/]+)).*$ selects the URL base path third element | [optional] 
**activation** | **str** | If defined this rule will only be applied to URLs that match this regex expression | [optional] 
**remove** | **int** | The match expression group to be removed from URL, by default 1 | [optional] 
**combine** | **str** | Defines how to combine parameter existing value ($1 existing value, $2 new value), by default the value is overridden | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


