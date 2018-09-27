import os
import sys
import pickle

count_tough=0
count_easy=0
count_improvement=0
count_regression=0

with open(sys.argv[1],'rb') as f:
	gt_val = pickle.load(f)

with open(sys.argv[2],'rb') as f:
	val_pred_model_S=pickle.load(f).tolist()

with open(sys.argv[3],'rb') as f:
	val_pred_model_S_dash = pickle.load(f).tolist()

for i in range(len(gt_val)):
	if val_pred_model_S[i] == gt_val[i]:
		if val_pred_model_S_dash[i] == gt_val[i]:
			count_easy+=1
		if val_pred_model_S_dash[i] != gt_val[i]:
			count_regression+=1
	else:
		if val_pred_model_S_dash[i] == gt_val[i]:
			count_improvement+=1
		if val_pred_model_S_dash[i] != gt_val[i]:
			count_tough+=1
print "Count Easy"
print (count_easy)
print "Count Tough"
print (count_tough)
print "Count Improvement"
print (count_improvement)
print "Count Regression"
print (count_regression)

