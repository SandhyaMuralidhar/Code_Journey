/* Write your PL/SQL query statement below */
SELECT
DISTINCT S.ID,
S.NAME
FROM
STUDENTS S
WHERE S.DEPARTMENT_ID NOT IN(
SELECT
D.ID
FROM
DEPARTMENTS D
WHERE
D.ID =S.DEPARTMENT_ID
);