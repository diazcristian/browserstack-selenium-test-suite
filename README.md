# browserstack-selenium-test-suite

Selenium test suite for BrowserStack, validating login, invite users, and logout functionality across multiple browsers in parallel.

### Directory Structure
    .
    ├── scripts/
    │ └── parallel.py                      # parallel execution of test cases across multiple browsers
    ├── requirements.txt                   # lists the required Python packages for the project
    ├── Jenkinsfile                        # defines the configuration and steps for the Jenkins pipeline
    └── README.md

### Test Suite Description

The suite contains a test doing the following:

- Log into www.browserstack.com using your trial credentials
- Assert that the homepage includes a link to Invite Users and retrieve the link’s URL
- Logs out of BrowserStack

Run across the following three browsers in parallel:

- Windows 10 Chrome
- macOS Ventura Firefox
- Samsung Galaxy S22
