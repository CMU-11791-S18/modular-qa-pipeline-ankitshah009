from Classifier import Classifier
from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier

class SVM(Classifier):
    def buildClassifier(self,X_features,Y_features):
        #clf= OneVsRestClassifier(svm.LinearSVC(C=0.0003),n_jobs=20)
	clf=svm.LinearSVC(C=0.0004).fit(X_features,Y_features)
        #clf= svm.SVC(kernel='rbf').fit(X_features,Y_features)
        return clf
