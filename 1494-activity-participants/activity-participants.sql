/* Write your PL/SQL query statement below */
with q1 as 
(select activity,count(*) cnt,dense_rank() over (order by count(*) asc) rn from friends group by activity order by 2 asc),
q2 as 
(select activity,count(*) cnt,dense_rank() over (order by count(*) desc) rn from friends group by activity order by 2 desc)

select activity from q1 where rn!=1
intersect 
select activity from q2 where rn!=1