  ightwatch Js
    - https://nightwatchjs.org/
    - Nightwatch JS is an E2E testing framework written in Node JS
    - Nightwatch and Chromedriver are needed and can be installed via NPM
        - npm install nightwatch chromedriver
Setup Nightwatch
    - Nightwatch requires having a nightwatch.json configuration file
    - This file will have the base configuration
    - On some systems the base configuration will have an error
        - The following line will need to be added for the server path declaration 
        - 'server_path': require('chromedriver').path
        - There is also a need to add a nightwatch.conf.js file in some instances
        - This seems to be on Windows platform and the js file should be in the root of the project

Test Runners
    - Nightwatch has its own test runner and assertion library 
    - Other frameworks have a lot of dependencies that you will have to install and tie together
    - A file can begin with module.exports to define an object
        - The test name is then defined within the object
            - This will be a function which accepts an argument
            - The argument is the browser object but you can define it to use any name
    - A specific test can also be ran
        - ./node_modules/.bin/nightwatch -t ./tests/<test_name>
        - In this case -> ./node_modules/.bin/nightwatch -t ./tests/nightwatch.basic.test.js
    - Mocha
        - Nightwatch gives users the option to use the Mocha BDD (Behavior Driven Development) interface to write your tests using their default test runner
        - Since version 1.3, Nightwatch has created their own Mocha interface that users can use so they would no longer have to create a config file 
        - nightwatch_mocha.json file is needed to be able to add test_runner to

Elements
Finding Elements
    - Nightwatch provides many different ways to find elements
    - The base way is the element function
        - element returns a web element JSON object
    - The .elements() function searches for multiple elements and returns the web element objects for those
        - This is the same as element but for multiple elements instead of singular

Element Interaction
    - There are a few methods that can be used for element interaction
        - clearValue -> this clears a text field that maybe under test
        - click, keys, moveToElement, setValue
        - moveToElement basically moves the cursor to a particular XY offset on the browser
        - click as expected clicks on a specified selector

Element State
    - Looking at 3 main methods
        - getText(), getValue(), isVisible()
    - getText() returns the visible text for an element
        - It requires a selector and a callback as parameters
        - This will return an object unless just the value is returned
    - getValue() is very similar to getText()
        - getValue works for form elements though and getText does not
        - This means that getValue will be needed for getting values that are within the form fields
        - setValue can be used to set a value in the field being tested if necessary
    - isVisible() will just determine if an element is visible or not
        - It will return either a true or false
        - If the element is visible there will a true returned

Navigation
    - init() function is an alias to the URL command that is used to navigate to a URL
        - In the nightwatch.json file there can be a launch url specified
        - This is added under default and is the base url for navigating to
    - url() is used to navigate to a specific URL
    - back() and forward()
        - As to be expected this navigate backwards and forwards in the browser
    - getTitle() returns the title of the current page
    - refresh() basically refreshes the current page
        - This can be useful when doing something on a page that needs to be refreshed in order to be shown
    - urlHash() this adds a specified hashtag to our current launch URL
        - The value should be seen in the url when test is ran

Actions
User Actions & Prompts
    - keys() this method sends a sequence of strokes to an active element
        - Different keys can be referenced through the Nightwatch client.Keys object
            - This is an uppercase K
        - There are some predefined keys based on the W3C WebDriver draft spec
        - An issue however is that Nightwatch, in their documentation, did not actually give a list of the available keys
        - The way to see keys is to create a file that will send the Keys object to the console
            - console.log(JSON.stringify(client.Keys, null, '\t'))
        - This may be added to documentation in the future

Mouse Interaction
    - This will make use of the .mouseButtonClick() command
    - This can be either right or left click or double click or even hold the button down
    - Using moveTo will need screen coordinates

Navigation
    - There are several different navigation methods available in Nightwatch
        - get the window position (getWindowPosition)
        - get the window size (getWindowSize)
        - maximize the window (maximizeWindow)
        - fullscreen window (fullscreenWindow)
        - open new window (openNewWindow)
        - get a window handle (windowHandle)
        - switch between windows (switchWindow)
    - When using the switchWindow command the results are in an array
        - To switch to the second window it will be window[1] as an array starts at 0

Alerts
    - There are methods provided by Nightwatch for interacting with Alerts
        - acceptAlert() which accepts the current display alert
        - dismissAlert() which is the opposite of acceptAlert()
        - There is also getAlertText() and setAlertText()

Asserts
Expect and Assert
    - There are two built-in Assertion libraries in Nightwatch
        - These are Assert and Expect
    - The Expect library is based on the Chai Assertion Library
        - https://www.chaijs.com/api/bdd/
        - This provides a lot of flexibility and capabilities that the Assertion library does not
        - This is because the Assertion library only extends the Node.js assert module, which only has limited assertion
    - One of the benefits of using the Expect API is being able to use language chains which improves readability of assertions
        - There are multiple chains that can be used -> to, be, is, and , has, at, does and of to name a few
        - This chained language does not affect the assertions other than better readability
    - There are 2 namespaces in the Assert library
        - Assert and Verify, either of which can be used
        - These can be used interchangably but there is a slight difference
            - If an assertion fails while using the assert, it will stop the test case and ignore all other assertions
            - On the other hand if using Verify it will log the failed assertion and execute the others
    - Choosing which to use can be a matter of personal preference

