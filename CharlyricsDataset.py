from __future__ import print_function
import os
import glob
import torch
import numpy as np
from pathlib import Path

from torch.utils.data import Dataset, DataLoader
from config import config


class CharLyricsDataset(Dataset):
    """ Character Lyrics Dataset """

    def __init__(self, folder_path, transform=None):
        self.folder_path = folder_path
        self.artists = self.get_artist_list()
        self.transform = transform

    def __len__(self):
        return len(self.artists)

    def __getitem__(self, idx):
        return self.artists[idx]

    def get_artist_list(self):
        files_list = map(
            lambda filepath: Path(filepath).stem,
            glob.glob(os.path.join(self.folder_path, "*.txt")),
        )
        # remove -, _ and capitalize
        names_list = map(
            lambda string_: string_.replace("-", " ").replace("_", " ").title(), files_list
        )
        return list(names_list)
