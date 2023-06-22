<b><p align=center> Bug Advocacy and Beyond </br>
Course Notes


<br /> <br /> <br />
  
<h1><p align=center>Module 0 – An Introduction to the Course  </h1><br/>

Best Use of this Course
 -
 - Some suggestions for getting the most from the course
  - Mindful Listening will help retain information
  - Take notes in any format
  - Attempt quizzes and exercises, this reinforces anything that has been learned
  - Apply what is learned to your context
  - Engage with the instructor
  - Taking breaks is important, think and reflect on the course
 
Before we go ahead with the Course
 -
 - A quote from Cem Kamer
  - It is not the person who finds the most bugs or embarasses the most coders but the one who gets the right bugs fixed 
 - The course will show 4 main things
  - How to advocate for bugs
  - How to use your bug report to build credibility
  - How to be an influential reporter of bugs
  - How to structure a bug report so that it is reads
 
Pre-requisites
 -
 - A basic understanding of software testing is needed
 - A web browser and a text editor is needed

<br /> <br /> <br />
  
<h1><p align=center> Module 1 – Key Terminologies & Concepts </h1><br/>

What is Quality? What is a Bug?
 -
 - Quality here is defined as the sum interaction between people, project and product
 - The model used is defined by Lalit Bahamare as the qualitri model
  - https://talesoftesting.com/introducing-quality-conscious-software-delivery/
  - https://talesoftesting.com/wp-content/uploads/2022/10/Lalitkumar-Bhamare-Quality-Conscious-Software-Delivery-eBook.pdf 
 - The people branch refers to the team involved in the software development
  - This includes testers, developers, testers, project managers 
  - The attitude of all of these people will have an effect on overall quality of product
 - The product branch covers the product functionality, reliability, performance, robustness and others including ease of use etc
  - Product quality will be a large factor in determining market success 
 - The project branch coves all the efforts involved in managing the project
  - This will include meetings, project phases, overall coordination between team members
 - A bug was defined as anything about the product that threatens its value
  - There are a huge amount of different types of bugs 
 
Exercise – Finding Bugs
 -
 - A quick exercise on finding bugs
 - Take a few minutes to think about bugs in the email and write 3 - 5 of them and rank them
 
Exercise – Trainer’s Edition
 -
 - Observations of the previous exercise
 - One bug is that the name of the person is spelled incorrectly
 - There are other bugs which are related to how the email is not correctly formatted and worded
 
Other Related Terms
 -
 - A fault in this case refers to any mistake in the code
  - This will cause the software to behave incorrectly   
 - A failure is the misbehaviour that is caused by the fault
 - An error is something that is wrong with the product as a whole
 - A critical condition is an environmental condition or step which reveals a problem
 - Defects are bugs with legal connotations, this term is often used in court cases
 - Symptom is a behaviour which suggests a larger underlying problem


<br /> <br /> <br />
  
<h1><p align=center>Module 2 – Testing – A Social Process </h1><br/>

Bug Report
  -
  - A bug report is a tester's primary work product
    - It is a tester's tool which sells a developer the idea of investing time into fixing the bug
  - This report will decided the quality of communication between a team
  - Information about a bug should be very clear and concise as well as attention grabbing
  - It is very important that bug reports be very clear
    - Bug reports are not something that only professional testers do 
    - Many bugs go unfixed due to not communicating the importance to the relevant stakeholders 
  - Bugs reports should always be reviewed and updated where necessary
  - One example bug workflow is available at the following URL
    - https://www.edlin.org/computing/bugtracking_workflow_process.html 
  
Testing – A Social Process
  -
  - Testers will usually work with a team, usually including different stakeholders 
  - There will be some issues within working with and within a team
    - Time with the team itself is likely to be limited
    - Developers are usually overcommitted with work so they will be under pressure
    - Customers are not forgiving to companies that are late with thing, this creates its own pressure
    - There are tradeoffs needed such as testing more or whether to improve reporting
    - Very often testers will be the bearers of bad news
  - The above can lead to a social kind of pressure on testers   
  
