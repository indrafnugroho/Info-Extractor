# 13518016
# Indra Febrio Nugroho
# Regex and Extractor

import re
import copy
from nltk import sent_tokenize
from BM import BMMatch
from KMP import KMPMatch

def RegexMatch(text, pattern):
	if (re.search(pattern, text)):
		return 1
	else:
		return -1

def algChooser(alg, text, keyword):
	idx = -1
	if (alg == "kmp"):
		idx = KMPMatch(text.lower(), keyword.lower())
	elif (alg == 'bm'):
		idx = BMMatch(text.lower(), keyword.lower())
	else:
		idx = RegexMatch(text.lower(), keyword.lower())
	return idx

def processFile(path, files, keyword, alg):
	listOfTotal = []
	listOfTime = []
	listOfWords = []
	listOfFiles = []
	for f in files:
		if (f.endswith(".txt")):
			file = open(path + f, 'r')
			text = file.read()
			reTime = re.compile(r'([A-Za-z]{4,6}\,? )?\(?\d{1,2}[\/\- ](\d{1,2}|[a-zA-Z]{3,})[\/\- ]?\d{2,4}\)?( (pukul )?\d{1,2}[\.\:]\d{1,2} ((WITA)|(WI[BT])))?')
			timeG = reTime.search(text)
			globalTime = timeG.group(0)
			arrOfWords = sent_tokenize(text)

			for words in arrOfWords:
				idx = algChooser(alg, words, keyword)
				if (idx > 0):
					reTotal = re.compile(r'(\d{1,3}(\.|\,))*\d{1,} (([Oo]rang)|([Pp]asien)|([OoPp]dp)|([Kk]asus))')
					totalRes = reTotal.search(words)
					reTime = re.compile(r'([A-Za-z]{4,6}\,? )?\(?\d{1,2}[\/\- ](\d{1,2}|[a-zA-Z]{3,})[\/\- ]?\d{2,4}\)?( (pukul )?\d{1,2}[\.\:]\d{1,2} ((WITA)|(WI[BT])))?')
					timeRes = reTime.search(words)

					if (totalRes and timeRes):
						w = totalRes.group().split(' ')
						listOfTotal.append(copy.deepcopy(w[0]))
						listOfTime.append(copy.deepcopy(timeRes.group()))
						listOfWords.append(copy.deepcopy(words))
						listOfFiles.append(copy.deepcopy(f))
				
					elif (totalRes):
						w = totalRes.group().split(' ')
						listOfTotal.append(copy.deepcopy(w[0]))
						listOfTime.append(copy.deepcopy(globalTime))
						listOfWords.append(copy.deepcopy(words))
						listOfFiles.append(copy.deepcopy(f))

	return listOfTotal, listOfTime, listOfWords, listOfFiles