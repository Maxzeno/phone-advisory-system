#!/usr/bin/env python
from py_recommendation.constants import STOPWORDS
from re import sub




class Utils(object):
    """Helper class for main api classes"""

    @staticmethod
    def cleanText(text_list):
    	return [" ".join(sub(r"(?!(?<=\d)\.(?=\d))[^a-zA-Z0-9 ]"," ",each).lower().split()) for each in text_list]
