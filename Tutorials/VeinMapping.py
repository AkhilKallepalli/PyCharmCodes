import sklearn
from sklearn import datasets
from PyQt5.QtWidgets import QApplication,QWidget

iris = datasets.load_iris()
digits = datasets.load_digits()

print(digits.data)
