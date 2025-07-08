# Write your MySQL query statement below
select max(e1.salary) as SecondHighestSalary from Employee e1 where(select count(distinct e2.salary) from Employee e2 where e2.salary>e1.salary)=1;