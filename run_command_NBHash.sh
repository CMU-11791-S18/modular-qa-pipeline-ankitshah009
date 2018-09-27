#!/bin/bash
python quasar_pipeline.py quasar-s_train_formatted.json quasar-s_dev_formatted.json NBHash
mv Y_val_pred.txt Y_val_pred_NBHash.txt
mv Y_val_true.txt Y_val_true_NBHash.txt
