"""
    GRM package
"""

# abstract DAO class
from .dao import DAO
# there is some my patterns
from .patterns import Singleton
# OS thread-safe realisation
from .try_os import try_os_io
