# SRA-Assignments
***
## Image Processing
> ### Contents
> 1. .[Image Rotation](#Image-Rotation)
> 1. .[Bluring and Sharpning](#Bluring-and-Sharpning)
>    - Mean, Gausian and Median Blur
>    - Laplacian filter for sharpning
> 1. .[Edge Detection](#Edge-Detection)
>    - Sobel
>    - Canny  
> 1. .[Morphological Transformations](#Morphological-Transformations)
>    - Dialation
>    - Erosion
> 1. .[Masking](#Masking)
> 1. .[Region of Intrest](#Region-of-Intrest)
#### Image Rotation
aliasing can be removed by interpolation or inverse matrix method<br>
bounding is to be done by translation
|orignal image|processed image|aliasing removed|
|---|---|---|
|![orignal image](/img_processing/orignal_assets/rotate.png)|![orignal image](/img_processing/processed_assets/rotate.png)|![orignal image](/img_processing/processed_assets/rotate2.png)
#### Bluring and Sharpning
|filter|orignal image|processed image|
|---|---|---|
|mean-filter|![orignal image](/img_processing/orignal_assets/blur.jpeg)|![orignal image](/img_processing/processed_assets/box-blur.png)|
|gaussian-filter|![orignal image](/img_processing/orignal_assets/blur.jpeg)|![orignal image](/img_processing/processed_assets/gausian.png)|
|median-filter|![orignal image](/img_processing/orignal_assets/filter.png)|![orignal image](/img_processing/processed_assets/median.png)|
|sharpening|![orignal image](/img_processing/orignal_assets/filter.png)|![orignal image](/img_processing/processed_assets/sharpen.png)|
#### Edge Detection
|filter|orignal image|processed image|
|---|---|---|
|vertical-edge|![orignal image](/img_processing/orignal_assets/edge-detection2.jpg)|![orignal image](/img_processing/processed_assets/vertical.png)|
|horizontal-edge|![orignal image](/img_processing/orignal_assets/edge-detection2.jpg)|![orignal image](/img_processing/processed_assets/hoerizontal.png)|
|sobel-edge|![orignal image](/img_processing/orignal_assets/edge-detection2.jpg)|![orignal image](/img_processing/processed_assets/sobel.png)|
#### Morphological Transformations
|filter|orignal image|processed image|
|---|---|---|
|dialation|![orignal image](/img_processing/orignal_assets/morphological.png)|![orignal image](/img_processing/processed_assets/dia.png)|
|erosion|![orignal image](/img_processing/orignal_assets/morphological.png)|![orignal image](/img_processing/processed_assets/erosion.png)|
#### Masking
|orignal image|processed image|
|---|---|
|![orignal image](/img_processing/orignal_assets/mask.jpg)|![orignal image](/img_processing/processed_assets/masking.png)|
#### Region of Intrest
|orignal image|processed image|
|---|---|
|![orignal image](/img_processing/orignal_assets/roi.jpg)|![orignal image](/img_processing/processed_assets/roi.png)|
## Acknowledgement
[SRA](https://github.com/SRA-VJTI)
