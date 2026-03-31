def calculate_average_scores(users):
    averages = []  
    
    for user in users:
        name = user["name"]
        scores = user["scores"]
        
        
        if len(scores) > 0:
            average = sum(scores) / len(scores)
        else:
            average = 0
        
        averages.append((name, average))  
    
    return averages

def has_admin_access(roles):
    return "admin" in roles  

def main():
    users = [
        {
            "name": "Alice",
            "scores": [85, 90, 72],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [60, 70, 65],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [95, 88, 92],
            "roles": {"admin"}
        }
    ]
    
    
    average_data = calculate_average_scores(users)
    
    
    for user in users:
        name = user["name"]
        roles = user["roles"]
        
        
        for data in average_data:
            if data[0] == name:
                average = data[1]
        
        print("Name:", name)
        print("Average Score:", average)
        print("Admin Access:", has_admin_access(roles))
        print()  



main()
