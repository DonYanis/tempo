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

# 2- Working Memory
memory = init_user(data,fc)
print(memory)

# 3- inference
inference_engine(data['name'], fc)