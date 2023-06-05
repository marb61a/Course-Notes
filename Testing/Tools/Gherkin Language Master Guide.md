<b><p align=center> 
Gherkin Language - The Master Guide </br>
Course Notes
    
<br />
<h1><p align=center> Course Introduction</h1></ br>


1. Introduction
    -
    - A quick welcome to the course
    - The Gherkin language is a very popular in the industry 
    - It can be used to gather business requirements and concisely write user stories, acceptance tests
    - Whether it's for a manual testing plan or part of an automated testing process in conjunction with Cucumber software.

2. Who is this course for?
    -
    - The course is for anybody interested in learning Gherkin
    - There are a few different people who will get more from the course
        - Business Analysts 
        - Testing Professional
        - Software Developer
        - Manager \ Business Owner

3. Before We Continue!
    -
    - Some quick housekeeping for the course

4. IMPORTANT NOTE!
    -
    - This course does not intend to provide any implementation examples in any language
        - There are many implementations of Gherkin and this wants to be independent
        - The course only covers using Gherkin itself
        - Other courses that are available will cover various language implementations
  
<br /> <br /> <br />
<h1><p align=center>How Gherkin Helps Business</h1></ br>

5. Module Introduction
    -
    - A quick overview of what the module covers

6. Behavioural Driven Development
    -
    - Behavioural Driven Development is also known as BDD
    - It is a way for developers to work with business and non-technical people
    - It does this by encouraging teams to collaborate together
    - BDD can run alongside agile practice, it does this by planning work in small enhancements
    - BDD can help build a shared understanding of a problem

7. What is Cucumber and what is Gherkin?
    -
    - Cucumber is an open source software tool that supports BDD
    - It offers ways to write scenarios or tests so that anyone can understand them
    - Cucumber is available in many languages such as Java or Ruby, PHP
    - Gherkin is used by cucumber to write acceptance tests or scenarios
    - It is a simple english like language with a specific syntax
    - Gherkin is parsed by cucumber to either pass or fail a scenario

8. Why learn Gherkin?
    -
    - Gherkin is an integral part of BDD with cucumber
    - It is widely used by testing professionals
    - It is also widely used by business analysts
    - It is a great skill to add on to a cv

9. Gherkin a universal language
    -
    - A quick animation showing testing in a company pre and post cucumber usage
    - The lesson learned is that product quality improves through a shared understanding

10. Gathering business requirements with Gherkin
    -
    - An animation covering some informal ways of gathering requirements
    - Meetings, At desk chats, email etc
    - Gherkin can be used to capture requirements and avoid problems with other methods

11. User stories with Gherkin
    - 
    - A user story is a description of a user's journey through features or functionality
    - It is written from the user's perspective
    - A user story should have an acceptance criteria, what is the expected result
    - There should also be an action which the user should perform
    - A user story also need to have some criteria or conditions which need to be met
    - User stories are part of Agile and Kanban development methodologies
    - There are a few things which need to be known to create a successful user story
        - Role\Actor or who is involved
        - Conditions, what are the prerequirements
        - Action what should they do eg click a button
        - Results, what happens after an action is performed
    - A quick example of a user that purchases a product from a website is used

12. Testing with Gherkin
    - 
    - Gherkin can be used for either manual or automated testing
    - Business requirements can feed into testing plans
    - Automated tests will offer feedback to the testing process
    - Automated testing will enhance the testing team not replace it
    - Automated tests can speed up the testing cycle and regression testing that is being done
    
13. Single source of truth
    -
    - Gherkin should be the single source of truth between a number of systems
    - Gherkin will be self-documenting as when scenarios are updated so is the documentation

14. Gherkin Workflow
    -
    - A quick example workflow involving a CEO and a business analyst
    - Then a tester joins in, all of the flow uses Gherkin

15. Module Summary
    -
    - A quick run through of what the module covered
    

<br /> <br /> <br />
<h1><p align=center>Learning Gherkin</h1></ br>

16. Module Intro
    -
    - Introduction to what will be covered in the module

17. Keywords Introduction
    -
    - Gherkin is a set of grammar rules that is structured in a certain way
    - It is written in human readable language made up of keywords
    - There are certain rule and syntax for automated tests
    - There are only a few keywords to learn

18. Feature Keyword
    -
    - This is a high level software feature or 'Epic'
        - https://www.wrike.com/agile-guide/agile-epics-guide/ 
    - This groups related scenarios together
    - A feature has 3 things
        - A feature summary
            - This is a one line summary of the feature 
        - A feature description
            - This is a multiline description which describes the feature in more detail
            - It is totally optional but using it is recommended 
            - Using it allows for the summary to be more brief
        - A list of scenarios
            - A feature should contain all scenarios that make up the feature 

