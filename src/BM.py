# 13518016
# Indra Febrio Nugroho
# Boyer Moore Algorithm

def BMMatch(text, pattern): 
	m = len(pattern) 
	n = len(text) 
	
	i = m - 1
	total = 0 # total matched pattern in the text
	matchedIdx = []

	lastOcc = buildLastOccurence(pattern) 

	if (i > n - 1) :
		return (-1)
	else :
		j = m - 1
		while (i <= n - 1):
			if (pattern[j] == text[i]):
				i -= 1
				j -= 1
				if (j == -1) :
					return (i+1)
					
			else :
				lo = lastOcc[ord(text[i])]
				i += m - min(j, 1+lo)
				j = m - 1

	if (total == 0):
		return (-1)

def buildLastOccurence(pattern): 
	# length of pattern
	m = len(pattern)
	# Init all occurrence as -1 
	lastOcc = [-1 for i in range(256)] 

	# Fill the value of last occurrence to the array
	for i in range(m): 
		lastOcc[ord(pattern[i])] = i; 

	return lastOcc 

def main(): 
	txt = "ABAAABCD"
	pat = "AX"
	BMMatch(txt, pat) 

if __name__ == "__main__" :
	main()
