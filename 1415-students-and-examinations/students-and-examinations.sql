/* Write your PL/SQL query statement below 
select s.student_id,s.student_name,b.subject_name,NVL(count(e.student_id),0) attended_exams 
from students s cross join subjects b left join examinations e on e.student_id=s.student_id and 
e.subject_name = b.subject_name   group by s.student_id,s.student_name, b.subject_name order by 1,2 ;select s.student_id, s.student_name ,j.subject_name,nvl(count(e.student_id),0) attended_exams from students s cross join subjects j left join examinations e on e.student_id = s.student_id and e.subject_name = j.subject_name  group by s.student_id, s.student_name ,j.subject_name order by s.student_id,j.subject_name*/

select s.student_id, s.student_name, b.subject_name, nvl(count(e.student_id),0) attended_exams  from students s cross join subjects b left join examinations e on e.student_id = s.student_id and b.subject_name = e.subject_name group by s.student_id, s.student_name, b.subject_name order by 1,3;