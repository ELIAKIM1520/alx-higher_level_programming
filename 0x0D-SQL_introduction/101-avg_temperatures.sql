-- import in hbtn_0c_0 database this table dump
-- dipsplays the average temperature (farenheit) by city ordered by tempure (descending)
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
