/* Write your PL/SQL query statement below *//*
with t1 as (select count(product_key) cnt from product )
select customer_id from (select customer_id,product_key from customer group by customer_id, product_key) group by customer_id having count(customer_id) = (select cnt from t1)*/






select customer_id  from(
select customer_id, count(distinct product_key) cnt from customer group by customer_id ) where cnt = (select count(product_key) from product)
