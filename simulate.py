import requests
import random
import time

# API endpoint
URL = "http://127.0.0.1:5000/report"

# Sample data
names = ["Arun", "Priya", "Ravi", "Karthik", "Meena", "Suresh", "Divya", "Gokul"]
severities = ["low", "medium", "high"]

# Sample accident locations (lat, lon)
locations = [
    (10.95, 78.08),  # near Karur
    (11.02, 76.95),  # near Coimbatore
    (10.80, 78.70),  # near Trichy
    (11.12, 77.35),  # near Erode
]

for i in range(10):  # generate 10 fake incidents
    lat, lon = random.choice(locations)
    data = {
        "reporter_name": random.choice(names),
        "location": {"lat": lat, "lon": lon},
        "injury_severity": random.choice(severities),
        "num_injured": random.randint(1, 3)
    }
    
    try:
        response = requests.post(URL, json=data)
        print(f"Report {i+1}: {response.json()}")
    except Exception as e:
        print(f"Error sending report {i+1}: {e}")
    
    time.sleep(1)  # wait 1 second between reports
