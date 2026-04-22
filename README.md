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