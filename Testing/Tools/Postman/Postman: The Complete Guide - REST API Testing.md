                    Postman: The Complete Guide
                    Course Notes
                    
                    
                    Section 1 - Introduction and first steps in Postman
Course overview 
  - A very brief high level overview of the course
  - There is real world API's being used
  - There is no course only material
  - There will be quizzes and assignments

Introduction and first steps in Postman
  - https://www.getpostman.com/
  - If you have the browser plugin remove it as it is now a standalone app
  - Postman is an easy to use tool and is ideal when writing an API
    - This is also true for testing popular API's not just newly written
  - It must be a restful HTTP api
  - It is recommended that you create an account when asked
    - This will allow you to save items that you are working on
  - A quick tour of the Postman tool
    - The first and most important tool looked at is the request builder
      - This will allow you to craft different requests using Postman
      - It will allow you to set HTTP methods, Address, Body, Headers, Cookies
    - Responses will be returned ASAP in the response section
    - Responses should be monitored closely
      - Various 4xx codes can indicate problems
    - There are 3 different ways of viewing responses
      - Pretty which will format returns like code
      - Raw which will show plain text
      - Preview which will be similar to html
      - There are options in each to view formats such as JSON, XML etc
    - The Postman tool has a lot of similarities to a web browser
    - The default method in Postman is GET
    - Postman allows for selecting protocols eg HTTPS
    - To add a second parameter to a query use the & character
    - Viewing parameters can be quickly done using the params button
    - Parameters can be rearranged or deleted which is very helpful for manual testing
    - Requests cannot be saved by themselves
      - Instead collections of requests can be saved
      - These requests can be renamed to make it easier to maintain them
    - Unsaved changes will have an orange marker to tell the user that they need to be saved
    - The drop down list of HTTP methods has a list of all available methods
      - The most regularly used request methods are GET, POST, PUT, DELETE and PATCH
    - Using the POST request will activate the body tab
      - This is because data can be sent with the body
      - There are 4 option available for sending form data
        - form-data and x-www-form-urlencoded basically mimic sending from a html form to a backend
        - The other 2 options are raw and binary
        - Most of the time the format will need to be JSON using the raw option
        - When making the request the server will recognise the JSON format
        - This will be shown in the response where the sent data will be returned under a JSON element

About this course
  - A quick review about the course and how to use the Udemy platform

Introduction and first steps in Postman Continued
  - A continuation of a simple demo of Postman functionality
  - Thus far the requests being sent are static
  - This is not relective of real world scenarios where requests will change frequently
  - Instead of using the GET or POST from the previous section this time uuid is used
    - This will generate a random uuid using GET
    - This can then be sent using the POST method
  - You can use variables within Postman
    - This can be done using the test tab
    - Although usually used for writing tests it can be used for writing code
  - After the request has been submitted the test part will be executed
    - The response body will then need to be extracted and saved to a variable
    - This variable can then be used with a new request and sent to a different end point
  - On the right of the test tab is the snippets panel
    - This provides several useful code snippets for common tasks
  - The snippet being used in this case is the set a global variable snippet
  - Once clicked there is code auto-generated
    - Syntax Example -- pm.globals.set("variable key", "variable value")
    - Used Example -- pm.globals.set("uuid", "foo")
    - Once executed this will have a global variable with an id of uuid and a value of foo
  - Values can be inspected using the eye button in the top right hand corner
    - This will show uuid and foo under the global variables section
  - Although these are still hardcoded thay can now be used in a POST request
  - Using variables in Postman is done with double parentheses
    - Syntax Example
        {
            "name": "John",
            "email": "john@example.com"
            "uuid": "{{uuid}}"
        }
    - 
  - 

The Postman Landscape
  -                     

Creating with API requests
Note about requestbin
  - The following lectures will be using an online tool called Requestbin.
    - http://requestbin.net/
  - It is recommended that students use this site
  - There is a caveat involved as this works differently than the videos show
  - There are also some other sites recommended
    - https://httpbin.org/
    - https://hookbin.com/
    - There is also an option to run an instance using Docker
      - https://github.com/Runscope/requestbin#deploy-your-own-instance-using-docker

