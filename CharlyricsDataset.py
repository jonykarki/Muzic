from __future__ import print_function
import os
import glob
import torch
import numpy as np
import utils
from pathlib import Path

from torch.utils.data import Dataset, DataLoader
from config import config


class CharLyricsDataset(Dataset):
    """ Character Lyrics Dataset """

    def __init__(self, folder_path, max_len, transform=None):
        self.folder_path = folder_path
        self.max_len = max_len
        self.artists = self.get_artist_list()
        self.num_artists = len(self.artists)
        self.raw_combined_lyrics = self.get_all_lyrics()
        self.transform = transform

    def __len__(self):
        return len(self.artists)

    def __getitem__(self, idx):
        # return the max_len number of chars starting from max_len*idx
        item = utils.char_to_label(
            self.raw_combined_lyrics[
                idx * self.max_len : idx * self.max_len + self.max_len
            ]
        )

        # return the padded sequences to feed into the RNN
        input_seq = item[:-1] + [100]
        output_seq = item[1:] + [-100]

        return (torch.tensor(input_seq), torch.tensor(output_seq))

    def get_all_lyrics(self):
        raw_lyrics = ""
        try:
            for artist in self.artists:
                with open(os.path.join(self.folder_path, f"{artist}.txt"), "r") as f:
                    raw_lyrics += f.read()
        except IOError as e:
            print(f"I/O error, {e.errno} {e.strerror}")
        return raw_lyrics

    def get_artist_list(self):
        files_list = map(
            lambda filepath: Path(filepath).stem,
            glob.glob(os.path.join(self.folder_path, "*.txt")),
        )
        # # remove -, _ and capitalize
        # names_list = map(
        #     lambda string_: string_.replace("-", " ").replace("_", " ").title(),
        #     files_list,
        # )
        return list(files_list)


if __name__ == "__main__":
    obj = CharLyricsDataset(config.DATA.LYRICS)
    obj[0]
