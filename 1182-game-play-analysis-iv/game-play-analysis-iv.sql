/* Write your PL/SQL query statement below with s1 as
(select player_id,event_date  from (select player_id,event_date, dense_rank() over (partition by player_id order by event_date) ra from activity) where ra=1 ),
s3 as
(select  count(distinct a.player_id) cnt from s1 a, activity b where a.player_id = b.player_id and b.event_date-a.event_date=1),
s2 as
(select count(distinct player_id) nt from activity)

select round((a.cnt/b.nt),2) fraction from s3 a, s2 b*/
/*
with s1 as (
select count(*) cnt1 from(
select player_id, device_id, event_date, games_played ,rank() over (partition by player_id order by event_date) ra, lead(event_date) over (partition by player_id order by event_date) le from activity) where ra=1 and le-event_date =1),
s2 as (select count(distinct player_id) cnt2 from activity )

select round(s1.cnt1/s2.cnt2,2) fraction  from s1,s2;
*/


select round(count(a2.player_id)/count(distinct a1.player_id) ,2) fraction from activity a1 left join activity a2 on a1.event_date = a2.event_date-1 and a1.player_id = a2.player_id and (a1.player_id,a1.event_date ) in (select  player_id, min(event_date) from activity group by player_id)