# Virtual Bank Dashboard Selenium Tests (In Progress)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-tested-green)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)


This repository contains frontend tests for the Virtual Bank Dashboard, written using Selenium. Since the tests interact directly with the DOM, they can be brittle — meaning if an element is removed or its selector changes, the test may fail.

To mitigate this, the test framework is structured into **three abstraction layers**:

1. **Page Elements** – where all raw selectors are defined.
2. **Page Objects** – higher-level classes that encapsulate actions on the page and reference selectors from Page Elements.
3. **Tests** – the actual test cases, which only call methods from the Page Objects.

This separation ensures that no raw selectors appear in the test logic, making it cleaner and easier to maintain.

---

### Why This Approach?

Imagine you have a form element with the ID `"profile_form"` and you reference it directly in multiple test cases:

```python
# Not ideal
self.assertEqual(driver.find_element(By.ID, "profile_form").is_displayed(), True)
```

If an admin later changes the ID to `"profile"`, every test that references `"profile_form"` will break.

Now, you might be tempted to use your IDE's search-and-replace to update all instances. However, this is risky, especially if other elements or variable names also include the word `"profile"` — it can lead to unintended changes even within the Python files themselves, potentially causing bugs or breaking test logic.

To avoid this, selectors are stored in one place (the Page Elements module). Page Objects reference those selectors using **dot notation**, e.g.:

```python
PROFILE_FORM.NAME_ID
```

If a selector changes, you only need to update it in the Page Elements file corresponding to page test — and all your tests will still work.

---

### Benefits

* 🔧 **Maintainability**: One place to update selectors.
* 🧪 **Test Isolation**: No business logic is tied to selectors.
* 📚 **Readability**: Tests read like clear, structured instructions.
* 🧱 **Scalability**: Adding or changing tests is straightforward and low-risk.


---

### 🧰 Setup Instructions

Follow the steps below to clone the repository, set up a virtual environment, install dependencies, and run the tests:

#### 1. **Clone the repository**

```bash
git clone https://github.com/EgbieAndersonUku1/virtualDashboardFrontEndTest.git .
cd your-repo-name
```

#### 2. **Create and activate a virtual environment**

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate.ps1
```

#### 3. **Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. **Run the tests**

If your tests are located in a `tests/` directory and follow standard Python unittest naming:
Make sure you are inside `virtual_bank_frontend_tests` folder

```bash
python -m unittest discover tests
```

Or run a specific test file:

```bash
python -m unittest tests/test_profile_form.py
```

---