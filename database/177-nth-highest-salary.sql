-- Table: Employee

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- id is the primary key column for this table.
-- Each row of this table contains information about the salary of an employee.
 

-- Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.



CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select max(salary) from 
      (select salary, dense_rank() over (order by salary desc) as s_rank
       from Employee) t
      where s_rank=n
  );
END