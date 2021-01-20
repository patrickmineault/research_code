import numpy as np
import unittest

from research_code.cka_step3 import cka

def _get_one():
    X = np.cos(.1 * np.pi * np.arange(10)).reshape((-1, 1))
    Y = np.cos(2 + .07 * np.pi * np.arange(10)).reshape((-1, 1))
    return X, Y

def _get_multi():
    X = np.cos(.1 * np.pi * np.arange(10).reshape((-1, 1)) * np.linspace(.5, 1.5, num=3).reshape((1, -1)))
    Y = np.cos(.5 + .07 * np.pi * np.arange(10).reshape((-1, 1)) * np.linspace(.7, 1.3, num=4).reshape((1, -1)))
    return X, Y

def _get_wide():
    X = np.cos(.1 * np.pi * np.arange(10).reshape((-1, 1)) * np.linspace(.5, 1.5, num=50).reshape((1, -1)))
    Y = np.cos(.5 + .07 * np.pi * np.arange(10).reshape((-1, 1)) * np.linspace(.7, 1.3, num=47).reshape((1, -1)))
    return X, Y

class TestCka(unittest.TestCase):
    
    @unittest.expectedFailure
    def test_wrong_dim(self):
        """It should throw an error if we have a different number of stimuli"""
        X = np.ones((8, 1))
        Y = np.ones((10, 1))
        cka(X, Y)

    def test_same(self):
        """The CKA of a matrix and itself is one"""
        X, _ = _get_one()
        self.assertAlmostEqual(cka(X, X), 1)

    def test_corr(self):
        """The CKA of two vectors is the square of the correlation coefficient"""
        X, Y = _get_one()
        c1 = cka(X, Y)
        c2 = np.corrcoef(X.squeeze(), Y.squeeze())[0, 1] ** 2
        self.assertAlmostEqual(c1, c2)

    def test_isoscaling(self):
        """CKA is insensitive to scaling by a scalar"""
        X, Y = _get_multi()
        c1 = cka(X, Y)
        c2 = cka(2.0 * X, - 1 * Y)
        self.assertAlmostEqual(c1, c2)

    def test_rotation(self):
        """CKA is insensitive to rotations"""
        X, Y = _get_multi()
        X0 = X[:, :2]
        X0p = X0 @ np.array([[1, -1], [1, 1]]) / np.sqrt(2)
        c1 = cka(X0, Y)
        c2 = cka(X0p, Y)
        self.assertAlmostEqual(c1, c2)

    def test_no_iso(self):
        """CKA is sensitive to column scaling"""
        X, Y = _get_multi()
        X0 = X[:, :2]
        X0p = X0 @ np.array([[1, 1], [10, 1]])
        c1 = cka(X0, Y)
        c2 = cka(X0p, Y)
        self.assertGreater(abs(c1 - c2), .001)

    def test_value(self):
        """Regression test: for this particular input, check that the value
        is the same as it always was."""
        X, Y = _get_multi()
        c1 = cka(X, Y)
        self.assertAlmostEqual(c1, 0.96577, places=4)

    def test_wide(self):
        """Smoke test."""
        X, Y = _get_wide()
        c1 = cka(X, Y)

if __name__ == '__main__':
    unittest.main()