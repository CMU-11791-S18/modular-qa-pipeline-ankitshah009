from Classifier import Classifier
from sklearn.neural_network import MLPClassifier

class MLP(Classifier):
    def buildClassifier(self,X_features,Y_features):
    	clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1).fit(X_features,Y_features)
        #clf= svm.SVC(kernel='linear').fit(X_features,Y_features)
        #clf= svm.SVC(kernel='rbf').fit(X_features,Y_features)
        return clf
