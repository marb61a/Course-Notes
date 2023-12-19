<b><p align=center>                    
  Fraud Prevention, Dispute Resolution and PCI-DSS Masterclass
 </br>
  Course Notes  
https://www.udemy.com/course/fraud-prevention/

<br />
<h1><p align=center>Section 1 : Masterclass Intro </h1><br/>

Masterclass Intro
  -
  - A very brief intro to the course

Useful Information
  -
  - Some tips on how to take the course

<br /> <br /> <br />
<h1><p align=center>Section 2 : Fraud Introduction</h1><br/>

Introduction
  -
  - A brief overview of how the course will show how to prevent fraud
    - Who performs fraud and what are their motivations
    - What are the different executions of fraud and how are they prevented
    - A full list of fraud prevention techniques
    - What combination of fraud prevention techniques are the best 

<br /> <br /> <br />
<h1><p align=center>Section 3 : Fraud Fundamentals</h1><br/>

Fraud Fundamentals
  -
  - Payment fraud is a global problem and is one that is expected to get worse
    - Losses tripled between 2011 and 2020, it is expected to grow a further 25% 
  - There are multiple stakeholders at risk from fraud
    - Online merchants, bank and customers
  - The risks of fraud that banks face are different from others
    - There are usually 3 main risks that banks face
    - Attrition risk which is the risk of losing clients or customers especially to competitors
    - Credit risk such as when clients do not pay bills
    - Fraud risk such as a customer account be defrauded
    - Attrition and credit risk can be managed but fraud risk requires close monitoring 
  - There are differences between fraud and disputes which need clarification
    - Fraud is actually a type of dispute between a merchant and a customer
    - There are 4 main types of problems that disputes originate from
      - Fraud where a customer was impersonated or their stolen information was used
        - Identity theft is one of the most pervasive forms of fraud and is tough to detect 
      - Authorization where the consumer did not allow the merchant to proceed
      - Processing error where the merchant has provided wrong or incomplete information
        - Some fraud cases are handled manuall, some automatically, a credit card with a blacklisted number will have trandactions automatically rejected 
      - Consumer disputes where a product is either faulty or fake or undelivered etc
      - A dispute normally occurs when a customer requests a chargeback of a transaction value
        - There is normally a reason code and it is provided by the card issuer, it will show the dispute type
        - A chargeback is a request for money to be returned to a customer
        
  
<br /> <br /> <br />
<h1><p align=center>Section 4 : Fraud:Approaches</h1><br/>

Module Intro
  -
  - Brief intro to what the module will cover
  
General Strategies: Intro
  -
  - Perpetrators of fraud usually employ one of a few major strategies to collect information and use it
    - In spite of specific contexts such as consumer fraud or card block farud the methods used to gain information mostly are similar and fall into a few groups
    - Convenience which uses readily available information
    - Social Engineering which manipulates people for information
    - Internal fraud where internal people leak sensitive information
    - Identity Theft where a person is impersonated

General Strategies: Convenience
  -
  - Convenience fraud is relatively simple
    - It uses readily available information that can be repurposed for fraud
    - It frequently occurs in situations where a fraudster has a lot of different information on many people
    - This allows for the easy testing of the details of multiple cards or people
    - There is a technique called skimming which copies the credit card that someone uses
      - https://www.forbes.com/advisor/credit-cards/how-to-spot-a-credit-card-skimmer/
      - https://www.fraudsmart.ie/personal/fraud-scams/card-cheque-fraud/counterfeit-skimming/ 
    - A fraudster can impersonate a retail worker getting credit card information
      - The same works for an actual retail worker who commits fraud 
    - They can plant a device on card readers to gather card information
      - This device is called a skimmer 
  - The convenience approach to fraud allows a fraudster to easily test different types of cards
    - The low hanging fruit in this situation are the transactions that are blocked
    - A fraudster is then able to go deeper on to banks that are less protected against fraud
  - Examples Of Convenience Strategies
    - A couple of examples are already covered, ATM skimmers and retail workers
    - A newer example is called a shimmer
      - A lot of skimmers stopped working once magnetic strips stopped being used on cards
      - Chip cards became more important and shimmers are the equivalent for these
        - https://chargebacks911.com/credit-card-shimmers/   

