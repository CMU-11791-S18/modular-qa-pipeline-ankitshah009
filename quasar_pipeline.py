import sys
import json
from sklearn.externals import joblib

from Retrieval import Retrieval
from Featurizer import Featurizer
from CountFeaturizer import CountFeaturizer
from TfidfFeaturizer import TfidfFeaturizer
from Classifier import Classifier
from MultinomialNaiveBayes import MultinomialNaiveBayes
from Evaluator import Evaluator
from SVM import SVM
from MLP import MLP
import numpy as np
import pickle


class Pipeline(object):
	def __init__(self, trainFilePath, valFilePath, retrievalInstance, featurizerInstance, classifierInstance):
		self.retrievalInstance = retrievalInstance
		self.featurizerInstance = featurizerInstance
		self.classifierInstance = classifierInstance
		trainfile = open(trainFilePath, 'r')
		self.trainData = json.load(trainfile)
		trainfile.close()
		valfile = open(valFilePath, 'r')
		self.valData = json.load(valfile)
		valfile.close()
		self.question_answering()

	def makeXY(self, dataQuestions):
		X = []
		Y = []
		for question in dataQuestions:
			
			long_snippets = self.retrievalInstance.getLongSnippets(question)
			short_snippets = self.retrievalInstance.getShortSnippets(question)
			
			X.append(short_snippets)
			Y.append(question['answers'][0])
			
		return X, Y


	def question_answering(self):
		dataset_type = self.trainData['origin']
		candidate_answers = self.trainData['candidates']
		X_train, Y_train = self.makeXY(self.trainData['questions'])
		X_val, Y_val_true = self.makeXY(self.valData['questions'])
		with open('Y_val_true.txt','wb') as f:
			pickle.dump(Y_val_true,f)

		#featurization
		X_features_train, X_features_val = self.featurizerInstance.getFeatureRepresentation(X_train, X_val)
		print np.shape(X_features_train), np.shape(X_features_val)
		self.clf = self.classifierInstance.buildClassifier(X_features_train, Y_train)
		
		#Prediction
		Y_val_pred = self.clf.predict(X_features_val)
		
		print Y_val_pred
		with open('Y_val_pred.txt','wb') as f:
			pickle.dump(Y_val_pred,f)

		self.evaluatorInstance = Evaluator()
		a =  self.evaluatorInstance.getAccuracy(Y_val_true, Y_val_pred)
		p,r,f = self.evaluatorInstance.getPRF(Y_val_true, Y_val_pred)
		print "Accuracy: " + str(a)
		print "Precision: " + str(p)
		print "Recall: " + str(r)
		print "F-measure: " + str(f)
		


if __name__ == '__main__':
	trainFilePath = sys.argv[1] #please give the path to your reformatted quasar-s json train file
	valFilePath = sys.argv[2] # provide the path to val file
	retrievalInstance = Retrieval()
	if sys.argv[3] == "NBcount":
		print "Naive Bayes and count features"
		classifierInstance = MultinomialNaiveBayes()
		featurizerInstance = CountFeaturizer()
		trainInstance = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance, classifierInstance)
	if sys.argv[3] == "NBtfidf":
		print "Naive Bayes and TFIDF features"
		classifierInstance = MultinomialNaiveBayes()
		featurizerInstance = TfidfFeaturizer()
		trainInstance = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance, classifierInstance)
	elif sys.argv[3] == "SVMcount":
		print "SVM and Count features"
		classifierInstance = SVM()
		featurizerInstance = CountFeaturizer()
		trainInstance = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance, classifierInstance)
	elif sys.argv[3] == "SVMtfidf":
		print "SVM and TfIDF features"
		classifierInstance = SVM()
		featurizerInstance = TfidfFeaturizer()
		trainInstance = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance, classifierInstance)
	elif sys.argv[3] == "MLPcount":
		print "MLP and Count features"
		classifierInstance = MLP()
		featurizerInstance = CountFeaturizer()
		trainInstance = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance, classifierInstance)
	elif sys.argv[3] == "MLPtfidf":
		print "MLP and TfIDF features"
		classifierInstance = MLP()
		featurizerInstance = TfidfFeaturizer()
		trainInstance = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance, classifierInstance)
