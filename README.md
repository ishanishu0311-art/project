# Secure Password Generator Utility

## Overview of the Project

This project is a command-line utility implemented in Python designed to generate strong, cryptographically random passwords. Its primary goal is to help users quickly and securely generate passwords that comply with standard security requirements, ensuring complexity by including a balanced mix of character types.

The application strictly adheres to a limited set of password lengths (8, 12, or 16 characters) and ensures every generated password contains a combination of uppercase letters, lowercase letters, digits, and special characters.

## Features

* **Fixed Password Lengths:** Users can select from three predefined, secure password lengths: 8, 12, or 16 characters.
* **Guaranteed Complexity:** Every generated password is guaranteed to contain characters from all four required sets:
    * Uppercase Letters (`A-Z`)
    * Lowercase Letters (`a-z`)
    * Digits (`1-9`)
    * Special Symbols (`$%&#@*!`)
* **User-Friendly Interface:** Simple text-based prompts guide the user through the selection process.

## Technologies/Tools Used

| Category | Item | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.x | The core programming language used for scripting. |
| **Modules** | `random` | Used for generating random selections from the character sets to ensure unpredictability. |
| **Tools** | Command Line/Terminal | The primary interface for running and interacting with the script. |

## Steps to Install & Run the Project

Since this project uses only standard Python libraries, there are no complex installation steps.

### 1. Prerequisites

You must have **Python 3.x** installed on your system.

### 2. Setup

1.  **Clone the Repository:**
    ```bash
    git clone [Your Repository URL Here]
    cd [Your Repository Name]
    ```
2.  **Save the Script:**
    Ensure the Python code is saved as a file (e.g., `password_generator.py`) in the root directory.

### 3. Running the Script
Test Case 1: Valid Input (Length 8)
Run the script: python password_generator.py

Enter 1 when prompted.

Expected Result: The output password should have exactly 8 characters and contain at least one character from the Uppercase, Lowercase, Digit, and Special Character sets.

Test Case 2: Valid Input (Length 12)
Run the script: python password_generator.py

Enter 2 when prompted.

Expected Result: The output password should have exactly 12 characters and contain a mix of all four character types.

Test Case 3: Invalid Input
Run the script: python password_generator.py

Enter 5 (or any number outside of 1, 2, 3) when prompted.

Expected Result: The script should print the error message: please select appropriate option.

Execute the file directly from your terminal:

```bash
python password_generator.py
## How to Run

Execute the script from your terminal using the Python interpreter:

```bash
python password_generator.py
