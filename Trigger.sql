#ChingMaoJin_22013213
#Name: Ching Mao Jin
#StudentID: 22013213
#Database System 2024 Sem2
-- When an athlete is deleted from the athlete table, its related details should be deleted from its child table
#Creating trigger after delete an athlete from the table

Drop Trigger if exists AfterDeleteAthlete;
Delimiter $$
Create Trigger AfterDeleteAthlete
After Delete on Athlete For Each row
Begin
    IF Old.Athlete_ID IS NOT NULL THEN
        Delete from Medallist
        where Athlete_ID=Old.Athlete_ID;

        Delete from Schedule
        where Athlete_ID=Old.Athlete_ID;

        Delete from Register
        where Athlete_ID=Old.Athlete_ID;
    END IF;
END $$
Delimiter ;