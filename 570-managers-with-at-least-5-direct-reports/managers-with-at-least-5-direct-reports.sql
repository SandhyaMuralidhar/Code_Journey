/* Write your PL/SQL query statement below select name from employee where id in(select managerid 
from employee group by managerid having count(managerid)>=5)*/

select e.name from employee e where e.id in (select managerid from employee group by managerid having count(managerid) >=5)
