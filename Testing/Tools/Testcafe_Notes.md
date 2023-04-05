<b><p align=center> TestCafe Notes
  -
  - https://www.devexpress.com/products/testcafestudio/ (not open source)
  - TestCafe is a free and opensource NodeJS tool to automate e2e testing
    - It runs on Windows, macOS and Linux
  - It supports desktop, mobile, remote and cloud browsers
    - These can also be headless
    - Tests can also be ran in Javascript or Typescript
  - It is an alternative to other testing and automation solutions
  - It is easy to install with one command
  - It is a unique technology
    - It does not control the browser like Puppeteer/Webdriver
    - It is not a browser itself unlike cypress
  - The core is a proxy server which tansforms JS/HTML code to include automation code
  - There are several reasons to use TestCafe
    - Not having to worry about waiting for an element to load
    - Parallel testing in multiple browsers is simple
    - Supports BDD, data driven testing and Page Object Model
    - It is compatible with CI tools
<br /> <br />

End to End testing
  -
  - This is also known as E2E testing
  - This is a technique to test whether an application flows from start to finish behaves as expected
  - These tests simulate real world user scenarios essentially testing an app how a real user would use the application
  - The purpose of performing E2E tests is to identify dependencies and to ensure data integrity is maintained between systems
  - The benefits of E2E testing are
      - Verification that the entire system is working properly
      - Prevention of bugs or regression issues
  - There are a few different components of TestCafe
    - Client-server
      - There is no external driver needed in TestCafe
      - This allows for cross browser and multi-platform testing
      - TestCafe uses a url rewriting proxy instead of WebDriver
      - This injects the driver script that emulates user actions into a test page
      - TestCafe uses 10.0.75.1 when testing
      - There are reasons for using a server in TestCafe
        - A database or web service can be launched from the tests
        - Access can be gotten to the server file system to read data samples or check uploads
        - Tests can make use of all Node.js features and external modules
        - Tests became faster and more stable as test logic is now separated from the automation scripts
        - Test code can't interrupt the page execution, because TestCafe doesn't inject user-written code
        - The latest syntax features like async/await are supported also with TestCafe
      - TestCafe API
          - Test code uses TestCafe API methods to interact with the tested page
          - There are 3 main types of interaction
            - Select Elements
            - Perform actions
            - Execute assertions
      - Page Proxying
      - Isolated Tests
        - TestCafe isolates each test run from subsequent tests and tests that run in parallel.
        - After a test is completed, TestCafe resets the browser state by
          - Deleting cookies
          - Clearing both local and session storage
          - Reloading the test page
  - TestCafe Studio vs Open-source TestCafe
    - TestCafe Studio is a cross-platform IDE for end-to-end testing or end-to-end web testing
    - It is also multi platform and works in every browser including mobile
    - It has a lot of features such as
      - Visual test recorder, Cross-browser testing and Comprehensive reports with powerful code editor

Install TestCafe
  -
  - Needs to have NodeJS installed
  - VS is used but can be any text editor
  - To check npm version for installing packages
    - Enter the following command npm -v
  - Install the testcafe extensions available on the VSCode marketplace
  - Install the testcafe npm packages

TestCafe Example
  -
  - Initial test examples will use the TestCafe demo site
  - This will be replaced by a more real world example later
  - It is important for testers to understand async\await in Javascript
      - https://www.freecodecamp.org/news/async-await-javascript-tutorial/
  - Async\Await is used by TestCafe in all cases
  - TestCafe tests must be organised into categories that are called fixtures
    - A JS/TS file with TestCafe tests can contain 1 or more fixtures
    - To declare a fixture simply use the fixture function
        - fixture 'Authentication Tests' .page 'url'
    - To create a test call the test function a pass a function which contains the test code
      - The test code function accepts the test controller objectas a parameter
          ```
            fixture 'MyFixture';
            test('Test1', async t => {
              // Test 1 Code
            })
            test('Test2', async t => {
              // Test 2 Code
            })
          ```
  - Test controller 
    -
    - A test controller exposes the test API's methods and passing to each function that can run server-side test code.
    - Some examples of functions are  test, beforeEach or afterEach.
    - A test controller can be used to 
      - Call test actions
      - Handle browser dialogs
      - Use the wait functions
      - Execute assertions
    - The test runner also uses a test controller to access the internal context required for the test API to operate.

