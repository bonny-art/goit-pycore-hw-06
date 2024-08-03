
from typing import Callable, Generator
import re

def generator_numbers(text: str) -> Generator[str, None, None]:
    """
    Generates floating-point numbers from a given text using regular expressions.

    Args:
        text (str): The input text containing floating-point numbers.

    Yields:
        Generator[str, None, None]: Floating-point numbers found in the text.
    """

    pattern = r"-?\b\d+\.\d+\b"

    position = 0
    while position < len(text):
        match = re.search(pattern, text[position:])
        
        if match:
            yield float(match.group())
            position += match.end()
        else:
            break
       

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculates the sum of floating-point numbers generated from the given text.

    Args:
        text (str): The input text containing floating-point numbers.
        func (Callable[[str], Generator[float, None, None]]): Function that generates floating-point numbers.

    Returns:
        float: The sum of floating-point numbers.
    """

    return sum(number for number in func(text))

if __name__ == "__main__":

    # Test cases
    tests = [
        {
            'input': "The total income includes 1000.01 as the main income, with additional 27.45 and 324.00.",
            'expected': 1000.01 + 27.45 + 324.00,
            'description': 'Standard case with multiple numbers'
        },
        {
            'input': "There are no numbers here!",
            'expected': 0.0,
            'description': 'Case with no numbers'
        },
        {
            'input': "The values are -100.50, -20.10 and 50.00.",
            'expected': -100.50 - 20.10 + 50.00,
            'description': 'Case with negative numbers'
        },
        {
            'input': "",
            'expected': 0.0,
            'description': 'Case with an empty string'
        }
    ]
    
    # Run tests
    passed_tests = 0
    failed_tests = 0

    for i, test in enumerate(tests):
        try:
            result = sum_profit(test['input'], generator_numbers)
            expected = test['expected']

            print(f"\nsum_profit({test['input']}) = {result}, expected: {expected}")

            assert result == test['expected'], f"Test case {i+1} failed ({test['description']}): got {result}, expected {test['expected']}"

            passed_tests += 1
        except AssertionError as e:
            print(e)
            failed_tests += 1

    # Print summary of test results
    print("\nTesting completed.")
    print(f"Passed tests: {passed_tests}")
    print(f"Failed tests: {failed_tests}\n")

    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")