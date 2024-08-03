
from typing import Callable, Dict

def caching_fibonacci() -> Callable[[int], int]:
    """
    Returns a function that computes the Fibonacci number for a given input n using memoization to cache results.

    Returns:
        Callable[[int], int]: A function that computes the Fibonacci number.
    """

    cache: Dict[int, int] = {}

    def fibonacci(n: int) -> int:
        """
        Computes the Fibonacci number for a given input n using memoization.

        Args:
            n (int): The position in the Fibonacci sequence.

        Returns:
            int: The Fibonacci number at position n.
        """

        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci

if __name__ == "__main__":
    fib = caching_fibonacci()
    
    # Test cases
    test_cases = [10, 15, 20, 30]
    expected_results = [55, 610, 6765, 832040]
    
    # Run tests
    passed_tests = 0
    failed_tests = 0
    
    for i, test_case in enumerate(test_cases):
        try:
            result = fib(test_case)
            expected = expected_results[i]

            print(f"\nfib({test_case}) = {result}, expected: {expected}")

            assert result == expected, f"Test case failed for n={test_case}: got {result}, expected {expected}"

            passed_tests += 1
        except AssertionError as e:
            print(e)
            failed_tests += 1
    
    # Print summary of test results
    print("\nTesting completed.")
    print(f"Passed tests: {passed_tests}")
    print(f"Failed tests: {failed_tests}\n")