First Test
  -
  - Added tests folder and firstTest.js
  - Need to prefix testcafe command with npx to run on Windows
  - This maybe because local installs are not added to the path

Using Selectors with Elements
  -
  - The Selector API provides methods and properties to select elements on the page and get their state
  - TestCafe uses standard CSS selectors to locate elements
  - This is similar to using document.querySelector in JavaScript or FindElementBy.CSSSelector in Selenium Webdriver
  - In a test  before the fixture there is a need to import the selector from TestCafe
    - This is done using the import keyword
    - This will remove hardcoded selectors in the test script
    - An array can be used if there is a need to import different names.
  - Before the selector and after the import there can be constants added for the various selecor elements needed
    - These will replace the presently hardcoded values

Specify the Start Webpage
  -
  - The URL is being passed with the fixture but can also be added with the test
    - The test url can differ from the fixture url
    - The fixture url can be set to something like a base page or base url 
    - This is similar to multiple other frameworks
  - The test url will be ran when specified ahead of the fixture url
    - This overrides the fixture specified url

Fixture and Test Metadata
  -
  - TestCafe allows you to specify additional information for tests in the form of key-value metadata
  - You can display this information in the reports and use them to filter tests
    - One example is a command which runs tests whose metadata's device property is set to mobile, and env property is set to production
      - npx testcafe chrome my-tests --test-meta device=mobile,env=production
    - Again the npx is needed to run the tests on some Windows machines
  - Metadata can also  be defined for tests and fixtures
    - This uses fixture.meta and test.meta
  - To run a test file with specific environment such as production
    - npx testcafe chrome .\tests\testMetaScript.js --test-meta env=production
    - Running the tests with the additional options will run both tests in the file rather than 1 which matches metadata

Interact with Page Elements
  -
  - Navigate
    - TestCafe provides a set of actions that you can use to interact with the page including
      - Click, Navigate, Hover, Drag, Type text and more
    - This will navigate to the URL specified in the test fixture and then to the navigateTo URL
  - IFrame
    - This uses the IFrame test example found at -> http://the-internet.herokuapp.com/iframe
    - switchToIframe() switches the test's browsing context to the specified iFrame
    - switchToMainWindow() switches back to the main window from the IFrame
  - Dropdownlist & Upload file
    - How to select an option inside the drop-down list
    - There are usually 2 things to do in TestCafe with dropdown lists
      - Get the dropdown list to drop and then select an option
    - Again using the internet.herokuapp.com site for uploading an image
      - https://the-internet.herokuapp.com/upload
    - Uploading a file in TestCafe is done using setFilesToUpload() function
      - This needs to have a path to the file(s) to be uploaded
      - setFilesToUpload() with TestCafe automatically waits until the file is uploaded to the server
      - This means that there are no additional commands or libraries needed
      - Uploads can also be cleared with one function -> clearUpload()
        - This removes all the file paths from the specific file upload input
  - Set Test Speed
      - Tests can be ran very quickly which may not give time to see what is occurring
      - This is why there is a need to be able to reduce test speed
      - This makes use of the setTestSpeed method
  - Set Page Timeout
      - setPageLoadTimeout() specifies the amount of time within which TestCafe waits for the window.load event to fire before starting the test
  - Drag & Hover
      - drag an element to a specific offset using TestCafe
      - Example is a slider and it will be able to be dragged to a specific offset
      - This makes use of the drag() command from TestCafe
      - drag uses different offsets of X and Y of the mouse pointer
      - Hover -> hovers a mouse pointer over a webpage element

 Hooks 
  -
  - What are TestCafe Hooks
    - TestCafe allows you to specify functions that are executed before a fixture or a test is started or after it's finished. 
    - Test hooks override fixture hooks
    - If a test runs in several browsers then the test hooks are executed in each browser
    - A hook can be specified for each test in a fixture with the fixture.beforeEach or fixture.afterEach methods

