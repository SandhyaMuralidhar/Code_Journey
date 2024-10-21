# Write your MySQL query statement below
/*with q1 as (select count(distinct customer_id) cnt from delivery )
select count(*)/q1.cnt from delivery d,q1 where (d.customer_id,d.customer_pref_delivery_date ) in(
select distinct customer_id,to_char(first_value(order_date) over (partition by customer_id order by order_date), 'yyyy-mm-dd') from delivery)

*/
with q1 as (
select customer_id, rank() over (partition by customer_id order by order_date asc) rn, order_date, customer_pref_delivery_date from delivery),
q2 as(
select sum(case when order_date=customer_pref_delivery_date then 1 else 0 end ) cnt from q1 where rn=1),
q3 as 
(select count(distinct(customer_id))cnt from delivery)
select round(q2.cnt/q3.cnt*100,2) immediate_percentage  from q2,q3;

