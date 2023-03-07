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
    - Uhsaved changes will have an orange marker to tell the user that they need to be saved
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
