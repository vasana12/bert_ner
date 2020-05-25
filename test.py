from transformers import *
from tokenization_kobert import KoBertTokenizer

model = BertModel.from_pretrained('monologg/kobert')
tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert')

s = tokenizer.tokenize('마지막으로 수박 위에 깨를 솔솔 뿌려 주었더니 더욱더 맛난 [수박나물:CVL-B] 완성! 따끈한 밥위에 [수박나물무침:CVL-B] 하나 올려서 먹음 그 식감과 함께 ')
print(s)

from konlpy.tag import Mecab

m = Mecab()
m.pos('경상북도')