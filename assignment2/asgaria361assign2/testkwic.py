from multiprocessing import Process

def lower_case_list(sent_list):
	new_list_to_sort = sent_list[:]
	for y in range(len(new_list_to_sort)):
		new_list_to_sort[y] = sent_list[y].lower()
	return new_list_to_sort 	


def list_pairs(split_lines_list, multi_pair_list):
	list_of_pairs =[]
	for j in range(len(split_lines_list)):
			for k in range(len(split_lines_list[j])):
				split_lines_list[j][k]= split_lines_list[j][k].translate(None, ".,!?:")

	for x in range(len(split_lines_list)):
		for y in range(len(split_lines_list[x])):
			for z in range(y+1, len(split_lines_list[x])):
				temporary_pair_list = [split_lines_list[x][y].lower(), split_lines_list[x][z].lower()]
				temporary_pair_list.sort()
				list_of_pairs.append(temporary_pair_list)
				

	pairs_used = []

	for e in range(len(list_of_pairs)):
		if list_of_pairs.count(list_of_pairs[e]) > 1 and list_of_pairs[e] not in pairs_used:
			multi_pair_list.append(((list_of_pairs[e][0].lower(), list_of_pairs[e][1].lower()), list_of_pairs.count(list_of_pairs[e])))
			pairs_used.append(list_of_pairs[e])
	multi_pair_list.sort()


	return multi_pair_list 

def circular_shifts(split_lines_list, ignoreWords):
	temporary_tuple_list = []
	for x in range(len(split_lines_list)):
		temporary_list = split_lines_list[x][:]
		for a in range (len(temporary_list)):
			for b in range (len(temporary_list)):		
				temporary_list[b] = split_lines_list[x][(a+b) % len(split_lines_list[x])] 
			temporary_tuple = (temporary_list[:], x )
			if ignoreWords:
				if temporary_tuple[0][0] not in ignoreWords:
					temporary_tuple_list.append(temporary_tuple)
			else:
				temporary_tuple_list.append(temporary_tuple)
	
	temporary_tuple_list= sorted(temporary_tuple_list, key=lambda j:lower_case_list(j[0]))

	return temporary_tuple_list

def kwic(myWords, ignoreWords=None, listPairs=False, periodsToBreaks=False):
	
	split_lines_list = []
	multi_pairs_list = []
	list_pairs_final = []
	start_ind = 0
	tuple_list = []
	if myWords == "":
		return []
	else:
	
		if(periodsToBreaks):
			for i in range ((len(myWords)) -1 ):
				if myWords[i] == '.' and i>0 and myWords[i-1] in [chr(t) for t in range (97, 123)] and myWords[i+1] == " ":
					split_lines_list.append(myWords[start_ind:i].split())
					start_ind = i+1
			split_lines_list.append(myWords[start_ind:].split())
		else:		
			split_lines_list=myWords.split('\n')
			split_lines_list=map(lambda l: l.split(), split_lines_list)
	

		if(listPairs):
			list_pairs_final = list_pairs(split_lines_list, multi_pairs_list)

		tuple_list = circular_shifts(split_lines_list, ignoreWords)

		if(listPairs):
			return (tuple_list, list_pairs_final)
		else:			 
			return tuple_list

	
