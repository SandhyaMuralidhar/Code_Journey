/* Write your PL/SQL query statement below 
with s1 as(
select s.user_id,count(c.user_id) cnt from signups s left join confirmations c on s.user_id = c.user_id group by s.user_id),
q2 as(
select c.user_id ,count(c.user_id) cnt from confirmations c where c.action = 'confirmed' group by c.user_id )

select s.user_id ,nvl(round(q.cnt/s.cnt,2),0) confirmation_rate  from s1 s left join q2 q on s.user_id = q.user_id order by 2,1   
with s1 as
(select s.user_id , nvl(count(c.user_id),0) t1 from signups s left join confirmations c on s.user_id = c.user_id group by s.user_id),
s2 as ( select s.user_id , nvl(count(c.user_id),0) t1  from signups s left join confirmations c on s.user_id = c.user_id and c.action like 'confirmed' group by s.user_id)

select s.user_id,case when c.t1=0 or s.t1=0 then 0.0 else round(c.t1/s.t1,2) end confirmation_rate from s1 s, s2 c where s.user_id=c.user_id*/

/*select s.user_id ,count(c.user_id) from signups s left join confirmations c on s.user_id = c.user_id group by s.user_id ;*/
with q1 as 
(select s.user_id, nvl(count(c.user_id),0) cnt1 from signups s left join confirmations c on s.user_id = c.user_id group by s.user_id),
q2 as (select s.user_id, nvl(count(c.user_id),0) cnt1 from signups s left join confirmations c on s.user_id = c.user_id and c.action = 'confirmed' group by s.user_id)
select q1.user_id, case when q1.cnt1!=0 then nvl(round((q2.cnt1/q1.cnt1),2),0) else 0 end confirmation_rate  from q1 inner join q2 on q1.user_id = q2.user_id;