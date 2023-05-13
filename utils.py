def get_BMI_category(weight, height):
    
    bmi = weight / (height ** 2) 
    if bmi < 18.5:
        return "LOW"
    elif 18.5 <= bmi <= 24.9:
        return "GOOD"
    elif 25.0 <= bmi <= 29.9:
        return "HIGH"
    else:
        return "VERYHIGH"

def get_weight_category(weight, height):
    bsa = 0.007184 * (height ** 0.725) * (weight ** 0.425) 
    ideal_weight = bsa * 25 
    if weight < 0.9 * ideal_weight:
        return "UNDER"
    elif 0.9 * ideal_weight <= weight <= 1.1 * ideal_weight:
        return "NORMAL"
    else:
        return "OVER" 
    
def get_nutrition_requirements(weight, height, gender, activity_level, training_goal, age):


    if age == "CHILD":
        age = 8
    elif age == "TEEN":
        age = 15
    elif age == "YOUNGADULT":
        age = 20
    elif age == "MIDDLE":
        age = 30
    elif age == "OLD":
        age = 50
    else:
        return "Invalid age"
    
    # Calculate basal metabolic rate (BMR) using Harris-Benedict equation
    if gender.lower() == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    elif gender.lower() == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
    else:
        return "Invalid gender"
    
    # Adjust BMR based on activity level
    if activity_level == "LOW":
        bmr *= 1.2
    elif activity_level == "MEDIUM":
        bmr *= 1.55
    elif activity_level == "HIGH":
        bmr *= 1.725
    elif activity_level == "VERYHIGH":
        bmr *= 1.9
    else:
        return "Invalid activity level"
    
    # Adjust macronutrient ratios based on training goal
    if training_goal == "LOSS":
        protein_ratio = 1.2
        fat_ratio = 0.1
        carb_ratio = 0.3
    elif training_goal == "GAIN":
        protein_ratio = 1.6
        fat_ratio = 0.25
        carb_ratio = 0.5
    elif training_goal == "MUSCLE":
        protein_ratio = 2.1
        fat_ratio = 0.3
        carb_ratio = 0.5
    elif training_goal == "GENERAL":
        protein_ratio = 1
        fat_ratio = 0.15
        carb_ratio = 0.3
    elif training_goal == "ENDURANCE":
        protein_ratio = 1.6
        fat_ratio = 0.2
        carb_ratio = 0.4
    else:
        return "Invalid training goal"
    
    # Calculate recommended daily intake of calories, protein, fat, carbohydrates, and fiber
    calories = bmr
    protein = protein_ratio * weight
    fat = fat_ratio * calories /9
    carbs = carb_ratio * calories /4
    fiber =  weight / 2
    
    # Return recommended daily intake as a dictionary
    return {"Calories": calories, "Protein": protein, "Fat": fat, "Carbohydrates": carbs, "Fiber": fiber}
