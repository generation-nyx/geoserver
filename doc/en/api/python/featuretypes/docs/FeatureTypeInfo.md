# FeatureTypeInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the resource. This name corresponds to the \&quot;published\&quot; name of the resource. | [optional] 
**native_name** | **str** | The native name of the resource. This name corresponds to the physical resource that feature type is derived from -- a shapefile name, a database table, etc... | [optional] 
**namespace** | [**FeatureTypeInfoNamespace**](FeatureTypeInfoNamespace.md) |  | [optional] 
**title** | **str** | The title of the resource. This is usually something that is meant to be displayed in a user interface. | [optional] 
**abstract** | **str** | A description of the resource. This is usually something that is meant to be displayed in a user interface. | [optional] 
**keywords** | [**FeatureTypeInfoKeywords**](FeatureTypeInfoKeywords.md) |  | [optional] 
**metadatalinks** | [**FeatureTypeInfoMetadatalinks**](FeatureTypeInfoMetadatalinks.md) |  | [optional] 
**data_links** | [**FeatureTypeInfoDataLinks**](FeatureTypeInfoDataLinks.md) |  | [optional] 
**native_crs** | **str** | The native coordinate reference system object of the resource. | [optional] 
**srs** | **str** | Returns the identifier of coordinate reference system of the resource. | [optional] 
**native_bounding_box** | [**FeatureTypeInfoNativeBoundingBox**](FeatureTypeInfoNativeBoundingBox.md) |  | [optional] 
**lat_lon_bounding_box** | [**FeatureTypeInfoLatLonBoundingBox**](FeatureTypeInfoLatLonBoundingBox.md) |  | [optional] 
**metadata** | [**list[MetadataEntry]**](MetadataEntry.md) | A list of key/value metadata pairs. | [optional] 
**store** | [**FeatureTypeInfoStore**](FeatureTypeInfoStore.md) |  | [optional] 
**cql_filter** | **str** | The ECQL string used as default feature type filter | [optional] 
**max_features** | **int** | A cap on the number of features that a query against this type can return. | [optional] 
**num_decimals** | **float** | The number of decimal places to use when encoding floating point numbers from data of this feature type. | [optional] 
**response_srs** | [**FeatureTypeInfoResponseSRS**](FeatureTypeInfoResponseSRS.md) |  | [optional] 
**overriding_service_srs** | **bool** | True if this feature type info is overriding the WFS global SRS list | [optional] 
**skip_number_matched** | **bool** | True if this feature type info is overriding the counting of numberMatched. | [optional] 
**circular_arc_present** | **bool** |  | [optional] 
**linearization_tolerance** | **float** | Tolerance used to linearize this feature type, as an absolute value expressed in the geometries own CRS | [optional] 
**attributes** | [**FeatureTypeInfoAttributes**](FeatureTypeInfoAttributes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


