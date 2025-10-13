<b><p align=center>Web Security - Course Notes 

<p align=center>https://frontendmasters.com/courses/web-security/


                    Section 1 - Introduction
1 - Introduction
Web Development has a huge security problem
  - Web Developers have fallen behind DevOps and Back End developers
Features & Deadlines are always in competition with security
  - This is true also of Techical Debt
  - The main reason is the business value or perceived value to the business
Attacks are escalating in their severity and impact
  - This is compounded by the fact that barriers to attack launch are lower than ever
  
2 - Course Demo Application
There is a sample app provided that the course will use for launching practice attacks on
  - There are some incomplete features which expand the list of available attack vectors
  - This can happen in real life with future feature flags left in which arent working yet
There course will make use of both viewpoints 
  - The student will be launching attacks on the app
  - After the attacks then there will be how to shore up the defences
    - This will hopefully get to the stage of negating many of the attacks
The app will use cookie based authentication
  - It will be tested using IE9
  - This is because of the need for different data points
    - Modern browsers which negate some attacks automatically and older ones which don't but are still in use

3 - Types of Hackers
There are 3 main types of hackers
  - Black Hat
    - These break into systems to cause damage or hold data for ransom and are usually drive by personal gain
  - Grey Hat
    - These types break into systems but cause no damage and are usually driven by curiosity
  - White Hat
    - These types of hackers break into systems with permission and report what they find
    - They also use a process called responsible disclosure for vulnerabilities they find to give time for fixes

4 - Hacker Motives
The M.O. of an attacker
  - Use various methods to gather information about your system
  - Research any vulnerabilities which may exist
  - Get an initial foothold in the system
    - Use the foothold to escalate to more serious attacks
    - The vulnerability is the game-over situation
    - Small scale footholds mean that the situation maybe beyond fixing
    - This means that the bar on recognising game-over situations should be lowered

5 - Course Agenda
The Agenda of the course will cover
  - Multiple attacks on the client
  - Cross Site Scripting (xss)
  - 3rd party assets eg npm dependencies
  - Cross Site Request Forgeries (CSRF)
  - Clickjacking Attcks which are also called UI redress attacks
  - CDN resource tampering
    - CDN's are not bullet proof, they are ran by people too!!
  - Https downgrade attacks
  - Man In The Middle Attacks


                    Cross-Site Scripting (XSS)
1 - Introducing Cross-Site Scripting (XSS)
Client Side Attacks
  - The first client side attack to be discussed is also the most prevalent XSS
    - It is called XSS because CSS already means something else
    - It is basically putting code where text is expected and tricking the browser into executing the code
    - It is an injection attack
    - Vulnerabilities are prevalent
     - The number of sites vulnerable is a minimum of 30%
     - Accurate data is not easy to obtain as most reports are from firms selling pen testing services
    - It allows an attacker to read data or perform operations on a users behalf
    - Example code which could allow XSS
     - This is ejs (embedded JS)
      ```
      <h1>Welcome, <%- name %></h1>
      name = "Mike";
      // Welcome Mike is returned
      // What would happen if code was injected
      <h1>Welcome, <%- name %></h1>
      name = "Mike<script>terrible()</script>"
      // This would be returned and the terrible script ran
      <h1>Welcome, Mike<script>terrible()</script></h1>
      ```

2 - Types of XSS Attacks
There are 4 main categories of XSS attacks
  - The instructor says 3 + 1 as the final one is debatable
  - Stored XSS
    - Code that executes the attackers script is persisted
    - This is usually added to a database
  - Reflected XSS
    - Transient response from a server causes a script to execute
    - A temporary server response can be tricked in to executing code
  - DOM Based XSS
    - These attacks do not have any server involvement
    - This means that code is passed in via queryParams
  - Blind XSS
    - It could be argued that this is the same as Stored XSS
    - This exploits a vulnerability in another app that an attacker cannot see or access under normal means
     - The example used is of a log reader app
     - There is likely to be less scrutiny of an internal app
     - These internal apps usually pull in public data so are attack vectors

3 - Locations for XSS Attacks
There are several XSS danger zones where attacks can happen
  - User-generated rich content eg WYSIWYG
  - Embedded content eg IFrame
  - Anywhere where users have control over a URL
    - Older browsers allowed url's like -- javascript:image_url
  - Anywhere that user input is reflected back
  - QueryParameters that are rendered into DOM
  - element.innerHTML = ?
    - This is a very easy exploit as it allows script tags

