import re
k,k2,s = {'SKH': 'C', 'SHK':'C', 'HSK':'C', 'HKS':'C', 'KHS':'C', 'KSH':'C'}, {'R':'S', 'B':'K', 'L':'H'}, input()
print(re.compile('|'.join(k.keys())).sub(lambda x: k[x.group()], ''.join([k2[i] for i in s])))