import timeit

NUM = 25

class ConvertBinary:
    

    
    def convert_binary(self, n):
        # Step 1: conver to binary manually
        bits = []
        while n > 0:
            bits.append(n % 2)
            n //= 2
            
        # Pad with zeros
        while len(bits) < 4:
            bits.append(0)

            
            
        # Extract the digts you need by position from bits
        third = bits[2]   # 3rd digit from right
        fourth = bits[3] # 4h from right
        
        return third, fourth
    
    
    def optimize_extract_binary_digits(self, n):
        # 3rd bit from right = bit at position 2
        third = (n // 4) % 2      # 4 == 2^2

        # 4th bit from right = bit at position 3
        fourth = (n // 8) % 2     # 8 == 2^3

        return third, fourth
    
    def decimal_to_binary(self, decimal):
        count = 0
        third_digit = None
        fourth_digit = None
        decimal_number = NUM

        while decimal_number > 0:
            
            digit = decimal_number % 2
            count += 1
            
            # Check if it's the 3rd or 4th digit
            if count == 3:
                third_digit = digit
            elif count == 4:
                fourth_digit = digit
            
            # Stop early if we have both digits
            if third_digit is not None and fourth_digit is not None:
                break
            
            # Update the number for the next bit
            decimal_number //= 2

        # Check if the binary number has enough digits
        if count < 4:
            return "Binary number has fewer than 4 digits"
        
        return third_digit, fourth_digit


    def baseTest(self):

        ITER = 1_000_000

        tests = {
            "brute": "self.convert_binary(NUM)",
            "optimize version": "self.optimize_extract_binary_digits(NUM)",
            "optimize version 2": "self.decimal_to_binary(NUM)",
        }

            # IMPORTANT: No indentation inside this string
        setup = """
from __main__ import cb, NUM 
self = cb
"""

        print(f"Benchmarking with NUM={NUM} for {ITER:} \n")
        print(f"{'Method':20s} | {'Result':6s} | Time (seconds)")
        print("-" * 50)

        for name, stmt in tests.items():
            result = eval(stmt)
            t = timeit.timeit(stmt, setup=setup, number=ITER)
            print(f"{name:20s} | {str(result):6s} | {t:.6f}")


if __name__ == "__main__":
    
    cb = ConvertBinary()
    
    print(cb.baseTest())


    