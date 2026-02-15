# 📚 Data Structures and Algorithms

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)](https://github.com/Parth-S-Mahale/Data-Structures-and-Algorithms)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![LeetCode](https://img.shields.io/badge/Platform-LeetCode-orange?style=flat-square&logo=leetcode)](https://leetcode.com/)
[![GeeksforGeeks](https://img.shields.io/badge/Platform-GeeksforGeeks-green?style=flat-square)](https://www.geeksforgeeks.org/)

> A comprehensive collection of Data Structures and Algorithms implementations, organized by algorithmic patterns and problem-solving strategies. This repository serves as both a learning resource and a reference for technical interview preparation.

## 🎯 Overview

This repository contains well-documented solutions to fundamental DSA problems from platforms like **LeetCode** and **GeeksforGeeks**. Each solution includes:

- **Clear explanations** of the approach
- **Time and Space complexity analysis**
- **Clean, readable code** following best practices
- **Links to original problem statements**

Whether you're preparing for coding interviews, strengthening your algorithmic thinking, or building a solid foundation in computer science fundamentals, this repository provides structured learning paths and practical implementations.

---

## ✨ Features

- ✅ **Organized by Topic**: Solutions grouped by data structures and algorithmic patterns
- ✅ **Multiple Approaches**: Different solutions with complexity trade-off discussions
- ✅ **Complexity Analysis**: Detailed time and space complexity breakdowns
- ✅ **Problem Tracking**: Excel sheet to monitor progress across platforms
- ✅ **Clean Code**: Pythonic implementations with descriptive variable names
- ✅ **Interview-Ready**: Patterns commonly seen in technical interviews
- ✅ **Platform Links**: References to original LeetCode and GeeksforGeeks problems
- ✅ **Active Updates**: Regular additions of new problems and optimizations

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage Examples](#-usage-examples)
- [Topics Covered](#-topics-covered)
- [Technologies Used](#-technologies-used)
- [Problem Tracking](#-problem-tracking)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contact](#-contact)

---

## 📁 Repository Structure

```
Data-Structures-and-Algorithms/
│
├── 01-Hashing/
│   ├── problem1.py
│   ├── problem2.py
│   └── README.md
│
├── 02-Recursion/
│   ├── problem1.py
│   ├── problem2.py
│   └── README.md
│
├── 03-Sorting-Algorithms/
│   ├── bubble_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── README.md
│
├── 04-Linear-Search/
│   ├── problem1.py
│   └── README.md
│
├── 05-2D-Matrix/
│   ├── matrix_traversal.py
│   └── README.md
│
├── Leetcode/
│   ├── arrays/
│   ├── strings/
│   ├── trees/
│   └── README.md
│
├── Master DSA using GFG and Leetcode.xlsx
├── LICENSE
└── README.md
```

### Navigation Guide

- **Topic-Based Folders** (`01-Hashing`, `02-Recursion`, etc.): Solutions organized by core algorithmic concepts
- **Leetcode Folder**: Platform-specific problems categorized by data structure type
- **Excel Tracker**: Progress monitoring sheet for systematic problem-solving
- Each folder contains:
  - Individual solution files (`.py`)
  - `README.md` with topic overview and problem links

---

## 🚀 Getting Started

### Prerequisites

Before running the solutions, ensure you have:

- **Python 3.x** or higher installed ([Download Python](https://www.python.org/downloads/))
- A code editor (VS Code, PyCharm, or any text editor)
- Basic understanding of Python syntax
- (Optional) Git for cloning the repository

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Parth-S-Mahale/Data-Structures-and-Algorithms.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Data-Structures-and-Algorithms
   ```

3. **Verify Python installation**:
   ```bash
   python --version
   # or
   python3 --version
   ```

That's it! No external dependencies are required as all solutions use Python's standard library.

---

## 💡 Usage Examples

### Running a Solution

Navigate to any topic folder and execute a solution file:

```bash
# Example: Running a hashing problem
cd 01-Hashing
python problem1.py
```

### Running Sorting Algorithms

```bash
cd 03-Sorting-Algorithms
python merge_sort.py
```

### Testing with Custom Input

Most solution files can be modified to accept custom inputs. Open the file and modify the test cases:

```python
# Example from a problem file
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 3, 4, 5]
    target = 9
    print(solution(nums, target))
    
    # Add your own test case
    custom_input = [10, 20, 30]
    custom_target = 50
    print(solution(custom_input, custom_target))
```

### Interactive Python REPL

```bash
# Start Python interactive mode
python

# Import and use functions
>>> from '01-Hashing.problem1' import solution
>>> result = solution([1,2,3], 3)
>>> print(result)
```

---

## 🎓 Topics Covered

### Data Structures
- **Arrays & Strings**
- **Hash Tables & Hash Maps**
- **Linked Lists**
- **Stacks & Queues**
- **Trees & Binary Search Trees**
- **Graphs**
- **Heaps & Priority Queues**
- **2D Matrices**

### Algorithmic Patterns
- **Hashing Techniques**: Frequency maps, two-pointer with hash, complement lookups
- **Recursion & Backtracking**: Tree recursion, DFS, backtracking
- **Sorting Algorithms**: Bubble, Selection, Insertion, Merge, Quick Sort
- **Searching**: Linear search, Binary search variants
- **Two Pointers**: Fast-slow pointers, sliding window
- **Dynamic Programming**: (Coming soon)
- **Greedy Algorithms**: (Coming soon)
- **Divide and Conquer**: Merge sort, binary search applications

---

## 🛠️ Technologies Used

| Technology | Purpose | Badge |
|------------|---------|-------|
| **Python 3.x** | Primary programming language | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Git** | Version control | ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) |
| **GitHub** | Repository hosting | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) |
| **Excel** | Problem tracking | ![Excel](https://img.shields.io/badge/Excel-217346?style=flat-square&logo=microsoft-excel&logoColor=white) |

### Libraries & Tools
- **Standard Library Only**: No external dependencies required
- **Built-in Modules**: `collections`, `itertools`, `functools`

---

## 📊 Problem Tracking

The repository includes an **Excel tracking sheet** (`Master DSA using GFG and Leetcode.xlsx`) to help you:

- ✅ Track solved problems across platforms
- 📈 Monitor progress by difficulty level
- 🎯 Identify weak areas requiring practice
- 📅 Set goals and deadlines
- 🔍 Quick reference to problem categories

**Features of the Tracker**:
- Problem name, difficulty, and platform
- Links to original problems
- Completion status
- Personal notes and approach summaries
- Time/space complexity quick reference

---

## 🤝 Contributing

Contributions are welcome! Whether you want to:

- 🐛 Fix bugs
- ✨ Add new solutions
- 📝 Improve documentation
- 💡 Suggest optimizations
- 🎨 Refactor code for better readability

### How to Contribute

1. **Fork the repository**
2. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**:
   - Add your solution with proper comments
   - Include time/space complexity analysis
   - Update README if adding new topics
4. **Commit your changes**:
   ```bash
   git commit -m "Add: [Problem Name] - [Approach Description]"
   ```
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request**

### Contribution Guidelines

- **Code Quality**: Follow PEP 8 style guidelines for Python
- **Documentation**: Add clear comments explaining your approach
- **Complexity Analysis**: Include Big-O notation in comments
- **Problem Links**: Provide links to original problem statements
- **Test Cases**: Include at least 2-3 test cases
- **Naming Convention**: Use descriptive file and function names

Example solution format:
```python
"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Description:
[Brief problem description]

Approach:
[Explain your solution approach]

Time Complexity: O(n)
Space Complexity: O(n)
"""

def solution(nums, target):
    # Implementation here
    pass
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

The MIT License allows you to:
- ✅ Use the code commercially
- ✅ Modify and distribute
- ✅ Use privately
- ✅ Sublicense

**Attribution**: If you use this repository for learning or reference, a star ⭐ would be appreciated!

---

## 🙏 Acknowledgments

This repository is inspired by and references problems from:

### Learning Platforms
- **[LeetCode](https://leetcode.com/)** - Extensive problem collection and online judge
- **[GeeksforGeeks](https://www.geeksforgeeks.org/)** - Tutorials, articles, and practice problems
- **[HackerRank](https://www.hackerrank.com/)** - Interview preparation kit

### Educational Resources
- **[freeCodeCamp](https://www.freecodecamp.org/)** - DSA curriculum and tutorials
- **[Abdul Bari's Algorithms Course](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)** - In-depth algorithm explanations
- **[NeetCode](https://neetcode.io/)** - Curated problem lists and video solutions
- **[Big-O Cheat Sheet](https://www.bigocheatsheet.com/)** - Complexity reference

### Community
- Stack Overflow community for debugging help
- GitHub users who provided feedback and suggestions
- Fellow developers sharing their DSA journeys

### Special Thanks
- To all open-source contributors who make learning accessible
- Problem setters on competitive programming platforms
- Technical interviewers who inspire continuous improvement

---

## 📬 Contact

**Parth S. Mahale**

- 💼 **LinkedIn**: [Connect with me](https://www.linkedin.com/in/parth-s-mahale/) *(Add your actual LinkedIn URL)*
- 🐙 **GitHub**: [@Parth-S-Mahale](https://github.com/Parth-S-Mahale)
- 📧 **Email**: your.email@example.com *(Add your email)*
- 🌐 **Portfolio**: [YourWebsite.com](https://yourwebsite.com) *(Add if applicable)*

### Let's Connect!

- 💬 Feel free to reach out for:
  - Questions about solutions
  - Collaboration opportunities
  - Technical discussions
  - Interview preparation tips

- 🤝 Open to:
  - Code reviews
  - Solution optimizations
  - Study group collaborations
  - Open-source contributions

---

## 🌟 Show Your Support

If you found this repository helpful:

- ⭐ **Star this repo** to show appreciation
- 🔀 **Fork it** to create your own version
- 👀 **Watch** for updates on new problems
- 📢 **Share** with friends preparing for interviews
- 💬 **Discuss** solutions and approaches in Issues

---

## 📈 Repository Stats

![GitHub repo size](https://img.shields.io/github/repo-size/Parth-S-Mahale/Data-Structures-and-Algorithms?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/Parth-S-Mahale/Data-Structures-and-Algorithms?style=flat-square)
![GitHub language count](https://img.shields.io/github/languages/count/Parth-S-Mahale/Data-Structures-and-Algorithms?style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/Parth-S-Mahale/Data-Structures-and-Algorithms?style=flat-square)

---

## 🎯 Roadmap

- [ ] Add more LeetCode medium/hard problems
- [ ] Implement Dynamic Programming section
- [ ] Add Graph algorithms (BFS, DFS, Dijkstra)
- [ ] Include system design patterns
- [ ] Create video walkthroughs for complex problems
- [ ] Add Java/C++ implementations
- [ ] Build interactive problem difficulty tracker
- [ ] Create topic-wise difficulty progression guides

---

<div align="center">

**Happy Coding! 🚀**

*"The only way to learn a new programming language is by writing programs in it."* - Dennis Ritchie

Made with ❤️ by [Parth S. Mahale](https://github.com/Parth-S-Mahale)

</div>
