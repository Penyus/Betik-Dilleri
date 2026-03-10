persons = [{
    "Name ": "John Doe",
    "Age ": 30,
    "City ": "New York"
        }, {
    "Name ": "Jane Smith",
    "Age ": 25,
    "City ": "Los Angeles"
        }, {
    "Name ": "Bob Johnson",
    "Age ": 35,
    "City ": "Chicago"
                    
    }, {
    "Name ": "Alice Brown",
    "Age ": 28,
    "City ": "Houston"
    }, {
    "Name ": "Charlie Davis",
    "Age ": 40,
    "City ": "Phoenix"
    }, {
    "Name ": "Emily Wilson",
    "Age ": 22,
    "City ": "Philadelphia"
    }, {
    "Name ": "David Lee",
    "Age ": 32,
    "City ": "San Antonio"
    }, {
    "Name ": "Sarah Miller",
    "Age ": 27,
    "City ": "San Diego"
    }, {
    "Name ": "Michael Anderson",
    "Age ": 38,
    "City ": "Dallas"
    }]  

for person in persons:
    print("Name:", person["Name "])
    print("Age:", person["Age "])
    print("City:", person["City "])
    print("-" * 20)