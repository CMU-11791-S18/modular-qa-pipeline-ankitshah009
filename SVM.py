from Classifier import Classifier
from sklearn import svm

class SVM(Classifier):
    def buildClassifier(self,X_features,Y_features):
        clf= svm.LinearSVC(C=0.0003).fit(X_features,Y_features)
        #clf= svm.SVC(kernel='rbf').fit(X_features,Y_features)
        return clf
