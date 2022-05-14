
def map_policy(item):
    finalValue={
        "policy_id":item[0],
        "date_of_purchase":item[1],
        "fuel":item[2],
        "VEHICLE_SEGMENT":item[3], 
        "premium":item[4], 
        "bodily_injury_liability":item[5], 
        "personal_injury_protection":item[6], 
        "property_damage_liability":item[7],
        "collision":item[8],
        "comprehensive":item[9],
        "customer_id" :item[10],
        "customer_gender":item[11] ,
        "customer_income_group" :item[12],
        "customer_region":item[13],
        "customer_marital_status":item[14]        
    }   
    return finalValue
def get_all_policies(mysql):
    final_response = []
    mycursor = mysql.connection.cursor()
    policy_selected_coloumn = "P.policy_id, P.date_of_purchase, P.fuel, P.VEHICLE_SEGMENT, P.premium, P.bodily_injury_liability, P.personal_injury_protection, P.property_damage_liability, P.collision, P.comprehensive,"
    customer_selected_coloumn = "C.customer_id ,C.customer_gender ,C.customer_income_group ,C.customer_region,customer_marital_status"
    query = f'select {policy_selected_coloumn}{customer_selected_coloumn} from policy as P INNER JOIN customers C ON P.customer_id = C.customer_id'
    mycursor.execute(query)
    data = mycursor.fetchall()
    for items in data:
        final_response.append(map_policy(items))
        
    mysql.connection.commit()
    mycursor.close()
    return final_response

def update_policy(mysql):
    return "success"
def route_functions(mysql, path,body):
    match path:
        case 'get-all-policies':
            return get_all_policies(mysql)
        case 'update-policies':
            return update_policy(mysql,body)
        case default:
            return "404"
