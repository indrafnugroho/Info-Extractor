# 13518016
# Indra Febrio Nugroho
# Regex

import re
from nltk import sent_tokenize
from BM import buildLastOccurence, BMMatch
from KMP import KMPMatch, calculateLPS

file = open('../test/1.txt', 'r')
text = file.read()
arrOfWords = sent_tokenize(text)

for words in arrOfWords:
	if (KMPMatch(words.lower(), 'positif') > 0):
		print(words)
		print("Check")
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

		print("")