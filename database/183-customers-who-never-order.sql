-- Write an SQL query to report all customers who never order anything.

select c.name 'Customers'
from Customers as c left outer join Orders
as o on c.Id=o.CustomerId
where o.Id is null