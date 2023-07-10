from sklearn.svm import SVC
from sklearn import metrics
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

print("Loading data...")

train_data = np.load('train_data.npy')
train_labels = np.load('train_labels.npy')
test_data = np.load('test_data.npy')
test_labels = np.load('test_labels.npy')


clf = SVC(kernel='rbf')
print("Running SVM...")
clf.fit(train_data, train_labels)

print("Predicting...")
# Predict the response for test dataset
y_pred = clf.predict(test_data)

print("Accuracy:",metrics.accuracy_score(test_labels, y_pred))
print("Precision:",metrics.precision_score(test_labels, y_pred, average='micro'))
print("Recall:",metrics.recall_score(test_labels, y_pred, average='micro'))
print("F1-score:",metrics.f1_score(test_labels, y_pred, average='micro'))

print(classification_report(test_labels, y_pred))
print(confusion_matrix(test_labels, y_pred))