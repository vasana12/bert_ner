import pymysql
import re
import kss
from konlpy.tag import Mecab

keyword = '수박'
channel = 'Naver Blog'
stdate = '2010-01-01'
endate = '2020-05-22'
nurl = 15000

conn = pymysql.connect(host='106.246.169.202', user='root', password='robot369',
                    db='crawl', charset='utf8mb4')
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "select * from htdocs where keyword=\'%s\' and channel=\'%s\' and publishtime>=\'%s\' and publishtime<=\'%s\' limit %s"\
      %(keyword,channel,stdate, endate,nurl)
print(sql)
curs.execute(sql)
rows = curs.fetchall()

text = ''

lines = []
new_line = []
nlp = Mecab()
for row in rows:
    text += row['htmltext']
text = text.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣]","")
text = re.sub(u"\\d+", " ", text)
text = re.sub(u"\\s+", " ", text)
text = text.replace(keyword,' '+keyword)
text = text.replace("  "," ")
lines = kss.split_sentences(text)

for line in lines:
    line = str(nlp.nouns(line))
    line = line.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣]','')
    line = re.sub(u"(http[^ ]*)", " ", line)
    line= re.sub(u"@(.)*", " ", line)
    line = re.sub(u"#", "", line)
    line = re.sub(u"\\d+", " ", line)
    line = re.sub(u"[^가-힣A-Za-z]", " ", line)
    line = re.sub(u"\\s+", " ", line)
    new_line.append(line)


print(new_line)
for line in new_line:

    with open('sample_pred_in_'+keyword+'.txt', "a", encoding="utf-8") as f:
        f.write(line+'\n')
