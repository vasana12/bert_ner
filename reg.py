import re


get_loc = lambda str : [x.replace("[","").replace(":LOC","") for x in re.findall('\\[[\\w]+:LOC',str)]
