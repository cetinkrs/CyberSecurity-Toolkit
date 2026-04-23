# CyberSecurity Toolkit 🛡️

This repository serves as a personal workspace containing various analysis, automation, and security tools developed for cybersecurity applications.

## 🛠️ Tool 1: Password Validator (`password_validator.py`)
A user-experience (UX) focused password analysis script designed to evaluate password strength against brute-force attacks.

**Key Engineering Principles Implemented:**
- **Fail-Fast Optimization:** Length validation is isolated from the main loop to preserve CPU cycles on inherently invalid inputs.
- **Time Complexity Considerations:** Character analysis is streamlined using a single-pass `if-elif` structure for mutually exclusive conditions, rather than sequential independent loops.
- **Comprehensive Feedback (UX):** Provides detailed, checklist-style error reporting to guide users precisely on missing security parameters.

**Evaluated Security Parameters:**
- [x] Minimum 8 characters in length
- [x] Uppercase and Lowercase letter requirements
- [x] Numeric digit requirement
- [x] Special character detection (Non-alphanumeric validation)
<br>

### 🛠️ Tool 2: Dynamic Port Analyzer (`port_analyzer.py`)

A core cybersecurity utility that simulates network port scanning by filtering and identifying "open" and potentially vulnerable ports from a given dataset. 

**Key Engineering Principles Implemented:**

* **Algorithmic Filtering:** Efficiently iterates through complex data structures (Dictionaries) to isolate and extract target values into Lists.
* **Clean Code & Type Hinting:** Enforces Python type hints (`dict` -> `list`) and PEP 8 standards for professional code readability and maintenance.
* **Self-Documenting Code:** Utilizes Docstrings for built-in documentation and IDE hover-support, alongside dynamic `if-else` state evaluations.