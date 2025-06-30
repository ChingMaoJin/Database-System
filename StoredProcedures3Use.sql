#ChingMaoJin_22013213
#Name: Ching Mao Jin
#StudentID: 22013213
#Database System 2024 Sem2
#Creating a stored procedure to delete Athlete name from the table

Drop Procedure if exists DeleteAthleteName; -- To ensure you do not create the same procedure
Delimiter $$  -- Change the delimiter to $$

#Creating procedure to take in AthleteID and return the deleted name

Create Procedure DeleteAthleteName(
    IN AthleteID int,
    OUT DeletedName Varchar(100)
)
Begin 
	Declare AthleteIDExists INT;
	DECLARE Delete_Name varchar(100);
	Select Count(Athlete_ID) into AthleteIDExists from Athlete where Athlete_ID=AthleteID; -- Assigning value into the local variable AthleteIDexists
    	IF AthleteIDExists>0 THEN -- Check the validity of the Athlete ID provided
    		Select Athlete_Name into Delete_Name from Athlete where Athlete_ID=AthleteID; -- Assigning value to the variable DeletedName
		#Delete tuple correspond to the athlete id
		set DeletedName=Delete_Name; -- Return the new name
		-- Delete the tuple from the Athlete table
		Delete from Athlete
		where Athlete_ID=AthleteID;
		
		-- There's a trigger to delete the child tables
		
	ELSE
        	set DeletedName='Athlete cannot be found with the provided id';
    	END IF;
END $$
Delimiter ;
