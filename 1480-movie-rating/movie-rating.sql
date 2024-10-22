/* Write your PL/SQL query statement below */
/*(
select name results from(
select name , rank() over (order by cnt desc, name asc) ra from (
select m.user_id, u.name, count(*) cnt from movieRating m inner join users u on m.user_id = u.user_id group by m.user_id,u.name)) where ra =1)

union all

(
select title results from (
select title , rank () over (order by av desc,title asc) ra from (
select v.title, avg(m.rating) av from movierating m  inner join movies v on m.movie_id = v.movie_id where m.created_at like '2020-02%'group by v.title) ) where ra =1)


*/










with q1 as 
(select u.user_id, u.name, count(m.user_id) cnt from users u inner join movierating m on u.user_id = m.user_id group by u.user_id,u.name),
q2 as (select name, rank() over (order by cnt desc, name asc) ra from q1),
q3 as (select m.movie_id, m.title, avg(r.rating) cnt1 from movies m inner join Movierating r on m.movie_id = r.movie_id where to_char(created_at) like '2020-02-%' group by m.movie_id, m.title),
q4 as (select title , rank() over (order by cnt1 desc, title asc) ra from q3)

select name results from q2 where ra=1
union all select title results from q4 where ra =1