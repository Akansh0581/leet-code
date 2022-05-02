-- Write an SQL query to report all the duplicate emails.

select email from Person group by email having count(*)>1
