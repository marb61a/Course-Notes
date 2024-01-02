<b><p align=center>   
Ultimate Privacy by Design Data Protection Course </br>
Course Notes  
https://www.udemy.com/course/privacy-by-design-mastercourse/


<br />
<h1><p align=center>Section 1: Introduction </h1><br/>

Introduction - Why Privacy by Design is extremely important
  -
  - Introduction to the instructor and course
  - Privacy By design is something that should be learned first by everybody involved in privacy
    - The only way to do this is to create a culture of privacy 
  - Issues are many times caused by people in the company not criminal
  - The only way to change people's behaviour is to embed privacy from the very beginning
  - Privacy by design which is a software development strategy and is decades old is now being discussed as a foundational strategy for all organisations
    - The original goal of privacy by design was to ensure developers were building privacy from the ground up 
     
What you will learn in this course?
   -
   - A quick run through of what the course covers
   - The approach is not only about GDPR but covers a lot of similar material
   - Data protection is not just about security related issues
     
IAPP certification learning plan - CIPT, CIPM, CIPP/E
   -
   - A look at the IAPP Certifications
     - https://iapp.org/certify/programs/
   - The author guarantees being able to take any of the IAPP certs after taking his courses

Powerpoint Presentations For Download
  -
  - A zip file containing presentations used in the course

One More Word Before We Start
  -
  - More content is available at the instructors Youtube channel as well as Patreon


<br /> <br /> <br />
<h1><p align=center>Section 2: Privacy by Design generalities and principles!</h1><br/>

How was privacy by design adopted during time!
   -
   - A brief run through of the history of the adoption of privacy by design
   - 
     
Privacy by Design Principle 1
  -
  -
     
Privacy by Design Principle 2
  -
  -
     
Privacy by Design Principle 3
  -
  -
     
Privacy by Design Principle 4
  -
  -
     
Privacy by Design - Principles 5, 6 and 7
  -
  - Privacy and other design requirements should not be treated as tradeoffs
    - Creative win-win solutions should be developed where possible 
  - Principle 5 -- End to end security (full lifecycle protection)
    - Security of personal information should be considered at everystage of the information lifercycle
      - Collecting, processing, storage, distribution and destruction 
    - Copiers with hard drives that were not disposed of properly could be a great source of information for bad actors
    - Principle 5 states that proper consideration be given for EVERY stage of the information lifecycle
    - What are the potential risks at each point in the lifecycle
      - What are the security processes that can be introduced to mitigate those risks 
  - Principle 6 Visibility and Transparency (Keep it open)
    - The use of personal information should not be obscured or obfuscated
      - Disclosure about that use should consider both the needs and the sophistication of the audience in question
      - Notice has been a principle of privacy since the 1970s
      - Almost every law has included a provision that requires disclosing the activities surrounding personal data
      - This is justified by disclosure being seen to provide an individual with the necessary information to make decisions
      - Limited diclosure increases the chances that decisions are based on inaccurate assumptions
      - Obfuscated disclosure where the individual is misled intentionally or not means that decisions will not be made fully understanding risks
    - Visibility and transparency are necessary but not wholly sufficient for privacy friendly designs
  - 
     
Are there any challenges?
  -
  - Privacy By Design has faced challenges in the past decade
  - Many of these challenges are down to the high level nature of the principles involved
    - This can mean that there is a lack of needed specificity in checklists or action items
  - In 2011 the authors of privacy by design stated that it provided no lead with respect to the principles according to which technology should be applied
  - This definition of privacy by design is therefore susceptible to interpretation
    - In one interpretation that any data can be collected as long as it is with a privacy label 
  - In 2012 Sarah Spiekermann said that privacy is a fuzzy concept
    - This is because there is no agreed upon methodology to engineer privacy into systems 
  - In 2015 Daniel Solove wrote in a blog post about the 4 challenges in privacy by design
    - Design choices are not fixed
    - Most of the design choices that implicate privacy are not value neutral
    - Privacy by design is only as good as the underlying concept of design
    - Privacy by design is difficult 
  - This course will address some of these but will not fix every problem
  - Many developers want simple solutions such as checkboxes
    - In this scenario simply following this list would mean assured privacy
  - Unfortunately in many cases this approach simply will not work
    - There are multiple ways to design systems including designs that are privacy friendly 
     