Assert 
    - This will use the Assert library
    - value() and valueContains() differ slightly
        - When comparing expected values if value() is used then it must match
        - Using valueContains() needs only a partial match eg Ste from Stephen
    - urlEquals() saves writing a method to get and compare a url
    - assert.title() which will assert the title of our current page by using the assert library
!!  - Ensure that casing of letters is correct
    - assert.attributeContains() which checks if the given attribute of an element contains the expected value
    - assert.containsText() will  check if an element contains text
        - This include checking the text on a button
    - assert.cssClassPresent() verifies whether a CSS class is present or not
        - This can be very useful where there are different element states
        - For example something may be activated by a class and there is a difference which needs to be verified

Expect
    - There are 3 methods which should be remembered
        - .equal(), .contain(), or .match()
        - The first 2 are used in many test cases
        - match() can be used to verify a certain pattern
        - These methods will perform assertions on a specific target on the current element
    - Also available in the Expect Library are startsWith() and endsWith()
    - The not() method will negate any assertions
    - Using the before() and after() methods will add retrying capabilities
        - The time involved will be specified in milliseconds
    - There are many things that can be checked including
        - Check for element visibility
        - If an element is present, or if it's enabled
        - If an element is active
        - It there is an attribute present and if it has a particular value
        - What the element type is using a() or an()
    - There can also be a count of the elements using element()

Tests and Global Hooks
    - Nightwatch provides the standard before, after, beforeEach, and afterEach hooks to be used in tests if needed
    - Most testing frameworks, if not all, have hooks that can be used
    - The before() is run before the suite gets executed
    - The after() is the opposite of the before() method and runs after suite execution
    - The beforeEach() is ran prior to each test in the suite
    - The afterEach() is ran after each suite test
    - Nightwatch makes the same set of hooks per test suite available globally
        - These hooks are outside the scope of a test
    - In order to use the global hooks there needs to be a globals path defined in nightwatch.json
    - Global hooks expect a callback function
        - The global before() hook can be beneficial for things like starting a server prior to test execution
        - The global after() hook is executed at session end and is the same as closing the selenium session
    - The beforeEach and afterEach are executed before our test suite, and it has access to the browser instance

Tests
Page Object
    - Transforming existing tests to make them use the Page Object Model
        - This is a way of making code reusable and avoiding repetition
        - It also makes test suites much easier to maintain
        - Page object does make it very easy to encapsulate the different Nightwatch methods
    - To use page objects it is necessary to specify a page_objects_path within the nightwatch.json file
        - "page_objects_path": [ "pages" ] where pages is the folder in the project root
    - The basic structure of a page object in Nightwatch should include certain items
        - elements, which is an object
        - commands, which is an array
        - url, which can be a function or a string
            - The page object can resolve this string or a function by using the object.Navigate function
    - Elements can be defined outside of modules
        - This will be down to the personal preference of the tester
    - There are a couple of ways of defining elements
        - Shorthand and Longhand
        - Shorthand would just be the selector name
        - Longhand would be an object with 2 keys, a selector and a locator strategy
        - XPath can also be used to define an element
        - By default, Nightwatch uses css_selector as the locateStrategy
        - This is why the Shorthand version works as explicit definition of locator strategy is not needed
    - Within the page object, we can access the elements by using the @ sign
        - For example @leftFormName, and Nightwatch will automatically resolve this name to this selector
    - Commands will be defined in an object
        - These objects can be contained in an array
    - Sections is where there are different sections defined within the page object
        - Elements and commands can be defined in sections
        - These will only be in scope in the section where they are declared
        - To access the section it will have to be defined in the test file
!!  - Remove unnecessary page refreshes as they may cause failures

Mocha Data Driven
    - Writing a test using  Mocha test runner and also using the page object
    - In Mocha there is a describe function which holds a suite of tests
    - Nightwatch already has its own built in test runner but there are reasons for using Mocha
        - There is the very familiar syntax
        - Mocha supports dynamic test creation so tests can be created dynamically alongside dynamic data assertion

Debugging
    - Nightwatch gives the .pause() method to help when we need to debug tests
    - The pause() method suspends the test for a given number of milliseconds 
    - If unspecified how long a test is to pause for, then the test will suspend indefinitely 

Reporting
    - By default Nightwatch has 2 reporters available
        - stdout which is what appears in the terminal
        - JUnit which has XML output
    - There is also the option to create a custom reporter
    - A custom reporter can be created by using the keyword reporter in globals file
        - This reporter has two arguments: results and the done callback
        - The results object has all the information that Nightwatch has gathered from our tests
        - This information can be used to either store the data or parse the data to be used by another system
!!  - Node has a built in FS module which can be used to write to a file
