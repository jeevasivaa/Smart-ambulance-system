from flask import Flask, request, jsonify, render_template
import pandas as pd
from utils import haversine
import os

app = Flask(__name__)

# Serve HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Handle both form and JSON data
@app.route('/report', methods=['POST'])
def report():
    if request.content_type == 'application/json':
        data = request.json
    else:
        # Data from HTML form
        data = {
            "reporter_name": request.form.get("reporter_name"),
            "location": {
                "lat": float(request.form.get("lat")),
                "lon": float(request.form.get("lon"))
            },
            "injury_severity": request.form.get("injury_severity"),
            "num_injured": int(request.form.get("num_injured"))
        }

    lat = data['location']['lat']
    lon = data['location']['lon']

    # Find nearest available ambulance
    ambulances = pd.read_csv('ambulances.csv')
    ambulances['dist'] = ambulances.apply(lambda r: haversine(lat, lon, r.lat, r.lon), axis=1)
    available = ambulances[ambulances.status == 'available']
    if available.empty:
        return jsonify({"error": "No ambulances available"}), 503
    chosen_ambulance = available.sort_values('dist').iloc[0].to_dict()

    # Find nearest hospital with beds
    hospitals = pd.read_csv('hospitals.csv')
    hospitals['dist'] = hospitals.apply(lambda r: haversine(lat, lon, r.lat, r.lon), axis=1)
    suitable = hospitals[hospitals.beds_available > 0]
    chosen_hospital = suitable.sort_values('dist').iloc[0].to_dict() if not suitable.empty else hospitals.sort_values('dist').iloc[0].to_dict()

    # Log the incident
    incident = {
        "reporter": data.get("reporter_name", "unknown"),
        "lat": lat,
        "lon": lon,
        "severity": data.get("injury_severity", "unknown")
    }
    df = pd.DataFrame([incident])
    file_exists = os.path.exists('incoming_incidents.csv')
    df.to_csv('incoming_incidents.csv', mode='a', header=not file_exists, index=False)

    # If request came from form, show result page
    if request.content_type != 'application/json':
        return render_template('result.html', ambulance=chosen_ambulance, hospital=chosen_hospital)

    return jsonify({"ambulance": chosen_ambulance, "hospital": chosen_hospital}), 200


if __name__ == '__main__':
    app.run(debug=True)