4 - XSS Attack Demonstration
Using the Linux distro Kali for demonstration
  - https://www.kali.org
  - This has a whole suite of security tools
  - The tools themselves can be used for good and bad
  - The course demonstrates an ARP attack
    - Web developers don't usually know how these things work
  - HTTPS can obviate some of the ARP attacks
  - There can be simple XSS attacks that do not need to be crafted
  - Phonegap and similar can be very dangerous
    - Ionic is highly optimised Phonegap
    - Most dangerous is the frameworks that essentially use webview iframes
     - These can break through traditional web app sandboxing
     - This is dangerous as Javascript binds to native functions and breaks through mobile sandboxes

Prevent XSS Attacks Quiz
XSS - As a feature
  - Some companies are starting to treat XSS as a feature
    - This includes ISP companies and is an argument in favour of net neutrality
  - This is a very bad idea
    - A compnay called XFinity has been injecting its script on Reddit
XSS Questions you should ask yourself
  - How confident are you in the XSS protection of your OSS libraries
    - One thing that should be looked for particularly in a view library is that
     - There is a procedure for resolving security issues eg email address that supports specific issues
     - GitHub issues are not appropriate in this case
     - Be careful about using browsers older than supported
  - How carefully do people scrutinize browser plugins
    - Few people read the full permissions of plugins
    - Be skeptical of plugins asking for permissions going beyond what is needed
    - Instructor suggests using incognito tab for online banking
  - If XSS happens what is the exposure
  - In your app what could a successful XSS attack escalate to 
    - This will differ form one organisation to another
    - This will also determine bug fixes etc at compromise will take precedence

Challenge 1: XSS Attack
There are 3 XSS vulnerabilities in the sample app
  - 2 of these are Reflected-XSS
  - Use multiple browsers to simulate multiple users
  - Students should try use at least one legacy browser when testing
  - Hosting can be done locally using *.lvh.me
    - This is essentially a DNS trick that resolves to localhost
    - It allows for having multiple domains, which is good for experimenting
The sample app
  - Will have to be cloned from a GitHub repo
  - Use yarn to install the packages
  - When registering in the app do not use a password that is used elsewhere
  - The challenge is to find the other 2 XSS vulnerabilities

Challenge 1: Solution
The solutions to the XSS challenges
  - When creating an account HTML tags can be added
    - In the example this is a <b> tag which makes things bold
    - This should be eliminated without being run as it means other code will be run
  - The next vulnerability is both a stored and reflected vulnerability
    - This happens after an account with a script is ran
    - The account is registered without warnings and a success message is shown
    - Inspecting the element shows the script tags inside the panel
  - The third vulnerabiity is found on the profile page
    - In the url the user is listed which should not happen
    - Adding a script tag is ran which would not happen in modern browsers
    - There is a console.log added in the script tags to stop pattern matching which would stop the script being ran

User Data
XSS Defenses - You should never put untrusted data in the following places
  - Directly in a script -- EG <script> <%- userData %> </script>
  - In a HTML comment -- EG <!--- <%- userData %> --->
  - In an attribute name -- EG <iframe <%- userData %>="myValue" />
  - In a tag name -- EG <<%- userData %> class="myElement">
  - Directly in a style block -- EG <style> <%- userData %> </style>
    - This is very difficult to do in modern browsers
  - On a general basis never trust raw user data
  - Escape user data before putting it into HTML, there are 2 things which you should do
    - Sanitize user data prior to persisting
    - Then sanitize it prior to being rendered to a screen
    - You should typically do both of these
    - Its easier to sanitize before rendering than worrying about disallowing all bad things without interfering with
      genuine user input
Example Syntax
  <script>alert('hi')</script>
  // This is gotten by using encodeURIComponent() function
  "%3Cscript%3Ealert('hi')%3C%2Fscript%3E"
  - Most view libraries do this automatically
  - EJS is used for the class and its the following
    <%= "Escaped Expression" %>
    <%- "Unescaped Expression" %>
    <% "Non-Rendered Expression" %>

