delete from Person
where Id not in 
( select A.Id from (select min(Id) as Id from Person GROUP BY Email) A )