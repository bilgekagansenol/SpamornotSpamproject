# Spam Email Classification Using Word2Vec and SVM

This project focuses on building a supervised machine learning model to classify spam emails using a dataset containing 5,786 emails. The dataset is sourced from [Kaggle's Spam Email Dataset](https://www.kaggle.com/datasets/jackksoncsie/spam-email-dataset).

## Methodology

### 1. Data Preprocessing
- Tokenized and cleaned the email text to remove noise and irrelevant elements.
- Converted cleaned words into vector representations using the Word2Vec technique.

### 2. Feature Extraction
- Word vectors were averaged to represent entire emails as single vectors.
- Used varying `min_count` values in Word2Vec to analyze its effect on model performance.

### 3. Model Training
- Trained three different SVM models using the vectorized representations.
- Utilized the RBF kernel for non-linear classification.
- Applied Grid Search to optimize SVM hyperparameters for the best performance.

### 4. Results
- The best model achieved an accuracy of **97.81%**, showcasing the effectiveness of the approach.
- Results and vector lists are included in the repository for replication and further analysis.

## Directory Structure

- **Vector Lists**: Contains the generated Word2Vec vectors for experimentation.
- **Models**: Stores the trained SVM models and their evaluation metrics.

## Analysis and Findings

Below are the key insights from the experiments:

- The variation in `min_count` parameter affects the model's ability to generalize. Higher `min_count` values filter out less frequent words, impacting vector quality.
- Fine-tuning SVM parameters with the RBF kernel significantly improved performance, particularly when combined with high-quality vector inputs.

## Analysis Results
Best parameters: {'C': 10, 'gamma': 0.1}
Best cross-validation accuracy: 0.9777378293562167
Accuracy (Best RBF kernel): 0.974694589877836
Classification Report (Best RBF kernel):
               precision    recall  f1-score   support

           0       0.98      0.99      0.98       856
           1       0.96      0.94      0.95       290

    accuracy                           0.97      1146
   macro avg       0.97      0.96      0.97      1146
weighted avg       0.97      0.97      0.97      1146



Best parameters: {'C': 10, 'gamma': 0.1}
Best cross-validation accuracy: 0.9790466825084646
Accuracy (Best RBF kernel): 0.9764397905759162
Classification Report (Best RBF kernel):
               precision    recall  f1-score   support

           0       0.98      0.99      0.98       856
           1       0.97      0.94      0.95       290

    accuracy                           0.98      1146
   macro avg       0.97      0.96      0.97      1146
weighted avg       0.98      0.98      0.98      1146


Best parameters: {'C': 10, 'gamma': 0.1}
Best cross-validation accuracy: 0.9770828075221555
Accuracy (Best RBF kernel): 0.9781849912739965
Classification Report (Best RBF kernel):
               precision    recall  f1-score   support

           0       0.98      0.99      0.99       856
           1       0.97      0.94      0.96       290

    accuracy                           0.98      1146
   macro avg       0.98      0.96      0.97      1146
weighted avg       0.98      0.98      0.98      1146
