/* Write your PL/SQL query statement below *//*
select product_id, year first_year, quantity, price from (
select product_id, year, quantity, price, rank() over (partition by product_id order by year) ra from sales ) where ra =1;*/






select product_id, year first_year, quantity,price from(
select s.product_id ,rank() over (partition by product_id order by year) ra, s.year, s.quantity, s.price from sales s) where ra =1;