9 - Sanitizing User Data
XSS Defenses - If you unescape then sanitize data first
  - These are some cheats for different libraries so you will know when you are in a danger zone
    - Ember & Vue -- {{{ "unescaped" }}}
      - This string will be treated as Html 
    - React -- return <div dangerouslySetInnerHTML={createMarkup()}/>;
    - Ejs -- <%- "Unescaped" %>
      - The course example app has a couple of examples of this issue which will need to be fixed
      - In this case the minus sign needs to be changed to an equals
    - Angular -- <div [innerHTML]="unescaped"></div>
    - Jade -- ! This is #{"<b>unescaped</b>"}!
Escape before putting user data in attributes
  - <div class="<%= 'UserValue' %>"></div>
  - Be especially careful of this when templating Javascript
    - <script>alert("Hello <%- userValue %>")</script>
  - Recommended to use https://github.com/ESAPI/node-esapi
    - This will check your app for issues, it is highly recommended by the instructor
  - User input should be treated as values not code

10 - Content Security Policy (CSP)
XSS Defenses Content Security Policy
  - Browsers cannot tell the difference between scripts downloaded from you origin vs another
    - This is called a single execution context
  - CSP allows modern browsers to be told which sources they should trust and for what type of resources
  - This information comes from a HTTP response header or meta tag
      - Content-Security_Policy: script-src 'self' https://example.example
                                 ---------         -----------------------
                                   name             sources
                                |--------------- directive ----------------|
                                
    - Multiple directives are allowed and are separated by semi-colon
    - Redefining a driective with the same name has no effect
    - By default directives are permissive
      - Content-Security-Policy: script-src: 'self' https://example.example;
                                 font-src: https://fonts.googleapis.com
  - There are some useful CSP directives
    - child-src -- Child execution contexts eg frames, workers
    - connect-src -- What you can connect to such as fetch, WebSocket, EventSource
    - form-action -- Where you can <form> submit to
    - img-src, media-src, object-src -- Where you can get images, media etc from
    - style-src -- Where external stylesheets can come from
    - upgrade-insecure-requests - Upgrades HTTP requests to HTTPS
    - default-src -- A fallback for when a specific directive is not provided
  - There are also some keywords which can be used alongside sources which are typically origins
    - none -- No sources allowed
    - self -- Current origin
    - unsafe-inline -- Allows inline JS and CSS
    - unsafe-eval -- Allows eval()
      - This is used by templating frameworks where a string is sent and evaluated juust in time
      - This improves the performance of webpages
 There are a few ways the unsafe-inline can be made a little safer
  - Script tags embedded in HTML is the most common form of XSS and banning it mitigates risk considerably
  - There are times however where JavaScript is needed and there are solutions
  - Cryptographic nonces must be generated per page load and must change unpredictably
Example Syntax
  // Cryptographic nonce example
  <script nonce=A9h3pdfn3f03nce8DnMIOErd7Gb>
    alert('This example is done inlne');
  </script>
  
  Content-Security-Policy: script-src 'nonce-A9h3pdfn3f03nce8DnMIOErd7Gb'
  
  Another way to do this is to add a checksum to the security policy 
    - Content-Security-Policy: script-src 'sha256-absd182.....='
    - The easiest way to define this is to use the browser itself
    - Use the error generated and move that into the CSP

11 - Challenge 2: Defend Against XSS Attacks
Implementing XSS defences
  - Custom linting rules can be used to scan and eliminate unsafe-inline
  - This also is useful with a Git pre-commit hook
  - Eliminating using automation is a good idea and it should be done as early as possible
The exercise in this section is to
  - Fix 3 XSS issues
  - Add a reasonable CSP to the example project
    - There is a library available to help with this
      - https://github.com/helmetjs/csp

12 - Challenge 2: Solution, Part 1
The example uses the VS Code IDE search facility which will search for a pattern
  - In this case it is the <%- pattern to be eliminated
  - Some may need to be kept otherwise use <%=
    - Most of these would be layout related eg <%- body -%>
  - There are other XSS vulnerabilities which allow users to see and manipulate other users data

