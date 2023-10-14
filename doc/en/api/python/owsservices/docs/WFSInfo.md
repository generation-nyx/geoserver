# WFSInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Status of the service | [optional] 
**name** | **str** | Name of the service. This value is unique among all instances of ServiceInfo and can be used as an identifier. | [optional] 
**title** | **str** | Title of the service | [optional] 
**maintainer** | **str** | Maintainer of the service | [optional] 
**abstrct** | **str** | Description of the service | [optional] 
**access_constraints** | **str** | Access constraints | [optional] 
**fees** | **str** | Any fees associated with the service | [optional] 
**versions** | [**WMSInfoVersions**](WMSInfoVersions.md) |  | [optional] 
**keywords** | **list[str]** | Keywords associated with the service. | [optional] 
**metadata_link** | [**list[WFSInfoMetadataLink]**](WFSInfoMetadataLink.md) |  | [optional] 
**cite_compliant** | **bool** | Status of service CITE compliance | [optional] 
**online_resource** | **str** | URL resource | [optional] 
**schema_base_url** | **str** | Base URL for the schemas describing the service | [optional] 
**verbose** | **bool** | Flag indicating if the service should be verbose | [optional] 
**gml** | [**WFSInfoGml**](WFSInfoGml.md) |  | [optional] 
**service_level** | **str** | Level of service provided by the WFS | [optional] 
**max_features** | **int** | Global cap on the number of features to allow when processing a request | [optional] 
**feature_bounding** | **bool** | Flag which determines if gml:bounds elements should be encoded at the feature level in GML output | [optional] 
**canonical_schema_location** | **bool** | Flag that determines the encoding of the WFS schemaLocation. True if the WFS schemaLocation should refer to the canonical location, false if the WFS schemaLocation should refer to a copy served by GeoServer. | [optional] 
**encode_feature_member** | **bool** | Flag that determines encoding of featureMember or featureMembers. True if the featureMember should be encoded False if the featureMembers should be encoded. | [optional] 
**hits_ignore_max_features** | **bool** | Flag that determines if WFS hit requests (counts) will ignore the maximum features limit for this server | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


