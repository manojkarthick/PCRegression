from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.base import BaseEstimator
from sklearn.base import RegressorMixin
from sklearn.utils.validation import check_is_fitted
from sklearn.utils.validation import check_random_state
import copy


class PCR(BaseEstimator, RegressorMixin):

    def __init__(self, fit_intercept=True, copy_X=True, normalize=False, n_jobs=1, n_components=None, copy=True,
                 whiten=False, svd_solver='auto', tol=0.0, iterated_power='auto', random_state=None):

        self.fit_intercept = fit_intercept
        self.copy_X = copy_X
        self.normalize = normalize
        self.n_jobs = n_jobs
        self.n_components = n_components
        self.copy = copy
        self.whiten = whiten
        self.svd_solver = svd_solver
        self.tol = tol
        self.iterated_power = iterated_power
        self.random_state = random_state

    def _get_dict(self, obj):

        for attr, value in obj.__dict__.items():
            self.__dict__[attr] = value

    def _set_attributes(self):

        if self._pca:
            self._get_dict(self._pca)
        if self._model:
            self._get_dict(self._model)

    def get_regression_model(self):

        return self._lr

    def get_transformed_data(self):

        transformed = self._X_reduced
        return transformed

    def _reduce(self, X):
        random_state = check_random_state(self.random_state)
        self._pca = PCA(n_components=self.n_components, copy=self.copy,
                        whiten=self.whiten, svd_solver=self.svd_solver, tol=self.tol,
                        iterated_power=self.iterated_power, random_state=random_state)

        self._pca.fit(X)
        self._X_reduced = self._pca.transform(X)

    def fit(self, X, y):

        self._model = LinearRegression(fit_intercept=self.fit_intercept,
                                       copy_X=self.copy_X,
                                       normalize=self.normalize,
                                       n_jobs=self.n_jobs)

        self._lr = copy.deepcopy(self._model)

        self._reduce(X)

        self._model.fit(self._X_reduced, y)
        self._set_attributes()
        return self

    def predict(self, X):
        check_is_fitted(self, "coef_")
        X_reduced_test = self._pca.transform(X)
        predictions = self._model.predict(X_reduced_test)
        return predictions