13 - Challenge 2: Solution, Part 2Adding a reasonable CSP to the app
  - The HelmetJS GitHub page has a sample policy which can be used as a template and modified if needed
  - It will then need to be required in order to be used eg cont csp = require('helmet-csp'); 
  - In Express app.use is a stack of middlewares normally
  - CSP should be placed near headers in order to make for better readability
  - reportOnly is normally set to false but for testing purposes is set to true 
    - This means that things will not be blocked but you will be alerted to issues 
  - In the sample directives there is a reportUri directive
    - reportUri: '/report-violation'
    - You can specify an endpoint where errors can be sent from browsers that detect violations
    - This can be used for what is called by some a dynamic-kill-switch
    - This allows for session\user termination for CSP violation and is a good place to hook in security software
    - There are downsides though as information about user status could be available
      - Information from outside domains can bleed through and inferences about user permissions can be drawn
  - The sandbox directive will deal with I-Frames
    - sandbox: ['allow-forms', 'allow-scripts']
    - Basically only I-Frames with the sandbox attribute will be allowed
    - This will limit the functionality of I-Frames
  - The values must be in the valid CSP format between quotes
  - Eliminating inline styles will eliminate an XSS vector completely
    - This is CSS best practice 

14 - Malicious Attachments
This will not completely protect you due to malicious attachments
    - Documents can have embedded code and are not inert
    - PDF files have had trojans added to them which will cause problems
  - Images can also have malware embedded
    - Changing image extensions can cause problems, the example uses jpg changed to html
    - The html in images can have links embedded
  - Allowing users to share attachments can help spread malware

15 - Challenge 3: XSS Attachment
This is an explation of the exercise that students will perform
Attack - XSS Attachment
  - This is broken down into a scenario based exercise
    - Image uploads are allowed in the scenario
    - These are hosted in the same domain as the app
    - There is a need to ensure that uploads are in fact images
    - Users have the ability to rename files
    - Check what happens when you visit the url of a particular renamed image
  - Students are allowed to see how far some of this goes

16 - Challenge 3: Solution
The tool that is used in the example is exif.js
  - Read the Exif comment field and pipe it into the clipboard, the command is as follows
    - node ./scripts/exif.js read ./examples/squirrel.jpg | pbcopy
  - Replace the Exif comment field with the content of a HTML file, the command is as follows
    - node ./scripts/exif.js write ./examples/squirrel.jpg scratch.html
    - One note is that it must all go on to one line, this is because you cannot have a multiline HTML file name
Browser will treat a document and image request completely differently
Using pbcopy will add something to the clipboard
The exif.js library is filetype sensitive

17 - Stopping Malicious Attachments
There are defenses available to combat XSS Attachment attacks
  - Restrict the file types that can be uploaded and also the ability to access these types
    - This reduces how much of an XSS vector an app is
    - Do not blindly trust filetypes
  - When using images, compression usually eliminates non-visible data and is best practice so use this
  - Do research before allowing file types eg PDF's can execute Javascript which a lot of people do not realise
    - Some browsers will allow this straight away   

                    Section 3 - Cross-Site Request Forgery (CSRF)
1 - Introducing Cross-Site Request Forgery (CSRF)
CSRF - Cross Site Request Forgery
  - This is the second most prevalent attack
  - This type of attack takes advantage of the fact that cookies for basic authentication are passed along with requests
  - This is one reason to align with REST conventions (GET, POST, DELETE etc)
    - There should be no GET requests that mutate data
    - Just allowing PUT and POST will not solve the issue
  - Example Syntax
    - This form which is hidden will be able to make a request
    - The request itself will not be seen which is called an Opaque request
    - The result will show whether the request was successful or not
    <form name="badform" method="post" action="https://equihax.com/api/transfer">
      <input type="hidden" name="destination" value="2"/>
      <input type="hidden" name="amount" value="8500"/>
    </form>
    <script type="text/javascript">
      document.badform.submit()
    </script>

2 - Challenge 4: CSRF
  - See if you can make a page on JSBin
    - JSBin is recommended instead of other similar sites like CodePen as you can create plain HTTP landing pages
    - The other sites use HTTPS which wil cause a mixed content warning
  - The challenge is to cause transfers for logged-in users
  - This should be tried with both GET and POST
  - Try and do as much damage as possible

3 - Challenge 4: Solution
  - This takes advantage of the fact that a GET request can be made that mutates data
    - Using both the image and form examples
  - IFrames can be used to avoid ongoing attacks being seen
  - GET requests are the most serious
    - You will not have to trick people into clicking a link like with POST

