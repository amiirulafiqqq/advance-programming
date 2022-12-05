#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import sys

#use list comprehension to create a list of rolls of a six sided value
rolls = [random.randrange(1,7) for i in range(int(sys.argv[1]))]

#numpy unique function return unique face and frequency of each face
values, frequencies = np.unique(rolls, return_counts = True)

title = f'Roling a six-sided Dice {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette = 'bright')
axes.set_title(title)
axes.set(xlabel='Dice Value', ylabel = 'frequency')

#scal y axis by 10% to make room for text above bars
axes.set_ylim(top=max(frequencies) * 1.10)

#display frequency & percentage above each patch (bar)
for bar, frequency in zip(axes.patches, frequencies):
	text_x = bar.get_x() + bar.get_width()/2.0
	text_y = bar.get_height()
	text = f'{frequency:,}\n{frequency/len(rolls):.3%}'
	axes.text(text_x, text_y, text_y,fontsize=11, ha='center', va='bottom')

plt.show()# display graph	