Risk
  -
  - Identifying and communicating the various risks is very important as a tester
  - Every piece of software or application is prone to certain risks
    - These cover everything from security to usability 
  - Having no risk would mean there was no need for testing
  - Find and communicate the risks that you discover
  - There will be a time when the business side willl be worried about risks
  - Study any existing information or bug reports available to see their impact, the risk levels etc 
  - A recommend ebook is Software Bug Stories
    - https://leanpub.com/softwarebugstories 
  
Importance of Persuasion
  -
  - Persuasion is a critical but overlooked skill in testing
  - Persuasion is needed to covince stakeholders to fix bugs which they may not otherwise consider
  - There are a lot of social factors that are involved in the ability to persuade

<br /> <br /> <br />
  
<h1><p align=center>Module 3 – Bug Advocacy – What & Why? </h1><br/>

What is Bug Advocacy?
  -
  - Bug Advocacy is presenting a bug in its strongest most honest lights
  - It connects bugs with concerns of multiple stakeholders
  - Good bug advocacy enables good decision making
  
Selling Bugs
  -
  - At certain levels bug advocacy is selling bugs
  - Simply reporting a bug and expecting immediate fixing is not always going to happen
  - Using some sales techniques such as showing product benefits will help when advocating for bugs to be fixed
  - Bug advocates will help bring their colleagues on this journey similar to the customers journey from sales
    - https://www.salesforce.com/products/guide/lead-gen/customer-journeys/
  - Professional testers will always add more information than just the baseics to bug reports  
  
Motivating the Buyer
  -
  - The maybe occasions where there is a need to motivate a developer to fix a bug
    - Again this will be very similar to motivating buyers that sales people use to entice buyers 
  - Ensure that they understand that the issue will affect lots of people
  - Fixing the bug is going to be comparitively easy compared to the consequences of not fixing it
    - The easier the bug is to reproduce also the more often and likely it is to occur 
  - Some bugs can be embarassing for the organisation, this can be a powerful motivator to fixing
  - Bugs violates claims that the company made about the product will lead to a loss of reputation
  - If somebody in management wants a bug fixed this can be a big motivator as it shows it is a high priority
  
Overcoming Objections
  -
  - This will require active research and investigation
  - What are the steps or operations required in reproducing the bug
  - Are there any conditions that are contributing or affect things and causing a problem
  - Are there any other critical conditions
  - Is there something else that can be altered to cause a bug
  - Are there areas of the software that are not being tested
  - Can the environment that the software is being tested in be changed
  - Is the bug version specific or does it occur in multiple versions
  - Can any the application settings be changed eg parameters that are passed to the application
  - Does the bug occur each time a certain operation is performed or is it intermittent and likely dependent on another issue
  - What type of input data is used, are there files, text limits may be an issue as might be the file type

<br /> <br /> <br />
  
<h1><p align=center>Module 4 – Structure of a Bug Report </h1><br/>

Structure of a Bug Report
  -
  - This covers the fields that are typically filled during a bug report
  - The first thing that people read in a bug report is the problem summary
    - This should give a good idea to readers what the issue is 
  - A failure when structure is recommended by the instructor
    - This details the issue and when it occurs  
    - An example is an application crashing when trying to save a file 
  - Another important field is the environment in which the bug occured
    - Some bugs only occur when there are certain hardware\software configurations are used 
  - What type of report is it
    - Is it a coding error, design issue, documentation issue or suggestion\change request 
  - Is the bug reproducible
  - What is the severity and the priority of the bug
  - Give a description of the problem
    - Describe the problem first 
    - List a step by step path to failure, number the steps and highlight the failure points
    - Explain what should have happened
    - List the environmental variables that aren't covered in bug reporting forms 
  - Is there a suggested fix available
  - What is the impact on the customer
  - What is the status of the bug, is it still awaiting a fix
  - Are there any additional comments needed 
  - What is the anticipated loss that occurs from the bug
  
Common Mistakes during Bug Reporting
  -
  - In bug reports there are some mistakes that are common
    - A poor title is used
    - There are grammar issues within the report
    - The report provides no proper details on the bug
    - Bug reports ignore the big picture
    - There are areas of the report that are unnecessary
    - There are unnecessary text areas in the report
    - Assigning the wrong severity to a bug
    - Confusing bug & change requests  
  
