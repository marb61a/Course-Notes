<b><p align=center> Basics in SQL Server</br>
Course Notes</br>


Select all information from the table 'Car'
```
  SELECT * FROM Car;
```

Select brand names from the table 'Car'
```
  SELECT brand FROM Car;
```

Select model and price from the table 'Car'
```
  SELECT model, price FROM Car;
```

Select all information from the table 'Car' where the production year is 1999
```
  SELECT *
  FROM Car
  WHERE PRODUCTIONYEAR = 1999;
```

Select all information from the table 'Car' where the cost is less than 10k
```
  SELECT *
  FROM Car
  WHERE Price > 10000;
```

Select all information from the table 'Car' where the production year is NOT 1999
```
  SELECT *
  FROM Car
  WHERE PRODUCTIONYEAR != 1999;
```

Select brand, model and production year information from the table 'Car' where the cost is less than 10k
```
  SELECT Brand, Model, PRODUCTIONYEAR
  FROM Car
  WHERE Price <= 10000;
```

Select Vin from the table 'Car' where cars where produced before 2005 or priced less than 10k
```
  SELECT Vin
  FROM Car
  WHERE PRODUCTIONYEAR < 2005
  OR Price <= 10000;
```

Select Vin from the table 'Car' where cars where produced after 1999 and priced less than 7k
```
  SELECT Vin
  FROM Car
  WHERE PRODUCTIONYEAR > 1999
  AND Price <= 7000;
```

Select Vin, Brand, Model from the table 'Car' where cars where produced between 1999 and 2005 inclusive
```
  SELECT Vin, Brand, Model
  FROM Car
  WHERE PRODUCTIONYEAR BETWEEN 1995
  AND 2006;
```

Select Vin, Brand, Model from the table 'Car' where cars where NOT produced between 1999 and 2005 inclusive
```
  SELECT Vin, Brand, Model
  FROM Car
  WHERE PRODUCTIONYEAR NOT BETWEEN 1995
  AND 2005;
```

Select Vin from the table 'Car' where cars  before 1999 or after 2005 and whose price is less than 4,000 or greater than 10,000.
```
  SELECT Vin
  FROM Car
  WHERE (PRODUCTIONYEAR < 1999 OR PRODUCTIONYEAR > 2005)
  AND (Price < 4000 OR Price > 10000);
```

Select all information from the table 'Car' where the brand is Ford
```
  SELECT *
  FROM Car
  WHERE Brand = 'Ford';
```

Select all information from the table 'Car' where the current owner is not the first owner </br>
An N before the string indicates that the string is in Unicode fomat </br>
https://www.w3schools.com/sql/func_sqlserver_unicode.asp
```
  SELECT *
  FROM Car
  WHERE FirstOwner = N'✗';
```

Select Vin, Brand, Model from the table 'Car' where the brand begins with F
This uses the LIKE function which uses the % operator to replace a number of characters in the string
```
  SELECT Vin, Brand, Model
  FROM Car
  WHERE Brand
  LIKE 'F%';
```

Select Vin from the table 'Car' where the model ends with s
This uses the LIKE function which uses the % operator to replace a number of characters in the string
This can be at the beginning or end of a string, in the middle or surrounding certain letters
```
  SELECT Vin
  FROM Car
  WHERE Model
  LIKE '%s';
```

Select all columns from the table 'Car' where the brand is N'Volk_wagen'
This uses an underscore character to replace exactly 1 character
```
  SELECT *
  FROM Car
  WHERE Brand
  LIKE N'Volk_wagen';
```

Select all columns from the table 'Car' where the cars have a price
This uses NULL values which represent unknown missing values
```
  SELECT *
  FROM Car
  WHERE Price
  IS NOT NULL;
```

Select all columns from the table 'Car' where the cars have an unknown price
This uses NULL values which represent unknown missing values
```
  SELECT *
  FROM Car
  WHERE Price
  IS NULL;
```

Select all columns from the table 'Car' where the cars have a price greater than or equal to zero
```
  SELECT *
  FROM Car
  WHERE Price >= 0;
```

