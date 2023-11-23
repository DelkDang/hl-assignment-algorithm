def miniMaxSum(intNumbers):
    evenNumbers = []
    oddNumbers = []

    # Initialize variables for minimum and maximum values
    minValue, maxValue = intNumbers[0], intNumbers[0]

    # Initialize a variable for the sum
    totalSum = 0

    # Calculate the sum and find the minimum and maximum values
    for num in intNumbers:
        totalSum += num
        minValue = minValue if num > minValue else num
        maxValue = maxValue if num < maxValue else num
        oddNumbers.append(num) if num % 2 else evenNumbers.append(num)

    # Print the result
    print(totalSum - maxValue, totalSum - minValue)

# Take input from the user
inputString = input()

# Split the input string into a list of strings
stringNumbers = inputString.split()

# Convert each string element to an integer
intNumbers = [int(num) for num in stringNumbers]

# Call the function with the input
miniMaxSum(intNumbers)
