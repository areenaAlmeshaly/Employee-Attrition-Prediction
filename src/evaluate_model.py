
from sklearn.metrics import (classification_report,confusion_matrix,accuracy_score,precision_score,recall_score,f1_score)

def evaluate_model(y_test, probs, threshold=0.35):

    preds = (probs >= threshold).astype(int)

    print("Classification Report:\n")
    print(classification_report(y_test, preds, zero_division=0))

    print("Confusion Matrix:\n")
    print(confusion_matrix(y_test, preds))
    
    metrics = {
    "accuracy": accuracy_score(y_test, preds),
    "precision": precision_score(y_test, preds, zero_division=0),
    "recall": recall_score(y_test, preds, zero_division=0),
    "f1": f1_score(y_test, preds, zero_division=0)}
    
    return metrics, preds