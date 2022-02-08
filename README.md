# DataAugmentation
This is a data augmentation tool for creating augmented data from a bunch of images under directory with GUI.

## Usage
1. First select the directory.

2. Then program will detect the extansions under that directory. Select the target extansion. Doesn't matter jpeg, png, tif etc..

3. Select augmentation types you want

4. Select what kind of a directory structure you want

5. Your new augmented images will be under the selected directory.

6. To reuse the tool you must delete old created files with their directory.


<img src="example_gui_photo.png">


## Dependencies
- OpenCV
- Skimage
- Numy
- Easygui


## Augmentation Types
- [x] Random Crop
- [x] Random Erasing
- [x] Contrast
- [x] Flip Horizontal
- [x] Flip Vertical
- [x] Flip Origin
- [x] Noise (Gaussian)
- [x] Rotate 90 Clockwise
- [x] Rotate 90 Counter Clockwise
- [x] Random Rotation
- [x] Translation
- [x] Brightness
- [x] Saturation
- [x] Hue
- [x] GrayScale
- [ ] Padding
