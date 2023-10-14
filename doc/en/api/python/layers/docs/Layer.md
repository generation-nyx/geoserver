# Layer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the layer | [optional] 
**path** | **str** | Location of the layer in the WMS capabilities layer tree | [optional] 
**type** | **str** | Type of published layer. Can be VECTOR, RASTER, REMOTE, WMS or GROUP. Must be consistent with resource definition. | [optional] 
**default_style** | [**StyleReference**](StyleReference.md) |  | [optional] 
**styles** | [**LayerStyles**](LayerStyles.md) |  | [optional] 
**resource** | [**LayerResource**](LayerResource.md) |  | [optional] 
**opaque** | **bool** | Controls layer transparency (whether the layer is opaque or transparent). | [optional] 
**metadata** | [**list[MetadataEntry]**](MetadataEntry.md) |  | [optional] 
**attribution** | [**LayerAttribution**](LayerAttribution.md) |  | [optional] 
**authority_urls** | [**list[AuthorityURL]**](AuthorityURL.md) |  | [optional] 
**identifiers** | [**list[Identifier]**](Identifier.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


