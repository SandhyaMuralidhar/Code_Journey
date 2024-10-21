/* Write your PL/SQL query statement below */
/*
select x, y , z, case when (x+y<=z) or (y+z<=x) or (z+x<=y) then 'No' else 'Yes' end triangle from Triangle*/








select x, y, z , case when (x+y>z) and (y+z>x) and (x+z>y) then 'Yes' else 'No' end triangle from triangle