Assertions
  -
  - TestCafe provides a comprehensive set of assertions
  - These are based on a behavior-driven development style or BDD style
  - In order to construct assertions the expected method of the test controller is used
  - In assertions the check is that the actual results are equal to the expected one
  - The equal() function is used
    - This takes the parameters expected, message, and options if we wanted to add anything else
    - The assertion query timeout can be specified in test code, with the options.timeout option
    - The assertion can only be tried or a timeout can be with the assertions, with options to timeout
  - There are different and a huge number of assertions methods with TestCafe including
    - ok, not ok
    - match, not match
    - within, not within
    - type of, not type of
    - contains, not contains

Skip Test
    - An additional feature with TestCafe is the ability to skip tests with one single configuration
    - Use the fixture.skip and test.skip methods for this
    - Also use fixture.only and test.only methods to specify that only a particular test or fixture should run while all the others should be skipped
    
Working with client-side information
  -
  - TestCafe allows for creating client functions that can return any serializable value from the client-side
    - This can be a current URL or custom data calculated by a client script
  - TestCafe has ClientFunction which needs to be imported like Selector
  - Using ClientFunction it is necessary to get window.location.href
    - This will always contains the current URL from the browser

Test execution
  -
  - TestCafe is designed to support most modern browsers
  - TestCafe automatically detects the popular browsers installed on a local computer
    - It is actively tested with 
      - Chrome with different versions, IE 11 +, Edge (legacy\chromium based), Safari, Firefox, Mobile (Saferi\Chrome)
  - To see which browsers are supported
    - testcafe --list-browsers
  - To run tests on all the local browsers using the following command
    - testcafe all tests
  - To run test on multiple browsers together
    - testcafe firefox,chrome,safari tests/firstTest.js

Run Tests in Parallel
  -
  - TestCafe allows for executing tests concurrently
  - In concurrent mode, TestCafe invokes multiple instances of each browser
    - These instances constitute the pool of browsers against which tests run concurrently
    - For example, each test runs in the first available instance
  - To enable using concurrency use -c or --concurrency at the command line
    - npx testcafe -c 5 chrome .\tests\testOnlyTest.js
    - This invokes 5 instances of Chrome and runs the tests concurrently
  - TestCafe concurrenncy means running or splitting the test with different concurrency
    - This is not repeating the test with the same or with each instance
  - Concurrency can also be used with testing against multiple browsers
    - npx testcafe -c 5 chrome,firefox .\tests\testOnlyTest.js
  - Live Mode
    - Live mode ensures TestCafe and the browsers remain active while working on tests
  - Use -L or --live flag to enable live mode from the command line interface
    - npx testcafe chrome .\tests\testOnlyTest.js -L
  - After entering the test to be ran in live mode there are some commands available
    - Ctrl+S to stop the test run
    - Ctrl+R to restart the test run
    - Ctrl+W to enable or disable watching files
    - Ctrl+C to quit the live mode and close the browsers
  - With live mode, changes can be made to anything in the script, and after that, the test will run again automatically and take the change
  - Concurrent test execution is not supported in Microsoft Edge

Filter Tests By Metadata & Name
  -
  - Tests and fixtures can be filtered by metadata
    - testcafe chrome ./tests/ --fixture-meta device=mobile,env=production
      - To filter fixtures with specific data, use the --fixture-meta argument
    - testcafe chrome tests/testMetaScript.js --test-meta env=production
      - runs the specified test 
  - Tests and fixtures can also be ran by name
    - testcafe safari ./tests/HooksTest.js -t "First Test"
    - The t option is added to add a test by name which is specified in a string at the end of the command
    - This can also be done in the runner.filter method

