C# Testing Notes

C# Scripting -> Framework
    - .NET Core is needed
        - https://dotnet.microsoft.com/download/dotnet-core
        - To check that .net is installed use the following command which should display the version being used
            - dotnet --version
    - Visual Studio Code is used but VS Community or another text editor can be used
        - If using VS Code the C# extension will be needed
        - Another extension being used is PackSharp
    - Once PackSharp is installed it can be used via the command palette
        - CTRL+SHIFT+P
    - In this case the option to be chosen is New Project -> Class Library
        - This will then have to be named and then hit enter
    - The integrated terminal will show the actual command that was used by PackSharp
        - dotnet new classlib --name <project name>
    - To create an NUnit Test project use the previous and select NUint 3 Test Project which is the following on the command line
        - dotnet new nunit --name <project name>
    - If creating projects these will need to be added to the solution file
        - The solution file will actually keep track of all your projects and your projects will keep track of all your dependencies
        - The solution file is rarely opened
        - To add projects to a solution use the following command
            - dotnet sln add <projects name>
    - After adding projects then the solution will have to be built using the following command
        - dotnet build
        - If everything is working there should be a build succeeded message
    - There maybe a need in VSCode for certain items to be added
        - There will be a message to add Required assets to build and debug
        - Once accepted this will generate a .vscode folder
    - To run tests use the following command
        - dotnet test

!! Filename
    - Filename and class name should match when class is public and is the only class in the file

Adding Selenium to project
    - Open command palette
    - Select PackSharp -> Bootstrap Selenium and then select the test project

Comparing Variables
    - When using driver.FindElement to find elements thy type of object returned is an IWebElement
    - This means that they cannot be compared to strings in an Assert statement
    - They way to solve this is to use a Text directive at the end of a driver.FindElement  ie -> .Text;

Scripting Problems
    - Scripting without optimisation strategies has several issues
    - Some of these are -> Repetition, Lack of Maintainability, Readability issues
    - These can be solved using what is called the Page Object Model

!!! Test Issues
    - Tests can fail for may reasons but some tend to repeat
    - Pages that are not maximised that need to be in order for elements to show
    - Popup elements such as accepting cookies

Page Object Model
    - It is a strategy to have 2 classes per Page
        - The first class can be the page map ie what is on the page
            - This should show what the user can do on the page
            - It can be the functions and methods that use the elements in the map to perform user actions
            - This can be thought of as a Page Map Pattern
            - Page Map Pattern is not required for the Page Object Model
        - 
!!! When making major changes to a project
    - It is best practice to clean up the project using the following command
        -  dotnet clean
    - Then do a rebuild using the dotnet build command

!!! When restore references does not show
    - This can happen after running dotnet build
    - Check the csproj files to ensure that there is a reference to the csproj file on which the project depends
    - This is similar to inheritance in OOP
    - In the the projects being put together the dependencies are as follows
        - Framework -> Royale -> Royale.Tests
    - Royale.Tests should have a reference  to the Royale csproj file and ...
        - This is in item group tags and is the following syntax
        - <ProjectReference Include="..\Royale\Royale.csproj" />

!!! Constructor
    - Shortcut to creating a Constructor
        - Type ctor and return twice
    - Constructor has to be the same name as the class

