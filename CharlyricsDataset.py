from __future__ import print_function
import os
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader

class CharLyricsDataset(Dataset):
    """ Character Lyrics Dataset """

    def __init__(self, folder_path, transform=None):
        self.folder_path = folder_path
        self.artists = list()
        self.transform = transform

    def __len__(self):
        return len(self.artists)

    def __getitem__(self, idx):
        return self.artists[idx]