Select all columns from the table 'Car' where the cars have a tax value greater than 2000
```
  SELECT *
  FROM Car
  WHERE (Price * 0.2) >= 2000;
```

Select all columns from the table 'Car' where the cars were produced between 1999 and 2005, are not Volswagens, Have a model beginning with p or f and have a set price
```
  SELECT *
  FROM Car
  WHERE PRODUCTIONYEAR BETWEEN 1995 AND 2006 AND
  Brand != 'Volkswagen'AND
  MODEL LIKE 'P%' OR MODEL LIKE 'F%' AND
  Price IS NOT NULL  
  ;
```


<b><p align=center> Data From Multiple Tables </br>

Select all the data from the Movie and Director tables
```
  SELECT *
  FROM Movie, Director
```

Select all the data from the Movie and Director tables so each movie is shown with it's director
```
  SELECT *
  FROM Movie, Director
  WHERE Director.id = Movie.DirectorId;
```

Select all the data from the Movie and Director tables so each movie is shown with it's director, using join
```
  SELECT *
  FROM Movie
  JOIN Director
  ON Movie.DirectorId = Director.Id;
```

Select director name and movie title from the Movie and Director tables so each movie is shown with it's director, using join
```
  SELECT
  Director.name,
  Movie.title
  FROM Movie
  JOIN Director
  ON Movie.DirectorId = Director.Id;
```

Select director name and movie title from the Movie and Director tables so each movie is shown with it's director, use as few characters as possible
```
  SELECT
  name,
  title
  FROM Movie
  JOIN Director
  ON Movie.DirectorId = Director.Id;
```

Select director name and movie title from the Movie and Director tables so each movie is shown with it's director, rename the title column to MovieTitle
```
  SELECT
  name,
  title as MovieTitle
  FROM Movie
  JOIN Director
  ON Movie.DirectorId = Director.Id;
```

Select all columns from the Movie and Director tables so each movie is shown with it's director, only have movies produced after 200
```
  SELECT *
  FROM Movie
  JOIN Director
  ON Movie.DirectorId = Director.Id
  WHERE PRODUCTIONYEAR > 2000;
```

Select all columns from the Movie and Director tables so each movie is shown with it's director, only have movies directed by Steven Spielberg
```
  SELECT *
  FROM Movie
  JOIN Director
  ON Movie.DirectorId = Director.Id
  WHERE Name = 'Steven Spielberg';
```

Select Title, Production Year from Movie table, Name and birth year from Director, Show birth year as BornIn, only select movies from directors under 40
```
  SELECT
  Title, PRODUCTIONYEAR, Name, BirthYear as BornIn
  FROM Movie
  JOIN Director
  ON Movie.DirectorId = Director.Id
  WHERE (PRODUCTIONYEAR - BirthYear) < 40;
```

Select Id, Title, Production Year from Movie table, Name and birth year from Director, Show birth year as BornIn and Production year as ProducedIn
```
  SELECT
  Movie.Id,
  Movie.Title,
  Movie.ProductionYear as ProducedIn,
  Director.Name,
  Director.BirthYear as BornIn
  FROM Movie
  JOIN Director
  ON Movie.DirectorId = Director.Id
  WHERE (Title LIKE '%a%' AND ProductionYear > 2000)
  OR (BirthYear BETWEEN 1945 AND 1996);
```

</br> </br>
<b><p align=center> Aggregating And Grouping</br>

Select all columns from the employee table ordered by salary
```
  SELECT *
  FROM Employee
  ORDER BY Salary
```

Select all columns from the employee table related to 2011 and ordered by salary
```
  SELECT *
  FROM Employee
  WHERE Year = 2011
  ORDER BY Salary  
```

Select all columns from the employee table sorted by last name descending
```
  SELECT *
  FROM Employee
  ORDER BY LastName DESC
```

Select all columns from the employee table sorted by department ascending and salary descending
```
  SELECT *
  FROM Employee
  ORDER BY Department ASC,
  Salary DESC
```

Select top 5 rows of Salary and Position from the employee table 
```
  SELECT 
  TOP 5 Salary,
  Position
  FROM Employee
```
Select top 5 largest salaries from the employee table, select the  
```
  SELECT 
  TOP 5 Salary,
  Position
  FROM Employee
  ORDER BY Salary DESC
```

