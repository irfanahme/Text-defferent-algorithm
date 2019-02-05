# streaming in nltk
# streaning use  to remove the same words in differnce form bcz
# they contain space in database

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
examper_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]


#for w in examper_words:
#	print(ps.stem(w))
new_text = "it is very important to be pythonly while you are pythoning with python. All pythoner have pythoned poorly at least once."
words =  word_tokenize(new_text)


for w in words:
	print(ps.stem(w))