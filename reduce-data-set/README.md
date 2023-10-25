# Reducing a dataset
This script will recursively reduce the size of a dataset.

The output will be a new dataset with non sequential elements from the dataset (don't worry about getting only the fisrt elements). Anyway, it isn't a random select, it's a stepped selection.

## Prerequisits
Python 3.x is the only requirement

## Arguments
| Short | Long        | Description         | Type          | Default                  |
|-------|-------------|---------------------|---------------|--------------------------|
| -s    | --size      | Target dataset size | Integer       | 200                      |
| -d    | --directory | Source directory    | String        | ./                       |
| -t    | --target    | Target directory    | String        | reduced_\<directoy>      |
| -ty   | --types     | File types          | Array<String> | [ 'jpeg', 'jpg', 'png' ] |

```
python3 reduce_dataset.py -d my_dataset -s 100 -t ../mini
```
This will create a new reduced dataset on the directory named `mini` with `100` image (`jpeg`, `jpg` and `png`) taken from `my_dataset`.
