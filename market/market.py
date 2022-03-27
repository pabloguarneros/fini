import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from assets.options import Option
from assets.stocks import Stock

class Market:

    def __init__(self):
        self.stocks = []
        self.options = []

    def _add(self,obj):
        if isinstance(obj, Option):
            #isinstance differs from type given that if obj inherits from Option, isinstance captures it
            self.options.append(obj)
        elif isinstance(obj, Stock):
            self.stocks.append(obj)

    def add(self, obj):
        print(type(obj))
        if type(obj) == list:
            for item in obj:
                self._add(item)
        else:
            self._add(obj)

    def has_arbitrage(self):
        
       