# Artwork-Extractor
A short script that extracts images from the [Painter by Numbers](https://www.kaggle.com/c/painter-by-numbers/data)
dataset hosted by Kaggle. The script examines the *train_info.csv* file and copies/moves specific images over into
a new directory based upon factors such as style, genre, and date.

## Setup
Ensure all artwork is in a single directory, as the script currently does not traverse subdirectories. The default
directory is `input` as is expected to be in the current working directory. This can be changed using the
`--in_dir` argument.

All possible arguments are listed below:
- `--style` artwork style
- `--genre` artwork genre
- `--date` artwork creation date: either a single year (e.g. `1950`) or comma-separated range (e.g. `1950,1970`)
- `--in_csv` CSV file to read for artwork
- `--in_dir` directory where artwork is stored
- `--out_dir` directory to put extracted artwork
- `--remove_original` whether to remove the copy of the image stored in `in_dir`, false by default

To find appropriate values for style, genre, and date, consult `train_info.csv`.

## Example
To extract all surrealist landscapes between 1990 and 1980 (inclusive), run:

`python art_extract.py --style=surrealism --genre=landscape --date=1900,1980`
