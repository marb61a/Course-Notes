                    JSON Web Token (JWT) Authentication with Node.js
                    Course Notes


1 - Course Overview JSON Web Token (JWT) Authentication with Node.js
Brief intro to the course
  - The course is project based and will involve connecting a simple app to a secured API

2 - Setup a Web Server in Node.js using Express
Example Syntax
  // index.js for setting up a simple Express server
  const express = require("express");
  const app = express();
  const PORT = 8888;
  
  app.get('/status, (req, res) => {
    const localTime = (new Date()).toLocaleTimeString();
    
    res
      .status(200)
      .send(`Server time is ${localTime}.`);
  });
  
  app.get();
  

3 - Set the Server Port in Express Using Environment Variables

4 - Add a POST Route To Express And Parse the Body

5 - Provide Users With A JSON Web Token

6 - Allow CORS in Node.js and Express

7 - Authenticate Users With JWT for Access to Protected Resources

8 - Connect a Front-End to a Secure API using JWTs

9 - Authenticate Users in a Single Page Application with Auth0
