import time
import memory_profiler
import unittest

from profiler import (
    slow_function,
    fast_function,
    memory_intensive_function,
)


class TestProfiler(unittest.TestCase):
    def time_function(self, func):
        """Times the execution of a function."""
        start_time = time.time()
        func()
        end_time = time.time()
        return end_time - start_time

    def test_slow_function(self):
        """Test the slow_function for execution time."""
        duration = self.time_function(slow_function)

        print(
            f"slow_function executed in "
            f"{duration:.2f} seconds."
        )

        self.assertGreater(
            duration,
            2,
            "slow_function should take more than 2 seconds.",
        )

    def test_fast_function(self):
        """Test the fast_function for execution time."""
        duration = self.time_function(fast_function)

        print(
            f"fast_function executed in "
            f"{duration:.2f} seconds."
        )

        self.assertLess(
            duration,
            1,
            "fast_function should take less than 1 second.",
        )

    def test_memory_intensive_function(self):
        """Test execution time and monitor memory usage."""
        mem_usage_before = memory_profiler.memory_usage()

        start_time = time.perf_counter()
        result = memory_intensive_function()
        duration = time.perf_counter() - start_time

        mem_usage_after = memory_profiler.memory_usage()

        print(
            f"memory_intensive_function executed in "
            f"{duration:.2f} seconds."
        )

        print(
            f"Memory usage before: "
            f"{mem_usage_before[0]:.2f} MiB, "
            f"after: {mem_usage_after[0]:.2f} MiB."
        )

        self.assertLess(
            duration,
            5,
            "memory_intensive_function should take "
            "less than 5 seconds.",
        )

        # Process memory need not increase after a scalar calculation.
        # Keep memory measurements for analysis and verify the result instead.
        n = 10000000
        expected = n * (n - 1) * (2 * n - 1) // 6
        self.assertEqual(
            result,
            expected,
            "memory_intensive_function should return the correct "
            "sum of squares.",
        )


def main():
    unittest.main()


if __name__ == "__main__":
    main()
