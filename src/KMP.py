# 13518016
# Indra Febrio Nugroho
# Knuth-Morris-Pratt Algorithm

def KMPMatch(text, pattern): 
	m = len(pattern) 
	n = len(text) 

	# create container that will hold the longest prefix suffix values for pattern 
	lps = [0 for i in range(m)]
	# calculate the lps
	calculateLPS(pattern, lps) 

	total = 0 # total matched pattern in the text
	matchedIdx = [] # container for index of matched pattern in the text
	i = 0 # index for text
	j = 0 # index for pattern 
	while i < n: 
		if (pattern[j] == text[i]): 
			i += 1
			j += 1
			if (j == m): 
				return (i-j)
				matchedIdx.append(i-j)
				total += 1
				j = lps[j-1] 
		elif (j > 0): 
			j = lps[j-1] 
		else: 
			i += 1

	# if (total > 0) :
		# print("Total matched pattern in the text: ", str(total))
		# print("Matched at index: ", end="")
		# print(matchedIdx)
	if (total == 0):
		# print("Pattern not found")
		return (-1)


def calculateLPS(pattern, lps): 
	m = len(pattern)

	i = 1
	j = 0 # length of the previous longest prefix suffix 

	while (i < m): 
		if (pattern[i]== pattern[j]): 
			lps[i] = j + 1
			i += 1
			j += 1
		elif (j > 0): 
			j = lps[j-1] 
		else: 
			lps[i] = 0
			i += 1

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
KMPMatch(text, pattern)