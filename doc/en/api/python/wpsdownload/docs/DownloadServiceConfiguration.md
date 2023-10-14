# DownloadServiceConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_features** | **float** | maximum number of features to download | [optional] 
**raster_size_limits** | **float** | maximum pixel size of the Raster to read | [optional] 
**write_limits** | **float** | maximum raw raster size in bytes (a limit of how much space can a raster take in memory). For a given raster, its raw size in bytes is calculated by multiplying pixel number (raster_width x raster_height) with the accumulated sum of each band’s pixel sample_type size in bytes, for all bands | [optional] 
**hard_output_limit** | **float** | maximum file size to download | [optional] 
**compression_level** | **int** | compression level for the output zip file | [optional] 
**max_animation_frames** | **int** | maximum number of frames allowed (if no limit, the maximum execution time limits will still apply and stop the process in case there are too many) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