Creating Requests
  - HTTP requests have 4 parts 
    - The request method such as GET, POST, PUT etc
    - The url where the request is to be sent
      - Using the requestbin site, you will need to create a requestbin
      - This will then generate a url which can be used for testing
        - In the video a paramterless request will return ok
        - Using now it will return an IP address
      - Reloading the postbin page will then show the methods involved and the headers as well as other information
      - After running postman with parameters in the request postbin will show the parameters as query string on the left of the page
      - By default what Postman sends is not urlencoded
        - If there are spaces between params sent they will be seen on requestbin with spaces
        - A single space that is url encoded is shown as %20
      - If you wish to url encode params being sent then you can right click and select encodeURIComponent
      - You can add descriptions to your postman requests
      - There is also an autocomplete available which will complete URL addresses being entered
      - Postman also supports path variables
        - Instead of having a user number eg user2, you could have :userid
      - It is good practice to check headers prior to send a request
    - Headers
      - These are also part of the request and have the form of a key-value
      - You can define your own headers as well as making use of your own
      - When you try to add a key you will get a drop down list of posssible pre-defined options
      - When selecting a header option if you send the request to requestbin it will show this option (after a page refresh)
      - The same goes for headers you are defining yourself
      - There are a number of headers that are automatically sent by Postman
      - Some of the headers that appear are from the request rather than Postman
    - Body
      - Body will only be visible for requests other than GET
      - form-data and x-www-form-urlencoded are very similar
        - This is similar to standard HTML forms being submitted
        - The difference will be that requests in urlencoded option will be automatically urlencoded
      - Postman will add a Content-Type to request
        - EG Form and Post parameters will show as will Content-Type: multipart/form-data
      - REST API's will expect requests in a certain format
        - This is usually JSON but some API's will accept other format eg XML
      - Binary is designed for info to be sent to your API that cannot be entereed into Postman
        - One example is an image file
        - Postman will give you an option to select a file which can then be sent to your server
      - When entering JSON pressing ctrl-b will automatically format the text properly
      - You cannot use form-data option for JSON you must use raw
      
Importing request from your browser
  - Importing complex requests with many parameters from your browser
  - The example uses the Trello which is a kanban application for todos
  - Also it is assumed that the request being made uses XHR
    - https://en.wikipedia.org/wiki/XMLHttpRequest
  - In the Chrome Dev-Tools Network panel
    - To open Dev-tools right click an element and select inpsect element, then select the Network tab 
  - Right click the sent request and the copy option and then copy as cURL
  - In the top bar select import and there is the option paste raw text and then import
  - Postman will fill the appropriate fields automatically


Inspecting Responses
  - It is hugely important to understand what is returned in responses
  - HTTP responses have 3 main parts
    - Status codes eg 200 is ok, 404 is an error code
      - This is very important as it indicates whether a request is successful or failed
      - Failed responses must be understood to be able to fix issues
      - Alongside status codes are response times and response sizes
        - Time responses cover the entire process
    - Body
      - Almost all body options refer to how the response is shown
      - Pretty will format raw text into a much more readable format
      - Preview will render html which may help make errors clearer
      - You can send and download images and Postman will render images
    - Headers
      - These will be shown as key and value
      - For known headers Postman on hover will offer more information
      - You can save requests which is useful for documenting API's

Cookies
  - Cookies are technically just a header
  - When sending a request header from Postman a sent-cookie header is part of the request
  - Set-cookie instructs the browser to save the cookie
  - In order to see exiting cookies Postman has the cookie manager
    - This is on the far right hand side of the params bar
  - Selecting the cookies option will show cookies for any domain you have sent a request to
  
 
Troubleshooting
  -

Saving Requests
  -


Writing tests and scripts
Introduction
  -

Your first test
  -

Testing an API
  -

Testing an API - Writing more tests
  -

Recap: Path parameters vs query parameters
  -

Refactoring Tests

