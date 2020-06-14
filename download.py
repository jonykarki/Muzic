from __future__ import print_function
import os
from sys import platform
import zipfile
import shutil
import glob
from config import config

try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

def download_data():
    data_folder = config.DATA.MIDI
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        filename = os.path.join(data_folder, "scale_chords.zip")
        if not os.path.exists(filename):
            url = "http://www.feelyoursound.com/data/scale_chords_small.zip"
            print("Downloading data from {}".format(url))
            urlretrieve(url, filename)
        try:
            print("Extracting {}".format(filename))
            with zipfile.ZipFile(filename) as zipp:
                zipp.extractall(data_folder)
            files = glob.glob(os.path.join(data_folder, "midi") + "/*.mid")
        finally:
            os.remove(filename)
        print('Finished Downloading')
    else:
        print("Data already exists in {}".format(data_folder))

    return os.path.join(data_folder, "midi")

if __name__ == "__main__":
    download_data()
