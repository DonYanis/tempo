from knowledge_base import *
from aima.logic import *
from aima.utils import *


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

    fc.tell(expr(f"Gender({data['name']},{data['gender']})"))
    fc.tell(expr(f"Age({data['name']},{data['age']})"))
    fc.tell(expr(f"Activity({data['name']},{data['activity']})"))
    fc.tell(expr(f"Weight({data['name']},{data['weight_cat']})"))
    fc.tell(expr(f"Goal({data['name']},{data['goal']})"))
    fc.tell(expr(f"Schedule({data['name']},{data['schedule']})"))
    fc.tell(expr(f"BMI({data['name']},{data['bmi']})"))


def backward_chaining(predicate, name, fc) :

    result = list(fol_bc_ask(fc,expr(f"{predicate}({name},x)")))

    if len(result) > 0 : 
        return result[0].get(x)
    return '-'


def inference_logic(name, fc) : 

    #health
    health_state = backward_chaining('Health', name, fc)
    print('health : ',health_state)

    #food
    food_consumption = backward_chaining('Food', name, fc)
    print('food : ',food_consumption)

    #trainig
    trainig = backward_chaining('Training', name, fc)
    print('train : ',trainig)

    #program
    program = backward_chaining('Program', name, fc)
    print('program : ',program)

    #eat
    food_to_eat = backward_chaining('Eat', name, fc)
    print('eat : ',food_to_eat)

    #avoid
    food_to_avoid = list(fol_bc_ask(fc,expr(f"Avoid(x)")))
    print('avoid : ',food_to_avoid)

    #advice
    advice = backward_chaining('Advice', name, fc)
    print('advice : ',advice)