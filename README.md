# browserstack-selenium-test-suite

Selenium test suite for BrowserStack, validating login, invite users, and logout functionality across multiple browsers in parallel.

## Directory Structure

project/
├── scripts/
│ └── parallel.py
├── requirements.txt
├── Jenkinsfile
└── README.md
## Test Suite Description

The suite contains a test doing the following:

- Log into www.browserstack.com using your trial credentials
- Assert that the homepage includes a link to Invite Users and retrieve the link’s URL
- Logs out of BrowserStack

Run across the following three browsers in parallel:

- Windows 10 Chrome
- macOS Ventura Firefox
- Samsung Galaxy S22
