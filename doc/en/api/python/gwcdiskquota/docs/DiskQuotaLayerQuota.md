# DiskQuotaLayerQuota

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layer** | **str** | The layer name. | [optional] 
**expiration_policy_name** | **str** | When a disk quota is reached, further tiles will be saved at the expense of other tiles which will be truncated. The Least Frequently Used (LFU) policy will analyze the disk quota page store and delete the pages of tiles that have been accessed the least often. The Least Recently Used (LRU) policy will analyze the diskquota page store and delete the tiles that haven’t been accessed in the longest amount of time. | [optional] 
**quota** | [**DiskQuotaLayerQuotaQuota**](DiskQuotaLayerQuotaQuota.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