19. Scenario Keyword
    -
    - The 'Scenario' uses an alias 'Example' in some implementations
    - A scenario is a situation that can be tested, it is a concrete example that illustrates a business rule
    - A scenario contains 3 things
      - A summary for the scenario which should be on one line, some examples include
        - User can view product details
        - User can add a product to the shopping basket
        - User can increase product quantity in basket
        - User can checkout of basket page
        - These are all tangible steps with an actor and an action
        - Some bad scenario examples include
          - User can use website
          - User can make a purchase
          - These are too vague with no actor or specific local action
      - A description
        - This is a multi-line description which describes the scenario in more detail  
        - This is option as the summary line is needed but it is recommended to be used
        - Its inclusion will allow the summary line to be less verbose
      - A list of steps
        - These steps are contained in the scenario to validate the software product 
        - They show the setup actions then the main action and the expected result

20. Given Keyword
    -
    - This keyword describe the situation or scene that is in the scenario
    - Typically it describes something that has happened in the past
    - The purpose of the given keyword is to put the system into a known state
    - Some examples again using the e-commerce example from previously include
      - Given I am logged in to the site
      - Given I have a product in my shopping basket

21. When Keyword
    -
    - This keyword describes the event or action that needs to take place
    - This is triggered by an actor which can be a person or another system
    - Some examples again using the e-commerce example from previously include
      - When I click the login button
      - When I press the clear button 

22. Then Keyword
    -
    - This keyword describes the result or expected outcome
    - The output here should be observable
    - Some examples again using the e-commerce example from previously include
        - Then an alert appears on screen
        - Then an email is sent

23. And Keyword
    -
    - The and keyword is used when there are multiple given, when or then keywords
    - It makes the steps easier to read
        - If there are multiple given statements for example as below
        - Given I am logged in
        - Given I have an item in my shopping basket
        - Given I have money in my account
        - This can be rewritten as
        - Given I am logged in
        - And I have an item in my shopping basket
        - And I have money in my account 
        - The same applies if when was being used instead of given
    
24. But Keyword
    -
    -
    
25. * (Asterix) Keyword
    -
    -
    
26. Main Keyword Recap
    -
    -
    
27. Rule Keyword
  -
  -

28. Background Keyword
  -
  -
  
30. Scenario Outline/Examples Keyword
2min
Play
30. @ Tag Keyword
1min
Play
31. Comments
1min
Play
32. Long description
    -
    -
    
33. Data Table
    -
    -
    
34. Multiple Languages
    -
    -
    
35. Gherkin Keyword Rules
    -
    -
    
36. Module summary
    -
    - A quick run through of what the module covered


<br /> <br /> <br />
<h1><p align=center> Applying Gherkin Knowledge</h1></ br>

37. Module Introduction
    -
    - Introduction to what will be covered in the module

38. Adding example Scenarios
    -
    - 

39. Examples with Given, When and Then
    -
    -
    
40. Introducing AND keyword
    -
    -
    
42. ERRATA: Next Video
    -
    -
    
44. Reusing Scenario steps
6min
Play
43. Introducing BUT keyword
3min
Play
44. Features and Scenarios
2min
Play
45. Combining When keywords together
4min
Play
46. Gherkin Challenge #1
1min
Start
47. ERRATA: Next Video
1min
Play
48. Gherkin Challenge #1 Solution
2min
Play
49. Comments in Gherkin
5min
Play
50. Making lists in Gherkin
4min
Play
51. Giving features descriptions
4min
Play
52. Gherkin Challenge #2
1min
Play
53. Making variables in Gherkin
4min
Play
54. Making variables in Gherkin continued
4min
Play
55. Gherkin Challenge #3
1min
Play
56. Gherkin Challenge #3 Solution
4min
Play
57. Introduction to Background in Gherkin
6min
Play
58. All about Data Tables
6min
Play
59. Data Table walk through
4min
Play
60. When and Data Tables combined
4min
Play
61. Scenario Outline keyword
7min
Play
62. More about Scenario Outline
8min
Start
63. NOTE: Notes for previous lesson
1min
Play
64. All about Tags
5min
Play
65. Use cases with Tags
4min
Play
66. Module Summary

    1min

Play
67. Module Introduction
3min
Start
68. Online Editor
1min
Play
69. Challenge 1
1min
Play
70. Challenge 1 Solution
2min
Play
71. Challenge 2
1min
Play
72. Challenge 2 Solution
6min
Play
73. Challenge 3
1min
Play
74. Challenge 3 Solution
5min
Play
75. Challenge 4
2min
Play
76. Challenge 4 Solution

    7min

Play
77. Thanks for learning
1min
Play
78. What next?
    -
    -
    
80. BONUS: Other courses
    -
    -
