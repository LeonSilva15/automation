# Tasks automation

Here are some scripts I created to avoid doing tedious or extensive tasks manually.

## compress-imgs
This script will resize all the images (jpeg, jpg and png) where it's located.

The output will be new resized images with the same name leaded with an underscore.
```
python3 compress_imgs.py 50
```

## reduce-dataset
This script will recursively reduce the size of a dataset.

The output will be a new dataset with non sequential elements from the dataset (don't worry about getting only the fisrt elements). Anyway, it isn't a random select, it's a stepped selection.
```
python3 reduce_dataset.py -d my_dataset -s 100 -t ../mini
```
