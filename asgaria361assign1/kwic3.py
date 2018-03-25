#sorts the tuple list
def kwic(myWords, ignoreWords=None, listPairs=False, periodsToBreaks=False):
	
	if myWords == "":
		return []
	else:
		time_to_split    = myWords.split()
		temporary_list   = time_to_split[:]
		temporary_tuple_list  = []
	
		for a in range (len(time_to_split)):
			for b in range (len(time_to_split)):
				temporary_list[b] = time_to_split[(a+b) % (len(time_to_split))] 
				
			temporary_tuple = (temporary_list[:], 0)
			temporary_tuple_list.append(temporary_tuple)
	
 		temporary_tuple_list.sort()
		return temporary_tuple_list
