/* Write your PL/SQL query statement below */
/*
select person_name from queue where turn in(select max(turn) from(
select turn, sum(weight) over (order by turn) sa from queue) where sa<=1000)*/


select person_name from ( 
select person_name, person_id, rank() over (order by turn desc) ra from(
select person_name, person_id,turn, sum(weight) over (order by turn) sa from queue) where sa<=1000) where ra =1