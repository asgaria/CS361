#sorted listpairs
def lower_case_list(sent_list):
	new_list_to_sort = sent_list[:]
	for y in range(len(new_list_to_sort)):
		new_list_to_sort[y] = sent_list[y].lower()
	return new_list_to_sort 	
			

def kwic(myWords, ignoreWords=None, listPairs=False, periodsToBreaks=False):
	
	if myWords == "":
		return []
	else:
	
		if(periodsToBreaks):
			cur_index = 0
			split_lines_list = []
			for i in range ((len(myWords))):
				if myWords[i] == '.':
					if myWords[i-1].islower() and myWords[i+1] == " ":
						split_lines_list.append(myWords[cur_index:i+1].split())
						cur_index = i + 1
			split_lines_list.append(myWords[cur_index:len(myWords)].split())				
		else:		
			split_lines_list = myWords.split('\n')
	
				
		temporary_tuple_list  = []
		time_to_split = split_lines_list[:]

		for x in range(len(split_lines_list)):
			if(periodsToBreaks == False):
				time_to_split[x] = split_lines_list[x].split()
			temporary_list = time_to_split[x][:]
			for a in range (len(time_to_split[x])):
					for b in range (len(time_to_split[x])):		
						temporary_list[b] = time_to_split[x][(a+b) % len(time_to_split[x])] 
					
					temporary_tuple = (temporary_list[:], x )
					if ignoreWords:
						if temporary_tuple[0][0] not in ignoreWords:
							temporary_tuple_list.append(temporary_tuple)
					else:
						temporary_tuple_list.append(temporary_tuple)
	
	 	temporary_tuple_list= sorted(temporary_tuple_list, key=lambda j:lower_case_list(j[0]))

		if(listPairs):
			list_of_pairs = []
			for j in range(len(split_lines_list)):
				for k in range(len(split_lines_list[j])):
					split_lines_list[j][k]= split_lines_list[j][k].translate(None, ".,!?:") 

			for x in range(len(split_lines_list)):
				for y in range(len(split_lines_list[x])):
					for z in range(y+1, len(split_lines_list[x])):
						temporary_pair_list = [split_lines_list[x][y], split_lines_list[x][z]]
						temporary_pair_list.sort()
						list_of_pairs.append(temporary_pair_list)

			multi_pair_list = []
			pairs_used = []

	
			for i in range(len(list_of_pairs)):
				if list_of_pairs.count(list_of_pairs[i]) > 1 and list_of_pairs[i] not in pairs_used:
					multi_pair_list.append(((list_of_pairs[i][0].lower(), list_of_pairs[i][1].lower()), list_of_pairs.count(list_of_pairs[i])))
					pairs_used.append(list_of_pairs[i])
			multi_pair_list.sort()
			return (temporary_tuple_list, multi_pair_list)
		else:			 
			return temporary_tuple_list

	
