#!/bin/bash
python quasar_pipeline.py quasar-s_train_formatted.json quasar-s_dev_formatted.json NBtfidf
mv Y_val_pred.txt Y_val_pred_NBtfidf.txt
mv Y_val_true.txt Y_val_true_NBtfidf.txt