4 - CSRF Tokens
  - How to know if you are vulnerable or not
  - Only Basic or cookie authentication schemes are vulnerable
    - The exception to this is a Client-side Cookie
      - If you remove somethng from a cookie that then needs to be placed into a request header
        - This is not suceptable to CSRF
        - This is because you need to be running code on a domain that can access that cookie
        - Web storage is partitioned on a per domain basis
        - If using the cookie as a means of storage only and the server is not looking at the cookie as a means of identtification
          - Then this type of attack does not work
        - This attack works when code is written on a site and a request is sent to another site
          - Cookies are usually sent in the response and that can be taken advantage of
      - By using this a user has mitigated the broadest form of the CSRF attack
  - LocalStorage and SessionStorage are only accessible on the client side
    - SessionStorage differs from LocalStorage as when the user closes the browser the SessionStorage data is destroyed
  - To try and solve the CSRF issue there are CSRf Tokens
    - Like a cryptographic nonce they are generated in an unpredictable way with each payload
    - Tokens are disposable meaning they can only be used once then destroyed
      - This means that an iterative algorithm for generating tokens is what should be in place to genereate new tokens
  - This has a level of similarity to 2 factor authentication
    - There are 2 pieces involved in the process
    - The first is something proving that you are authenticated
    - Something that proves that you are sending a request from an appropriate place
  - For server rendered apps meta tags are ok to use

5 - Request Origin
  - Modern Browsers send an Origin heaeder with each request
    - This can not be altered by client side code
    - Although it may appear that you can alter this header your changes will not stick
    - IE11 may not send this header in some instances
  - In cases where there is no Origin header there is usually a Referer header
    - This is misspelled intentionally
  - If behind a proxy then some information can be gotten form the Host and X-Forwarded-Host headers
    - If using Heroku you will be behind Squid

6 - Cross-Origin Resource Sharing (CORS)
  - The next best practice is to set CORS headers properly
  - This is what allows a browser to send a request from one domain to another
  - It involves what is called an OPTIONS Preflight
    - This is a low overhead request to a server to findout what is allowed
  - Example Syntax
    - // Preflight request to server
    - Origin: http://foo.example
    - Access-Control-Request-Method: POST
    - Access-Control-Request-Headers: Authorization, Content-Type
    -
    - // Preflight response from server
    - Access-Control-Allow-Origin: http://foo.example
    - Access-Control-Allow-Methods: POST, PUT, GET, OPTIONS
    - Access-Control-Allow-Headers: Autorization, Content-Type
    - Access-Control-Max-Age: 86400
    - 
    - // Main request to the server
    - Origin: http://foo.example
    - Access-Control-Request-Method: POST
    - Access-Control-Request-Headers: Authorization, Content-Type
    - Authorization: Bearer ashgsdye6yhysythgfjdf
    - Content-Type: application/json

6 - Cross-Origin Resource Sharing (CORS) (Cont)
  - The preflight request has no body just headers
  - All of the request happen internally and is not something that an app has control over

7 - Challenge: 5: Defend Against CSRF
  - Add a CSRF token to the sample application
  - The csurf package is already installed
    - Csurf is middleware for protecting againt CSRF attacks
      - https://github.com/expressjs/csurf
  - Most of the work will be done in 2 files /routes/transfers.js /views/transfers.ejs
  - If IE 9 is set up on the machine then experiment with that
  - You will add csurf as a request handler
    - The function in each route is also a handler and csurf should come between Router.verb and function
  - Router.all covers all HTTP verbs and should be changed to Router.post

8 - Challenge 5: Solution
  - Using the csurf library which is made by the express team
  - Firstly import the library 
    - var csurf = require('csurf');
  - Then there will need to be the proper middleware setup
    - const csrfProtection = csrf({cookie: true})
  - This const can then be added to both routes being used in the example
    - '/' and '/perform'
    - Simply add to the route eg router.get('/', csrfProtection, function(req, res){})
  - At this point you should be able to get a value from the request object
    - ie csrfToken: req.csrfToken()
    - This should be added to the render of the response ie res.render
  - The csrf token should be available in the template via a hidden input
    - <input type="hidden" name="_csrf" value="<% csrfToken %>"
    - In this example the syntax is correct for ejs
  - There should be an extra field on the transfers page now
    - It should contain the non-reuseable token
  - There may be routes eg process that only allow entry when a csrf token is present
  - Trying to edit or change a token will cause an error when trying to perform an action
  - There should be a 403 error and the csrf attack will no longer work
    - It might be a good idea not to shock a stack trace on error
    - This will give attackers an idea of system internals
    - Redirecting users to an error page is probably the best approach
  


                    Section 4 - Clickjacking
