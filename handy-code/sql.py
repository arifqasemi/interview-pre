"SELECT (SELECT DISTINCT salary   FROM Employee order by salary DESC limit 1 OFFSET  1) as SecondHighestSalary"

"SELECT email as Email From Person group by email Having Count(*) > 1"

"SELECT e.name as Employee from Employee as e join Employee as m on e.managerId = m.id where e.salary > m.salary"

"SElECT e.name Department,d.name Employee,e.salary Salary from Employee as e join Department as d on e.departmentId  = d.id where e.salary =(SELECT Max(salary) from Employee where departmentId =e.departmentId)"

"SELECT name as Customers from Customers as c left join  Orders as o on o.customerId  =c.id where o.id IS Null"
"UPDATE Salary SET sex= CASE WHEN sex = 'f' THEN 'm' WHEN sex ='m' THEN 'f' ELSE sex END"

"SELECT w1.id FROM Weather w1 JOIN Weather w2   ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 WHERE w1.temperature > w2.temperature;"