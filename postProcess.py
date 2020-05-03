from data import data
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
codeLicenses = ['MIT License', 
			   'Apache License', 
			   'GPLv3', 
			   'BSD 2-clause',
			   'BSD 3-clause',
			   'GPLv2', 
			   'GPLv2.1',
			   'LGPLv2.1',
			   'LGPLv3', 
			   'Mozilla Public License',
			   'The Unilicense',
			   'Boost Software',
			   'Pre-Release']

nonCodeLicenses = ['CC0-1.0', 'CC-BY-4', 'CC-BY-SA-4']

copyright = ['copyright', 'retain the above copyright', 'without modification', 'with or without modification', 'without warranty', 'reproduce and distribute copies']

confidential = ['Proprietary and confidential', 'All rights reserved', 'Unauthorized copying strictly prohibited']



def createHorizontalDoubleBarGraph(name, x, y1, y2, y1_axis, y2_axis, title):
	N = len(x)
	ind = np.arange(N) 
	width = 0.3

	fig,ax = plt.subplots(figsize=(10,8))
	N = len(x)
	ind = np.arange(N)
	
	# make a plot
	ax.bar(ind, y1, width, color="red")
	# set x-axis label
	# ax.set_xlabel("Type of License",fontsize=14)
	# set y-axis label
	ax.set_ylabel(y1_axis, color="red",fontsize=14)

	ax.set_xticks(ind + width / 2, x)
	ax.set_xticks(np.arange(len(x)))
	ax.set_xticklabels(x, rotation=90)

	# twin object for two different y-axis on the sample plot
	ax2 = ax.twinx()

	# make a plot with different y-axis using second axis object
	ax2.bar(ind + width, y2, width, color="blue")
	ax2.set_ylabel(y2_axis,color="blue",fontsize=14)
	fig.subplots_adjust(bottom=0.35)

	# fig.text(0, -1.25, "Data source: www.github.com | "  
	# 		 "Author: Neal Soni (Yale '22)", fontsize=10) 
	ax.set_title(title)
	# plt.show()
	# save the plot as a file
	fig.savefig(name + '.jpg',
	            format='jpeg',
	            dpi=100,
	            bbox_inches='tight')

repositories = []
for codeLicense in codeLicenses:
	repositories.append(int(data[codeLicense]['Repositories']['count']))

code = []
for codeLicense in codeLicenses:
	code.append(int(data[codeLicense]['Code']['count']))

createHorizontalDoubleBarGraph( name='(Repositories & Code) vs Open Source Code Licenses', 
								x=codeLicenses, 
								y1=repositories, 
								y2=code, 
								y1_axis="Repositories Count", 
								y2_axis="Code Count", 
								title='(Repositories & Code) vs Open Source Code Licenses')

repositories = []
for codeLicense in nonCodeLicenses:
	repositories.append(int(data[codeLicense]['Repositories']['count']))

code = []
for codeLicense in nonCodeLicenses:
	code.append(int(data[codeLicense]['Code']['count']))

createHorizontalDoubleBarGraph( name='(Repositories & Code) vs General Open Source Licenses', 
								x=nonCodeLicenses, 
								y1=repositories, 
								y2=code, 
								y1_axis="Repositories Count", 
								y2_axis="Code Count", 
								title='(Repositories & Code) vs General Open Source Licenses')




# # data to plot
# n_groups = len(codeLicenses)

# # create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.35
# opacity = 0.8

# rects1 = plt.bar(index, np.array(repositories), bar_width,
# alpha=opacity,
# color='b',
# label='Repositories')

# rects2 = plt.bar(index + bar_width, np.array(code), bar_width,
# alpha=opacity,
# color='g',
# label='Code')

# plt.xlabel('Person')
# plt.ylabel('Scores')
# plt.title('Scores by person')
# plt.xticks(index + bar_width, np.array(codeLicenses))
# plt.legend()

# plt.tight_layout()
# plt.show()