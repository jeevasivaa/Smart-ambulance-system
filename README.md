# 🚑 Smart Ambulance System

A **Healthcare Data Analytics Project** that connects accident reporters, ambulances, and hospitals in real-time.  
It uses **Flask (Python)** for backend APIs, **Streamlit** for hospital dashboard visualization, and datasets of ambulances & hospitals to simulate real-world emergency responses.

---

## 📌 Features
- Accident report submission via **Web Form** or **API (Postman/JSON)**
- Automatic assignment of **nearest available ambulance**
- Automatic assignment of **nearest hospital with available beds**
- Live **dashboard for hospitals** to view accident cases
- CSV logging of all incoming incidents
- Scalable datasets (500+ ambulances & hospitals supported)

---

## 🛠️ Tech Stack
- **Python 3**
- **Flask** → REST API for accident reporting
- **Streamlit** → Real-time hospital dashboard
- **Pandas** → Data handling (ambulances, hospitals, incidents)
- **Postman** → API testing

---

## 📂 Project Structure
SmartAmbulanceSystem/
│── app.py # Flask API
│── dashboard.py # Streamlit dashboard
│── simulate.py # Accident simulation script
│── generate_data.py # Generates ambulance & hospital datasets
│── utils.py # Haversine distance calculator
│── ambulances.csv # Ambulance dataset (500 entries)
│── hospitals.csv # Hospital dataset (500 entries)
│── incoming_incidents.csv # Logs of accident reports
│── templates/
│ ├── index.html # Accident report form
│ └── result.html # Response page
│── venv/ # Virtual environment


---

## ⚡ Setup & Installation

### 1. Clone Repository
```bash
git clone https://github.com/your-username/SmartAmbulanceSystem.git
cd SmartAmbulanceSystem
