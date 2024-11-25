/* Write your PL/SQL query statement below */
/*select product_name, unit from(
select p.product_name, o.product_id, sum(o.unit) unit from orders o inner join products p on p.product_id = o.product_id where to_char(o.order_date) like '2020-02%' group by o.product_id,p.product_name) where unit>= 100;
*/

/* Write your MySQL query statement below*/
select p.product_name, sum(o.unit) unit from products p inner join orders o on p.product_id = o.product_id  where to_char(order_date,'yyyy-mm') like to_char('2020-02')group by p.product_name having sum(unit)>=100