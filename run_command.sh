#!/bin/bash
python quasar_pipeline.py quasar-s_train_formatted.json quasar-s_dev_formatted.json NBcount
mv Y_val_pred.txt Y_val_pred_NBcount.txt
mv Y_val_true.txt Y_val_true_NBcount.txt
python quasar_pipeline.py quasar-s_train_formatted.json quasar-s_dev_formatted.json NBcount
mv Y_val_pred.txt Y_val_pred_NBcount.txt
mv Y_val_true.txt Y_val_true_NBcount.txt
python quasar_pipeline.py quasar-s_train_formatted.json quasar-s_dev_formatted.json SVMcount
mv Y_val_pred.txt Y_val_pred_SVMcount.txt
mv Y_val_true.txt Y_val_true_SVMcount.txt
python quasar_pipeline.py quasar-s_train_formatted.json quasar-s_dev_formatted.json SVMtfidf
mv Y_val_pred.txt Y_val_pred_SVMtfidf.txt
mv Y_val_true.txt Y_val_true_SVMtfidf.txt
python quasar_pipeline.py quasar-s_train_formatted.json quasar-s_dev_formatted.json MLPcount
mv Y_val_pred.txt Y_val_pred_MLPcount.txt
mv Y_val_true.txt Y_val_true_MLPcount.txt
python quasar_pipeline.py quasar-s_train_formatted.json quasar-s_dev_formatted.json MLPtfidf
mv Y_val_pred.txt Y_val_pred_MLPtfidf.txt
mv Y_val_true.txt Y_val_true_MLPtfidf.txt
