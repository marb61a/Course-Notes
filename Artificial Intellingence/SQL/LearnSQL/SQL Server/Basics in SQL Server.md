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