General Strategies: Social Engineering
  -
  - Social Engineering is the practice of manipulating someone into revealing information that is confidential
    - This is usually done by someone pretending to be someone that they are not 
  - There are 2 major approaches to social engineering
    - Via phone and impersonating an employee eg getting a password from someone by pretending to be tech support
    - Phishing using anything from emails, SMS texts even websites to make users think that they are in a trusted environment 
  - Social engineering in most cases is reliant on using existing information known to the fraudster so that they appear legitimate
    - This makes the target assume that the fraudster is who they claim to be so that they reveal information
    - Someone for instance impersonating a company employee can use OSINT on the person
      - https://www.sans.org/blog/what-is-open-source-intelligence/ 
    - This allows the fraudster to contact a target and convince them to share something such as a password 
  - There are different examples available
    - Banking communication where an email or SMS is sent pretending to be a financial institution
      - This is phishing and is aimed at tricking people into giving away password details 
    - Social Networks have a variation of phishing called Social Network Phishing
      - Emails pretending to be from Facebook 
    - Calls from the security team, this is the most frequent type of social engineering
      - Some pretends to be from the security team and has a very convincing reason to share sensitive information  
  
General Strategies: Internal Fraud
  -
  - Internal Fraud consists of using proprietarty information that you have access to in order to commit fraud
  - This can include a couple of ways
    - If a person works for a fraud detection service and provides information to allow others to bypass the detection mechanisms
    - If working in customer support of a retailer and using knowledge of automatically approved charges to allow for purchasing products fraudulently 
  - It can be one of the most difficult methods to detect as the person involved knows how to avoid detection
  - There are 2 major types of Internal Fraud
    - First-party fraud
      - This is where the consumer themselves perform fraud eg exploiting return policies to use and return items with no intention of buying
    - Third-party fraud
      - This is where a person with internal knowledge of a company sells information obtaining a fee of some kind
      - This type of fraud is usually done at scale with multiple small value transactions
  - Some example include
    - Fenceable items, corporate fraud and insurance fraud   

General Strategies: Identity Theft
  -
  -

Specific Executions: Intro
  -
  - Brief intro to what the module will cover

Specific Executions: Consumer Fraud
  -
  - In this type of fraud perpetrators usually use generators to generate blocks of card numbers
    - These will usually have the first 6 digits in common
    - The cards seen as valid will be used to make purchases
    - Once successful numbers are identified they are exploited further
    - These blocks of numbers can be used to brute force against a website
    - Prior to online shopping sometimes physical cards were made with these fake numbers
  - This type of fraud usually targets smaller banks that may not have the latest verification methods available
    - This allow for testing large quantities of numbers
  - In this type of fraud the same card will be used with multiple addresses, phone numbers and names
    - Sometimes these fake addresse are drop off points for purchases instead of the cardholder address  
  - Velocity of Use and Velocity of Change mechanisms can help offer some protection
    - This is because they will detect that the same card is being used for different addresses
    - Another way is that the address being used is different from the cardholder 

Specific Executions: Card Block Fraud
  -
  -

Specific Executions: Single-Use Fraud
  -
  - This type of fraud is usually done for highly sellable items or cash returns
    - It is as the name suggests using a card a single time
    - It can be tough to detect as there is only a single transaction with a single card 
  - There are multiple approaches that leverage this as long as the card is only used once
    - Information can be obtained through social engineering or stolen from internal records
    - It can even be the numbers that were generated through a block generator  
  - As said previously it can be usually done for highly sellable goods
    - Alternatively an immediate cash return where cash is obtained in a single transaction
    - The account information maybe valid or not
    - It could be valid card that has been stole or a number generated one
    - The delivery address will always be different and is going to be a drop off point
    - Velocity of Change and use detection mechanisms can help offer some protection for multiple merchants
    - It is nearly impossible to detect for just one merchant
    - Setting up rules for sellable items on first treansaction can help
  - Some examples are
    - Using a stolen card to buy jewellry and delivering to a drop off point
    - Again using a stolen card this time to buy electronic currency such as bitcoin
    - Using a card to buy an item and then returning for cash is another method   

