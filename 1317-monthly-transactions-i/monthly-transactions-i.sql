/* Write your PL/SQL query statement below select to_char(trans_date,'yyyy-mm') month, country, count(*) trans_count , sum(case when state='approved' then 1 else 0 end) approved_count , sum(amount) trans_total_amount , sum(case when state='approved' then amount*1 else 0 end) approved_total_amount from transactions group by to_char(trans_date,'yyyy-mm'), country order by 1;;; select to_char(trans_date,'yyyy-mm') month, country ,count(country) trans_count,sum(case when state =  'approved' then 1 else 0 end) approved_count,sum(amount) trans_total_amount,sum(case when state =  'approved' then amount else 0 end) approved_total_amount from transactions group by to_char(trans_date,'yyyy-mm'), country
*/

/*,sum(case state when "approved" then 1 else 0 end)*/

select to_char(trans_date,'yyyy-mm') month , country, count(*) trans_count, sum(case when state= 'approved' then 1 else 0 end) approved_count,sum(amount) trans_total_amount, sum(case when state='approved' then amount else 0 end) approved_total_amount from transactions group by to_char(trans_date,'yyyy-mm'), country
