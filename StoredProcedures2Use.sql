#ChingMaoJin_22013213
#Name: Ching Mao Jin
#StudentID: 22013213
#Database System 2024 Sem2

#Creating Stored Procedures for second use
/*2Use:Deleting a sport from the event table will cause the relevant sports being deleted from other tables
and the athlete that has selected the deleted sport will be replaced with a sport available under the event table*/

Drop Procedure if exists DeleteAndReplaceSports;
Delimiter $$
Create Procedure DeleteAndReplaceSports(
    IN NewSport Varchar(100),
    IN DeletedSport Varchar(100)
)

Begin 
    -- Delete the rows under Event table that matches with the DeletedSport
    Delete from Event
    where Sport=DeletedSport;

    -- Replace the tables that contain the deleted sport with the new sport

    Update Coach
    set Sport=NewSport
    where Sport=DeletedSport;

    Update Team
    set Sport=NewSport
    where Sport=DeletedSport;

    Update Venue
    set Sport=NewSport
    where Sport=DeletedSport;

    Update Athlete
    set Sport=NewSport
    where Sport=DeletedSport;

    Update Medallist
    set Sport=NewSport
    where Sport=DeletedSport;

    Update Schedule
    set Sport=NewSport
    where Sport=DeletedSport;
END $$
Delimiter ;
