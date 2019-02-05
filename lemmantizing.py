#lemmantizing same as real world
 
#              lemmatizing is silmarly operation like streaming change in end result of lemmantizing in same word 

from nltk.stem import WordNetLemmatizer

lemmantizer = WordNetLemmatizer()

print(lemmantizer.lemmatize('cats'))
print(lemmantizer.lemmatize('cacti'))
print(lemmantizer.lemmatize('geese'))
print(lemmantizer.lemmatize('rocks'))
print(lemmantizer.lemmatize('python'))


print(lemmantizer.lemmatize('better', pos = "a"))
print(lemmantizer.lemmatize('best', pos = "a"))
print(lemmantizer.lemmatize('run'))
print(lemmantizer.lemmatize('run', pos = "v"))