#!/usr/bin/env python

"""A library that provides a Python interface to the Recommendation System"""

__author__       = 'Kashyap Madariyil'
__email__        = 'kashyapmadariyil@gmail.com'
__copyright__    = 'Copyright (c) 2020 Kashyap Madariyil'
__license__      = 'MIT License'
__version__      = '0.1.5'
__url__          = 'https://github.com/kashy750/RecoSystem'
__download_url__ = 'https://pypi.org/project/py-recommendation/'
__description__  = 'A library that provides an easy ready-to-use Recommendation engine.'



from .error import RecoError

from .input_data import (
	ItemData,
	UsersData
)	
from .py_recosys import (
	SimilarItem,
	UserContent
)
