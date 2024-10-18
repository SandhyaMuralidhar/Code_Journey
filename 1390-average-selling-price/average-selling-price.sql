/* Write your PL/SQL query statement below with s1 as (select u.product_id, u.units, p.price, u.units* p.price SP from prices  p inner join unitssold u on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date)
select product_id , round(sum(sp)/sum(units),2) average_price from s1 group by product_id*/
/*
with s1 as
(select p.product_id,sum(u.units*p.price) t1 from prices p inner join unitssold u on u.product_id =p.product_id and u.purchase_date between p.start_date and p.end_date group by p.product_id ),
s2 as (
select p.product_id,sum(u.units) t2 from prices p inner join unitssold u on u.product_id =p.product_id and u.purchase_date between p.start_date and p.end_date group by p.product_id)

select s.product_id,round(s.t1/q.t2,2) average_price  from s1 s inner join s2 q on s.product_id=q.product_id
select product_id, nvl(round((sum(total)/sum(units)),2),0) average_price from (
select p.product_id, nvl(p.price,0) ,u.units,nvl(p.price,0) *nvl(u.units,0) total from prices p left join unitssold u on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date) group by product_id
*/
select p.product_id, nvl(round((sum(u.units * nvl(p.price,0))/sum(u.units)),2),0) average_price  from prices p left join Unitssold u on u.product_id = p.product_id and u.purchase_date between p.start_date and p.end_date group by p.product_id