Specific Executions: Cash Return Fraud
  -
  -

Specific Executions: Collusive/Affiliate Fraud
  -
  -

Specific Executions: Dynamic/Tested Fraud
  -
  -

Perpetrators: Intro
  -
  - Brief intro to what the section will cover

Perpetrators: Consumers
  -
  -

Perpetrators: Hackers and Crackers
  -
  -

Perpetrators: White-Collar Criminals
  -
  -

Perpetrators: Organized Crime Rings
  -
  -

Module Conclusion
  -
  - Brief run through of what the module had covered


<br /> <br /> <br />
<h1><p align=center>Section 5: Fraud:Prevention Techniques</h1><br/>

Module Intro
  -
  - Brief intro to what the module will cover
  
Data Verification: Intro
  -
  - There are transaction elements other than verifying a person's identity the can be verified
  - One example is to use velocity checks
    - These are used to identify the probability of fraud in a transaction
    - This is where how frequently information is used or changed can be verified
  - Transaction information such as credit card details are another thing that can be verified    

Data Verification: Velocity Checks
  -
  - As the name says Velocity Checks are about verifying the speed at which specific information is changed or used
  - There are 2 different checks that can be used
    - Velocity of use checks
      - This is a metric that captures the amount of times a certain information field has been used
      - One example is the number of times a credit card number has been used
      - It can be used to detect fake shipping addresses used for multiple purposes
      - Bust-out fraud where a card is used for multiple purchases in a short time is a real life use
        - https://www.chargebackgurus.com/blog/bust-out-fraud 
    - Velocity of change checks
      - This metric captures the amount of times that a inforrmation field has been changed within a certain timeframe
      - One example is the change of an address associated with a certain card number
      - It is regularly used to detect fraud at scale such as using the same cards with different names or addresses

Data Verification: Card Verification
  -
  - Verification of a credit card is extremely important
  - There are a few recognised techniques that are used
    - Luhn or Mod10 Verification
      - https://www.creditcardvalidator.org/articles/luhn-algorithm
      - This is a simple checksum needed to validate that the card in use is valid
      - It is usually performed prior to sending the credit card to the bank 
    - Bank Identification Number (BIN) Verification
      - This is similar to Luhn
      - The first 6 digits are checked to identify bank, issuer and other information 
    - Card Security Schemes (CVV & CVV2)
      - https://chargebacks911.com/cvv2/
      - These measures are widely used to give some protection when a cardholders card number has been obtained
  - BIN and Luhn verifications are much more about data inegrity
    - They make sure that time is not wasted by sending incorrect information is not sent to the bank 
    - They are also good at detecting card fraud
    - A lot of unsuccessful attempts to use the card may mean that somebody is trying to brute force numbers
  - CVV checks are especially good at make sure that a card is possessed by the cardholder
    - Without this anyone could use the card without consequence  

Data Verification: Charge/Deposit Verifications
  -
  - These are 2 more techniques that can provide an additional layer of security but they do come with extra costs and additional time
    - Charge Verification
      - A merchant calls a bank and verifies a transaction
      - This will cost more due to needing to have staff on hand
      - It should be reserved for using only on higher value orders 
    - Deposit Verification
      - This consists of making a small deposit in a customer's account and having them verify it
      - It is used to make sure that the customer has access to the bank account they are using
      - This approach takes times and importantly does not stop identity theft  
  - Some examples
    - PayPal is an example of an institution that uses deposit verification
    - Bitcoin brokers use deposit checks regularly due to the amount of anonymous fraud
    - Car dealerships are examples of places where charge verification measures are used

