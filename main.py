from utils import *
from ai_utils import *

#input
data = {
    'name': 'JOHN',
    'age' : 'YOUNGADULT',
    'gender' : 'MALE',
    'activity' : 'MEDIUM',
    'height': 1.8,
    'weight' : 70,
    'goal' : 'MUSCLE',
    'schedule' : 'FLEXIBLE'
}

# non ai stuff
data['bmi'] = get_BMI_category(data['weight'], data['height'])
data['weight_cat'] = get_weight_category(data['weight'], data['height'])
macros = get_nutrition_requirements(data['weight'], data['height'],data['gender'], data['activity'],data['goal'],data['age'] )


# ai stuff : 

# 1- knowledge base
fc = init_FAI_KB()
init_user(data,fc)

# 2- inference
inference_logic(data['name'], fc)