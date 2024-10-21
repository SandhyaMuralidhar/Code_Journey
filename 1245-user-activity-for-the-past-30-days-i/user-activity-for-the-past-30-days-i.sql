/* Write your PL/SQL query statement below *//*
with t1 as
(select activity_date, user_id from activity group by activity_date,user_id)

select to_char(t1.activity_date,'yyyy-mm-dd') day , count(user_id) active_users  from t1 where to_date('2019-07-27','yyyy-mm-dd')-activity_date <30 and to_date('2019-07-27','yyyy-mm-dd')-activity_date > -1 group by activity_date order by 1 desc;*/







select  to_char(activity_date,'yyyy-mm-dd') day, count(distinct user_id )active_users from activity  where activity_date between to_date ('2019-07-27', 'yyyy-mm-dd')-29 and to_date ('2019-07-27', 'yyyy-mm-dd')  group by  activity_date order by 1 asc;