Identity Verification: Intro
  -
  - Brief intro to what the section will cover

Identity Verification: Lists
  -
  - Having positive and negative lists can be important to prevent consumer fraud
  - There are a few common types
    - Hot-lists or black-lists which is a list of consumers to block
      - This is usually to flag customers that have previously committed fraud and are blocked 
    - Warm-lists which are lists of customers that are classed as risky
      - They may not have committed fraud but have participated in questionable activities
      - This can be things such as unsatisfied returns 
    - White-lists are lists of customers that are trusted  
  - Hot-lists or black-lists are the most common type of list
    - They can be created using multiple elements of the account information
    - They may not be able to help against one-time or dynamic fraud but are very effective against many other methods
    - There is a similar term called denied party checks
      - These are checks on public databases of parties which are denied from doing business due to fraud allegations
      - They are public hot-lists and should be leveraged  
  - Some examples are
    - Credit card blacklists which are vital in tracking fraudlent card that have been used
    - Warm to hot which is putting customers that maybe an issue on a warm list so they can be upgraded if necessary
    - Hotlisting somebody's phone number or address can be useful against card block attacks 

Identity Verification: Simple Field Verification
  -
  - There are some quick and easy checks that can be done to verify parts of a person's identity
  - These are not deep checks but provide a basic level of authentication
    - They are considered as the first layer of authentication
    - After this then more complex techniques are used
    - They will not provide too much protection for high-risk and high value tranactions but can be used for mass low-value transactions
  - As with anything that may cause a delay this can affect good orders but they are on the whole necessary 
  - Age Verificiation
    - This is where a customer is made to verify their age
    - It can be providing document eveidence eg passport or sometimes simply by adding a date of birth
    - Some industries such as gambling will reuqire age verification because they are adult only
  - Email Verification
    - Customers are often asked to verify their email account prior to being allowed to purchase from a site
    - Sometimes this can happen over the phone but it can delay sales
    - Often a one time password is sent to the email account to ensure that it really is the person
  - Telephone Number Identification
    - This is a bit more advanced but it can determine where a call comes from and what type of phone was used
    - Prices using this can vary but it is usually not too expensive

Identity Verification: Address Verifications
  -
  - There are 3 types of verifications that can be performed on a consumer's address
    - They are good to prevent fraud based on false shipping locations 
  - Address Verification Services (AVS)
    - This verifies the billing address of the card
    - AAV+ (Advanced Address Verification) is used on shipping too
    - https://www.fraudpractice.com/identitytools/advanced-address-verification-(aav)
  - Delivery Address Verification
    - This checks the shipping address to make sure that it is valid
    - It is the more costly option but helps prevent fraud that relies on drop-off points or invalid shipping address
  - Freight Forwarder Verification
    - This checks whether the address is not a freight forwarder
    - It is a tool to help prevent international forwarding fraud
  - Verification of the billing address is fairly cheap and is widely available
    - AVS is available for most cards but AAV+ only some
    - It is usually part of the card verification process
  - Verification of the shipping address is more costly
    - This helps prevent shipping to fake addresses
  - Which one of these or combination depends on the type of fraud being looked at   

Identity Verification: Manual Authentication
  -
  - 

Identity Verification: Automated Lookups
  -
  - There are 3 techniques that are reliant on automatically looking up information on the cardholder
    - This is to obtain supporting information about the validity of the transaction
  - Phone Lookups
    - This is an automated service used to verify the cardholder's phone number 
  - Address Lookups
    - This is the same as the phone number but for an address instead
    - This can be problematic especially around the time a person is moving address 
  - Credit Lookup
    - This is a more complete option but is more expensive
    - It provides more extensive information on a person such as address, phone number, email etc
  - These mechanisms are rarely used as standalone techniques but are used along with others to verify information already entered
  - Phone and address lookups are cheap but can fail regularly due to inconsistent information being entered
    - Lag periods can also cause problems as somebody could have changed phone but that is not reflected for several months 
  - Credit checks are more expensive but again mistakes can be made although less regularly than the other 2
    - These are only used for transactions that justify the cost 

