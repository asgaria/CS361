#returns the tuple of 1 line

def kwic(words, ignoreWords=None, listPairs=False, periodsToBreaks=False):
	if(words == ""):
		return []
	else:	
		return [([words], 0)]
