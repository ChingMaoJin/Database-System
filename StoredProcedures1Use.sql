#ChingMaoJin_22013213
#Name: Ching Mao Jin
#StudentID: 22013213
#Database System 2024 Sem2

#Creating Stored Procedures for first use
/* Use: When the athlete has entered the name wrongly, the name has to be corrected. */
Drop Procedure if exists UpdateAthleteName; -- To ensure you do not create the same procedure
Delimiter $$  -- Change the delimiter to $$

#Creating procedure to take in NewName and AthleteID and return the updated name

Create Procedure UpdateAthleteName(
    IN NewName Varchar(100), 
    IN AthleteID int,
    OUT UpdatedName Varchar(100)
)
Begin 
	Declare AthleteIDExists INT;
	Select Count(Athlete_ID) into AthleteIDExists from Athlete where Athlete_ID=AthleteID;
    	IF AthleteIDExists>0 THEN -- Check the validity of the Athlete ID provided
		# Update the Athlete name to the new one
		Update Athlete
		set Athlete_Name=NewName
		where Athlete_ID=AthleteID;
		set UpdatedName=NewName; -- Return the new name

	ELSE
        	set UpdatedName='Athlete cannot be found with the provided id';
    	END IF;
END $$
Delimiter ;