Select the Year column for all rows in the Employee table
```
  SELECT 
  Year
  FROM Employee 
```

Select the Year column for all rows in the Employee table, each year should be shown only once
```
  SELECT DISTINCT
  Year
  FROM Employee 
```

Select Department and Position columns from the Employee eliminating any duplicates
```
  SELECT DISTINCT
  Department, Position
  FROM Employee 
```

Count all rows in the Employee table and name the column EmployeeNumber
```
  SELECT
  COUNT (*) As EmployeeNumber
  FROM EMPLOYEE
```

Count all non null positions in the Employee table and name the column EmployeeNumber
```
  SELECT
  COUNT (Position) As PositionNumber
  FROM EMPLOYEE
```

Count all non null positions in the Employee table and name the column DistinctPositions
```
  SELECT
  COUNT (DISTINCT Position) As DistinctPositions
  FROM EMPLOYEE
```

Select the highest salary from the Employee table and name the column MaxSalary
```
  SELECT
  MAX (Salary) As MaxSalary
  FROM EMPLOYEE
```

Select the average salary from the Employee table from the year 2013 and name the column MaxSalary
```
  SELECT
  AVG (Salary) As AvgSalary
  FROM EMPLOYEE
  WHERE Year = 2013
```

Select the sum of all salaries from the Employee table in the marketing department from the year 2014 and name the column TotalSalary
```
  SELECT
  SUM (Salary) As TotalSalary
  FROM EMPLOYEE
  WHERE Department = 'Marketing' AND
  Year = 2014
```

Find the number of employees in each department in the year 2013. Show the department name together with the number of employees in that department in 2013. Name the last column DepartmentEmployees
```
  SELECT
  COUNT (Department) As DepartmentEmployees, Department
  FROM EMPLOYEE
  WHERE Year = 2013
  GROUP BY Department
```

Show all departments together with their lowest and highest salaries in 2014. Name the last two columns MinDepartmentSalary and MaxDepartmentSalary, respectively.
```
  SELECT
  Department,
  MIN(Salary) As MinDepartmentSalary,
  MAX(Salary) As MaxDepartmentSalary
  FROM EMPLOYEE
  WHERE Year = 2014
  GROUP BY Department
```

Find the average salary for each department in 2015. Name the column AvgDepartmentSalary.
```
  SELECT
  Department,
  AVG(Salary) As AvgDepartmentSalary
  FROM EMPLOYEE
  WHERE Year = 2015
  GROUP BY Department  
```

Find the average salary for each employee. Show each employee's first and last name and average salary. Group the table by last name and first name. Name the aggregate column AvgSalary.
```
  SELECT
  FirstName,
  LastName,
  AVG(Salary) As AvgSalary
  FROM EMPLOYEE
  GROUP BY FirstName, LastName
```

Find all employees who have spent more than 2 years at the company. Select their last name and first name together with the number of years they have worked. Name the column EmployeeYears.
```
  SELECT
  FirstName,
  LastName,
  Count(*) As EmployeeYears
  FROM EMPLOYEE
  GROUP BY FirstName, LastName
  HAVING COUNT(*) > 2
```

Find all departments where the average salary in 2012 was greater than 3000. Show the department name together with the average salary. Name the column AvgDepartmentSalary.
```
  SELECT
  Department,
  AVG(Salary) as AvgDepartmentSalary
  FROM EMPLOYEE
  WHERE Year = 2012
  GROUP BY Department
  HAVING AVG(Salary) > 3000
```

Sort the employees according to their total salaries at the company. The greatest values should appear first. Show the last name, first name, and the sum. Name the column TotalSalary
```
  SELECT
  FirstName,
  LastName,
  SUM(Salary) as TotalSalary
  FROM EMPLOYEE
  GROUP BY FirstName, LastName
  ORDER BY SUM(Salary) DESC
```

