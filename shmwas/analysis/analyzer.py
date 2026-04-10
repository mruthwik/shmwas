import pandas as pd

def table(patients):
    data = []

    for p in patients:
        data.append({"name": p.name, "age": p.age})

    df = pd.DataFrame(data)
    print(df)