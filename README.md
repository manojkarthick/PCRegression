# PCRegression
Python package to build principal components regression models using the scikit-learn library. This package follows the same principles as the scikit-learn API and exposes similar `fit` and `predict` methods.

View it on PyPI at: https://pypi.org/project/PCRegression/

### Installation
This tool has been built with python3. Install from PyPI using pip.

```shell
# If Python3 is your default python, use
$ pip install git-trend

# If Python 3.x is not your primary version of python, then use
$ pip3 install git-trend 
```
**NOTE**:   You can check your python version using `python -V`.

### Examples

General fit and predict API:

```python

X_train, X_test , y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=1)
pcr = PCR(n_components = 7)
pcr.fit(scale(X_train), y_train) # Scale your predictors for best results.
predictions = pcr.predict(scale(X_test))
```
K-Fold Cross validation using PCR:

```python
from sklearn.model_selection import KFold, cross_val_score
pcr = PCR(n_components=7)

kf_10 = KFold( n_splits=10, shuffle=True, random_state=1)

pcr.fit(scale(X_train), y_train)
X_reduced_train = pcr.get_transformed_data()
regr = pcr.get_regression_model()
n = len(X_reduced_train)

mse = list()

score = -1*cross_val_score(regr, np.ones((n,1)), y_train.ravel(), cv=kf_10, scoring='neg_mean_squared_error').mean()    
mse.append(score)

for i in np.arange(1, n):
    score = -1*cross_val_score(regr, X_reduced_train[:,:i], y_train.ravel(), cv=kf_10, scoring='neg_mean_squared_error').mean()
    mse.append(score)

print(mse)
```

### Important Parameters

* `n_components` : Number of components to keep.
* `copy` : Keep a copy of the data passed to the fit method()
* `random_state` : The seed used by the random number generator
* `fit_intercept` : Whether to calculate the intercept for this model
* `normalize` : If True, the regressors X will be normalized before regression.


### Requirements
1. scikit-learn >= 0.13.3
2. numpy >= 1.8.2
