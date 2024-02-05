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
  SELECT Vin , Brand, Model
  FROM Car
  WHERE PRODUCTIONYEAR BETWEEN 1995
  AND 2006;
```