Technological Verification: Intro
  -
  - Brief intro to what the section will cover

Technological Verification: Device/Token Authentication
  -
  -

Technological Verification: Digital Signatures
  -
  -

Technological Verification: Consumer Location
  -
  -

Scores and Rules
  -
  -

Processes: Intro
  -
  - Brief intro to what the section will cover

Processes: Insurance and Guarantees
  - 
  -

Processes: Reviews/Representment
  -
  - These are 2 processes that specifically pertain to the merchant's bank
    - They are useful in many situations not just fraud or general disputes 
  - Manual Reviews
    - In this process staff of the bank perform manual reviews of transactions
    - Because there is a lot of human involvement it is quite expensive and should be reserved for big transactions 
  - Chargeback Representment
    - Here the bank allows the merchant bank to represent them against the issuer for a chargeback
    - This will allow for any evidence to be submitted in a structured manner 
  - Both of the processes have large variations in success as well as time and cost involved
  - There can be many factors at play such as the experience of personnel involved, it can even come down to luck
  - There are no guarantees with either and they should not be used in lower value transactions
    - This is because transaction value will not cover the process cost 
  - Some examples are

Module Outro
  -
  - A brief recap of the key takeaways from the module


<br /> <br /> <br />
<h1><p align=center>Section 6: Fraud:Prevention Strategy</h1><br/>

Module Intro
  -
  - Brief intro to what the module will cover

Strategy Stages
  -
  -
  
Technique Considerations
  -
  -

Data Usage Considerations
  -
  -

Data Processing Considerations
  -
  -

Module Outro
  -
  - A brief recap of the key takeaways from the module
  

<br /> <br /> <br />
<h1><p align=center>Section 7: Fraud Conclusion</h1><br/>

Conclusion
  -
  - A very brief run through of the previous fraud related modules


<br /> <br /> <br />
<h1><p align=center>Section 8: Dispute Resolution:Introduction</h1><br/>

Introduction
  -
  - 

<br /> <br /> <br />
<h1><p align=center>Section 9: Dispute Resolution:Consideration</h1><br/>

Dispute Considerations
  -
  - When discussing payment related disputes it is important to clarify some concepts
  - The first one being the difference between fraud and a dispute
  - Disputes are disagreements between two parties
    - In payment related disputes they usually occur between the merchant and the customer\cardholder
    - Fraud is usually only one of the reasons for the dispute
    - If a card is stolen or used without authorisation that is fraud
    - Customers are not the only party that can commit fraud, the merchant can commit fraud too
    - There are also non-fraud related disputes such as processing errors
  - There are also needed distinctions between contractual and non-contractual disputes
    - Payment disputes are usually because of a transaction and are considered contractual disputes
      - It is important to understand that contractual disputes do not need to involve an actual contract
      - The can be based on what are called agreed upon terms
      - One example would be the terms of a transaction stated at the time of purchase such as mobile phone service provider
    - Non-contractual disputes also exist but payment disputes differ
      - Some disputes like IP or copyright infringment where there is no contract or relationship between the two parties  
  - Some examples include
    - If a person disputes a card charge as it was stolen it is both fraud and a dispute
    - A customer may not feel that the quality of a product matches what was promised
    - All payment disputes are contractual as there is some sort of agreement between the parties   

<br /> <br /> <br />
<h1><p align=center>Section 10: Dispute Resolution:ADR</h1><br/>  

Intro
  -
  - Brief intro to what the module will cover
  - ADR is an acronym for Alternative Dispute Resoultion

Negotiation
  -
  - 

Mediation
  -
  -

Arbitration
  -
  -

Outro
  -
  - A brief recap of the key takeaways from the module

