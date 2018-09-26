#!/bin/bash
python quasar_pipeline.py quasar-s_train_formatted.json quasar-s_dev_formatted.json SVMtfidf
mv Y_val_pred.txt Y_val_pred_SVMtfidf.txt
mv Y_val_true.txt Y_val_true_SVMtfidf.txt
