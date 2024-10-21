/* Write your PL/SQL query statement below with s1 as (select query_name, sum(case when rating<3 then 1 else 0 end) cnt from queries group by query_name ),
s2 as (select query_name, nvl(sum(rating/position),0) sa, NVL(count(*),0) tot from queries group by query_name)
select s1.query_name,round(s2.sa/s2.tot,2) quality,round(s1.cnt/s2.tot*100,2) poor_query_percentage  from s1 , s2 where s1.query_name=s2.query_name;

*/
with q1 as 
(select query_name , round(avg(rating/position),2) quality, count(*) tot from queries group by query_name),
q2 as (select query_name , sum(case when rating<3 then 1 else 0 end) cnt from queries group by query_name )
select q1.query_name, q1.quality , round((q2.cnt/q1.tot)*100,2) poor_query_percentage from q1 inner join q2 on q1.query_name=q2.query_name;