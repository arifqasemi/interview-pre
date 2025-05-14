COUNT()
############

SELECT department, COUNT(*) AS employee_count
FROM Employee
GROUP BY department;

MAX()
###########
SELECT department, MAX(salary) AS top_salary
FROM Employee
GROUP BY department;




MIN()
SUM()
##############
SELECT region, SUM(amount) AS total_sales
FROM Sales
GROUP BY region;

SELECT department, SUM(salary) AS total_salary
FROM Employee
GROUP BY department;


AVG()
###############