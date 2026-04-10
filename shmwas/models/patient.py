from models.record import Record

class Patient(Record):

    def setup(self, pid, name, age, gender, blood, height, weight, phone):
        super().setup()

        self.id = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.blood = blood
        self.height = height
        self.weight = weight
        self.phone = phone

        self.conditions = []
        self.allergies = []
        self.vitals = []
        self.prescriptions = []
        self.symptoms = []
        self.diagnostics = []
        self.lifestyle = []

    def add_condition(self, cond):
        if cond not in self.conditions:
            self.conditions.append(cond)

    def add_allergy(self, allergy):
        if allergy not in self.allergies:
            self.allergies.append(allergy)

    def add_vital(self, bp, sugar, hr):
        self.vitals.append({
            "bp": bp,
            "sugar": sugar,
            "hr": hr
        })

    def add_prescription(self, p):
        self.prescriptions.append(p)

    def add_symptom(self, s):
        self.symptoms.append(s)

    def add_diagnostic(self, d):
        self.diagnostics.append(d)

    def add_lifestyle(self, l):
        self.lifestyle.append(l)

    def display(self):
        print("\nID:", self.id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Blood:", self.blood)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Phone:", self.phone)
        print("Conditions:", self.conditions)
        print("Allergies:", self.allergies)
        print("Vitals:", self.vitals)