Lambda Operator
    - => operator (C# reference)
    - There are several different cases that this operator can be used for
    - It can represent a method which takes a parameter and returns the successor of it
        - For example x => x + 1

Abstract Class
    - This means that this class can only be inherited by other objects and it cannot be instantiated by itself
    - This means that it could be used on each page rather than just one

Commonalities
    - When objects have things in common, just like the pages, we call them base attributes or base properties

Virtual 
    - The Virtual keyword means that classes that inherit this class can override them to give them new functionality or new values

Override
    - When a class inherits from another class and the members names are the same
        - The inheriting class needs to override the inherited class using the override keyword

Last
    - When using the Last method have a using System.Linq in the file

Interfaces
    - Interfaces are rules or contracts that must be followed by any class that implements them
    - This can be very powerful to use as it guarantees that multiple classes will have the same method name or signatures

NUnit - [TestCaseSource]
    - https://docs.nunit.org/articles/nunit/writing-tests/attributes/testcasesource.html
    - This  is used on a parameterized test method to identify the source from which the required arguments will be provided
    - The data is kept separate from the test itself and may be used by multiple test methods

NUnit - [Parallelizable]
    - We can greatly improve our test run time by running our tests in parallel
    - https://docs.nunit.org/articles/nunit/technical-notes/usage/Framework-Parallel-Test-Execution.html

Test Filter Flag
    - When running dotnet tests there can be filters passed in for example a category
        - dotnet test --filter testcategory=cards
    - This will not work when using the same driver across all tests

!!! Driver
    - Tests cannot run in parallel due to sharing the instance of the WebDriver
    - This could be fixed by instantiating a new WebDriver within each test, rather than declaring it at the top of our class
        - There are however side effects to this approach
    - Creating a static or global WebDriver will not work either
        - This will not allow tests to be ran in parallel
    - The solution is to use a ThreadStatic attribute
        - https://www.xspdf.com/resolution/58492696.html
        - Each executing thread will have a separate instance of the field, and independently sets and gets values for that field
        - https://docs.microsoft.com/en-us/dotnet/api/system.threadstaticattribute?view=net-5.0

?? Operator in C#
    - This is what is called the null coalescing operator
    - https://docs.microsoft.com/en-in/dotnet/csharp/language-reference/operators/null-coalescing-operator

Adding Packages
    - This is done with PackSharp
    - Add a package and choose the folder 
    - This allows for finding a package using NuGet
        - NuGet is a package manager for .NET
        - https://www.nuget.org/
    - This use the following cli command
        - dotnet add <folder_name> package <package_name>

Newtonsoft JSON
    - https://www.newtonsoft.com/json
    - Popular high-performance JSON framework for .NET 
    - This can serialize and deserialize .NET objects

RestSharp
    - https://restsharp.dev/
    - This is a REST API client library for .NET

Deserializing
    - This is turning a JSON string into a C# object

Number of Workers
    - NUint allows for adding an argument for the number of workers to be executed at the same time
    - The command which is case sensitive is as follows
        - NUnit.NumberOfTestWorkers
        - dotnet test --filter name=card_is_on_cards_page -- NUnit.NumberOfTestWorkers=4
        - It is probably an idea to stick to 3 or 4 instead of 20 on a local machine which may not have the power

!!! Test cases
    - Despite writing a low number of tests (2) using TestCaseSource changes things
    - This is coming from an API with 93 cases
    - This means that there will be 186 tests from a single endpoint with 2 tests

!!! Default filter
    - Using the dotnet test command the default filter is by name for example
        - dotnet test --filter user_can_copy_the_deck

!!! Default webdriverwait timeout
    - The default timeout is 500 milliseconds. (Inherited from DefaultWait<T>.)
    - https://www.selenium.dev/selenium/docs/api/dotnet/html/T_OpenQA_Selenium_Support_UI_WebDriverWait.htm

Recursive
    - When setting recursive to true this will not only delete the directory but all of the subdirectories and files within it as well

Creating A directory use the following
    - Directory.CreateDirectory
    - This takes the necessary path passed in as a parameter

Writing 
    - Write a new line to a file using File.AppendText
    - WriteLine and Write are similar but Write will instead of making a brand-new line and then writing the text to it
        - It will append on the line that it is currently on

Logging
    - There are different types of logging to be considered
        - Logging as a step, as an informational message, as a warning, an error and logging a fatal break

NUnit
    - https://nunit.org/

Current Test 
    - A current running test is equal to TestContext.CurrentContext.Test.Name

OneTimeSetUp
    - https://docs.nunit.org/articles/nunit/writing-tests/attributes/onetimesetup.html
    - This attribute is to identify methods that are called once prior to executing any of the tests in a fixture

Race Conditions
    - It is defined as anomalous behaviour due to unexpected critical dependence on the relative timing of events
    - This is a way of saying that 2 or more things are trying to work with the same data at the same time
    - Bugs in race conditions are pretty hard to find

Lock
    - A Lock is a mechanism that forces the workers to wait in line until the current worker exits the Lock
    - This resolves race conditions

Config
    - Having a config file, that is essentially your settings file
    - This will not only centralize these options but make it very easy to make change which effect all test suites

Shortcut
    - To add properties use the following Shortcut
    - Type prop and hit tab (In some editors twice)
    - Typing propfull will generate full property

Maximising Windows
    - There are different ways of maximising a Window
    - One option is to pass a --start-maximized argument to the Driver Options
    - There is another way which is to call Driver.Manage().Window.Maximize()
    - The issue is that those methods may not work for Mac or Linux

Passing or Failing Tests
    - This will use the TestContext from NUnit
    - The full path is TestContext.CurrentContext.Result.Outcome.Status.
    - This will tell whether a test has passed or failed
    - This is used with TestStatus and can be .Passed effect

Screenshots
    - Uses the ITakesScreenshot Interface then Current for the driver
    - There needs to be a path to save the image file

WaitHelpers.ExpectedConditions
    - This is a package form DotNetSeleniumExtras
    - ExpectedConditions in OpenQA.Selenium.Support.UI is deprecated so is not to be used
    
