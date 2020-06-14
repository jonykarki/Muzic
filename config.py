from easydict import EasyDict as edict 
import os

_C = edict()
config = _C

_C.DATA = edict()
_C.DATA.BASE = os.path.join(os.path.abspath(os.pardir), "data")