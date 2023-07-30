import loguru

# Configure loguru to write logs to a file named 'app.log' with a maximum size of 1 MB per file
loguru.logger.add("app.log", rotation="1 MB")

def calculate_sum(a, b):
    result = a + b
    loguru.logger.debug(f"Sum calculated: {a} + {b} = {result}")
    return result

def main():
    num1 = 10
    num2 = 20

    # Log the beginning of the calculation
    loguru.logger.info(f"Starting the calculation of {num1} + {num2}")

    result = calculate_sum(num1, num2)

    # Log the result
    loguru.logger.success(f"Calculation successful! The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
