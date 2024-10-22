# Write your MySQL query statement below
#select (case when MOD(id,2)=1 and t.cnt!=id then id+1 when MOD(id,2)=1 and t.cnt=id then id else id-1 end )id , student from seat ,(select count(*) cnt from seat ) t order by id;


select (case when mod(id,2)!=0 and id!=(select count(*) from seat) then id+1 when mod(id,2)=0 then id-1 else id end) id, student from seat order by 1;