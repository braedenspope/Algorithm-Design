# Algorithm Design Course

This repository contains all assignments and projects completed during my Algorithm Design course. Each lab focuses on implementing fundamental algorithms and data structures while emphasizing proper coding practices, efficiency analysis, and testing through assertions.

## Course Overview

The course covers essential computer science concepts including:
- Algorithm efficiency and Big O notation
- Search algorithms (linear and binary search)
- Sorting algorithms
- Sequence generation and mathematical algorithms
- File I/O and JSON data handling
- Authentication systems
- Input validation and error handling

## Repository Structure

```
Algorithm-Design/
├── Lab01.py                    # Number guessing game
├── Lab02.py                    # Authentication system
├── Lab06.py                    # Binary search implementation
├── Lab08.py                    # Selection sort algorithm
├── Lab10.py                    # François sequence generator
├── Lab12.py                    # Prime number generator (Sieve of Eratosthenes)
├── Advanced_Search_Design.pdf  # Binary search algorithm design and pseudocode
├── Numerical_Sequence_Design.pdf # François sequence algorithm design and trace
├── Prime_Number_Design.pdf     # Prime generation algorithm design and trace
├── Sort_Design.pdf            # Selection sort algorithm design and analysis
├── Monopoly_Program_Design.pdf # Complex flowchart design for Monopoly logic
└── README.md                  # This file
```

## Design Documentation

Each major algorithm implementation is accompanied by detailed design documents that include:
- **Pseudocode**: Step-by-step algorithm design in structured English
- **Trace Tables**: Line-by-line execution tracking with variable states
- **Algorithmic Efficiency Analysis**: Big O notation and complexity reasoning
- **Test Cases**: Worked examples showing algorithm execution

## Lab Assignments

### Lab 01: Python Review - Number Guessing Game
**File:** `Lab01.py`

A classic number guessing game that demonstrates:
- Random number generation
- User input validation
- Loop control structures
- List management for tracking guesses

**Features:**
- User-defined difficulty range
- Feedback system (too high/too low)
- Guess tracking and final statistics

---

### Lab 02: Authentication Program
**File:** `Lab02.py`

A secure authentication system that reads user credentials from JSON files.

**Key Concepts:**
- JSON file parsing and error handling
- Username/password validation
- Exception handling for file operations
- Security best practices

**Input:** JSON file with username and password arrays
**Output:** Authentication success/failure messages

---

### Lab 06: Advanced Search (Binary Search)
**Files:** `Lab06.py`, `Advanced_Search_Design.pdf`

Implementation of binary search algorithm on sorted arrays with comprehensive design documentation.

**Algorithm Details:**
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- Handles edge cases including empty arrays
- Demonstrates divide-and-conquer approach

**Design Document Features:**
- Complete pseudocode with structured algorithm steps
- Detailed explanation of binary search logic
- Edge case handling for empty lists and failed searches

**Features:**
- File-based input from JSON
- Efficient searching on sorted data
- Comprehensive error handling

---

### Lab 08: Sorting Algorithm (Selection Sort)
**Files:** `Lab08.py`, `Sort_Design.pdf`

Implementation of selection sort with extensive assertion testing and complete design analysis.

**Algorithm Details:**
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- In-place sorting algorithm
- Finds maximum element and places it in correct position

**Design Document Features:**
- Detailed pseudocode with variable tracking
- Complete trace table showing algorithm execution on test case [52, 15, 39, 26]
- Step-by-step analysis of pivot and swap operations
- Efficiency analysis (note: original design document states O(log n) but actual implementation is O(n²))

**Key Features:**
- Robust assertion testing for validation
- JSON file input/output
- Step-by-step sorting demonstration

---

### Lab 10: Numeric Sequence (François Numbers)
**Files:** `Lab10.py`, `Numerical_Sequence_Design.pdf`

Generates François numbers (a Fibonacci-like sequence) up to a specified index with detailed algorithm analysis.

**Sequence Definition:**
- F(1) = 2, F(2) = 1
- F(n) = F(n-1) + F(n-2) for n > 2

**Design Document Features:**
- Complete pseudocode showing iterative approach
- Detailed trace table for calculating the 7th François number
- Line-by-line execution tracking: [2, 1] → [2, 1, 3] → [2, 1, 3, 4] → [2, 1, 3, 4, 7] → [2, 1, 3, 4, 7, 11] → [2, 1, 3, 4, 7, 11, 18]
- Algorithmic efficiency analysis confirming O(n) complexity

