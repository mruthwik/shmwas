import csv

def export_csv(patients):
    try:
        with open("patients.csv", "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
                "id", "name", "age", "gender",
                "blood", "height", "weight", "phone"
            ])

            for p in patients:
                writer.writerow([
                    p.id,
                    p.name,
                    p.age,
                    p.gender,
                    p.blood,
                    p.height,
                    p.weight,
                    p.phone
                ])
    except:
        print("Error writing CSV")