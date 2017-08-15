# -*- coding: utf-8 -*-

from openpyxl import load_workbook
from matplotlib import pyplot
#import numpy as np

wb = load_workbook('data_analysis_lab.xlsx')
sh = wb['Data']

def getValue(x): return x.value

year = list(map(getValue,sh['A'][1:]))
rel = list(map(getValue,sh['B'][1:]))
act = list(map(getValue,sh['C'][1:]))

pyplot.xlabel('Год')
#pyplot.xticks(np.arange(min(year),max(year),5))
pyplot.ylabel('Активность | Отношения')
pyplot.plot(year,act,label="Солнечная активность")
pyplot.plot(year,rel,label="Отношения")
pyplot.show()