<br /> <br /> <br />
<h1><p align=center>Section 11: Dispute Resolution:ODR</h1><br/>  

Intro
  -
  - Brief intro to what the module will cover

Context and Principles
  -
  -
  
Steps and Categories
  -
  -

Implementation and Case Studies
  -
  -

Outro
  -
  - A brief recap of the key takeaways from the module

<br /> <br /> <br />
<h1><p align=center>Section 12: Dispute Resolution:In Merchant Banking</h1><br/>  

Intro
  -
  - Brief intro to what the module will cover

General Guidelines
  -
  -

Disputes by Payment System
  -
  -

Dispute Lifecycle
  -
  -

Scheme Involvement
  -
  -

Outro
  -
  - A brief recap of the key takeaways from the module

<br /> <br /> <br />
<h1><p align=center>Section 13: Dispute Resolution:Reason Codes</h1><br/>  

Intro
  -
  - Brief intro to what the module will cover

Fraud: Introduction
  -
  - Brief intro to what the section will cover

Fraud: Not Authorized/Recognised
  -
  -

Fraud: Fraudulent Processing
  -
  -

Fraud: Monitored Merchant or Card
  -
  -

Fraud: EMV Liability Shift
  -
  -

Authorization: Introduction
  -
  - Brief intro to what the section will cover
  
Authorization: Missing/Declined Authorization
  -
  -

Authorization: Card in Recovery/Lost/Stolen
  -
  -

Authorization: Invalid Information
  -
  -

Processing Errors: Introduction
  -
  - Brief intro to what the section will cover
  
Processing Errors: Invalid Code or Data
  -
  -
  
Processing Errors: Invalid Amount/Account
  -
  -

Processing Errors: Duplicate/Other Payment
  -
  -

Processing Errors: Currency Mismatches
  -
  -
  
Processing Errors: Late Presentment
  -
  -
  
Consumer Disputes: Introduction
  -
  - Brief intro to what the section will cover

Consumer Disputes: Mismatch of Goods
  -
  -

Consumer Disputes: Cancelled/Not Completed
  -
  -

Consumer Disputes: Credit Not Processed
  -
  -

Outro
  -
  - A brief recap of the key takeaways from the module
  
<br /> <br /> <br />
<h1><p align=center>Section 14: Dispute Resolution:Outro</h1><br/>  

Course Outro
  - 
  - A brief recap of the key takeaways from the subject modules


<br /> <br /> <br />
<h1><p align=center>Section 15: PCIDSS:Introduction</h1><br/>  

Course Intro
  - 
  - Brief intro to what the next several subject modules will cover

Module Intro
  -
  - Brief intro to what the module will cover
  
Terminology Clarifications
  -
  -

PCI-DSS History
  -
  -

Merchant Assessment
  -
  -

Anatomy of a Payment Flow
  -
  -

Module Outro
  -
  - A brief recap of the key takeaways from the module


Module Intro
  -
  - Brief intro to what the module will cover
  -
    
Overview
  -
  -

Requirement 1: Keep a Firewall
  -
  -

Requirement 2: No Defaults
  -
  -

Requirement 3: Protect Stored Data
  -
  -

Requirement 4: Protect Transmitted Data
  -
  -

Requirement 5: Prevent Malware
  -
  -

Requirement 6: Develop Securely
  -
  -

Requirement 7: Need-to-Know Access
  -
  -

Requirement 8: Identify Access
  -
  -

Requirement 9: Restrict Physical Access
  -
  -

Requirement 10: Monitor Networks
  -
  -

110. Requirement 11: Test Regularly


111. Requirement 12: InfoSec Policy


General Patterns and Recap
  -
  -

Module Outro
  -
  - A brief recap of the key takeaways from the module


Course Outro
  - 
  - A brief recap of the key takeaways from the subject modules

