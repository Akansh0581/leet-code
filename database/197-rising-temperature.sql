-- # Table: Weather

-- # +---------------+---------+
-- # | Column Name   | Type    |
-- # +---------------+---------+
-- # | id            | int     |
-- # | recordDate    | date    |
-- # | temperature   | int     |
-- # +---------------+---------+
-- # id is the primary key for this table.
-- # This table contains information about the temperature on a certain day.
 

-- # Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

-- # Write your MySQL query statement below
select w1.id Id
from Weather as w1
join Weather as w2
on w1.recorddate=date_add(w2.recordDate, INTERVAL 1 DAY)
where w1.Temperature>w2.Temperature