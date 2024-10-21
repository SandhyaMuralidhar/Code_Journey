
/* Write your PL/SQL query statement below select contest_id, round(count(user_id)/(select count(user_id) from users)*100,2) percentage from register group by contest_id order by 2 desc,1; */
select contest_id, round((count(*)/(select count(*) from users)*100),2) percentage from register group by contest_id order by 2 desc, 1 asc;