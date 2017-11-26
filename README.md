# Artwork-Extractor
A short script that extracts images from the [Painter by Numbers](https://www.kaggle.com/c/painter-by-numbers/data) dataset hosted by Kaggle. The script examines the *train_info.csv* file and copies/moves specific images over into a new directory based upon factors such as style, genre, and date.

## Setup
Ensure all artwork is in a single directory, as the script currently does not traverse subdirectories. The default directory is `input` as is expected to be in the current working directory. This can be changed using the `--in_dir` argument.

All possible arguments are listed below:
- `--style` the artwork style (as named in `train_info.csv`)
- `--genre` the artwork genre (as above)
- `--date` the artwork date (as above)
- `--in_csv` the CSV file to read for artwork
- `--in_dir` the directory where artwork is stored
- `--out_dir` the directory to put extracted artwork
- `--remove_original` whether to remove the copy of the image stored in `in_dir`, false by default

## Example
To extract all surrealist landscapes, run: `python pextract.py --style=surrealism --genre=landscape`
