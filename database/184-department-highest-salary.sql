-- Table: Employee

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | id           | int     |
-- | name         | varchar |
-- | salary       | int     |
-- | departmentId | int     |
-- +--------------+---------+
-- id is the primary key column for this table.
-- departmentId is a foreign key of the ID from the Department table.
-- Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

-- Table: Department

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- +-------------+---------+
-- id is the primary key column for this table.
-- Each row of this table indicates the ID of a department and its name.
 

-- Write an SQL query to find employees who have the highest salary in each of the departments.

select Department,Employee,salary 
from(
    select e.departmentId ,e.name as Employee,e.salary,MAX(e.salary) OVER(PARTITION BY e.departmentId) as Salary_rank, d.name as Department
    from Employee e
    left join Department d
    on e.departmentId = d.id
) x 
where x.Salary_rank = x.salary
