#ChingMaoJin_22013213
#Name: Ching Mao Jin
#StudentID: 22013213
#Database System 2024 Sem2

#Creating View for first use
-- 1: Create a view to show athletes that are included in the gold medallist

Drop View if Exists GoldMedal;
Create View GoldMedal as
Select A.Athlete_Name, M.Medal_Place from 
Athlete A inner join Medallist M
On A.Athlete_ID=M.Athlete_ID AND Medal_Place=1;