from Featurizer import Featurizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB


#This is a subclass that extends the abstract class Featurizer.
class HashingVectorizer(Featurizer):

	#The abstract method from the base class is implemeted here to return hashing features
	# Got Idea to use this from sklearn documentation on vectorizer - feature extraction
	# http://scikit-learn.org/stable/modules/feature_extraction.html#nqy18
	# Vectorization scheme is simple and holds in memory mapping from string token to the integer feature indices - 
	# This scheme is useful for the larger corpus, larger vocabulary will grow in size and in memory usage as well. 
	def getFeatureRepresentation(self, X_train, X_val):
		hash_vect = HashingVectorizer()
		X_train_hashes = hash_vect.transform(X_train)
		X_val_hashes = hash_vect.transform(X_val)
		return X_train_hashes, X_val_hashes
