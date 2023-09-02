# HowRU-app-data-cleanup
This repository contains the python scripts available to clean data from HowRU.

### `scripts` folder:
* contains all python scripts (also in jupyter notebook format through .ipynb files)

### `original data` folder:
* contains example starting data
* data inputted into this folder should be processed throuh python scripts
  * this clean data can then be transferred to the `clean data` folder

### `clean data` folder:
* contains the output data that is returned fromt the python scripts

## Setup
To run the code, you need packages `numpy`, `pandas`, `scipy`, `matplotlib`, `itertools`, `glob`, `csv`, `os`, `re`, and `json`. If you do not have any programming software or a specific python environment (such as Anaconda) I recommend watching [this video](https://www.youtube.com/watch?v=qI3P7zMMsgY&pp=ygUPYW5hY29uZGEgdnNjb2Rl).

## Running Scripts
To take new data from the app and transform it into a more readable csv, you must first put the new data into the original data folder. Different app tasks create data in differrent formats. For OSPAN and FTT data, place in the `OSPAN data` and `FTT data` subfolders respectfuly. The format for OSPAN and FTT data should be based on each subject (if there is new data from the OSPAN or FTT tasks, formt as txt file and the data should only be for one subject... not multiple

Then, run the correct python script for the new data. Note that there are specific scripts for OSPAN, FTT, and WPA.

❗IMPORTANT❗

There are lines in the code that need to be edited if you wish to transform new data from the app. Lines which contain the `read_csv` and `to_csv` functions must be changed to the correct path for where you are fetching the data and storing the transformed data respectfully.
