#ChingMaoJin_22013213
#Name: Ching Mao Jin
#StudentID: 22013213
#Database System 2024 Sem2
#Creating trigger after insert on athlete table
-- this trigger will automatically insert tuples into Schedule and Register table.

Drop trigger if exists AfterInsertAthlete;
Delimiter $$
Create Trigger AfterInsertAthlete
After insert on Athlete
For each row
Begin
    -- Declaring local variables
    Declare Event_StartDate DATE;
    Declare Event_EndDate DATE;
    Declare EventID INT;

    -- Assigning the local variables
    Select Start_Date, End_Date, Event_ID into Event_StartDate,Event_EndDate, EventID from Event
    Where Sport=NEW.Sport -- New.Sport refer to the newly insert sport in Athlete table
    Limit 1; -- Limit the return output to one

    -- Inserting into Schedule table with the start_date and end_date of the event
    INSERT INTO Schedule(Athlete_ID, Start_Date, End_Date, Competition_Type,Sport,Event_ID)
    VALUES(NEW.Athlete_ID, Event_StartDate, Event_EndDate, NEW.Competition_Type, NEW.Sport, EventID);

    -- Inserting into register table
    INSERT INTO Register(Athlete_ID, Event_ID, Registration_Date)
    VALUES(NEW.Athlete_ID, EventID, CURDATE());

End $$
Delimiter ;
