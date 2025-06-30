#ChingMaoJin_22013213
#Name: Ching Mao Jin
#StudentID: 22013213
#Database System 2024 Sem2
#Creating VIEW for third use

-- Creating a view to get the Athlete_ID, Event_ID, and Athlete_Name that are in the medallist
DROP VIEW IF EXISTS isIncluded;
CREATE VIEW isIncluded as 
SELECT M.Athlete_ID, M.Event_ID, A.Athlete_Name
FROM Athlete A INNER JOIN Medallist M 
ON A.Athlete_ID=M.Athlete_ID;