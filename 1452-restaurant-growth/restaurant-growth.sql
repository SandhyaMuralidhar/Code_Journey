/*select visited_on,amount, average_amount from (
select visited_on , sum(amount) over (order by visited_on rows 6 preceding) amount,
round(avg(amount) over (order by visited_on rows 6 preceding),2) average_amount,
row_number() over (order by visited_on ) rn
from
(select to_char(visited_on, 'yyyy-mm-dd') visited_on, sum(amount) amount from customer group by to_char(visited_on, 'yyyy-mm-dd')))
where rn>6;*/


select to_char(visited_on,'yyyy-mm-dd') visited_on, amount, average_amount from(
select visited_on, sum(amount) over (order by visited_on rows 6 preceding ) amount, round(avg(amount) over (order by visited_on rows 6 preceding),2) average_amount, rank() over (order by visited_on) ra from (select visited_on, sum(amount) amount from customer group by visited_on)) where ra>6;