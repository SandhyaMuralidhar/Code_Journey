/* Write your PL/SQL query statement below 
with q1 as (select visits.visit_id from visits left join transactions on visits.visit_id = transactions.visit_id
minus
select visits.visit_id from visits inner join transactions on visits.visit_id = transactions.visit_id)

select count(visits.customer_id) from (select q1.visit_id, visits.customer_id from q1 inner join visits on visits.visit_id = q1.visit_id) group by  visits.customer_id

select v.customer_id from visits v inner join transactions t on v.visit_id = t.visit_id 
select customer_id , count(*) count_no_trans  from visits where visit_id in (select visit_id from visits minus select visit_id from transactions) group by customer_id;
*/
with q1 as (
select visit_id from visits minus select visit_id from transactions)
select v.customer_id, count(*) count_no_trans  from visits v inner join q1 on q1.visit_id = v.visit_id group by v.customer_id;