Headless Mode
  - Headless mode can be very useful when running CI servers
  - This consumes less resources as there is no GUI
  - Use the :headless parameter to launch a browser in headless mode.
  - This can be ran with either firefox or chrome
    - testcafe chrome:headless tests/firstTest.js
    - testcafe firefox:headless tests/firstTest.js
  - Headless is not available with Safari

<br /><br /><br />

<h1><p align=center>Deep Dive With TestCafe</h1><br /><br />
  
Wait Mechanisms
  -
  - There are different mechanisms with TestCafe for the wait, for actions, or with selectors or assertions
  - TestCafe has a built-in automatic waiting mechanism
    - There is no  requirement for a dedicated API to wait for redirects or page elements to appear
    - These mechanisms work when TestCafe performs test actions, evaluates assertions and selectors, sends requests, and navigates the browser
  - Wait Mechanisms for actions
    - TestCafe automatically waits for the target element to become visible when an action is executed
    - TestCafe tries to evaluate the specific selector multiple times within the timeout
    - If the element does not appear the test will fail
    - The timeout option to specify the selector timeout in the test code
      - This can be done 2 ways
        - Pass the timeout to the runner.run API method or add it on the cli
  - Wait Mechanism for Selectors
    - Using a Selector TestCafe will automatically wait for an element to appear in the DOM
    - There is also a way to  require that TestCafe should wait for an element to become visible
      - This uses the the visibilityCheck selector option 
  - Wait Mechanism for Assertions
    - TestCafe assertions use a Smart Assertion Query mechanism
    - This is activated when a selector property or a client function as an actual value is passed
    - When an action triggers a redirect, TestCafe automatically waits for the server to respond
    - The test continues if the server doesn't respond within 15 seconds

Debugging
  -
  - There are different ways to debug our test cases with TestCafe
  - The first method is to use Debug Mode
    - Add --debug on the command line
      - A debug can also be added in a test using debug()
    - After this is added the test being ran is started in debug mode
    - This allows for checking step by step on what occurred during the test
    - In this mode, test execution is paused before the first action or assertion
      - This is to allow invoking the developer tools and the debug
    - When the test execution reaches t.debug that was already added in a test
      - The test pauses to allow opening browser developer tools
      - This will allow for checking page state, DOM elements, location, their CSS, and more
      - In the broswer window the footer displays a status report in which test execution can be resumed or skipped to the next action
    - Debug Mode on Fail
      - This is where a test is setup to automatically enter debug mode on failure
      - It is done using the command line parameter --debug-on-fail
      - npx testcafe chrome .\tests\testOnlyTest.js --debug-on-fail
    - Use the Unlock page switch in the footer to unlock the tested page and interact with its elements
  - Taking Screenshots
    - This can be done on failure or during tests
    - A screenshot can be either the entire page or with an element
  - An additional feature is the ability to record videos
    - Again this is done in TestCafe natively without a need to use an external API

Take Screenshots
  -
  - There are some prerequisites for Screenshots
    - TestCafe allows for taking screenshots on the tested webpage at any moment during a test run or automatically whenever a test fails
    - Screenshots required .NET 4.0 or newer install on Windows machines
    - Use t.takeScreenshot to take a screenshot of the entire page, or t.takeElementScreenshot action to capture a particular element.
    - Screenshots are not supported when you run tests in remote browsers
    - Using -s can be a shortcut for screenshot

