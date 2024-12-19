def sum_array(array):
    # Initialize the sum to 0
    sum = 0  # O(1) - Constant time operation
    for element in array:  # O(n) - Iterate through all elements of the array
        sum += element  # O(1) - Add each element to the sum
    return sum  # O(1) - Return the final result

# Analysis:
# - The loop is the dominant factor, with O(n).
# - Overall complexity: O(n).