Show the last name and first name of each employee together with each employee's average salary and the number of years they have worked at the company.
Use the following aliases: AverageSalary for each employee's average salary and YearsWorked for the number of years they have worked at the company. 
Show only those employees who have spent more than two years at the company. Order the results by average salary in descending order.
```
  SELECT
  FirstName,
  LastName,
  AVG(Salary) as AverageSalary,
  COUNT(Year) as YearsWorked
  FROM EMPLOYEE
  GROUP BY LastName, FirstName
  HAVING COUNT(Year) > 2
  ORDER BY AVG(Salary) DESC
```



<b><p align=center> More on JOINS </br>
Get all the data from the Room table
```
  SELECT
  *
  FROM Room
```

Get all the data from the Student table
```
  SELECT
  *
  FROM Student
```

Get all the data from the Equipment table
```
  SELECT
  *
  FROM Equipment
```

Join the Student and Room tables so that each student is shown together with the room they live in. Select all columns.
```
  SELECT *
  FROM Student
  JOIN Room
  ON Student.RoomId = Room.id;
```

Show each student's name together with the number of the room they live in.
Select the name of the student and room number.
```
  SELECT
  Student.Name,
  Room.RoomNumber
  FROM Student
  JOIN Room
  ON Student.RoomId = Room.id;
```

Now, use the full name INNER JOIN to join the Room and Equipment tables so that each piece of equipment is shown together with its room.
INNER JOIN is the correct name for JOIN
```
  SELECT
  *
  FROM Equipment
  JOIN Room
  ON Equipment.RoomId = Room.id;
```

Show all information for all students. If a student is assigned to a room, show all information for the room as well.
```
  SELECT
  *
  FROM Student
  LEFT JOIN Room
  ON Student.RoomId = Room.id;
```

Select all pieces of equipment together with the rooms they are assigned to. Show each piece of equipment even if it isn't assigned to a room.
```
  SELECT
  *
  FROM Equipment
  LEFT JOIN Room
  ON Equipment.RoomId = Room.id;
```

Show all information for each student and the room they live in. Show all rooms, even ones with no students assigned to them. 
This can be accomplished with a LEFT JOIN by reordering the tables but use a RIGHT JOIN for the exercise.
Show all information for all students. If a student is assigned to a room, show all information for the room as well.
```
  SELECT
  *
  FROM Student
  RIGHT JOIN Room
  ON Student.RoomId = Room.id;
```

Show the room each student is assigned to. Show all students, even those who are not assigned to any room. Use a RIGHT JOIN
```
  SELECT
  *
  FROM ROOM
  RIGHT JOIN Student
  ON Student.RoomId = Room.id;
```

Show the room each student is assigned to. Include students without a room and rooms without students. Show only two columns: RoomNumber and Name.
```
  SELECT
  Room.RoomNumber,
  Student.Name
  FROM ROOM
  FULL JOIN Student
  ON Student.RoomId = Room.id;
```

Use the full name RIGHT OUTER JOIN to show all kettles together with their rooms (even if there is no room assigned).
```
  SELECT
  *
  FROM ROOM
  RIGHT OUTER JOIN Equipment
  ON Equipment.RoomId = Room.id
  WHERE Name = 'kettle';
```

Use INNER JOIN on the Room and Equipment tables so that all pieces of equipment are shown together with their rooms. 
Use the table aliases R and E, respectively. Select the ID and Name columns from the Equipment table and the RoomNumber and Beds columns from the Room table.
```
  SELECT
  E.ID,
  E.Name,
  R.Roomnumber,
  R.Beds
  FROM ROOM AS R
  INNER JOIN Equipment AS E 
  ON E.RoomId = R.id;
```

We want to know who lives with the student Jack Pearson in the same room. 
Use a self join to show all information for Jack Pearson together with all information for each student living with him in the same room.
Remember to exclude Jack Pearson himself from the result!
```
  SELECT
  *
  FROM Student AS St1
  JOIN Student AS St2
  ON St1.RoomId = St2.RoomId
  WHERE St1.Name = 'Jack Pearson'
  AND St2.Name != 'Jack Pearson'; 
```

For each room with two beds where there are actually two students, show one row that contains the following information:
    The name of the first student.
    The name of the second student.
    The room number.
