-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT   city, AVG(value) as average FROM temperatures GROUP BY city   ORDER BY average DESC;
 