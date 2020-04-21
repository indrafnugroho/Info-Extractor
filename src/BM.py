# 13518016
# Indra Febrio Nugroho
# Boyer Moore Algorithm

def buildLastOccurence(pattern): 
	# length of pattern
	m = len(pattern)
	# Init all occurrence as -1 
	lastOcc = [-1 for i in range(128)] 

	# Fill the value of last occurrence to the array
	for i in range(m): 
		lastOcc[ord(pattern[i])] = i; 

	return lastOcc 

def BMMatch(text, pattern): 
	m = len(pattern) 
	n = len(text) 
	
	i = m - 1
	total = 0 # total matched pattern in the text
	matchedIdx = []

	lastOcc = buildLastOccurence(pattern) 

	if (i > n - 1) :
		# print("Pattern not found")
		return (-1)
	else :
		j = m - 1
		while (i <= n - 1):
			if (pattern[j] == text[i]):
				i -= 1
				j -= 1
				if (j == -1) :
					return (i+1)
					total += 1
					matchedIdx.append(i+1)
					j = m - 1
					i += 2*m
			else :
				lo = lastOcc[ord(text[i])]
				i += m - min(j, 1+lo)
				j = m - 1

	if (total == 0):
		# print("Pattern not found")
		return (-1)
	# else :
		# print("Total mathed pattern in the text: ", str(total))
		# print("Matched at index: ", end="")
		# print(matchedIdx)
	

def main(): 
	txt = "ABAAABCD"
	pat = "AX"
	BMMatch(txt, pat) 

main()