Don't change any column names. Each pair of students should only be shown once. The student whose name comes first in the alphabet should be shown first.
In terms of T-SQL, "first in the alphabet" means "less than" for text values. In other words, 'A' is less than 'B.'
```
  SELECT
  St1.Name,
  St2.Name,
  RoomNumber
  FROM Student AS St1
  JOIN Student AS St2
  ON St1.RoomId = St2.RoomId
  JOIN Room ON
  St2.RoomId = Room.id
  WHERE St1.Name < St2.Name
  AND Room.Beds = 2;
```

<br/><br/>
<b><p align=center> Subqueries </br>
5 Tables - Country, City, Mountain, Trip, Hiking Trip

Show all information about all cities that have the same area as Paris.
```
  SELECT
    *
  FROM City
  WHERE Area = (
      SELECT Area
      FROM City
      WHERE Name = 'Paris'
  );
```

Find the names of all cities that have a population less than that of Madrid.
```
  SELECT
    Name
  FROM City
  WHERE Population < (
      SELECT Population
      FROM City
      WHERE Name = 'Madrid'
  );
```

Find all information about trips that are more expensive than the average across all trips.
```
  SELECT
    *
  FROM Trip
  WHERE Trip.Price > (
    SELECT
      AVG(Trip.Price)
    FROM Trip
  );
```

Find all information about hiking trips with a difficulty of 1, 2, or 3.
```
    SELECT
    *
    FROM HikingTrip
    WHERE Difficulty
    IN (1, 2, 3);
```

Find all information about all trips in cities with an area exceeding 100.
```
    SELECT
    *
    FROM Trip
    WHERE Trip.CityId IN (
      SELECT
        City.Name
      FROM City
      WHERE City.Area > 100
    );    
```

Find all information about cities that are less populated than all countries in the database.
```
    SELECT
    *
    FROM City
    WHERE City.Population < ALL (
      SELECT
        Country.Population
      FROM Country
    );    
```

Find all information about all city trips that have the same price as any hiking trip.
```
  SELECT
  *
  FROM Trip
  WHERE Trip.Price = ANY (
    SELECT
    HikingTrip.Price
    From
    HikingTrip
  )
```

Change the template (the answer from the last exercise) so it uses SOME instead of ANY.
```
  SELECT
  *
  FROM Trip
  WHERE Trip.Price = SOME (
    SELECT
    HikingTrip.Price
    From
    HikingTrip
  )
```

Find all information about each country whose population is less than or equal to the population of the least populated city in that specific country.
```
  SELECT
   *
  FROM Country
  WHERE Country.Population <= (
    SELECT
      MIN(City.Population)
    FROM City
    WHERE City.CountryId = Country.id
  );
```

For each country, find all information about cities in that country with a rating higher than the average rating of all cities in that country.
```
  SELECT
   *
  FROM City AS MainCity
  WHERE MainCity.Rating > (
    SELECT
      AVG(City.Rating)
    FROM City
    WHERE City.CountryId = MainCity.CountryId
  );
```

Show all information about all trips to cities with a city rating lower than 4.
```
  SELECT
    *
  FROM Trip
  WHERE Trip.CityID IN (
    SELECT
      City.ID
    FROM City
    WHERE City.Rating < 4
  );
```

Select all countries where there is at least one mountain.
```
  SELECT
  *
  FROM Country
  WHERE EXISTS(
    SELECT
    *
    FROM Mountain
    WHERE Mountain.CountryId = Country.Id
  )
```

Select all mountains with no hiking trips to them.
```
  SELECT
  *
  FROM Mountain
  WHERE NOT EXISTS(
    SELECT
    *
    FROM HikingTrip
    WHERE HikingTrip.MountainId = Mountain.Id
  )
```

Select the hiking trip with the longest distance (Length column) for every mountain.
```
  SELECT
  *
  FROM HikingTrip AS MainTrip
  WHERE MainTrip.Length >= ALL(
    SELECT
    HikingTrip.Length
    FROM HikingTrip 
    WHERE MainTrip.MountainId = HikingTrip.MountainId
  )
```
