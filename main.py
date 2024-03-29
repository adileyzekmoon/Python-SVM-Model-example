import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics

# load up existing dataset in datasets library
cancer = datasets.load_breast_cancer()
print('Features: ', cancer.feature_names)
print("Labels: ", cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# print(x_train, y_train)

# build SVM model, using a linear kerel; most effective for this dataset
svm_model = svm.SVC(kernel="linear")
# train SVM model
svm_model.fit(x_train,y_train)

prediction = svm_model.predict(x_test)

acc = metrics.accuracy_score(y_test, prediction)
print(acc)