**Features:**
- Dynamic sequence generation
- Input validation for positive numbers
- Efficient iterative approach

---

### Lab 12: Prime Number Generation (Sieve of Eratosthenes)
**Files:** `Lab12.py`, `Prime_Number_Design.pdf`

Efficient algorithm for finding all prime numbers up to a given limit with comprehensive design documentation.

**Algorithm Details:**
- **Time Complexity:** O(n log log n)
- **Space Complexity:** O(n)
- Uses the Sieve of Eratosthenes method
- Optimized to only check factors up to √n

**Design Document Features:**
- Complete pseudocode with step-by-step algorithm design
- Detailed trace table showing execution for finding primes ≤ 10
- Variable state tracking: shows how numbers get marked with "X" as composites
- Example execution: starts with [0,1,2,3,4,5,6,7,8,9,10], marks multiples of 2, then 3, etc.
- Algorithmic efficiency analysis (note: document states O(n) but actual complexity is O(n log log n))

**Features:**
- Mathematical optimization techniques
- Boolean array for efficient marking
- Comprehensive prime number listing

---

### Additional Design Documentation

#### Monopoly Program Design
**File:** `Monopoly_Program_Design.pdf`

A comprehensive flowchart demonstrating complex algorithmic thinking for a Monopoly game scenario. This advanced design shows:

**Problem:** Determining steps needed to place a hotel on Pennsylvania Avenue
**Complex Decision Tree Including:**
- Property ownership validation
- House and hotel availability checking
- Fund sufficiency calculations
- Multi-property coordination logic
- Hotel swapping strategies between properties

**Design Methodology:**
- Complete flowchart with decision diamonds and process rectangles
- Multiple exit conditions and error handling paths
- Demonstrates advanced algorithmic planning beyond basic lab assignments
- Shows progression to real-world problem-solving scenarios

## Technical Highlights

### Error Handling
All programs implement robust error handling including:
- File not found exceptions
- Invalid input validation
- Edge case management (empty arrays, negative numbers)

### Code Quality
- Comprehensive commenting and documentation
- Assertion-based testing for validation
- Clear variable naming and code structure
- Input validation and user-friendly error messages

### Algorithm Analysis
Each implementation includes:
- Time and space complexity analysis
- Efficiency considerations
- Optimization techniques where applicable

## Learning Outcomes

Through these assignments, I developed proficiency in:

1. **Algorithm Design:** Understanding and implementing classical algorithms with formal design documentation
2. **Efficiency Analysis:** Big O notation and performance optimization with detailed complexity reasoning
3. **Data Structures:** Arrays, lists, and their applications in various algorithmic contexts
4. **Problem Solving:** Breaking down complex problems into manageable steps using pseudocode and flowcharts
5. **Testing:** Using assertions and edge case validation with comprehensive trace table analysis
6. **File Operations:** JSON parsing and error handling in real-world scenarios
7. **Code Documentation:** Writing clear, maintainable code with supporting design documents
8. **Algorithm Tracing:** Step-by-step execution analysis for debugging and verification

## Design Process Methodology

The course emphasized a structured approach to algorithm development:

1. **Problem Analysis:** Understanding requirements and constraints
2. **Pseudocode Design:** Creating structured English descriptions of algorithms
3. **Trace Table Creation:** Manual execution tracking for verification
4. **Efficiency Analysis:** Formal complexity analysis with Big O notation
5. **Implementation:** Converting designs to working Python code
6. **Testing:** Comprehensive validation using assertions and edge cases

## Course Reflection

Each lab presented unique challenges and learning opportunities:
- **Lab 01:** Variable type management and user interaction
- **Lab 02:** JSON manipulation and file handling
- **Lab 06:** Empty list handling in binary search with formal design process
- **Lab 08:** Implementing correct sorting algorithm with trace table validation
- **Lab 10:** François sequence generation with mathematical precision
- **Lab 12:** Mathematical optimizations in prime generation using classical algorithms

The design documents demonstrate the progression from basic programming concepts to advanced algorithmic thinking, emphasizing the importance of formal design before implementation. The trace tables and efficiency analyses show deep understanding of how algorithms execute and scale.

---

*This repository represents coursework completed as part of my computer science education, focusing on fundamental algorithms and their practical implementation.*
