from models.patient import Patient
from utils.id_generator import generate_id
from utils.validators import validate_age, validate_phone
from storage.json_store import save_data, load_data
from storage.csv_store import export_csv
from analysis.vital_trends import average_bp, average_sugar, detect_high_bp
from analysis.analyzer import table
from analysis.lifestyle_stats import show as life_stats
from analysis.spending import show as spend_stats
from visual.charts import plot_age
from visual.dashboards import show as dashboard

patients = []

def load_patients():
    data = load_data()

    for d in data:
        p = Patient()
        p.setup(
            d["id"], d["name"], d["age"], d["gender"],
            d["blood"], d["height"], d["weight"], d["phone"]
        )

        p.conditions = d.get("conditions", [])
        p.allergies = d.get("allergies", [])
        p.vitals = d.get("vitals", [])

        patients.append(p)

def add_patient():
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    blood = input("Blood: ")
    height = input("Height: ")
    weight = input("Weight: ")
    phone = input("Phone: ")

    if not validate_age(age):
        print("Invalid age")
        return

    if not validate_phone(phone):
        print("Invalid phone")
        return

    p = Patient()
    p.setup(generate_id(), name, age, gender, blood, height, weight, phone)

    patients.append(p)
    save_data(patients)

def add_vital():
    pid = int(input("ID: "))

    for p in patients:
        if p.id == pid:
            bp = input("BP: ")
            sugar = input("Sugar: ")
            hr = input("HR: ")

            p.add_vital(bp, sugar, hr)
            save_data(patients)
            return

    print("Patient not found")

def view():
    for p in patients:
        p.display()

def analyze():
    average_bp(patients)
    average_sugar(patients)
    detect_high_bp(patients)
    table(patients)

def visuals():
    plot_age(patients)
    dashboard()

def menu():
    while True:
        print("\n1 Add Patient")
        print("2 Add Vital")
        print("3 View")
        print("4 Analyze")
        print("5 Export CSV")
        print("6 Visuals")
        print("7 Lifestyle Stats")
        print("8 Spending Stats")
        print("9 Exit")

        c = input("Choice: ")

        if c == "1":
            add_patient()
        elif c == "2":
            add_vital()
        elif c == "3":
            view()
        elif c == "4":
            analyze()
        elif c == "5":
            export_csv(patients)
        elif c == "6":
            visuals()
        elif c == "7":
            life_stats()
        elif c == "8":
            spend_stats()
        elif c == "9":
            break

load_patients()
menu()