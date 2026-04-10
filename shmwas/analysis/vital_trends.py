import numpy as np

def average_bp(patients):
    values = []

    for p in patients:
        for v in p.vitals:
            try:
                sys = int(v["bp"].split("/")[0])
                values.append(sys)
            except:
                pass

    if len(values) == 0:
        print("No BP data")
        return

    arr = np.array(values)
    print("Average BP:", np.mean(arr))

def average_sugar(patients):
    values = []

    for p in patients:
        for v in p.vitals:
            try:
                values.append(int(v["sugar"]))
            except:
                pass

    if len(values) == 0:
        print("No sugar data")
        return

    arr = np.array(values)
    print("Average Sugar:", np.mean(arr))

def detect_high_bp(patients):
    for p in patients:
        for v in p.vitals:
            try:
                sys = int(v["bp"].split("/")[0])
                dia = int(v["bp"].split("/")[1])

                if sys > 140 or dia > 90:
                    print("High BP:", p.name)
            except:
                pass