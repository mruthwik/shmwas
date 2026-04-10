import json

def save_data(patients):
    data = []

    for p in patients:
        data.append({
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "gender": p.gender,
            "blood": p.blood,
            "height": p.height,
            "weight": p.weight,
            "phone": p.phone,
            "conditions": p.conditions,
            "allergies": p.allergies,
            "vitals": p.vitals
        })

    try:
        with open("patients.json", "w") as f:
            json.dump(data, f)
    except:
        print("Error saving JSON")

def load_data():
    try:
        with open("patients.json", "r") as f:
            return json.load(f)
    except:
        return []