Exercise – Reporting Bugs
  -
  - An exercise on reporting bugs
  - The exercise is to find and report 1 bug
  - The focus should be on creating a detailed bug report
    - This should help a new developer understand and evaluate it easily 
  - Make necessary assumptions if there are any questions
    - State those assumptions in the bug description 
  
Self-Evaluation
  -
  - Self Evaluation of the exercise
  - What seems to be the problem
  - What was being done right before the problem occurred
  - What are the details of the test environment
  - Did you do screenshots, recordings and evidence
  - What type of test data was used, what were the values
  - Is this actually a problem and for whom
  - How consistently can the bug be reproduced
  - What are the risks and impact of the bug and what are the worst case scenarios
  - Was there any further analysis needed

<br /> <br /> <br />
  
<h1><p align=center>Module 5 – Levels of Bug Reporting </h1><br/>

Levels of Bug Reporting
  -
  - There are 4 main levels of bug reporting
  - Standard Reporting which is the most basic of the bug reports
    - This is the type of bug reports that people getting started in software testing do, sometimes experienced people still use it 
  - Improvised Standard is the next level up and is similar to standard reporting with additional information included
    - This additional information can be screenshots, videos etc which are all designed to assist the developer reproduce the bug 
  - Reporting With Advocacy which is where bug advocacy starts to come into play
    - At this level it is not just the bug information given but also the impact that it may have that is put forward
  - Reporting With Advocacy & Investigation which is a step beyond just advocating about bugs
    - Bugs themselves are investigated but so are the root causes
  
Standard Reporting
  -
  - This is the most common type of report within the software industry
  - It can be seen as a bad practice albeit industry wide
  - Some bugs do need precise steps to reproduce but some maybe standard and do not need detailing
  - Some bugs even though a sequence of steps are used is not about steps
  - Using a detailed series of steps will give the impression that a developer may not know how to use the application
  - Expected results can be piece of unneeded information
  
Improvised Standard
  -
  - This is a much better report than the level 1 standard report
  - There is clarity on issues rather than just mentioning symptoms
  - There should not be any obvious questions from the developer
  - Depending on the situation it can allow the tester to show knowledge of the root issue
  - It allows for a demonstration of some of the investigative work done by the tester
  
Reporting with Advocacy
  -
  - Highlighting an appealing business case for why this specific bug should be fixed
  - Again the same bug has been used which is that the customer information is not persisting throughout their journey
  - Again this is an incremental improvement on the previous level of reporting
  - There is a clarity shown on the actual issue rather than just the symptoms
  - There is an awareness of how users would use the application and how the bug would impact them and by extension the business
  - This type of bug report also demonstrates the business value of the bug reporter
  
Level 4 Reporting
  -
  - Again the same bug has been used which is that the customer information is not persisting throughout their journey
  - This is a further incremental improvement on the previous reporting type
  - The report demonstrates the level of investigation done after finding a bug
  - There are several points elucidated in the report
    - The technical root cause of the bug
    - The impact that the bug will have on different stakeholders
    - Information on how consistently the bug has been reproduced
    - Any state dependency that may be present within the application
    - The behaviour of the app on similiar paths
    - Any screenshots showing the above can be added 
  - There may be other related bugs which can be grouped together
  - There is a need not to constantly report the same bug or issue too often
  
Contextual Reporting
  -
  - This is not related to the previous 4 levels though it can be considered a 5th level
  - The example is a bug that was communicated
  - It may be a good approach if the bug that occured was down to a build issue
  - Synchronous communication is a good way to resolve server or build issues
  - Creating a new issue each time a build issue occurs is a good way of creating enough noise to get things resolved
  - This type of reporting maybe become overkill so if there is a way of resolving the issue then it should be tried


<br /> <br /> <br />
  
<h1><p align=center>Module 6 – Bug Advocacy – Tips & Traps 2 </h1><br/>