Video Recording with TestCafe
  -
  - TestCafe allows you to record the videos of test runs, but we should install the FFmpeg library to record the videos
  - If FFmpeg is not installed it can be using npm 
    - npm install --save @ffmpeg-installer/ffmpeg
  - The videos that are generated are then saved in MP4 format
  - To enable the video recording add --video to the cli command of the test run
    - To keep videos together setup a videos folder and an artifacts folder to hold all test related artifacts
  - Video will not run in VS code but folder can be opened and video should run
  - To run only when tests are failing use the following options 
    - npx testcafe chrome .\tests\elementScreenshotDemo.js --video artifacts/videos --video-options failedOnly=true
  - There are a few options that TestCafe supports for videos
    - failedOnly -- When true records failed tests only
    - singleFile -- When set to true saves recordings as a single file

Visual Studio Code Extensions
  -
  - Testlatte is already installed
  - There are code snippets available having installed the extensions
  - There are multiple different options available for the different code blocks
  - Tests folder will need to be renamed to test to use the test runner

<h1><p align=center>Pages</h1><br /><br />
  
Page Model
  -
  - Page Model is a test automation pattern that allows you to create an abstraction of the test pages
    - This allows is to be used in the test code to refer to the page element
  - Why use the Page Object Model or Page Model
    - There are several problems which using the Page Object Model solves
      - Changes in locator names will need to be adjusted in multiple file as there is no shared file
      - Code duplication coming from repetition
      - Difficulty in maintaining due to large amounts of unnecessary files 
  - In this model classes are created for each page in the application
    - The class then has web page elements, also add the methods which perform actions or operations on those elements

Important
  -
  - Chrome may fail tests due to screen not being maximised
  - Firefox still has the same elements available in a reduced size window
  - Use the maximizeWindow() command
  - May need to use this inside await functions on occasion if some elements are not being seen

TestCafe uses the .testcaferc.json configuration file to store its settings
  -
  - Settings specified when running TestCafe from the command line and the programming interfaces override settings from .testcaferc.json
  - Keep .testcaferc.json in the directory from which test cases are ran

Data-Driven Tests with TestCafe
  -
  - Data-Driven Tests is a procedure when you repeat the same scenario with different input parameters
    - The results are then verified with the output values
  - Test data is always an important part of automated tests
    - Test data is not just the value or the text in the application, but it's about the whole environment being tested
    - Usually hardcoded data such as a URL is used 
    - Hardcoded data though is not configurable
  - Test data allows for different scenarios to be tested
    - For example a form allowing positive and negative reviews
    - Data can be in different formats -> JSON, XLS, CSV to name a few

<br /><br /><br />

<h1><p align=center>Behaviour Driven Development</h1><br /><br />
  
Introduction to BDD and Cucumber JS/HTML
  -
  - Behavior-Driven Development is a technique for building software in which the product owner, developers, and the testers collaborate together 
    - This is so that they can agree about the acceptance criteria
  - The Behavior-Driven pattern is improving communication and collaboration between teams
  - Similar to TDD or Test-Driven Development, which starts development by writing test cases
    - BDD is similar but start by writing the business features file prior to writing the automated test cases
  - When writing features use plain English sentences and the Gherkin language
  - Step Definition file
    - To start implementing the steps from the feature file in real code
  - To run tests using the Cucumber file
    - ./node_modules/.bin/cucumber-js
  - In order to run multiple sets of data scenario will have to be changed
    - This will change to Scenario Outline 
  - The final item that can be added are Tags
    - Add a tag to the scenario eg e2e and then run from the cli
    - ./node_modules/.bin/cucumber-js --tags "@e2e"
  - Cucumber HTML report
    - npm i cucumber-html-reporter
    - This will integrate html reports on testing
  - Adding entry to package.json to run testcafe cucumber is not working so full command is needed
    - ./node_modules/.bin/cucumber-js --tags '@e2e' --format json:reports/report.json
  - To see generated report 
    - node <file_name> 
    - In order to see the html version there will need to be a cucumber_report.json file presently
    - These can be created blank and the cli can be change to point to the correct file like such
      - ./node_modules/.bin/cucumber-js --tags '@e2e' --format json:test/report/cucumber_report.json


<br /><br /><br />

<h1><p align=center>Reports</h1><br /><br />
  
