/* Write your PL/SQL query statement below 
select user_id , concat(upper(substr(name,1)),lower(substr(name,2))) name from users order by 1*/

select user_id, concat(upper(substr(name,0,1)),lower(substr(name,2))) name  from users order by 1;