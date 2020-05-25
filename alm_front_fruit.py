from collections import Counter
import re
import pandas as pd
import pymysql
from konlpy.tag import Mecab
keyword = '대추'
channel = 'Naver Blog'
stdate = '2010-01-01'
endate = '2020-05-21'
nurl = 15000

nlp = Mecab()
conn = pymysql.connect(host='106.246.169.202', user='root', password='robot369',
                    db='crawl', charset='utf8mb4')
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "select * from htdocs where keyword=\'%s\' and channel=\'%s\' and publishtime>=\'%s\' and publishtime<=\'%s\' limit %s"\
      %(keyword,channel,stdate, endate,nurl)
print(sql)
curs.execute(sql)
rows = curs.fetchall()
text = ''
tnqkr_list=[]
for row in rows:
    text = row['htmltext']
    text = re.sub(u"(http[^ ]*)", " ", text)
    text = re.sub(u"@(.)*", " ", text)
    text = re.sub(u"#", "", text)
    text = re.sub(u"\\d+", " ", text)
    text = re.sub(u"[^가-힣A-Za-z]", " ", text)
    text = re.sub(u"\\s+", " ", text)
    text = text.replace(keyword,' '+keyword)
    text = text.replace("  "," ")
    text = nlp.pos(text)
    tnqkr_list.extend(text)
print(text)
# get_loc = lambda str : [x.replace("[","").replace(":LOC","") for x in re.findall('\\[[\\w]+:LOC',str)]
front_list = []
for i,word in enumerate(tnqkr_list):
    if i!=0 and word[0]==keyword:
        for x in range(0,5):
            if tnqkr_list[i-x][1] =='VA' or tnqkr_list[i-x][1] == 'IC' or tnqkr_list[i-x][1]=='NNG' or tnqkr_list[i-x][1]=='NNP':
                front_list.append(tnqkr_list[i-x])

count = Counter(front_list)
dict = count
pd_list=[]
for i in dict.keys():
    if i[0]!=keyword and len(i[0])>1:
        pd_dic = {'keyword' : i[0], 'morphs' :i[1], 'count': dict[i]}
        pd_list.append(pd_dic)

print(pd_list)
pd = pd.DataFrame(pd_list,columns=('keyword','morphs','count'))
pd.to_excel('loc_count/front_'+keyword+'.xlsx', encoding='utf-8',index=True)
#
# from konlpy.tag import Mecab
# m = Mecab()
# m = m.pos('맛있는 수박')
# print(m)