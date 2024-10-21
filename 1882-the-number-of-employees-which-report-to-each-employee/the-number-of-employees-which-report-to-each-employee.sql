# Write your MySQL query statement below/*
/*with s1 as 
 (select b.reports_to , count(b.reports_to) reports_count,round(avg(b.age)) average_age  from employees b  group by b.reports_to)
select a.employee_id, a.name,  s1.reports_count, s1.average_age from s1 s1 inner join employees a where a.employee_id = s1.reports_to order by 1 ;*/

 with q1 as 
(select reports_to , count(*) cnt, round(avg(age)) average_age from employees group by reports_to )

select e.employee_id , e.name, q1.cnt reports_count, q1.average_age from employees e inner join q1 on q1.reports_to = e.employee_id order by e.employee_id