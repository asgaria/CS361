import eventspec


class Kwic:
	
	def __init__(self, periodsToBreaks=False, ignoreWords=None):
		self.es = eventspec.EventSpec("kwic.fsm")
		self.es.event("callConstructor")
		self.periods_breaks = periodsToBreaks
		self.ignore_words = ignoreWords
		self.words = ""
		self.line_count = 0
	def addText(self, new_text):
		self.es.event("callAddText")
		self.words += new_text

	def reset(self):
		self.es.event("callReset")
		self.words = ""

	def lower_case_list(self, sent_list):
		new_list_to_sort = sent_list[:]
		for y in range(len(new_list_to_sort)):
			new_list_to_sort[y] = sent_list[y].lower()
		return new_list_to_sort 	



	def split_the_lines(self):
		start_ind = 0
		split_lines_list = []

		if self.words == "":
			return []
		else:	
			if(self.periods_breaks):
				for i in range ((len(self.words)) -1 ):
					if self.words[i] == '.' and i>0 and self.words[i-1] in [chr(t) for t in range (97, 123)] and self.words[i+1] == " ":
						split_lines_list.append(self.words[start_ind:i+1].split())
						start_ind = i+1
				split_lines_list.append(self.words[start_ind:].split())
			else:		
				split_lines_list=self.words.split('\n')
				split_lines_list=map(lambda l: l.split(), split_lines_list)
		return split_lines_list

	def index(self):
		self.es.event("callIndex")
		split_lines_list = self.split_the_lines()	
		temporary_tuple_list = []
		temporary_list = []
		for x in range(len(split_lines_list)):
			temporary_list = split_lines_list[x][:]
			for a in range (len(temporary_list)):
				for b in range (len(temporary_list)):		
					temporary_list[b] = split_lines_list[x][(a+b) % len(split_lines_list[x])] 
				temporary_tuple = (temporary_list[:], x )
				self.line_count = x
				if self.ignore_words:
					if temporary_tuple[0][0].translate(None, ".,!?") not in self.ignore_words:
						temporary_tuple_list.append(temporary_tuple)
				else:
					temporary_tuple_list.append(temporary_tuple)
	
		temporary_tuple_list= sorted(temporary_tuple_list, key=lambda j:self.lower_case_list(j[0]))

		return temporary_tuple_list

	def listPairs(self):
		self.es.event("callListPairs")
		split_lines_list = self.split_the_lines()
		split_list = []
		multi_pair_list = []
		if(self.line_count == 0):
			return multi_pair_list

		for j in range(len(split_lines_list)):
			split_list.append(split_lines_list[j][:])
			for k in range(len(split_lines_list[j])):
				split_list[j][k]= split_lines_list[j][k].translate(None, ".,?!:")
			while "" in split_list[j]:
				split_list[j].remove("")

		pairs_used = []
		list_of_pairs = []


		for x in range(len(split_list)):
			for y in range(len(split_list[x])):
				for z in range(y+1, len(split_list[x])):
					temporary_pair_list = [split_list[x][y].lower(), split_list[x][z].lower()]
					temporary_pair_list.sort()
					list_of_pairs.append(temporary_pair_list)
				
		for e in range(len(list_of_pairs)):
			if list_of_pairs.count(list_of_pairs[e]) > 1 and list_of_pairs[e] not in pairs_used:
				if(list_of_pairs[e][0].lower() != list_of_pairs[e][1].lower()):	
					multi_pair_list.append(((list_of_pairs[e][0].lower(), list_of_pairs[e][1].lower()), list_of_pairs.count(list_of_pairs[e])))
					pairs_used.append(list_of_pairs[e])
					multi_pair_list.sort()


		return multi_pair_list 
			


				

