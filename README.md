# Fraud Detection 
An end-to-end MLOps for Fraud Detection.

## 1. Project Scope
- Problem Statement: Develop a machine learning system to detect fraudulent mobile money transactions in a real-time environment.
- Data Sources: See **2. Dataset**
- Metric Selection: Given the nature of mobile money transactions and the goal of detecting fraudulent activities, the following metrics are important:
    - Precision: Out of the transactions flagged as fraudulent, what proportion are truly fraudulent? High precision is crucial to avoid false accusations and inconvenience to users.
    - Recall (Sensitivity): Among all the actual fraudulent transactions, what proportion did the model correctly detect? High recall ensures that most fraudulent activities are captured.
    - F1-Score: The balance between precision and recall is important. F1-Score is especially relevant when there is an imbalance between genuine and fraudulent transactions.
    - Area Under the ROC Curve (AUC-ROC): Given the real-time nature of the problem, a solid ROC curve analysis will help you understand the trade-offs between true positive rate and false positive rate at different threshold levels.
    - Area Under the Precision-Recall Curve (AUC-PR): Since fraud detection often involves imbalanced data, AUC-PR is a valuable metric, as it focuses more on the performance of the positive class.

## 2. Dataset
Paysim synthetic dataset of mobile money transactions. Each step represents an hour of simulation. This dataset is scaled down 1/4 of the original dataset which is presented in the paper "PaySim: A financial mobile money simulator for fraud detection".

Overview:
- step: Maps a unit of time in the real world. In this case 1 step is 1 hour of time.
- type: CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER.
- amount: amount of the transaction in local currency.
- nameOrig: customer who started the transaction.
- oldbalanceOrig: initial balance before the transaction.
- newbalanceOrig: customer's balance after the transaction.
- nameDest: recipient ID of the transaction.
- oldbalanceDest: initial recipient balance before the transaction.
- newbalanceDest: recipient's balance after the transaction.
- isFraud: identifies a fraudulent transaction (1) and non fraudulent (0)
- isFlaggedFraud: flags illegal attempts to transfer more than 200.000 in a single transaction.

See more detail at [Synthetic Financial Datasets For Fraud Detection](https://www.kaggle.com/datasets/ealaxi/paysim1).


## Reference
- E. A. Lopez-Rojas , A. Elmir, and S. Axelsson. "PaySim: A financial mobile money simulator for fraud detection". In: The 28th European Modeling and Simulation Symposium-EMSS, Larnaca, Cyprus. 2016

