from .lifxlan import LifxLAN
from .message import *
from .msgtypes import *
from .unpack import unpack_lifx_message
from .device import *
from .light import *
from .multizonelight import *
from .group import Group
from .tilechain import TileChain, Tile
from .utils import *
from .common_constants import *
from .common_functions import *

__version__     = '1.2.7'
__description__ = 'API for local communication with LIFX devices over a LAN.'
__url__         = 'https://github.com/wesnicol2/lifxlan'
__author__      = 'Meghan Clark & Wes Nicol'
__authoremail__ = 'mclarkk@berkeley.edu'
__license__     = 'MIT'
