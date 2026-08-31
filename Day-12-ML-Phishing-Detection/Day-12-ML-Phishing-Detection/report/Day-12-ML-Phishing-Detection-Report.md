# Day 12 Report

## Objective
Train a basic text classifier for phishing-email detection.

## Dataset
50 synthetic samples: 25 phishing-like and 25 legitimate-like messages.

## Model
CountVectorizer + Multinomial Naive Bayes.

## Results
Use the actual measured accuracy and confusion matrix from output/metrics.txt. Do not claim a target accuracy unless the test produces it.

## Limitations
A small synthetic dataset is not representative of real mail traffic; model performance can change significantly with data quality and drift.
