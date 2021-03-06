SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID;

SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION='Sick' ORDER BY ANIMAL_ID;

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged';

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID;

SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC;

SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;

SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1;

SELECT DATETIME AS 시간 FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;

SELECT COUNT(ANIMAL_ID) FROM ANIMAL_INS

SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS WHERE NAME IS NOT NULL;

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS "count" FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE;

SELECT NAME, COUNT(NAME) as "COUNT" FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME HAVING COUNT(NAME) > 1 ORDER BY NAME;

SELECT hour(DATETIME) as hour, count(datetime) as count FROM ANIMAL_OUTS WHERE hour(DATETIME) between 9 and 19 GROUP BY hour ORDER BY hour;

group by 마지막 문제 해결 못함

SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL ORDER BY ANIMAL_ID;

SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL ORDER BY ANIMAL_ID;

SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE FROM ANIMAL_INS;

SELECT ANIMAL_ID, NAME WHERE ANIMAL_OUTS WHERESELECT ANIMAL_ID, NAME FROM ANIMAL_OUTS WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_INS) ORDER BY ANIMAL_ID;

SELECT A.ANIMAL_ID, A.NAME FROM ANIMAL_INS AS A, ANIMAL_OUTS  AS B WHERE A.ANIMAL_ID = B.ANIMAL_ID AND A.DATETIME > B.DATETIME ORDER BY A.DATETIME;

SELECT I.NAME, I.DATETIME FROM ANIMAL_INS AS I LEFT OUTER JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID WHERE  O.ANIMAL_ID IS NULL ORDER  BY I.DATETIME  LIMIT  3;

SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME FROM ANIMAL_INS AS I, ANIMAL_OUTS AS O WHERE I.ANIMAL_ID = O.ANIMAL_ID AND I.SEX_UPON_INTAKE LIKE 'Intact%' AND (O.SEX_UPON_OUTCOME LIKE'Spayed %' OR O.SEX_UPON_OUTCOME LIKE 'Neutered%');







