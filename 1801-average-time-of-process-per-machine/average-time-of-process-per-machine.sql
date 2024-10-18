# Write your MySQL query statement below
/*
with q1 as
(select a.machine_id,a.process_id, a.timestamp t1 from activity a where a.activity_type = 'start' group by a.machine_id,a.process_id ),
q2 as
(select a.machine_id,a.process_id, a.timestamp t1 from activity a where a.activity_type = 'end' group by a.machine_id,a.process_id )
select q1.machine_id,round(avg(q2.t1-q1.t1),3) processing_time from q1 inner join q2 on q1.machine_id=q2.machine_id and q1.process_id=q2.process_id group by q1.machine_id
with q1 as(
select machine_id, process_id , timestamp end_time from activity where activity_type = "end" group by machine_id, process_id ),
q2 as (
 select machine_id, process_id , timestamp start_time from activity where activity_type = "start" group by machine_id, process_id  
)
select q1.machine_id, round(avg(q1.end_time-q2.start_time),3) processing_time  from q1 inner join q2 on q1.machine_id =q2.machine_id and q1.process_id=q2.process_id group by q1.machine_id;*/

with q1 as (
select a.machine_id , b.timestamp-a.timestamp processing_time from activity a inner join activity b on a.machine_id =b.machine_id and a.process_id = b.process_id and a.activity_type='start' and b.activity_type= "end" )
select q1.machine_id, round(avg(q1.processing_time),3) processing_time from q1 group by q1.machine_id;