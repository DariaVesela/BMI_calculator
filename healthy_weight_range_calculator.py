
import pint


def calculate_bmi(weight, height):

    return weight / (height / 100) ** 2

def healthy_weight_range(height):
    lower_bmi = 18.5
    upper_bmi = 24.9

    lower_weight = lower_bmi * (height / 100) ** 2
    upper_weight = upper_bmi * (height / 100) ** 2
    return lower_weight, upper_weight

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))

    bmi = calculate_bmi(weight, height)
    lower_weight, upper_weight = healthy_weight_range(height)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your healthy weight range is: {lower_weight:.2f} kg - {upper_weight:.2f} kg")


if __name__ == "__main__":
    main()
