#naive_bayes


import nltk
import random
from nltk.corpus import movie_reviews 
import pickle

 
documents = [(list(movie_reviews.words(fileid)), category)
			  for category in movie_reviews.categories()
			  for fileid in movie_reviews.fileids(category)]


#documents = []


#for category in movie_reviews.categories():
#	for fileid in movie_reviews.fileids(category):
#		documents.append(list(movie_reviews(fileid)), category)


random.shuffle(documents)

#print(documents[1])

all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def find_features(document):
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

#  posterior = prior occcurences * liklihood / edvidence

#classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Naive Bayes Algo accuracy:", (nltk.classify.accuracy(classifier, testing_set)))
classifier.show_most_informative_features(15)

#save_classifier = open("naivebayes.pickle", "wb")
#pickle.dump(classifier, save_classifier)
#save_classifier.close()