from collections import Counter
import re
import pandas as pd
get_loc = lambda str : [x.replace("[","").replace(":LOC","") for x in re.findall('\\[[\\w]+:LOC',str)]
f = open('sample_pred_out.txt','r')
text = f.read()
x =get_loc(text)
count = Counter(x)
count
print(count)