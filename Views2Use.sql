#ChingMaoJin_22013213
#Name: Ching Mao Jin
#StudentID: 22013213
#Database System 2024 Sem2

#Creating VIEW for second use
-- Create a view to get a summary of athlete details such the athlete_ID, athlete_Name, medal place, sport, start_date, coach_name, team_name

DROP VIEW IF EXISTS AthleteSummaryDetails; 
CREATE VIEW AthleteSummaryDetails As
Select A.Athlete_ID, A.Athlete_Name, M.Medal_Place, A.Sport, S.Start_Date, A.Coach_Name, A.Team_Name
from Athlete A 
left outer join Medallist M on A.Athlete_ID=M.Athlete_ID
inner join Schedule S on A.Athlete_ID=S.Athlete_ID;