class Patient:
    def __init__(self, first_name, last_name, year_of_birth, weight, height, cholesterol_level):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.weight = weight
        self.height = height
        self.cholesterol_level = cholesterol_level

    def calculate_age(self):
        current_year = 2024
        return current_year - self.year_of_birth

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return bmi

    def categorize_age(self):
        age = self.calculate_age()
        return "Minor" if age < 18 else "Adult"

    def categorize_bmi(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def categorize_cholesterol(self):
        if self.cholesterol_level < 200:
            return "Normal"
        elif 200 <= self.cholesterol_level < 240:
            return "Borderline High"
        else:
            return "High"

    def health_summary(self):
        return {
            "Full Name": f"{self.first_name} {self.last_name}",
            "Age Category": self.categorize_age(),
            "BMI Category": self.categorize_bmi(),
            "Cholesterol Level": self.categorize_cholesterol()
        }


def main():
    patients = []
    while True:
        first_name = input("Enter the patient's first name: ")
        last_name = input("Enter the patient's last name: ")
        year_of_birth = int(input("Enter the year of birth: "))
        weight = float(input("Enter weight (in kg): "))
        height = float(input("Enter height (in meters): "))
        cholesterol_level = float(input("Enter cholesterol level (mg/dL): "))

        patient = Patient(first_name, last_name, year_of_birth, weight, height, cholesterol_level)
        patients.append(patient)

        summary = patient.health_summary()
        print("\n--- Health Summary for", summary["Full Name"], "---")
        for key, value in summary.items():
            print(f"{key}: {value}")

        another = input("Would you like to enter another patient's details? (Yes/No): ")
        if another.lower() != 'yes':
            break

    print("Thank you for using the Patient Health Profile Manager & Analyzer!")


if __name__ == "__main__":
    main()
