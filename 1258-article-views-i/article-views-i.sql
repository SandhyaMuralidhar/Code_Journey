/* Write your PL/SQL query statement below 
select author_id id from views where author_id = viewer_id group by author_id order by 1;*/
select v1.author_id id from views v1 inner join views v2 on v1.author_id = v2.viewer_id and v1.author_id =v2.author_id group by v1.author_id order by 1; 