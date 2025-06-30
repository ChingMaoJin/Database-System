#ChingMaoJin_22013213
#Name: Ching Mao Jin
#StudentID: 22013213
#Database System 2024 Sem2
-- Designing ques and implementing ans as sql queries
-- Part 3 Useful Ques
-- Q1: What is the coach name of the athelete
select Coach_Name from Athlete;

-- Q2: What are the male athletes
select Athlete_Name,Athlete_ID, gender from Athlete where gender='M'
order by(Athlete_ID) desc;

-- Q3: What is the event time for all types of football match
select Event_Time, Sport from Event where Sport Like '%football%';

-- Q4: Remove the athlete name from medallists
Alter table Medallist Drop Column Athlete_Name;

-- Q5: What are the athletes that are included in the medallists
Select A.Athlete_Name, M.Medal_Place from Athlete A LEFT OUTER JOIN Medallist M
on A.Athlete_ID=M.Athlete_ID
where M.Athlete_ID IS NOT NULL;

-- Q6: What are the athletes that awarded gold medal
select A.Athlete_Name, M.Medal_Place, M.Athlete_ID from Athlete As A inner join 
(select Medal_Place, Athlete_ID from Medallist where Medal_Place=1) as M
on M.Athlete_ID=A.Athlete_ID
order by(M.Athlete_ID) desc;

-- Q7: What is the coach for football
select Coach_Name, Sport from Coach
where Sport like '%football%';

-- Q8: What is the venue for badminton
select Venue_Name, Sport from Venue
where Sport='Badminton';

-- Q9: What is the event date for football
select Date_Format(Start_Date, '%e %M %Y') as Event_Date, Sport from Event
where Sport like '%football%';

-- Q10: What are the athletes that are not in the medallists
select A.Athlete_Name, A.Athlete_ID from Athlete as A left outer join Medallist as M 
on A.Athlete_ID=M.Athlete_ID
where M.Athlete_ID is null;

-- Q11: Group the athlete based on the same sport and display the column number of athlete and sport
select Count(Athlete_Name) as Num_of_Athletes, Sport from Athlete Group by (Sport);

-- Q12: How many events takes place between 2024-8-20 to 2024-9-20
select Count(Sport) as Num_Of_Events from Event
where Start_Date between '2024-08-20' and '2024-09-20';

-- Q13: Total numbers of athletes that are not in the medallists
select count(A.Athlete_ID) as number_of_Athletes_not_on_medalList from Athlete as A left outer join Medallist as M
on A.Athlete_ID=M.Athlete_ID
where M.Athlete_ID is null;

-- Q14: Find the average age of the athletes of each sport
select Avg(Age) as Average_Age, Sport from Athlete
Group By(Sport);

-- Q15: Display the athletes who are taking the sport and the sport
select A.Athlete_Name as Athlete1, B.Athlete_Name as Athlete2, A.sport
from Athlete A, Athlete B
where A.sport=B.sport
AND A.Athlete_ID <> B.Athlete_ID
order by (A.sport); 