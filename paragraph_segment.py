import glob
import numpy as np
import pandas as pd
import pickle
import re
import random

### Collect all results
results = []

##############################################################################
#                                                                            #
#                      STATE DEPARTMENT PREPROCESSOR                         #
#                                                                            #
##############################################################################

sd_header_delimiter = '[0-10000]##[a-z0-9]\.|[0-10000]##Section\ [0-9]\.'
url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
# Open all text files for the source
sd_files = glob.glob("human_right_text_files/*_State_Department.txt")
for file in sd_files:
	with open(file, errors = 'ignore') as f:
		lines = f.read().splitlines()
	indexes = []
	line_lengths = np.array([len(line) for line in lines if len(line) > 0])
	pct = np.percentile(line_lengths, 50) # arbitratily picked, not tuned
	for i, line in enumerate(lines):
		indexes.append(i)
		if len(re.findall(url_pattern, line)) > 0:
			continue
		if len(re.findall(sd_header_delimiter, line)) > 0:
			print(line)
			print(file)
			continue
		if len(line) < pct and '.' not in line:
			continue
		else:
			results.append({
				'source' : "SD",
				'file' : file,
				'indexes' : indexes,
				'paragraph' : line
			})
			indexes = []

##############################################################################
#                                                                            #
#                     AMNESTY INTERNATIONAL PREPROCESSOR                     #
#                                                                            #
##############################################################################

# Open all text files for the source
ai_files = glob.glob("human_right_text_files/*_Amnesty_International.txt")
for file in ai_files:
	with open(file, errors = 'ignore') as f:
		lines = f.read().splitlines()
	line_lengths = np.array([len(line) for line in lines if len(line) > 0])
	pct = np.percentile(line_lengths, 30) # arbitratily picked, not tuned
	indexes = []
	for i, line in enumerate(lines):
		indexes.append(i)
		if len(re.findall(url_pattern, line)) > 0:
			print(line)
			continue
		if len(line) < pct and '.' not in line:
			continue
		else:
			results.append({
				'source' : "AI",
				'file' : file,
				'indexes' : indexes,
				'paragraph' : line
			})
			indexes = []

##############################################################################
#                                                                            #
#                      HUMAN RIGHTS WATCH PREPROCESSOR                       #
#                                                                            #
##############################################################################

def percent_title_case(line):
	words = line.split()
	return np.average([int(w[0].isupper()) for w in words])

# Open all text files for the source
hrw_files = glob.glob("human_right_text_files/*_Human_Rights_Watch.txt")
for file in hrw_files:
	paragraphs = []
	with open(file, errors = 'ignore') as f:
		lines = f.read().splitlines()
	line_lengths = np.array([len(line) for line in lines if len(line) > 0])
	pct = np.percentile(line_lengths, 30) # arbitratily picked, not tuned
	paragraph = ''
	indexes = []
	for i, line in enumerate(lines):
		indexes.append(i)
		if len(re.findall(url_pattern, line)) > 0:
			print(line)
			continue
		if len(line) < pct and '.' not in line and percent_title_case(line) > .6:
			continue
		else:
			if line[-1] == '.':
				paragraph += ' %s' % line
				paragraphs.append(paragraph)
				results.append({
					'source' : "HRW",
					'file' : file,
					'indexes' : indexes,
					'paragraph' : paragraph
				})
				indexes = []
				paragraph = ''
			else:
				paragraph += ' %s' % line

data = pd.DataFrame(results)
data.to_csv('research_data.csv', index=False)