1 - Introducing Clickjacking
A quick demo of the clickjacking process
  - Often there is a domain/subdomain very similar to a legitimate one used
  - The illegitimate domain is then placed into an iFrame
  - Its opacity is set to 0 and users therefore think that they are clicking on a legitimate page
  - One of the most famous attacks is the Adobe Global Flash Security Settings Page
  - This falls in the UI redress attack category
  - It can also be used for capturing keystrokes
  - Some of the more sophisticated versions are very difficult to detect

2 - Challenge 6: Clickjacking
The challenge here is
  - To pre-populate the form using queryParams -> url?formAccount=16&accountTo=21 etc
  - Again use JSBin to create a landing page that uses the clickjacking technique
    - The aim is to trick the user into unintentionally performing an action
  - This when combined with XSS could be very powerful

3 - Challenge 6: Solution
  - How to stage a clickjacking attack
  - The easiest way to operate an IFrame for clickjacking is to set it around 50% opacity
  - Then position the IFrame as accurately as possible
  - There will need to be manipulations of CSS styles to accomplish the above
  - When editing the styles using the alt-shift-up/down arrow will add\subtract 10 pixel from values rather than 1
  - At the end chnage opacity to 0.0
  - After positioning if watched carefully the cursor will change going from the page to the IFrame

4 - Stopping Clickjacking
  - Defending against clickjacking in modern browsers
  - X-Frame-Options -> This is a HTTP response header
    - This informs the browser what it is allowed to do to a document, it will not know until it downloads the specific document
    - This can not be put inside another page, it must be the top level frame inside a browser tab
    - X-Frame-Options: DENY
    - X-Frame-Options: SAMEORIGIN
    - X-Frame-Options: ALLOW-FROM https://abc.com
  - Chrome & Safari do not respect ALLOW-FROM
    - In this case the Frame-ancestors CSP directive will have to be used instead
  - Example Syntax
    // Clickjacking Defences - Legacy Browsers
    // This is a hack that will give a similar effect to above
    // It is a combination of a style tag and some script
    <style id="clickjack">
      body{
        // There is a difference between visibility:none and display:none 
        // display:none will not take up any space in the DOM, it is as if it
        // is not there are all rather than just opaque
        display: none !important
      }
    </style>
    
    // In this case self is an alias for window and top is the top frame
    // If you are the top grab the clickjack and remove it
    if(self === top){
      var cj = document.getElementByID("clickjack");
      cj.parentNode.removeChild(clickjack);
    } else {
      top.location = self.location
    }
    
5 - Challenge 7: Defend Against Clickjacking
  - Add both modern and legacy browser defences for clickjacking
  - Verify that attacks used perviously no longer work
  - The CSP may need altering if any inline scripts are used
  - This will be done in the topmost layout file -> main-layout.ejs (legacy)
  - Modern solution will need a header adder to server/index.js
  - Simply add the app.use and a function which contains a response with .setHeader
    - This request response should handle xframe-options

6 - Challenge 7: Solution
  - Defending against a clickjacking attack
  - This will give safety in both older and newer browsers
  - Example Syntax (Legacy Browsers)
    // Grab the previously used code for legacy browsers
    // This will go into the main-layout.ejs file
    // The script part will need to be put in script tags and added to the body of the layout file
    <script>
      if(self === top){
        var cj = document.getElementByID("clickjack");
        cj.parentNode.removeChild(clickjack);
      } else {
        top.location = self.location
      }
    </script>
    
    // The style tag element will be added to the head of the layout file
    <style id="clickjack">
      body{
        display: none !important
      }
    </style>
    
  - Example syntax (Modern Browsers)
    // In the index.js file
    // If there is no next present there will be an error
    app.use(function(req, res, next) {
      res.setHeader('X-Frame-Options', 'DENY')
      next();
    })
    
  - Example syntax 
    // The above code will create an error in the console the sha present will need to 
    // added in to the CSP in order to work, this will mitigate the risk of clickjacking
    app.use({
      // Specify directives as normal
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'", "'sha256-<sha_value>'"]
      }
    })
    


                    Section 5 - Third Party Assets
