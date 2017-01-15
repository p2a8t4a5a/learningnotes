#librarys
1.NumPy
multidimensional array (ndarray)
pip install NumPy (pandas,matplotlib,IPython,SciPy)


#charpter 2
import json
path='ch02/...'
records=[json.loads(line) for line in open(path)]
time_zones=[rec['tz'] for rec in records if 'tz' in rec]
from collections import defaultdict
def get_counts(seq):
	counts=defaultdict(int)
	for x in seq:
		counts[x]+=1
	return counts
from collections import Counter
counts=Counter(time_zones)
counts.most_common(10)
#mark 23 huatu shibai
	
	


