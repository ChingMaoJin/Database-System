#ChingMaoJin_22013213
#Name: Ching Mao Jin
#StudentID: 22013213
#Database System 2024 Sem2

-- Creating tables for the database

-- Drop the child tables before the parent tables
Drop Table if exists Register; 
Drop Table if exists Schedule;
Drop Table if exists Medallist;
Drop Table if exists Event;
Drop Table if exists Athlete;
Drop Table if exists Venue;
Drop Table if exists Team;
Drop Table if exists Coach;

Create Table Coach( 
    Coach_ID int not null, -- Primary Key
    Coach_Name Varchar(100) not null,
    Gender Char(2) not null, -- Only accept 'M' or 'F'
    Country char(5) not null,
    Sport Varchar(100) not null, 
    Primary Key(Coach_ID) -- Primary key constraint
);

Create Table Team( 
    Team_ID int not null, -- Primary Key
    Team_Name Varchar(30) not null,
    Coach_Name Varchar(50) not null,
    Country char(5) not null,
    Sport Varchar(100) not null,
    Primary Key(Team_ID) -- Primary key constraint
);

Create Table Venue( 
    Venue_ID int not null, -- Primary Key
    Venue_Name Varchar(100) not null,
    Sport Varchar(100) not null,
    Primary Key (Venue_ID) -- Primary key constraint
);

# References to Coach

Create Table Athlete(
    Athlete_ID int not null, -- Primary Key
    Athlete_Name Varchar(50) not null,
    Gender char(2) not null,
    Team_Name Varchar(30),
    Country char(5) not null,
    Competition_Type Varchar(12) not null,
    Coach_Name Varchar(50) not null,
    Sport Varchar(100) not null,
    Coach_ID int not null, -- Foreign Key
    Age int not null Check(Age>=14 AND Age<=35), -- Check constraint
    constraint fk_Coach Foreign Key(Coach_ID) References Coach(Coach_ID) ON DELETE CASCADE, -- Foreign key constraint
    Primary Key(Athlete_ID)
);

# References to Venue
-- Event ID can uniquely identify sports, start_Date and end_date

Create Table Event(
    Event_ID int not null, -- Primary Key
    Sport Varchar(100) not null,
    Competition_Type Varchar(12) not null,
    Start_Date Date not null,
    End_Date Date not null,
    Venue_ID int not null,
    Event_Time Time not null,
    Primary Key(Event_ID),
    constraint fk_Venue Foreign Key(Venue_ID) References Venue(Venue_ID) ON DELETE CASCADE
);

# References to Athlete

Create Table Medallist( 
    Athlete_ID int not null, -- Primary Key && Foreign Key
    Event_ID int not null, -- Primary Key && Foreign Key
    Athlete_Name Varchar(50) not null, -- This will be shown to remove in Designing and implementing queries
    Medal_Place int not null,
    Competition_Type Varchar(12) not null,
    Gender char(2) not null,
    Country char(5) not null,
    Sport Varchar(100) not null,
    Primary Key(Athlete_ID, Event_ID),
    constraint fk_AthleteID Foreign Key(Athlete_ID) References Athlete(Athlete_ID) 
    ON DELETE CASCADE,
    constraint fk_MedallistEventID Foreign Key(Event_ID) References Event(Event_ID)
    ON DELETE CASCADE
);

# References to Athlete and Event

Create Table Schedule( 
    Athlete_ID int not null, -- PK & FK
    Start_Date Date not null,
    End_Date Date not null,
    Competition_Type Varchar(12) not null,
    Sport Varchar(100) not null,
    Event_ID int not null, -- PK & FK
    Primary Key(Athlete_ID, Event_ID), -- Composite Keys since each athlete may be participating in more than one event, there may be duplicate athlete id in the table.
    constraint fk_Schedule_AthleteID Foreign Key(Athlete_ID) References Athlete(Athlete_ID) ON DELETE CASCADE, -- Use a different name for fk_AthleteID
    constraint fk_Schedule_Event Foreign Key (Event_ID) -- Must follow the primary key constraints order the table 'event'
    References Event(Event_ID) ON DELETE CASCADE
);

# References to Athlete and Event

Create Table Register(
    Athlete_ID int not null, -- PK & FK
    Event_ID int not null, -- PK & FK
    Registration_Date DATE not null,
    Primary Key(Athlete_ID, Event_ID), -- Composite keys since each athlete may have registered for more than one event
    constraint fk_Register_AthleteID Foreign Key (Athlete_ID) References Athlete(Athlete_ID) ON DELETE CASCADE, -- Declaring a foreign key constraint
    constraint fk_Register_Event Foreign Key (Event_ID)
    References Event(Event_ID) ON DELETE CASCADE
);
