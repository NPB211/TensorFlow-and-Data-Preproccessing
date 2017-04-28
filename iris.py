from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Loading Data
iris = load_iris()
X = iris.data[:, [0, 3]] # sepal length and petal width
y = iris.target

# standardize
X[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
X[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()

lr = LogisticRegression()
lr.fit(X, y)

# you could also use tensorflow for a more complex classification