TestCafe Reports
  -
  - Reporters are plugins used to output test run reports in a certain format
  - Reporter plugins are npm packages
  - TestCafe ships with multiple Reporters
    - spec (default), xUnit, JSON, List, HTML, Allure Report
  - To install the TestCafe HTML reporter
    - npm install testcafe-reporter-html 
  - After installation the reporter can be ran from the cli
    - npx testcafe firefox .\tests\RegistrationSteps.js --reporter html
    - This will send HTML to the console by default
  - In order to generate a HTML file there is an additional command needed
    - npx testcafe firefox .\tests\RegistrationSteps.js --reporter html:report.html
  - Open command does not exist on Windows platform
    - start can be used instead
    - To start the report file use start report.html
    - This will open the file in the default browser

Allure Reports
  - To install the Allure reports package
    - npm install testcafe-reporter-allure
  - To run the Allure reporter
    - npx testcafe firefox .\tests\RegistrationSteps.js --reporter allure
  - After running there will be an Allure folder generated holding the results
    - The results files will be in XML
  - After this then the Allure command line module will need to be installed
    - npm install -g allure-commandline
  - To then view the allure reports
    - allure generate allure/allure-results --clean -o allure/allure-report && allure open allure/allure-report
  - There will be an issue using the concatenated command to generate the report and open
    - As above the open command cannot be used so start will be needed
    - Also instead of double ampersnad separators && instead use a semi-colon

<br /><br /><br />

<h1><p align=center>Visual Testing</h1><br /><br />
  
Visual Testing With Applitools and TestCafe
  -
  - Applitools provides a software testing platform, powered by Visual AI, or artificial intelligence
    - It can be used by test automation, manual QA, and DevOps teams
  - Applitools SDKs work with existing test frameworks to take screenshots of pages, elements, regions, or iframes, and upload them along with DOM snapshots
  - Applitools AI then compares them with the previous test executions' screenshots, like Baselines, and reports if there is a bug or not
  - There is a need for a free account with Applitools
      - Using Github to signup is allowed
  - There is a need to get an API key to use in projects

Adding Eyes-TestCafe to Existing Tests
  -
  - The Eyes-TestCafe package will need to be installed
    - npm i -D @applitools/eyes-testcafe

Github Actions
  -
  -  GitHub Actions make it easy to automate all your software workflow
    - This now has world-class CI/CD, or continuous integration and continuous delivery
  - You can build, test, and deploy your code right from GitHub
    - As well as the ability to make code reviews, branch management, and the issues management work the way that you want
  - Run a workflow on any GitHub action, like kick-off workflows with GitHub Actions events like push, issue creation, or a new release
  - Combine and configure actions for the services you use, built, and maintained by the community

What is the GitHub Actions workflow?
  -
  - Workflows are custom automated processes that you can set up in your repository to build, test, package, release, or deploy any code project on GitHub
  - Workflows run in Linux, macOS, and Windows, and containers on GitHub-hosted machines
  - You can create a workflow file configured to run a specific event - like every pull request, scheduled, or manually

Create a Github Account
  -
  - https://github.com/
  - A free github acccount will be needed to be able to use Github actions
  - There are complete set of notes on github functionality available at the following address
    - https://github.com/marb61a/Course-Notes/tree/master/Testing/Tools/Git/Step%20By%20Step

YAML Files for GitHub Actions
  -
  - https://yaml.org/
  - YAML is a human friendly data serialization standard for all programming languages
  - To start to setup actions select the actions tab inside the GitHub repo 
  - Most of the time GitHub will auto-detect the file type and will suggest workflows for them
  - There are some of the steps that can be skipped
  - Comment lines are part of the Yaml file but again are not needed
  - The Github marketplace is a place to get plugins to extend Github
    - https://github.com/marketplace
  - There is a plugin needed to run TestCafe tests
    - There are a couple available actions available 
    - Install TestCafe and Run Tests are the actions needed
  - The checkout action fetches the repository
  - The uses action in the yaml file installs the needed package
  - After proposing a new to start a commit a PR or pull request can be made

