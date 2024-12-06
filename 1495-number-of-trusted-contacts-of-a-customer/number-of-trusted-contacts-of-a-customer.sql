/* Write your PL/SQL query statement below */
with q1 as 
(select i.invoice_id , s.customer_name, i.price from invoices i inner join customers s on s.customer_id =i.user_id order by 1),
q2 as 
(select i.invoice_id, nvl(count(c.user_id),0) cnt1 from invoices i left join contacts c on i.user_id = c.user_id  group by i.invoice_id order by 1),
q3 as
(select i.invoice_id, nvl(count(s.customer_name),0) cnt2 from invoices i left join contacts c on i.user_id = c.user_id left join customers s on s.customer_name = c.contact_name group by i.invoice_id order by 1)
select q1.invoice_id , q1.customer_name, q1.price, q2.cnt1 contacts_cnt,q3.cnt2 trusted_contacts_cnt from q1 inner join q2 on q1.invoice_id=q2.invoice_id inner join q3 on q1.invoice_id = q3.invoice_id order by 1