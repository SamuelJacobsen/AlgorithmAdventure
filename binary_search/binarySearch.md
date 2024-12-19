# 📘 Binary Search

This README explains the concept of **Binary Search**, an efficient algorithm for finding elements in sorted arrays. Inspired by the book *Grokking Algorithms*, this guide is designed to help you study and practice binary search effectively.

## 🔍 What is Binary Search?

Binary Search is a method used to locate a specific element in a **sorted array**. By repeatedly dividing the search range in half, it drastically reduces the number of comparisons needed compared to a linear search.

## ⚙️ How Does It Work?

1. Start with the full array as the search range.
2. Find the middle element.
3. Compare the target value to the middle element:
   - If they are equal, you’ve found the target.
   - If the target is smaller, continue searching in the left half.
   - If the target is larger, search in the right half.
4. Repeat until the target is found or the range is empty.

## 🧮 Algorithm Complexity

- **Best Case:** \(O(1)\) – The target is found on the first comparison.
- **Worst Case:** \(O(\log n)\) – The search range is halved repeatedly.
- **Requirement:** The array **must be sorted** beforehand.
