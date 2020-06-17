from easydict import EasyDict as edict 
import os

_C = edict()
config = _C

_C.BASEPATH = os.path.abspath(os.pardir)

# Data folders
_C.DATA = edict()
_C.DATA.BASE = os.path.join(_C.BASEPATH, "data")
_C.DATA.MIDI = os.path.join(_C.DATA.BASE, "midi")
_C.DATA.LYRICS = os.path.join(_C.BASEPATH, "azlyrics-scraper")

# train parameters
_C.TRAIN = edict()
_C.TRAIN.LEARNING_RATE = 0.008
_C.TRAIN.MAX_LEN = 100
_C.TRAIN.HIDDEN_SIZE = 512
_C.TRAIN.LSTM_N_LAYERS = 2
_C.TRAIN.BATCH_SIZE = 3
_C.TRAIN.EPOCHS = 10