1 - Introducing Third Party Assets
Items that fall under third party assets include
  - Non hosted scripts
  - Version dependency for use in development eg "express": "^4.15.2"
    - This is fuzzy as there as multiple possible versions as the ^ signifies from this version up
  - Tracking code eg Google Analytics
    - This maybe the worst of the three
    - The example code is used to generate its own script tag which then pulls in the real code it uses

2 - Challenge 8: Subresource Integrity
  - Add SubResource Integrity (SRI) attributes to the script and some style tags for the material design library
    - This is locally hosted and not from a remote CDN
    - If assets were deployed on a CDN they are at risk of tampering
  - Add some trivial code to either file
  - Observe how the browser will now refuse to fully load the resources

3 - Challenge 8: Solution
  - The file being added to is the main-layout ejs file
  - Adding an integrity field which is set to nothing to to the link and style tags will cause a browser complaint
    - This may not work in some cases, there maybe a need to add a fake integrity attribute eg sha256-xxxxx
    - The console errors should show the hashes that should be used and they can be added to the integrity field
  - The crossorigin attribute is set to anonymous
    - This basically says to send no cookies or authentication credantials in the request just make the request
  - With reject hash fields there will be no CSS or JS



                    Section 6 - Man-in-the-Middle
1 - Introducing Man-in-the-Middle Attacks
  - The scenario is a user connecting over a public wifi hotspot
    - The attacks will take advantage of a couple of things
      - Laptops etc remember what networks they have been connected to unless cleared
      - When the laptop sees a network of the smae name it will attempt to rejoin it
      - This is because these networks will be trusted by default
  - A pineapple is a wifi device used in pen testing
  - Wifi devices broadcast what they are looking for
  - When joining a public wifi network the router is trusted as the first DNS server in-line
    - DNS translates IP addresses into names
  - Some companies that offer Wifi utilise DNS poisoning
    - This is to drive users to pages where terms and conditions are agreed in order to use the service

2 - Hardware
  - Demo of some pen testing hardware\software
    - WIFI Pineapple
      - The WiFi Pineapple lets pentesters perform targeted man-in-the-middle attacks, advanced reconnaissance, credential harvesting
      - https://docs.hak5.org/hc/en-us/categories/360000979333-WiFi-Pineapple
      - There are hardware disguises eg Smoke Alarm covers
    - Kali Linux
      - This is used by a lot of pen testers due to the amount of tools already installed
    - WiFi antenna (USB)
      - Hi powered antenna (10 - 15 times more powerful than installed hardware)
    - Femtocell
      - Creates a WiFi network
      - This can be a security risk as devices will join automatically

3 - Encrypting Data
  - Defending against man in the middle
    - The best way to defend is to encrypt data in flight
  - Using SSL\TLS
  - The benefit here is that a secret key is needed to read or alter a request or response
  - Certificates identify domains and require domain validation
    - This is to prove you have control over a domain
    - This can be adding an entry to a DNS table
    - This can be applicable to hiring a new employee and they need credential
  - Some types of enhanced validation may need government id (Up to the issuer)
    - This is where the green address bar is seen in the address bar
    - These are supposed to ask for a government id
  
  
  
                    Section 7 - HTTPS
1 - Introducing HTTPS
  - The percentage of the web using using HTTPS has increased steadly
  - A brief run through of the path to HTTPS 

2 - HTTPS & Cryptography
  - In order to communicate securely there are 2 types of encryption to be dealt with
  - Symmetric Encryption and Public Key Encryption
    - Symmetric Encryption is very fast much faster than Public Key
    - There is also no practical limit on content size
      - This is probably what most people who have locked a file with a password have used
  - If an encryption key was generated on a per-connection basis this would be almost perfect except for a catch on how to shear keys safely
    - Reusing keys is not good in cryptography as randomness is good
  - This is where Public Key cryptography comes in
    - There are 2 different types of keys Public and Private
    - The public key is used to create messages that are encrypted, the private kay decrypts them
    - The algoritms involved are very complex
  - Public Key Encryption, The key Exchange
    - This can be slow but is necessary for a system that is getting encrypted messages without divulging how to send them
    - The server sends it public key and certificate to the client
    - The client and server compare cipher suites
      - Cypher suites are essentially the methodologies used for the faster symmetric encryption used later
    - Finally a seesion key is generated be the client
      - This is encrypted with the servers public key so that only the server can read it
    - The session key is what is used for encrypted data exchange
  - Public keys are for writing messages
  - Private keys are for reading messages
  - The RSA algorithm is generated by the product of 2 huge prime numbers
  - Because of the size of the math involved there is a limit on the size of a message
  - Private keys can be use to sign messages

