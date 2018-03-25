#splits the list by new line characters

def kwic(myWords, ignoreWords=None, listPairs=False, periodsToBreaks=False):
	
	if myWords == "":
		return []
	else:
		split_lines_list = myWords.split('\n')
	
		
		temporary_tuple_list  = []
		time_to_split = split_lines_list[:]
		
		for x in range(len(split_lines_list)):
			time_to_split[x] = split_lines_list[x].split()
			temporary_list = time_to_split[x][:]
			for a in range (len(time_to_split[x])):
					for b in range (len(time_to_split[x])):		
						temporary_list[b] = time_to_split[x][(a+b) % len(time_to_split[x])] 
					
					temporary_tuple = (temporary_list[:], x )
					temporary_tuple_list.append(temporary_tuple)
	
	 	temporary_tuple_list.sort()
		return temporary_tuple_list
