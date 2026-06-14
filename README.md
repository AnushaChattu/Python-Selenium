# Python Selenium Automation Framework

## Overview

This project is an automated testing framework built using **Python** and **Selenium WebDriver**. It is designed to automate web application testing, improve test coverage, reduce manual effort, and provide reliable test execution with detailed reports.

The framework follows industry-standard automation practices and can be extended for regression, smoke, functional, and end-to-end testing.

---

## Features

* Web UI Automation using Selenium WebDriver
* Python-based test scripts
* Reusable test components
* Data-driven testing support
* Cross-browser execution
* Screenshot capture on failure
* Detailed test reporting
* Easy maintenance and scalability

---

## Tech Stack

* Python 3.x
* Selenium WebDriver
* PyTest / Unittest
* ChromeDriver
* WebDriver Manager
* HTML Reports

---

## Project Structure

```text
Python-Selenium/
│
├── tests/
│   ├── test_login.py
│   ├── test_registration.py
│   └── test_dashboard.py
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── base_page.py
│
├── utilities/
│   ├── config.py
│   ├── logger.py
│   └── helpers.py
│
├── screenshots/
│
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Prerequisites

Before running the project, ensure the following are installed:

* Python 3.8 or higher
* Google Chrome
* ChromeDriver
* pip package manager

Verify installation:

```bash
python --version
pip --version
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/AnushaChattu/Python-Selenium.git
cd Python-Selenium
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/test_login.py
```

### Generate HTML Report

```bash
pytest --html=reports/report.html
```

### Run Tests in Verbose Mode

```bash
pytest -v
```

---

## Test Reports

After execution, reports can be found in:

```text
reports/
```

The report contains:

* Execution Summary
* Passed/Failed Tests
* Error Details
* Execution Duration

---

## Best Practices Followed

* Page Object Model (POM)
* Reusable Components
* Clean Code Structure
* Explicit Waits
* Configuration Management
* Scalable Test Design

---

## Future Enhancements

* Jenkins CI/CD Integration
* Parallel Test Execution
* Docker Support
* API Automation Integration
* Database Validation
* Cloud Browser Execution

---

## Author

### Anusha Chattu

GitHub Repository:
https://github.com/AnushaChattu/Python-Selenium

---

## License

This project is intended for educational purposes, automation practice, and learning Selenium with Python.

Feel free to fork, enhance, and contribute.