3 - TLS Handshake
  - Using chat bubbles to demo the TLS handshake
    - Client --
      - Hey I wish to communicate securely and understand ciphers
        - The certificate check out so this must be you
          - I too will be encrypting all my messages from now on  
    - Server --
      - Hey here is my certificate to prove my id, it is signed by someone you trust and here is my public key so you can send me stuff secretly
          - I will be encrypting all my messages from now on      

4 - OpenSSL
  - This is the industry standard library for cryptography
  - DO NOT implement your own algorithm, protocol or handshake etc
  - OpenSSL is not that user friendly
  - It will not be needed all that often
  - This is a cli tool, there is no relly good GUI tools available
    - Commands Example
      - Generate a private key
        - openssl gen rsa -aes128 -out my-private.key 2048
      - Generate a public key from a private key
        - openssl rsa -pubout -in my-private.key -out my-public.key
      - Make a new certificate signing request
        - openssl req -new -key my-private.key -out my-request.csr
      - Sign the certificate with a private key
        - openssl x509 -req -days 3 -in my-request.csr -signkey my-private.key -out my-certificate.crt

5 - Challenge 9: Defend Against Man-in-the-Middle Attack
  - The challenges are
    - Generate a RSA private/public key pair that is valid for 1 day
    - Use the Node JS HTTPS module to serve the example app over HTTPS
      - There is an existing HTTP module which needs to be swapped out
    - Add the certificate to the OS trust store (for Win/Mac OSX users)
    
6 - Challenge 9: Solution
  - In index.js
    // replace http requirement with https
    var https = require('https');
    
    let server = https.createServer({
      cert: 'filename',
      key: 'filename',
      passphrase: 'key-passphrase'
    }, app);
  - After the above code is added then there will have to be a certificate generated
    - openssl gen rsa -aes128 -out my-private.key 2048
  - After the first command you will be asked for a pass phrase
    - Private keys are not something that should be stored in unencryptred form
  -
  


                    Section 8 - HTTPS Downgrade
1 - Introducing HTTPS Downgrade
  - URL's with proper certificates shuld be in place so that HTTPS is being used
  - There is a question about what to do with plain HTTP connections
  - The typical approach is to redirect HTTP to HTTPS
  - This is a good approach but there is a question as to what happens if a user clicks on a plain HTTP link
    - In this case the initial request is over HTTP
    - The server should respond with a 301 redirect to HTTPS
  - The initial request is still vulnerable to a MITM attack
    - This approach is called SSL stripping and there are libraries available
    - From the perspective of the server the connections is secure
    - The way that the attack works is to maintain a secure session with the server and an insecure session with the user
  - This leaves a dependency on the user noticing the URL

2 - Defending Against HTTPS Downgrade
  - Ask users to bookmark pages, this is because autocomplete remains HTTPS
    - This should be implmented as much as possible
  - In the Content-Security-Policy: upgrade-insecure-requests
  - Most if not all search engines favour HTTPS
  - Browser plugins attempt a secure upgrade wherever possible
  - Recommended to install HTTPS Everywhere
    - This will attempt to upgrade requests wherever it can

3 - Bad Certificate
  - Even if a user take the above precuations an attacker can still forge a certificate
  - Server Name Indication (SNI) is an extension to TLS which allows attackers to see the hostname client wants to talk to
  - Attackers will not know anything else however it is usually enough

4 - Defending Against Bad Certificates
  -

5 - Challenge & Solution 10: Defend Against HTTPS Downgrade
  - 

6 - Certificate Authority Compromise
  -



                    Section 9 - Wrapping Up
1 - Wrapping Up Web Security
A few final words from the course author and thanking the students
