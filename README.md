# Application QA Testing Framework

A testing framework for validating application functionality, including API endpoints and UI interactions. Built with Python, Selenium, and Pytest.

***

## 🎯 Task files
- [Test Cases](docs/test_cases.md)
- [Bugs](docs/bugs.md)
- [Strategy and Recommendations](docs/strategy_and_recomendations.md)

### 🧑‍💻 Extra tools used
- [Allure](https://docs.qameta.io/allure/) for test reporting and visualization
- [Python-dotenv](https://pypi.org/project/python-dotenv/) for environment variable management
- [Pydantic](https://pydantic.dev/) for data validation and modeling
- [MyPy](https://mypy-lang.org/) for static type checking
- [Ruff](https://pypi.org/project/ruff/) for code linting and formatting

### 📊 Execution report
[Allure Report](docs/allure-report.zip)

To see the report, unzip the file and run `allure open` command. The report includes test execution results, logs, and screenshots for UI tests.
```bash
unzip docs/allure-report.zip -d docs/allure-report
allure open docs/allure-report
```
***

## 🚀 Setup and Installation

### Prerequisites

- Python 3.12+
- Chrome browser (for UI tests)
- Access to the application API and web interface

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dvts1471/task.git
   cd task
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   ```bash
   brew install allure  # for macOS OR for other systems: https://docs.qameta.io/allure/#_installing_a_commandline
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your application credentials and URLs
   ```

   Required environment variables:
   - `APP_URL`: Web application URL
   - `BASE_API_HOST`: API base URL
   - `API_MODULE`: API module path (default: /api)
   - `API_TOKEN`: User authentication token
   - `LOG_LEVEL`: Logging level (default: INFO)

***

## 🧪 Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test Categories

```bash
# API tests only
pytest -m api

# UI tests only
pytest -m ui

# Critical tests only
pytest -m critical

# End-to-end tests
pytest -m e2e
```

### After test run Allure Report can be generated

```bash
allure generate
```
```bash
allure open
```

***

## 🏗️ Project Structure

```
task/
├── core/                          # Core (mainly abstract) framework components
│   ├── api/                       # API testing utilities
│   ├── ui/                        # UI testing components
│   └── utils/                     # Shared utilities
│       ├── driver_manager.py      # Selenium WebDriver management
│       └── logger.py              # Logging configuration
├── main/                          # Application-specific implementations
│   ├── api_clients/               # API clients for specific endpoints
│   └── ui/                        # UI page implementations
├── tests/                         # Test suites
└── docs/                          # Documentation and test artifacts
```
