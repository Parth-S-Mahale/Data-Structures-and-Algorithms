# Data Structures and Algorithms

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A structured collection of core data structure and algorithm implementations in Python.

This repository is organized by algorithmic strategy rather than by platform. It focuses on clarity, time complexity awareness, and reusable problem-solving patterns.

---

## Repository Structure

/
├── 01-Hashing/
├── 02-Recursion/
├── 03-Sorting-Algorithms/
├── 04-Linear-Search/
├── 05-2D-Matrix/
├── Leetcode/
└── Master DSA using GFG and Leetcode.xlsx


### Directory Breakdown

**01-Hashing/**  
Dictionary-based lookup optimization, frequency maps, complement lookup patterns.

**02-Recursion/**  
Recursive decomposition, stack reasoning, divide-and-conquer techniques.  
MDN Recursion Overview:  
https://developer.mozilla.org/en-US/docs/Glossary/Recursion

**03-Sorting-Algorithms/**  
Classic sorting implementations with complexity comparison.

**04-Linear-Search/**  
Single-pass scanning and conditional traversal strategies.

**05-2D-Matrix/**  
Matrix traversal patterns, nested iteration, boundary traversal.

**Leetcode/**  
Problem implementations grouped by pattern (sliding window, recursion, hashing, etc.).

**Master DSA using GFG and Leetcode.xlsx**  
Tracking sheet for problem difficulty and categorization.

---

## Techniques Demonstrated

### Hash Table Optimization
- Frequency counting
- O(1) average lookup using Python `dict`
- Complement lookup patterns (Two Sum pattern)

Python dict documentation:  
https://docs.python.org/3/library/stdtypes.html#dict

---

### Recursion & Divide-and-Conquer
- Base case design
- Call stack reasoning
- Tree-style problem breakdown

MDN Recursion Overview:  
https://developer.mozilla.org/en-US/docs/Glossary/Recursion

---

### Sorting Strategy Comparison
- In-place vs auxiliary space tradeoffs
- Stability considerations
- Worst-case vs average-case performance

---

### Matrix Traversal Patterns
- Nested iteration over 2D arrays
- Index boundary control
- Grid-style computation patterns

---

## Big-O Reference Summary

| Technique              | Typical Time Complexity | Typical Space Complexity |
|------------------------|--------------------------|---------------------------|
| Hashing Lookup        | O(1) average             | O(n)                      |
| Linear Search         | O(n)                     | O(1)                      |
| Recursive DFS         | O(n)                     | O(n) stack                |
| Basic Sorting (n²)    | O(n²)                    | O(1) or O(n)              |
| Efficient Sorting     | O(n log n)               | O(log n) or O(n)          |
| Matrix Traversal      | O(rows × cols)           | O(1)                      |

---

## Dependencies

- Python 3.x
- Standard Library only

No external runtime dependencies.
