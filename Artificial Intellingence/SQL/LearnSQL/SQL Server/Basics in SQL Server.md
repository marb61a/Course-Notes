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
