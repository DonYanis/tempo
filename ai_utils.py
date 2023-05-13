from knowledge_base import *
from aima.logic import *
from aima.utils import *
from advice import *

def init_FAI_KB():

    fc = FolKB()

    for exp in HEALTH_STATE : 
        fc.tell(expr(exp))
    
    for exp in FOOD_CONSUMPTION : 
        fc.tell(expr(exp))

    for exp in TRAINING : 
        fc.tell(expr(exp))
    
    for exp in TRAINING_PROGRAM : 
        fc.tell(expr(exp))

    for exp in EAT_FOOD : 
        fc.tell(expr(exp))
    
    for exp in AVOID_FOOD : 
        fc.tell(expr(exp))

    for exp in ADVICE : 
        fc.tell(expr(exp))

    return fc


def init_user(data, fc):

    memo  = [
        f"Gender({data['name']},{data['gender']})",
        f"Age({data['name']},{data['age']})",
        f"Activity({data['name']},{data['activity']})",
        f"Weight({data['name']},{data['weight_cat']})",
        f"Goal({data['name']},{data['goal']})",
        f"Schedule({data['name']},{data['schedule']})",
        f"BMI({data['name']},{data['bmi']})",
    ]


    for exp in memo : 
        fc.tell(expr(exp))

    return memo


def generate_agenda(name):

    agenda = []
    for predicate in ['Health','Food','Training','Program','Eat','Advice'] :
        agenda.append([predicate,f"{predicate}({name},x)"])

    agenda.append(['Avoid','Avoid(x)'])

    return agenda


def backward_chaining(fc, exp) :

    result = list(fol_bc_ask(fc,expr(exp)))
    if len(result) > 0 : 
        data = []
        for dic in result : 
            data.append(str(dic.get(x)))
        return data
    return None


def inference_engine(fc, agenda) : 

    data = {}
    for couple in agenda :
        result = backward_chaining(fc, couple[1])
        if couple[0] == 'Advice' :
            data[couple[0].lower()] = replace_advice(result)
        else:
            data[couple[0].lower()] = result
    
    return data


def replace_advice(advice):
    
    temp = []
    for adv in advice:
        temp.append(Aj[str(adv)])
    
    return temp