# Compressing images script
This script will resize all the images (jpeg, jpg and png) where it's located

## Prerequisits
We use pillow for processing the images
```
pip install pillow
```

## Arguments
- We can send the quality of the images we want to set using the first argument
```
python3 compress_imgs.py 50
```
This will set the quality to 50, the smaller the number the lower the quality.
Set to 10 by default.

## Recomendations
- We can modify the code to receive the path where the images are located
- We can modify the code to receive only a set of predefined images to be compressed
- We can extend the image types
- We can add image file types detection
