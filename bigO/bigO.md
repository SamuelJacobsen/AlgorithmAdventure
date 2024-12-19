# Big O Notation

The **Big O notation** is a way to describe the performance of an algorithm in terms of **execution time** or **memory usage** as the input size grows. It is a fundamental tool for analyzing algorithm efficiency.

---

## 🌟 **Why use Big O?**

- **Algorithm comparison:** Helps understand which algorithm is more efficient for different input sizes.
- **Performance prediction:** Allows estimating the impact of large amounts of data.
- **Focus on worst-case:** Ensures preparedness for the most demanding scenarios.

---

## ⏱ **Execution Time vs. Growth**

The execution time of an algorithm is measured by its complexity growth relative to the **input size (n)**.

- **Lower growth:** More efficient algorithm.
- **Higher growth:** Less efficient algorithm for large inputs.

### ⚖ **Comparison of common complexities**
| Big O Notation | Name                          | Example Algorithm               | Growth               |
|----------------|-------------------------------|---------------------------------|----------------------|
| O(1)           | Constant                      | Direct access to an index       | 🔵 Constant          |
| O(log n)       | Logarithmic                   | Binary search                   | 🔵 Slow growth       |
| O(n)           | Linear                        | Simple iteration                | 🟡 Moderate growth   |
| O(n log n)     | Linear-logarithmic            | Merge Sort, Quick Sort          | 🟡 Moderate/fast     |
| O(n²)          | Quadratic                     | Bubble Sort, Selection Sort     | 🔴 Fast growth        |
| O(2ⁿ)          | Exponential                   | Backtracking decision problems  | 🔴 Very fast          |
| O(n!)          | Factorial                     | Permutation algorithms          | 🔴 Extremely fast    |

---

## 🛠 **How to analyze complexity?**

1. **Identify the input size (n):** Example: number of elements in an array.
2. **Count dominant operations:** Ignore constants and lower-order terms.
3. **Use Big O notation:** Express the algorithm's behavior as the input size grows indefinitely (\`n → ∞\`).

---