It is extremely important to include privacy from early stages!
  -
  - Most people feel that their privacy is out of their control and they are helpless to do anything
    - This is despite it being very important to people
    - They are resigned to losing their privacy but it may not be their fault
  - There are both structural and psychological reasons why people are not in a position to protect their own privacy
  - Structural Asymmetry
    - Asymmetry is a result when one party has a distinct advantage over another
    - This can occur in a number of ways and their are 3 different types of asymmetry that affect and individual's privacy interests
      - 
    - 
  - 

<br /> <br /> <br />
<h1><p align=center>Section 3: Let's define a privacy by design Model!</h1><br/>

What is this section about?
  -
  - A brief intro to what the section covers
  
Individuals 
  -
  - In any given model there will usually be a class of individual whose privacy is of concern
    - This can be a customer, user or even a job candidate 
  - There may also be non-obvious classes who could suffer a privacy violation inadvertently when a product or service is being developed
    - This goup can include bystanders, friends, associates and employees who may engage with a customer
    - One example is Uber where customers are entititled to privacy but the driver has some expectations of that too as well as pedestrians etc
  - Individuals should be classified so that each class has a distinct set of risks
    - Different threat actors, different potential violations and differing sets of activities that make them more or less susceptable to differing violations
    - One example is segmenting online customers from in-store customers although both are customers
  - Segmentation of individuals will come down to 3 questions
    - Who interacts with them either directly or indirectly through data processing and how do these interactions happen
    - What information is collected or processed about them and why
    - How frequently do either type of interaction occur 
  - Within each of the separate classes there may be sections that are also susceptable to privacy violations
    - This can be due to previous or historic infringements
    - It could also be due to the different motivations of different threat actors against the section
    - These sections could also have distinct privacy expectations as well as particular sensitivity to the consequences of a breach
  - There have been attempts in the past to group people together by their attitudes towards privacy
    - One example of this is the Westin index
      - https://www.cs.cmu.edu/~ponguru/CMU-ISRI-05-138.pdf
    - Westin's approach though is more about subjecive views of privacy rather than objective analysis 
  - The course author proposes a different approach to identifying sensitive sections
    - This would be based on historical examples and legal protections
  - The following are some examples of what are considered as sensitive populations or sections
    - 
  -  
  
Important Actors
  -
  - Any party that interacts with an individual or their information is a potential threat
  - This can be a party that directly or indirectly interacts with an individual
    - It can also be someone who interacts with an individual through processing their data 
  - These interactions usually fall into a few different categories
    - They can be continuous like using a social media application
    - Periodic such as a census in a country which happens every few years
    - Random which can be something like shoulder surfing in a cafe
    - Occasional such as at a restaurant that an individual frequents
    - Fleeting which is something like a CCTV catching a car licence plate driving by 
  - Interactions can occur as a result of events that are scheduled or unscheduled
  - All of the above are domain actors and all respresent a potential threat
  - The term domain actors is used in whatever system is being discussed
    - A domain actor can be something like a database hosting service because they control use, storage etc
  - When talking about they risk they pose to an individual the term threat actor is appropriate
    
  - 

Links and Relationships
  -
  -
  
Privacy by Design - Example 1
  -
  -
  
Privacy by Design - Example 2
  -
  -
  
Privacy by Design - Example 3
  -
  -
  
Violations - Overview
  -
  -
  
Information collection
  -
  -
  
Information processing (part 1)
  -
  -
  
Information processing (part 2)
  -
  -
  
Information dissemination (part 1)
  -
  -
  
Information dissemination (part 2)
  -
  -
  
Invasions
  -
  -
     
Centralization
  -
  - A control is a way to minimise the risk of privacy violation
  - In the privacy model a control reduces a threat actor's access to an individual, information about the individual
    - It will also govern the threat actor's behaviour through technical, administrative or operational means 
  - The rest of the section will cover system architecture as a means of introducing controls
    - There will also be some tactics and strategies for controls introduced 
  - The Engineering By Privacy article contrasts the privacy by policy approach
    - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1085333   
  - 
     
Identifiability
  -
  -


<br /> <br /> <br />
<h1><p align=center>Section 4: Privacy by Design Model - Data Oriented Strategies</h1><br/>

