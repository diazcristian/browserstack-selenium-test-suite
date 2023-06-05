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

## Local Testing

To test the code locally, follow these steps:

1. Clone the project repository to your local machine:

```
git clone https://github.com/diazcristian/browserstack-selenium-test-suite.git
```

3. Create and activate a virtual environment (optional but recommended):

``` 
    python3 -m venv bsenv 
    source bsenv/bin/activate
```

4. Install the project dependencies:

``` 
pip install -r requirements.txt
```

5. Set up the necessary environment variables:

- `BROWSERSTACK_USERNAME`: Your BrowserStack username.
- `BROWSERSTACK_ACCESS_KEY`: Your BrowserStack access key.
- `BROWSER_STACK_EMAIL`: Email to loging in Browserstack
- `BROWSER_STACK_PW`: Password to loging in Browserstack

You can either set these environment variables on your operating system or create a `.env` file in the project's root directory and define them there.

6. Run the `parallel.py` script:

```
python3 scripts/parallel.py
```

## Jenkins Configuration

If you want to set up and run these tests in Jenkins, follow the Jenkinsfile code provided in this repository.