Bug Advocacy Tips
  -
  - Look for any information available beyond test results
  - Try to motivate the developer to fix the bug issue
  - Go one step deeper and research the conditions behind the failure
  - Make the risk analysis presentation more compelling
  - Continue to hone writing skills
  
Bug Advocacy Traps
  -
  - Advocate for bug repair but know when to stop, don't be the quality police
  - Try to avoid confusing bug severity with priority as this can happen
  - Get out of the quality assurance mindset, testers are only part of a team


<br /> <br /> <br />
  
<h1><p align=center>Module 7 – Credibility & Influence </h1><br/>

Credibility and Influence
  -
  - There are 2 main factors in getting a bug fixed
  - Quality of Report
    - How clear is the writing
    - Has there been any follow up testing
    - Has an impact analysis been done along with testing 
  - The credibility & influence of the reporter 
  
Factors Affecting Credibility
  -
  - Your Choices as a tester
    - Do you report each and every bug that you find
    - Do you report on minor bugs
    - Do you report only the larger bugs that occur
    - Is every bug analysed fully
    - Is the analysis that has been done in-depth enough
    - Do you insist that every bug is fixed 
  - What is the extent and depth of your reporting
  - How comprehensive is the report
    - Does the report provide the requisite level of detail needed 
  
Project Timelines and Bug Reporting
  -
  - Discussing the relationship between bug reporting and the various timelines in a project
  - Bug reporting is a very important part of software testing
  - Bug reporting will have to be calibrated to project timelines
  - Early in the schedule all types of bugs are reported
  - Later in the project schedule, reporting of bugs becomes more selective
    - Minor and low visibility may not be seen as important at this stage
    - Informal reporting processes might be important such as mentioning an issue in passing
    - There will probably be separate tagging for minor issues   
  
Influence
  -
  - Influence is the ability to persude others to take action
  - There are some different ways that this influence can be applied
    - Provide your audience with facts and data
    - Appeal to their emotions
    - Build up trust and rapport betwenn you all 
  - Influence or Influencing requires skills such as
    - Communication skills across all mediums
    - Negotiating skills are very important part of influence
    - Collaboration skills and the ability to work properly with others has a huge bearing on the ability to influence

<br /> <br /> <br />
  
<h1><p align=center>Module 8 – Structuring of a Bug Report </h1><br/>

How to Structure a Bug Report?
  -
  - Badly reported bugs can be very frustrating for all involved
    - It can lead to fixes taking much longer than need be the case 
  - Structure all bug reports in a clear and concie manner
  - Place the bug details in a very visible area
  - Describe the bug so accurately that others would recognise it
  - Include the date and time that the bug was discovered
  - Detaill how to find the bug again
  - Give a brief summary of the bug
  - Highlight how damaging or dangerous the bug could be
  - Explain the location and environment of where the bug is found
  
RIMGEA – The Bug Reporting Mnemonic 
  -
  - Replicate it - see if the bug can be reproduced
  - Isolate it - Try to limit the steps or conditions that trigger the bug
  - Maximize is - Try to see if there is a worse failure
  - Generalise it - Try to braoden the extent of the bug
  - Externalise it - Try to see the impact from another stakeholder's perspective
  - And say it dispassionately - Try to have bug reports easy to understand 

<br /> <br /> <br />
  
<h1><p align=center>Module 9 – Tools to assist you </h1><br/>

Tools
  -
  - https://birdeatsbug.com/
  - https://chrome.google.com/webstore/detail/gofullpage-full-page-scre/fdpohaocaechififmbbbbbknoalclacl
  - https://getgreenshot.org/
  - https://www.grammarly.com/
  - https://screenrec.com/
  - https://bugmagnet.org/
  - https://www.getmagical.com/
  - https://www.wordtune.com/
  - https://www.cockos.com/licecap/
  - http://www.supportdetails.net/
  
Further Resources
  -
  - Some reading recommendations

<br /> <br /> <br />
  
<h1><p align=center>Bug Advocacy Cheatsheet </h1><br/>

Cheatsheet
  -
  - Downloadable cheatsheet made available by the course instructor
  
Conclusion and Thank You 
  -
  - End of course and a final word from the instructor
  
