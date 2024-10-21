/* Write your PL/SQL query statement below *//*
select user_id, count(follower_id) followers_count from (
select user_id, follower_id from followers group by user_id, follower_id) group by user_id order by 1 */









select user_id, count(distinct follower_id)  followers_count from followers group by user_id order by 1;