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
print("Memory : \n",memory)

# 3- genearating the agenda
agenda = generate_agenda(data['name'])
print("Agenda : \n",agenda)

# 4- inference
result = inference_engine(fc, agenda)


output = {
    'health' : result['health'][0],
    'food' : result['food'][0],
    'training' : result['training'][0],
    'program' : result['program'],
    'eat' : result['eat'],
    'avoid' : result['avoid'],
    'advice' : result['advice'],
    'macros': macros,
    'extra' : {
        'workingmemory' : memory,
        'agenda' : agenda
    }
}

print(output)

# Dump the object to a JSON file
with open("output.json", "w") as f:
    f.write(output.__str__().replace("'", "\""))