def palindrome_string(n: int) -> bool:
    """
     Determine whether an integer is a palindrome using string reversal.

    This method converts the integer to a string and checks whether the
    string reads the same forwards and backwards. It is typically the
    fastest and most concise approach in Python due to optimized C-level
    string operations.

    Parameters
    ----------
    n : int
        The integer to evaluate.

    Returns
    -------
    bool
        True if `n` is a palindrome, otherwise False.
    """
    s = str(n)
    return s == s[::-1]


def palindrome_full_reverse(n: int) -> bool:
    """
    Determine whether an integer is a palindrome by reversing all digits.

    This method reconstructs the reversed integer using arithmetic
    operations only. It is useful in algorithmic contexts where converting
    the number to a string is not allowed.

    Parameters
    ----------
    n : int
        The integer to evaluate.

    Returns
    -------
    bool
        True if `n` is a palindrome, otherwise False.
    """
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev == original


def palindrome_half_reverse(n: int) -> bool:
    """
    Determine whether an integer is a palindrome by reversing only half
    of its digits.

    This optimized approach avoids reversing the entire number. Instead,
    it builds the reversed second half until it becomes greater than or
    equal to the remaining first half. This reduces computation and is
    the preferred arithmetic solution for large integers or interview
    settings where string conversion is disallowed.

    Parameters
    ----------
    n : int
        The integer to evaluate. Negative numbers and numbers ending in
        zero (except zero itself) are automatically non-palindromes.

    Returns
    -------
    bool
        True if `n` is a palindrome, otherwise False.
    """
    if n < 0 or (n % 10 == 0 and n != 0):
        return False

    rev = 0
    while n > rev:
        rev = rev * 10 + n % 10
        n //= 10

    return n == rev or n == rev // 10


def check_num_ispalindrone(num) ->bool:
    """
    Determine whether an integer is a palindrome using the classic
    full‑reverse arithmetic method.

    This method reconstructs the reversed form of the input integer by
    repeatedly extracting the last digit and appending it to a running
    reversed value. It does not rely on string conversion, making it a
    clear and fundamental demonstration of digit‑manipulation logic.

    Parameters
    ----------
    num : int
        The integer to evaluate.

    Returns
    -------
    bool
        True if `num` reads the same forwards and backwards, otherwise False.
    """
    temp = num
    rev_num = 0

    while num > 0:

        #extract the last digit
        digit = num % 10

        #append the digit to the reverse_num
        rev_num = rev_num * 10 + digit

        #floor the num by 10
        num //= 10

    if temp == rev_num:
        return True
    
    return False


import timeit

# Test input
NUM = 1234543218

# Number of iterations
ITER = 1_000_000

tests = {
    "string method": "palindrome_string(NUM)",
    "full reverse": "palindrome_full_reverse(NUM)",
    "half reverse": "palindrome_half_reverse(NUM)",
    "classic method": "check_num_ispalindrone(NUM)",
}

setup = """
from __main__ import (
    palindrome_string,
    palindrome_full_reverse,
    palindrome_half_reverse,
    check_num_ispalindrone,
    NUM
)
"""

print(f"Benchmarking with NUM={NUM:,} for {ITER:,} iterations:\n")

# Print header
print(f"{'Method':20s} | {'Result':6s} | Time (seconds)")
print("-" * 50)

for name, stmt in tests.items():
    # Compute True/False once (not inside timeit)
    result = eval(stmt)

    # Benchmark timing
    t = timeit.timeit(stmt, setup=setup, number=ITER)

    # Print row
    print(f"{name:20s} | {str(result):6s} | {t:.6f}")