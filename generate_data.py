import pandas as pd, random

ambulances = []
hospitals = []

for i in range(1, 501):
    lat = round(12.90 + random.uniform(0, 0.2), 6)
    lon = round(77.55 + random.uniform(0, 0.2), 6)
    status = random.choice(["available", "busy"])
    ambulances.append([f"A{i}", lat, lon, status])

    beds = random.randint(0, 20)
    hospitals.append([f"H{i}", f"Hospital_{i}", lat, lon, beds])

pd.DataFrame(ambulances, columns=["id","lat","lon","status"]).to_csv("ambulances.csv", index=False)
pd.DataFrame(hospitals, columns=["id","name","lat","lon","beds_available"]).to_csv("hospitals.csv", index=False)

print("Generated 500 ambulances & 500 hospitals ✅")
