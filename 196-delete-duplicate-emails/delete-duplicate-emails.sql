/*
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your PL/SQL query statement below
 delete from person where id not in (select id from(
select id, rank() over (partition by email order by id) ra from person) where ra=1)
 */
delete from person where id in (select p2.id from person p2,person p1 where p1.email=p2.email and p2.id>p1.id)