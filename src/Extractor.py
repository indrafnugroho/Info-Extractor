# 13518016
# Indra Febrio Nugroho
# Regex

import re
import os
from nltk import sent_tokenize
from BM import buildLastOccurence, BMMatch
from KMP import KMPMatch, calculateLPS

def algChooser(alg, text, keyword):
	idx = -1
	if (alg == "Knuth-Morris-Pratt"):
		idx = KMPMatch(text.lower(), keyword.lower())
	elif (alg == 'Boyer Moore'):
		idx = BMMatch(text.lower(), keyword.lower())
	else:
		idx = RegexMatch(text.lower(), keyword.lower())
	return idx

def RegexMatch(text, pattern):
	if (re.search(pattern, text)):
		return 1
	else:
		return 0

path = "../test/"
files = os.listdir(path)
for f in files:
	if (f.endswith(".txt")):
		file = open(path + f, 'r')
		text = file.read()
		arrOfWords = sent_tokenize(text)

		for words in arrOfWords:
			if (KMPMatch(words.lower(), 'positif') > 0):
				print("Keyword(s): ", end="")
				print('positif')
				reTotal = re.compile(r'(\d{1,3}(\.|\,))*\d{1,} (([Oo]rang)|([Pp]asien)|([OoPp]dp)|([Kk]asus))')
				totalRes = reTotal.search(words)
				if (totalRes):
					print("Total: ", end="")
					print(totalRes.group())

				reTime = re.compile(r'([A-Za-z]{4,6}\,? )?\(?\d{1,2}[\/\- ](\d{1,2}|[a-zA-Z]{3,})[\/\- ]?\d{2,4}\)?( (pukul )?\d{1,2}[\.\:]\d{1,2} ((WITA)|(WI[BT])))?')
				timeRes = reTime.search(words)
				if (timeRes):
					print("Time: ", end="")
					print(timeRes.group())

				print(words, end=" ")
				print("(", f, ")")

				print("")