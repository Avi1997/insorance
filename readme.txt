
POINTS TO REMEMBER--------------------------------------------------------------
To run application change the value in config according to your server
replace the excel data in data.csv file

TABLE STRUCTURE-----------------------------------------------------------------

policy
-----------------------------------------------------------------------------------------------------
policy_id int NOT NULL,                                                                             -
date_of_purchase VARCHAR(255),                                                                      -
fuel VARCHAR(20),                                                                                   -
VEHICLE_SEGMENT VARCHAR(5),                                                                         -
premium VARCHAR(255),                                                                               -
bodily_injury_liability int,                                                                        -
personal_injury_protection int,                                                                     -
property_damage_liability int,                                                                      -
collision int,                                                                                      -
comprehensive int,                                                                                  -
customer_id int,                                                                                    -
PRIMARY KEY (policy_id),                                                                            -
FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)                                          -
-----------------------------------------------------------------------------------------------------

customers
----------------------------------------------------------------------------------------------------- 
customer_id int NOT NULL,                                                                           -
customer_gender VARCHAR(80),                                                                        -
customer_income_group VARCHAR(50),                                                                  -
customer_region VARCHAR(20),                                                                        -
customer_marital_status int,      
PRIMARY KEY (customer_id)                                                                           -
-----------------------------------------------------------------------------------------------------