import csv
from typing import final

customers = []
policies = []

#this function traverse the data and save it to the local variables
def map_data():
    with open("data.csv") as f:
        d = csv.DictReader(f)
        l = list(d)

        for val in l:
            policy = {
                "policy_id": val["Policy_id"],
                "date_of_purchase": val["Date of Purchase"],
                "customer_id": val["Customer_id"],
                "fuel": val["Fuel"],
                "VEHICLE_SEGMENT": val["VEHICLE_SEGMENT"],
                "premium": val["Premium"],
                "bodily_injury_liability": val["bodily injury liability"],
                "personal_injury_protection": val[" personal injury protection"],
                "property_damage_liability": val[" property damage liability"],
                "collision": val[" collision"],
                "comprehensive": val[" comprehensive"],

            }
            customer = {
                "customer_gender": val["Customer_Gender"],
                "customer_income_group": val["Customer_Income group"],
                "customer_region": val["Customer_Region"],
                "customer_marital_status": val["Customer_Marital_status"],
                "customer_id": val["Customer_id"],
            }
            if customer not in customers:
                customers.append(customer)
            if policy not in policies:
                policies.append(policy)

#it will create database
def create_db(mysql):
    mycursor = mysql.connection.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS insurance_company")
    mysql.connection.commit()
    mycursor.close()

#this function create all required Table
def create_table(mysql):
    mycursor = mysql.connection.cursor()
    #mycursor.execute("CREATE TABLE insurance_company.customers (customer_id int NOT NULL,customer_gender VARCHAR(80),customer_income_group VARCHAR(50),customer_region VARCHAR(20),customer_marital_status int,PRIMARY KEY (customer_id))")
    #mycursor.execute("CREATE TABLE insurance_company.Policy (policy_id int NOT NULL,date_of_purchase VARCHAR(255),fuel VARCHAR(20),VEHICLE_SEGMENT VARCHAR(5),premium VARCHAR(255),bodily_injury_liability int,personal_injury_protection int,property_damage_liability int,collision int,comprehensive int,customer_id int,PRIMARY KEY (policy_id),FOREIGN KEY (customer_id) REFERENCES insurance_company.customers(customer_id));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS  insurance_company.customers (customer_id int NOT NULL,customer_gender VARCHAR(80),customer_income_group VARCHAR(50),customer_region VARCHAR(20),customer_marital_status int)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS  insurance_company.Policy (policy_id int NOT NULL,date_of_purchase VARCHAR(255),fuel VARCHAR(20),VEHICLE_SEGMENT VARCHAR(5),premium VARCHAR(255),bodily_injury_liability int,personal_injury_protection int,property_damage_liability int,collision int,comprehensive int,customer_id int,PRIMARY KEY (policy_id));")
    
    mysql.connection.commit()
    mycursor.close()
 
#function which inserts data in to database   
def insert_excel(mysql):
    mycursor = mysql.connection.cursor()    
    for customer in customers:
        query = f'insert into insurance_company.customers (customer_id ,customer_gender ,customer_income_group ,customer_region,customer_marital_status) values'
        values = f'({customer["customer_id"]} ,"{customer["customer_gender"]}" ,"{customer["customer_income_group"]}" ,"{customer["customer_region"]}",{customer["customer_marital_status"]})'
        final_query = f'{query}{values}'
        mycursor.execute(final_query)
    
    for policy in policies:
        query = f'insert into insurance_company.Policy (policy_id, date_of_purchase, fuel, VEHICLE_SEGMENT, premium, bodily_injury_liability, personal_injury_protection, property_damage_liability, collision, comprehensive, customer_id) values'
        values = f'({policy["policy_id"]}, "{policy["date_of_purchase"]}", "{policy["fuel"]}", "{policy["VEHICLE_SEGMENT"]}", "{policy["premium"]}", {policy["bodily_injury_liability"]}, {policy["personal_injury_protection"]}, {policy["property_damage_liability"]}, {policy["collision"]}, {policy["comprehensive"]}, {policy["customer_id"]})'
        final_query = f'{query}{values}'
        mycursor.execute(final_query)
    mysql.connection.commit()
    mycursor.close()
    
    

map_data()  
#Flow decider for the first time where we save data from excel to database
def mysql_save_toDb(mysql): 
    create_db(mysql)
    create_table(mysql)
    insert_excel(mysql)
    