Run with multiple OS and NodeJS versions
  -
  - This will again make use of the above processes
  - The example will also use something called the strategy and matrix
  - A matrix is a set of keys and values that allows you to spawn several jobs starting from a single job definition
  - This is done inside the strategy sections 
  - Depending on the project needs it may be necessary to make a branch for the yaml file
  - In the build definition the strategy section can be add like below
  - strategy:
    matrix:
      os: [ubuntu-latest, windows-latest]
      node: [8, 10, 12]
  - This will use both multiple versions of Node and multiple OS versions

TestCafe Docker image
  -
  - Docker is a tool that allows developers or system admins to easily deploy their applications in a sandbox
    - https://www.docker.com/
    - These are called containers and will run on a host operating system
  - Docker is that it allows users to package an application with all of its dependencies into a standardized unit for software development
    - Unlike virtual machines, containers don't have high overhead and hence enable more efficient usage of the underlying system and resources
  - What are containers?
    - Previously virtual machines wered used to run applications
    - VMs run applications inside the guest operating systems, which run on virtual hard powered by server host OS
      - VMs are great at providing full process isolation for applications
    - There are very few ways a problem in the host operating system can affect a software running as a guest operating system
      - This is true vice versa but VM isolation can be expensive resource wise
    - Containers take a different approach by leveraging the low-level mechanics of the host operating system
      - Containers provide most of the isolation of virtual machines at a fraction of the computing power
    - Why use containers
      - Containers offer a logical packaging mechanism in which applications can be abstracted from the environment in which they run
      - This decoupling allows container-based applications to be deployed easily and consistently regardless of the target environment
      - This gives the developers the ability to create predictable environments that are isolated from the rest of the application and they can be run anywhere
  - Installing Docker
      - There will be different ways of installing Docker on each platform
      - https://docs.docker.com/docker-for-windows/install/
      - To check if installation is successful use the following command
        - docker info
        - This should show all the details about the Docker desktop version - the containers, images, and all the info that's related to Docker
  - Download TestCafe Docker Image
    - To download the TestCafe Image with Docker use the following command
        - docker pull testcafe/testcafe
        - This will download the latest version from TestCafe Docker Image 
    - The latest Docker image contains all the dependencies you need to run TestCafe
      - The image includes the Test Cafe executable for running tests and this also includes recent versions of Firefox and chromium-browser to run your tests
      - Tests can be ran in headless mode or normal mode since the image is set up with the XVFB display server
      - This display server allows you to use functionality like taking a screenshot during your test runs
    - When you run the test using Docker image, you want to see the browser open up and run your test, even in Normal mode
    - Running a graphical interface using Docker on your desktop such as a web browser, requires additional configuration to allow Docker to use your desktop display server
    - This may be a complicated solution and varies by system
  - Running your tests inside TestCafe's Docker Container
    - To run the test to inside the Docker container use the following command
      - docker run -v ${TEST_FOLDER}:/tests -it testcafe/testcafe ${TESTCAFE_ARGS}
      - ${TEST_FOLDER} is the local folder for our tests
      - /tests is the folder that we need to copy our tests inside the Docker container
      - Then there is a need to name the version of the container with TestCafe
      - After that the TestCafe arguments can be passed such as the browser name, the test file etc
    - Just mention that we can run on Chromium or Firefox because the Docker container just includes these two browsers 
      - It does not include the Chrome browser