Privacy Data-Oriented Strategies - SEPARATE
  -
  - This section covers the 8 different strategies for countering privacy violations
    - Each of these will have underlying tactics 
  - Four of these strategies can be thought of as data orientated as they manipulate data
    - The other four are process oriented although they may implicate data-orientated tactics 
  - Enforcing a policy may involve excluding collection of some data
    - Giving an individual control may also involve them excluding data from processing 
  - At an even lower level tactics are implemented by techniques
    - Some techniques will cross tactics 
  - 
  
Privacy Data-Oriented Strategies - MINIMIZE (part 1)
  -
  -
     
Privacy Data-Oriented Strategies - MINIMIZE (part 2)
  -
  -
     
Privacy Data-Oriented Strategies - HIDE
  -
  -
  
Privacy Data-Oriented Strategies - ABSTRACT 
  -
  -
  
Privacy Data-Oriented Strategies - ENFORCE 
  -
  -
  
Privacy Data-Oriented Strategies - DEMONSTRATE
  -
  -
  
Privacy Data-Oriented Strategies - INFORM
  -
  -
  
Privacy Data-Oriented Strategies - CONTROL
  -
  -
  
Privacy Data-Oriented Strategies - Architecture Redux
  -
  -
  
Information Flow
  -
  -
     
Domains and Subdomains
  -
  -
  
App example
  -
  -
  
Exercises
  -
  -

<br />
<h1><p align=center>Section 5: Privacy Analysis - The FAIR method for privacy risk </h1><br/>

Risk Analysis from Privacy perspective 
  -
  - There have been 3 main deficiencies that efforts at privacy risk analysis has suffered from
    - The first is that they have focused on risks to the organisation such as privacy law compliance risk and the potential cost of fines
      - This has led to a special kind of myopia, because they are focused on legal violations they do not anticipate things like social backlash
      - This is especially true when new technologies sidestep regulation rules
    - The next deficiency is a terminology problem
      - An absence of controls is usually labelled as a risk which is a mislabelling
      - The controls exist as a preventative measure against the actual underlying risk
      - This is not only something that happens in privacy risk assessment but also in IT security too
      - Unencrypted data is one example of a commonly mislabelled risk, encryption is a control, lacking it is not a risk
      - The risk in this case is that someone without permission will access the data and use it in a way that violates privacy
    - Most risk analysis methodologies are qualitative in nature
      - Risks are framed in terms of likeliness of occurrence (high, low or medium)
      - People often use qualitative analysis to provide cover for inaccuracies in judgement
      - This cover though often causes miscommunication and bad decision making
      - The major deficiency here is that without more it can be difficult to determine which controls are cost effective
  - This section covers a modified Factor Analysis of Information Risk to quantify privacy risk
    - It focuses on risks to individuals rather than organisations
    - The entire FAIR approach will not be covered but how it maps to privacy violations will be
  - Risk Analysis cannot be done in isolation
    - It must be done holistically because there is always potential that outside factors may influence risk to the individual   
  
A FAIR method for privacy risk 
  -
  - FAIR decomposes risk into it's constituent parts
  - The purpose is to find factors that can be calculated or reasonably estimated
    - This builds up an estimate of the overall risk 
  - The goal here is not certainty but instead a logical and defensible range
  - Privacy risk is the probable frequency and magnitude of future privacy violations
    - Having a range helps rather than trying to make specific predictions 
  - Potential privacy is an act where a threat of an act by a threat actor could constitute a privacy violation 

What is Frequency?
  -
  -
  
Vulnerability
  -
  -
  
Magnitude
  -
  -
  
How to apply controls (part 1)
  -
  -
  
How to apply controls (part 2)
  -
  -
  
Risk at the organization level
  -
  -
  
Quantitative Risk Management - example 1 (part 1)
  -
  -
  
Quantitative Risk Management - example 1 (part 2)
  -
  -

App Example
  -
  -
     
Exercises
  -
  -

<br />
<h1><p align=center>Section 6: Let's create the privacy by design Methodology! </h1><br/>

The purpose of this methodology!
  -
  -
  
Quality Attributes
  -
  -
  
Identify Information Needs 
  -
  -
  
Imposing Controls - ARCHITECT & SECURE
  -
  -
  
Imposing Controls - Supervise & Balance
  -
  -
  
Online Behavioral Advertising & Mobile Phone monitoring
  -
  -
  
Integrating privacy by design into the business 
  -
  -
  
How the methodology meets the initial principles
  -
  -
  
The App under the methodology 
  -
  -
     
Final Exercises
  -
  -
