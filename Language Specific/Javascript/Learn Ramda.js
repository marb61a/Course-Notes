                    Learn Ramda.js
                    Course Notes 


1 - Refactor to Point Free Functions with Ramda using compose and converge
Example Syntax
  // The lambda library must be included, code starting off example
  const R = require('ramda');
  
  const person = {
    id: 1,
    name: Joe
  }
  
  const generateUrl = (id) => "avatar-url";
  
  const getUpdatedPerson = (person) => {
    const url = generateUrl(person.id);
    return R.assoc('avatar', url, person);
  }
  
  const result = getUpdatedPerson(person);
  console.log(result);
  
  // Code at the end of example, this refactors the existing code
  
  

2 - Eliminate Function Arguments (Point-Free Style) with Ramda's Converge

3 - Convert a QueryString to an Object using Function Composition in Ramda

4 - Select a Subset of Properties from a Collection of Objects in Ramda

5 - Handle Branching Logic with Ramda's Conditional Functions

6 - Declaratively Map Predicates to Object Properties Using Ramda where

7 - Change Object Properties with Ramda Lenses

8 - Add and Remove Items in Arrays using Filter, Reject and Partition in Ramda

9 - Build a Functional Pipeline with Ramda.js

10 - Pick and Omit Properties from Objects Using Ramda

11 - Curry and Uncurry Functions with Ramda

12 - Declaratively Map Data Transformations to Object Properties Using Ramda evolve

13 - Count Words in a String with Ramda's countBy and invert

14 - Handle Errors in Ramda Pipelines with tryCatch

15 - Create an Array From a Seed Value with Ramda's unfold

16 - Convert a Promise.all Result to an Object with Ramda's zip and zipObj

17 - Filter an Array Based on Multiple Predicates with Ramda's allPass Function

18 - Create a Query String from an Object using Ramda's toPairs function

19 - Convert Object Methods into Composable Functions with Ramda

20 - Sort an Array of Objects by Multiple Fields with Ramda's sortWith

21 - Refactor a Promise Chain to Function Composition using Ramda

22 - Refactor to a Point Free Function with Ramda's useWith Function

23 - Get a List of Unique Values From Nested Arrays with Ramda

24 - Debug Function Compositions with Ramda's Tap Function