Run Tests on a remote device
  -
  - Run Tests on a Mobile Device (Remote)
    - To run tests on a remote mobile device, the device must have network access to the TestCafe server
    - The first thing needed is to create a remote browser connection
    - After that, TestCafe generates a URL to open in the browser that needs to be tested
    - This URL is exposed through the API or displayed in the console
    - To access this URL from the desired browser, it then connects to the TestCafe server and starts the test
    - When running tests in the browser desired the is no screenshot taking or resizing the browser window
    - The steps for running tests on a mobile device are
      - Open the console and type a command to run the tests with remote as a browser alias
      - Add --qr-code flag to generate a QR code for the mobile device
    - An example command is as follows
      - testcafe remote tests/test.js --qr-code
      - testcafe remote means that it will run on the remote device
      - The test needed to be ran is passed and the QR is then output to the console
    - Scan the QR code with a mobile device that has network access to the TestCafe machine or TestCafe server, and open the link
      - TestCafe will then start tests in the mobile browser
    - Then like the example above run the code on the remote browser
    - After clicking enter the QR code will need to be minimised so that it can be scanned with mobile
    - San the code and there shoul be an option open the website
    - Once opened we'll be connected with TestCafe, because we are on the same network
    - After the webpage is opened and the test has passed the results are sent to the TestCafe cli
    - At this point the mobile is then disconnected
 
 Report Portal
  -
  - What is ReportPortal?
    - ReportPortal is a service that provides increased capabilities to speed up result analysis and reporting through the use of built-in analytics features
    - It can be a great addition to continuous integration and to the continuous testing process
    - Some of the main features of ReportPortal are
      - Platform integration, ReportPortal integraes very quickly and easily with Jenkins, Jira, BDD process, majority of functional and unit testing frameworks
        - Real-time integration provides businesses the ability to manage and to track execution statuses directly from the ReportPortal
        - Test case execution results are stored following the same structure used in reporting suites and test plans 
        - Logs, screenshots, binary data, the execution pipeline of certain test cases are also available
      - Collaborative analysis as ReportPortal allows for analysing test automation results
        - Particular test cases can be associated with a product, a bug, an automation issue, a system issue, or can be submitted as an issue
      - Historical data of test execution
        - ReportPortal provides enhanced capabilities along with auto result analysis by historical data of test execution and automatic analysis with each execution
          - It automatically figures out the root cause of a fail
          - Test results can be flagged and an engineer can be alerted about an issue to see if further actions are required
  - What technologies are used with ReportPortal?
    - As the is a need for high performance and a high load rate can be expected cutting edge technologies are used
    - These include PostgreSQL, REST Web services, and mobile responsive UI
  - Installation steps with Docker
    - To be able to run ReportPortal locally, there is a need to use Docker Engine or Docker Compose
    - The first step is to make sure that these are installed
    - The following command can be used
      - curl [https://raw.githubusercontent.com/reportportal/reportportal/master/docker]
          (https://raw.githubusercontent.com/reportportal/reportportal/master/docker) -compose.yml -o docker-compose.yml
    - To then start the application use the following command
      - docker-compose -p reportportal up -d --force-recreate
      - -d is the detach mode
      - --force-recreated is for when ReportPortal has been installed previously, it needed to be recreated from the beginning
    - After this the open the web browser the IP address of the deployed environment is needed as well as port 8080
        - If local then it is localhost:8080
  - Install and Run ReportPortal with Docker
    - https://reportportal.io/
    - https://reportportal.io/installation
    - Install using Docker
    - Firstly make and change into a directory
    - Then use the following command to download the docker compose file
      - curl [https://raw.githubusercontent.com/reportportal/reportportal/master/docker]
            (https://raw.githubusercontent.com/reportportal/reportportal/master/docker) -compose.yml -o docker-compose.yml
    - Return to the URL then start the application use the following command
      - docker-compose -p reportportal up -d --force-recreate
    - There are default password available when installation is complete
  - Configure ReportPortal with TestCafe
    - The npm module for ReportPortal TestCafe needs to be installed 
      - npm install testcafe-reporter-reportportal
    - When running from the command line a reporter can be specified using --reporter
      - Example -> testcafe chrome 'path/to/test/file.js' --reporter reportportal
    - A .env file can also be created by adding the following required variables for the ReportPortal
    - This .env file needs to be at the root of the project
