function sumArray(array) {
    let sum = 0;  // O(1) - Constant initialization
    for (let element of array) {  // O(n) - Iterates through all elements of the array
        sum += element;  // O(1) - Adds each element
    }
    return sum;  // O(1) - Returns the final result
}

// Analysis:
// - The loop is the dominant element with O(n).
// - Total complexity: O(n).