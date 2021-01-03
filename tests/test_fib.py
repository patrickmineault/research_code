import time
import unittest
from example_pkg import fib

class TestFib(unittest.TestCase):
    def test_fib(self):
        # 1, 1, 2, 3, 5, etc.
        self.assertEqual(fib.fib(0), 1)
        self.assertEqual(fib.fib(2), 2)
        self.assertEqual(fib.fib(4), 5)
        self.assertEqual(fib.fib(99), 354_224_848_179_261_915_075)

    def test_memoization(self):
        """Check that the memo-ized version is much faster than the naive."""
        def _fib(n):
            if n >= 2:
                return _fib(n-2) + _fib(n-1)
            else:
                return 1

        t0 = time.time()
        val = fib.fib(15)
        dt = time.time() - t0

        t0 = time.time()
        val2 = _fib(15)
        dt2 = time.time() - t0

        self.assertEqual(val, val2)
        self.assertGreater(dt2, dt * 10)

if __name__ == "__main__":
    unittest.main()