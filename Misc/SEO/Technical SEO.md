<b><p align=center>                    
  Blue Array Academy Technical SEO </br>
  Course Notes  
https://www.bluearrayacademy.com/


An Introduction to Technical SEO <br/>
What is Technical SEO?
  - SEO has 3 main pillars - Content, Links and Technical
  - SEO is about improving a site visibility for search engines
  - Most are oriented towards Google seacrh as it is the market leader
  - Content is ranked by algorithms when search is used
  - Prior to content ranking it is important that search engines can find the website
  - Technical SEO comes into play at this point
  - Technical SEO ensures that search engine bots can access and understand a website as quickly as easy as possible
  - There are several topics in Technical SEO 
    - Information Arhictecture
    - Crawling, Indexing, Rendering and Ranking
    - Various tools
    - Page Experience
    - Schema, On-Page
    - Security
    - Images
    - Accessibility

Morals & Ethics
  - There are some things to consider when investigating a site from a technical perspective
  - Provide Solutions over Problems
    - When conducting a site audit it is very easy to provide problems
    - These problems observed in isolation rarely give any context to cause or solutions
    - Problems should be quoted specifically, the scale and the solutions to the problem
    - Root causes are essential to issues being fully understood
  - Work with team members
    - Analysis of sites and discovery of solutions and problems needs to be communicated to all parties effectively
    - Providing problems and solutions helps with this and can be provided in different ways to different audiences
    - Team members may not know technical jargon or reasoning behind decisions
  - Crawling Ethics
    - Ensure that permission is granted before crawling a site, check before hand
    - There will be times when anti-crawling software will be in place
  - General Ethics
    - Do not break the law
    - Always follow best practice
    - Do the best thing for a client
    - Do not provide clients with misleading information
  - Environmental Considerations
    - Try do the right thing for the environment
    - Send on the data that needs to be sent and reduce C02 emissions
    - Have webpages as light as possible

The Basics - Hosting
  - There are 2 types of host that need to be known
    - Web Hosts which is where content is stored
    - Domain Hosts which is where information on domain names is stored
  - Web Hosting
    - In order for content to be published on the internet there needs to be a place to publish it, in this case a website
    - This site has to be hosted somewhere
    - When a user requests a web address that is on your site, the server that hosts the website talks with the request and if able then fulfills it
    - The web site hosting can either be with a company or hosted yourself.
  - Hosted vs Self-Hosted
    - Hosted sites are typically built with site builders such as Wix, WordPress or Squarespace
    - Self-Hosted sites are usually easier to customise but this needs to be carefully done
    - When self hosting a lot of work that external hosts do needs to be done such as running backups
  - Shared vs Dedicated Hosting
    - Once a hosted solution has been decided on then it is time to decide on either shared or dedicated hosting
    - Shared is much cheaper and is better for those with limited technical skills as there will not be as many options
    - Dedicated Hosting is good for technical minded people and is like owning your own home
  - What should a good host do
    - Provide excellent technical support when needed
    - There should be the option to have either a dedicated or shared server
    - There should be no problem scaling as demand increases
    - There should be a focus on security
    - Additional functionality should be available such as the ability to whitelist IP Addresses
  - Content Delivery Networks (CDN's) 
    - Although not strictly necessary for a website there are advantages to using them
    - They are a group of servers which are distributed around the globe allowing for faster worldwide content delivery
    - They can be used in addition to web hosting as they allow for content caching on their servers
    - They inprove both performance and security and they reduce dependence on a single server thus improving uptime

Networking
  - Protocols
    - There are multiple protocols used to ensure that servers talk to one another and users get their data
       - IP which is used for network routing
       - TCP which ensures data is delivered reliably
       - HTTP which transfers data between devices
       - HTTPS which is an encrypted version of HTTP and is used more
       - TLS/SSL which is the encryption that HTTTPS uses 
  - Header Requests
    - After a web address has been typed into a browser a request is then sent to a server
    - It contains various information that allows the server to tailor it's response
     - Requested URI, Host, The type of data accepted by the browser, a User Agent, Source IP
  - Header Responses
    - Depending on the information that is sent to the server in the header request, the server will then respond with its own headers 
    - After this then if the browser is allowed to view content, it will begin downloading HTML from the server using details from the response

Standards
  - What is W3C
    - This is an organisation which develops standards for the Web
    - Due to the advent of website builders these standards are not as rigouously adhered to as they once were
    - Most website builders are used by people who may not know HTML
    - W3C offers a HTML validator whichallows people to test & check on a per site basis
      - https://validator.w3.org/ 
  - Why should you care?
    - If invalid HTML is used there is no guarantee it will render correctly in all browsers
    - Validation may not be important for the Googlebot as long as the site is rendered and structured data can be extracted 
    - Valid HTML is still important as it can help pages render and load faster
    - Broken HTML within the head section of a page can cause problems for the Google crawler which can cause other elements not to be seen
    - There maybe rendering issues for users if there is invalid HTML
  - What are RFC's
    - Request For Comments are used to develop a network protocol that is seen as standard
    - Almost all netowrk protocols made for the internet are built on RFC's
    - IP, TCP, SMTP, FTP, HTTP etc are built on RFC's
    - There are a lot of Non-SEO focused RFC's being published
  - Robot Exclusion Protocol
    - It was never turned into a standard when created in 1994
    - This has led to many different interpretations down the years
 

A Technical View of how search works
Crawling
  - Search engines return a list of webpages based on a user's search
  - These are known as SERP's or Search Engine Results Pages
  - It is not possible to search the entire internet for every single query in real time
  - An index is a list of words, phrases etc that can be used to return predetermined results
  - Index requires crawling every site prior to searching
  - Google will be the search engine focused on as it is by far the market leader
  - Crawling in it's simplist terms is discovery, it is what the search engine do to find pages
  - The Crawling process is as follows
    - A webpage is discovered and its URL is noted as well as the HTTP response code
    - The webpage DOM (Document Object Model) is then gone through to find and note each link found
    - These will then be crawled as well
    - Sometimes a URL is not stored, this is done by using a HTML directive telling the search engine not to follow a link
    - This is called a nofollow directive
    - Site hierarchies are also stored for indexing purposes
  - Other pieces of software that crawl around the web can be thought of as crawlers, bots, etc but here the search engine crawlers are of interest
  - When crawling search engines do not restrict themselves solely to webpages, other items gathered include
    - Images, Videos, Documents, Book scans, some databases, user generated content such as map locations 
    - This helps monetise searchs
  - Only in an ideal world would a search engine be aware of all sites and updated their change immediately
  - Resources however large are still limited and crawling everything is not feasible
  - 
Indexing
