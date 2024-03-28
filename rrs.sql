--
-- Database: `railway_reservation`
--

-- --------------------------------------------------------

CREATE TABLE Train (
    Train_Number INT NOT NULL PRIMARY KEY,
    Train_Name VARCHAR(255) NOT NULL,
    Premium_Fair FLOAT NOT NULL,
    General_Fair FLOAT NOT NULL,
    Source_Station VARCHAR(255) NOT NULL,
    Destination_Station VARCHAR(255) NOT NULL
);

CREATE TABLE Train_Status (
    TrainDate DATE NOT NULL,
    TrainName VARCHAR(255) NOT NULL,
    PremiumSeatsAvailable INT NOT NULL,
    GenSeatsAvailable INT NOT NULL,
    PremiumSeatsOccupied INT NOT NULL,
    GenSeatsOccupied INT NOT NULL,
    PRIMARY KEY (TrainDate, TrainName),
    FOREIGN KEY (TrainName) REFERENCES Train(Train_Name) ON DELETE CASCADE
);

CREATE TABLE Passenger (
    First_Name VARCHAR(255) NOT NULL,
    Last_Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(255) NOT NULL,
    County VARCHAR(255) NOT NULL,
    Phone VARCHAR(10) NOT NULL,
    SSN CHAR(9) NOT NULL PRIMARY KEY,
    Birth_Date DATE NOT NULL
);

CREATE TABLE Booked (
    Passenger_SSN CHAR(9) NOT NULL,
    Train_Number INT NOT NULL,
    Ticket_Type VARCHAR(10) NOT NULL,
    Status VARCHAR(10) NOT NULL,
    PRIMARY KEY (Passenger_SSN, Train_Number),
    FOREIGN KEY (Passenger_SSN) REFERENCES Passenger(SSN) ON DELETE CASCADE,
    FOREIGN KEY (Train_Number) REFERENCES Train(Train_Number) ON DELETE CASCADE
);

--
-- Dumping data for table `Train`
--


INSERT INTO `Train` values (1,`Orient Express`,800,600,`Paris`,`Istanbul`),
(2, `Flying Scottsman`,4000,3500,`Edinburgh`,`London`),
(3, `Golden Arrow`,980,860,`Victoria`,`Dover`),
(4, `Golden Chariot`,4300,3800,`Bangalore`,`Goa`),
(5, `Maharaja Express`,5980,4510,`Delhi`,`Mumbai`);

--
-- Dumping data for table `Train_status`
--


INSERT INTO `Train_Status` values
(`2022-02-19`,`Orient Express`,10,10,0,0),
(`2022-02-20`, `Flying Scottsman`,8,5,2,5),
(`2022-02-21`, `Maharaja Express`,7,6,3,4),
(`2022-02-21`, `Golden Chariot`,6,3,4,7),
(`2022-02-22`, `Golden Arrow`,8,7,2,3);


--
-- Dumping data for table `Booked`
--


INSERT INTO `Booked` values
(264816896,3,`Premium`,`Booked`),
(240471168,2,`General`,`Booked`),
(302548590,2,`General`,`WaitL`),
(284965676,3,`Premium`,`WaitL`);


--
-- Dumping data for table `Passanger`
--



INSERT INTO `Passenger`  values
(`James`,`Butt`,`6649 N Blue Gum St`,`New Orleans`,`Orleans`,`504-845-1427`,264816896,`10/10/68`),
(`Josephine`,`Darikjy`,`4 B Blue Ridge Blvd`,`Brihton`,`Livingston`,`810-374-9840`,240471168,`11/1/75`),
(`Art`,`Venere`,`8 W Cerritos Ave #54`,`Bridgeport`,`Gloucester`,`856-264-4130`,285200976,`11/13/82`),
(`Lenna`,`Paprocki`,`639 Main St`,`Anchorage`,`Anchorage`,`504-845-1427`,264816896,`10/10/68`);
