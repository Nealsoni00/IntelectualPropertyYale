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

termCopyright = 'copyright'
generalLicenseTerms = ['retain the above copyright', 'without modification', 'with or without modification', 'without warranty', 'reproduce and distribute copies']

confidential = ['Proprietary and confidential', 'All rights reserved', 'Unauthorized copying strictly prohibited']



def createHorizontalDoubleBarGraph(name, x, y1, y2, y1_axis, y2_axis, title, angle=90):
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
	ax.set_xticklabels(x, rotation=angle)

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
	            dpi=200,
	            bbox_inches='tight')


def createPieGraph(name, labels, sizes, title):
	# labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
	# sizes = [38.4, 40.6, 20.7, 10.3]
	# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
	sizes, labels = zip(*sorted(zip(sizes, labels)))

	fig, ax = plt.subplots()
	ax.pie(sizes, labels=labels, autopct='%1.f%%',
	        shadow=True, startangle=90)
	# Equal aspect ratio ensures that pie is drawn as a circle
	ax.axis('equal')  
	plt.tight_layout()
	# plt.show()
	ax.set_title(title)

	fig.savefig(name + '.jpg',
	            format='jpeg',
	            dpi=200,
	            bbox_inches='tight')


	# patches, texts = plt.pie(sizes, shadow=True, startangle=90)
	# plt.legend(patches, labels, loc="best")
	# plt.axis('equal')
	# plt.tight_layout()
	# plt.show()


repositories = []
for codeLicense in codeLicenses:
	repositories.append(int(data[codeLicense]['Repositories']['count']))

code = []
for codeLicense in codeLicenses:
	code.append(int(data[codeLicense]['Code']['count']))


createPieGraph(name='Code of Open Source Licenses', 
				labels=codeLicenses,
				sizes=code,
				title='Code of Open Source Licenses')

createHorizontalDoubleBarGraph( name='(Repositories & Code) vs Open Source Code Licenses', 
								x=codeLicenses, 
								y2=repositories, 
								y1=code, 
								y2_axis="Repositories Count", 
								y1_axis="Code Count", 
								title='(Repositories & Code) vs Open Source Code Licenses')

repositories = []
for codeLicense in nonCodeLicenses:
	repositories.append(int(data[codeLicense]['Repositories']['count']))

code = []
for codeLicense in nonCodeLicenses:
	code.append(int(data[codeLicense]['Code']['count']))

createHorizontalDoubleBarGraph( name='(Repositories & Code) vs General Open Source Licenses', 
								x=nonCodeLicenses, 
								y2=repositories, 
								y1=code, 
								y2_axis="Repositories Count", 
								y1_axis="Code Count", 
								title='(Repositories & Code) vs General Open Source Licenses')

createPieGraph(name='Code of General Open Source Licenses', 
				labels=nonCodeLicenses,
				sizes=code,
				title='Code of General Open Source Licenses')


repositories = []
for codeLicense in generalLicenseTerms:
	repositories.append(int(data[codeLicense]['Repositories']['count']))

code = []
for codeLicense in generalLicenseTerms:
	code.append(int(data[codeLicense]['Code']['count']))


createHorizontalDoubleBarGraph( name='(Repositories & Code) vs General Restriction Terms', 
								x=generalLicenseTerms, 
								y2=repositories, 
								y1=code, 
								y2_axis="Repositories Count", 
								y1_axis="Code Count", 
								title='(Repositories & Code) vs General Restriction Terms',
								angle = 45)


repositories = []
for codeLicense in confidential:
	repositories.append(int(data[codeLicense]['Repositories']['count']))

code = []
for codeLicense in confidential:
	code.append(int(data[codeLicense]['Code']['count']))


createHorizontalDoubleBarGraph( name='(Repositories & Code) vs Confidential Terms', 
								x=confidential, 
								y2=repositories, 
								y1=code, 
								y2_axis="Repositories Count", 
								y1_axis="Code Count", 
								title='(Repositories & Code) vs Confidential Terms',
								angle = 45)



allLicenses = sum([codeLicenses, nonCodeLicenses, generalLicenseTerms, confidential],[])
repositories = []
for codeLicense in allLicenses:
	repositories.append(int(data[codeLicense]['Repositories']['count']))

code = []
for codeLicense in allLicenses:
	code.append(int(data[codeLicense]['Code']['count']))

createHorizontalDoubleBarGraph( name='(Repositories & Code) vs All Terms', 
								x=allLicenses, 
								y2=repositories, 
								y1=code, 
								y2_axis="Repositories Count", 
								y1_axis="Code Count", 
								title='(Repositories & Code) vs All Terms',
								angle = 85)


df = pd.DataFrame({"Type": allLicenses, "Code" : code, "Repositories" : repositories})
df.to_csv("LicensesData.csv", index=False)


openSourceTermsCount = 0
openSourceLicenses = sum([codeLicenses, nonCodeLicenses],[])
for codeLicense in openSourceLicenses:
	openSourceTermsCount += int(data[codeLicense]['Code']['count'])
closedSourceTermsCount = 0
for codeLicense in confidential:
	closedSourceTermsCount += int(data[codeLicense]['Code']['count'])


createPieGraph(name='Open vs Closed Code File Licenses', 
				labels=['Open Source', 'Closed Source'],
				sizes=[openSourceTermsCount, closedSourceTermsCount],
				title='Open vs Closed Code File Licenses')


openSourceTermsCount = 0
openSourceLicenses = sum([codeLicenses, nonCodeLicenses],[])
for codeLicense in openSourceLicenses:
	openSourceTermsCount += int(data[codeLicense]['Repositories']['count'])
closedSourceTermsCount = 0
for codeLicense in confidential:
	closedSourceTermsCount += int(data[codeLicense]['Repositories']['count'])

createPieGraph(name='Open vs Closed Repository Licenses', 
				labels=['Open Source', 'Closed Source'],
				sizes=[openSourceTermsCount, closedSourceTermsCount],
				title='Open vs Closed Repository Licenses')

createPieGraph(name='With vs Without Modification Allowed', 
				labels=['Allow Modification', "Don't Allow Modification"],
				sizes=[62574024, 32289895],
				title='With vs Without Modification Allowed')



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