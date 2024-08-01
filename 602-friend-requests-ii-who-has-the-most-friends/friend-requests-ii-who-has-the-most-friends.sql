/* Write your PL/SQL query statement below */
select id, num from (
select id, num, row_number() over (order by num desc)  ra from(
select id,sum(num) num from (
select requester_id id, count(accepter_id) num from requestAccepted group by requester_id
union all
select accepter_id id, count(requester_id) num from requestAccepted group by accepter_id) group by id) ) where ra=1