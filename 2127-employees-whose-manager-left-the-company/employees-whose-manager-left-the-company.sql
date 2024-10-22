/* Write your PL/SQL query statement below */
--select e1.employee_id from employees e1 where e1.salary <30000 and e1.manager_id not in (select distinct employee_id from employees) order by 1


select employee_id from employees where salary <30000 and manager_id not in(select employee_id from employees) order by 1;