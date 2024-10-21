/* Write your PL/SQL query statement below *//*
select max(num) num from(
select num from Mynumbers group by num having count(num)=1);*/






select max(num) num from (
select num, count(*) from Mynumbers group by num having count(*)=1);