Play
115. Intro
1min
Play
116. Acquisition Strategy
9min
Start
Quiz 77: Acquisition Strategy Quiz
Play
117. Code Analysis
7min
Start
Quiz 78: Code Analysis Quiz
Play
118. Code Signing
8min
Start
Quiz 79: Code Signing Quiz
Play
119. Controls by Data Classification
9min
Start
Quiz 80: Controls by Data Classification Quiz
Play
120. Criticality Analysis
8min
Start
Quiz 81: Criticality Analysis Quiz
Play
121. Cryptographic Protection
8min
Start
Quiz 82: Cryptographic Protection Quiz
Play
122. Cyber Threat Hunting
9min
Start
Quiz 83: Cyber Threat Hunting Quiz
Play
123. Data De-Identification and Anonymisation
9min
Start
Quiz 84: Data De-Identification and Anonymisation Quiz
Play
124. Data Governance Structures
9min
Start
Quiz 85: Data Governance Structures Quiz
Play
125. Data Purpose and Authority
10min
Start
Quiz 86: Data Purpose and Authority Quiz
Play
126. Data Retention and Disposal
9min
Start
Quiz 87: Data Retention and Disposal Quiz
Play
127. Defense-In-Depth
8min
Start
Quiz 88: Defense-In-Depth Quiz
Play
128. Information Tainting
9min
Start
Quiz 89: Information Tainting Quiz
Play
129. Locked Rooms/Devices/Ports
7min
Start
Quiz 90: Locked Rooms/Devices/Ports Quiz
Play
130. Media Downgrading/Redacting
10min
Start
Quiz 91: Media Downgrading/Redacting Quiz
Play
131. Physical Media Protection
7min
Start
Quiz 92: Physical Media Protection Quiz
Play
132. Provider Assessment and Monitoring
9min
Start
Quiz 93: Provider Assessment and Monitoring Quiz
Play
133. Security/Privacy Architectures
9min
Start
Quiz 94: Security/Privacy Architectures Quiz
Play
134. System Safe Modes
9min
Start
Quiz 95: System Safe Modes Quiz
Play
135. Thin/Diskless Devices
9min
Start
Quiz 96: Thin/Diskless Devices Quiz
Play
136. Usage Agreements
8min
Start
Quiz 97: Usage Agreements Quiz
Play
137. Visitor Controls
9min
Start
Quiz 98: Visitor Controls Quiz
Play
138. Outro

    1min

Play
139. Introduction

Assembling: Introduction
  -
  -

Assembling: Actions and Implementation
  -
  -

Assembling: Roles and Responsibilities
  -
  -

Assembling: Scope, Framework, Roadmap
  -
  -

Assembling: Governance Structures
  -
  -

Assembling: Trackable Metrics
  -
  -

Presenting: Intro
  -
  -
  
Presenting: Recency and Primacy
  -
  -

Presenting: Leveraging Specifics
  -
  -

Presenting: Displayed Authority
  -
  -

Presenting: The Hero's Journey
  -
  -

Presenting: Tiredness and Distraction
  -
  -

Dealing with Objections: Introduction
  -
  -

Dealing with Objections: Flipping and Diagnosing
  -
  -

Dealing with Objections: UP Answers
  -
  -

Dealing with Objections: Progress and Loss
  -
  -

Dealing with Objections: Political Capital
  -
  -

Securing Buy-In: Introduction
  -
  -

Securing Buy-In: Implementation and Opinions
  -
  -

Securing Buy-In: Tailored Benefits
  -
  -

Securing Buy-In: Effort Shaping
  -
  -

Securing Buy-In: Future Lock-In
  -
  -

Full Runthroughs: Introduction
  -
  -

Full Runthroughs: Pitching PCI-DSS
  -
  -

Full Runthroughs: Pitching Vendor Assessments
  -
  -

Full Runthroughs: Pitching Data Governance
  -
  -

Full Runthroughs: Pitching Data Management
  -
  -

Module Outro
  -
  -
  
Bonus Lecture
  -
  -
  
