/* Write your PL/SQL query statement below 
select  distinct num ConsecutiveNums from (
select num, lead(num) over(order by id) next , lag(num) over(order by id) prev from logs) where next-prev=0 and num=prev;*//*

select distinct l2.num  ConsecutiveNums from logs l1, logs l2 , logs l3 where l2.id-1 = l1.id and l3.id-1 = l2.id and l1.num=l2.num and l2.num = l3.num;*/






select distinct num ConsecutiveNums from(
select num, lead(num) over (order by id) next_num, lag(num) over (order by id) prev_num from logs) where next_num = num and num = prev_num;