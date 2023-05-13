#Health state : skinny, good, fat, obese
HEALTH_STATE = [
    'Weight(x,UNDER) & BMI(x,LOW) ==> Health(x,TOO_SKINNY)' ,
    'Weight(x,NORMAL) & BMI(x,LOW) ==> Health(x,SKINNY)' ,
    'Weight(x,NORMAL) & BMI(x,GOOD) ==> Health(x,PERFECT)' ,
    'Weight(x,OVER) & BMI(x,GOOD) ==> Health(x,GOOD)' ,
    'Weight(x,NORMAL) & BMI(x,HIGH) ==> Health(x,FAT)' ,
    'Weight(x,OVER) & BMI(x,HIGH) ==> Health(x,FAT)' ,
    'Weight(x,OVER) & BMI(x,VERYHIGH) ==> Health(x,OBESE)' ,
]

#food consumption : reduce, maintain, increase
FOOD_CONSUMPTION = [
    'Health(x,OBESE) ==> Food(x,REDUCE)',
    'Health(x,FAT)==> Food(x,REDUCE)',
    'Health(x,GOOD) & Goal(x,LOSS)==> Food(x,REDUCE)',

    'Health(x,GOOD) & Goal(x,GENERAL)==> Food(x,MAINTAIN)',
    'Health(x,PERFECT) & Goal(x,GENERAL)==> Food(x,MAINTAIN)',
    'Health(x,GOOD) & Goal(x,ENDURANCE)==> Food(x,MAINTAIN)',
    'Health(x,PERFECT) & Goal(x,ENDURANCE)==> Food(x,MAINTAIN)',

    'Health(x,TOO_SKINNY) ==> Food(x,INCREASE)',
    'Health(x,SKINNY) ==> Food(x,INCREASE)',
    'Health(x,GOOD) & Goal(x,MUSCLE)==> Food(x,INCREASE)',
    'Health(x,PERFECT) & Goal(x,MUSCLE)==> Food(x,INCREASE)',
    'Health(x,PERFECT) & Goal(x,GAIN)==> Food(x,INCREASE)',
    'Health(x,GOOD) & Goal(x,GAIN)==> Food(x,INCREASE)',
]

#training intesity : low, average, high 2_3 3_4 5_6
TRAINING = [
    'AGE(x,CHILD) ==>Training(x,AVERAGE)',
    'Schedule(x,BUSY) ==>Training(x,LOW)',
    'Schedule(x,FLEXIBLE) & Goal(x,GENERAL)  ==>Training(x,LOW)',

    'Schedule(x,FLEXIBLE) & Goal(x,GAIN) ==>Training(x,AVERAGE)',
    'Schedule(x,FLEXIBLE) & Goal(x,ENDURANCE) ==>Training(x,AVERAGE)',
    'Schedule(x,FLEXIBLE) & Goal(x,LOSS) ==>Training(x,AVERAGE)',
    'Schedule(x,FLEXIBLE) & Goal(x,MUSCLE) ==>Training(x,AVERAGE)',
    'Schedule(x,OPEN) & Goal(x,GENERAL) ==>Training(x,AVERAGE)',
    'Schedule(x,OPEN) & Goal(x,GAIN) ==>Training(x,AVERAGE)',

    'Gender(x,MALE) & Schedule(x,OPEN) & Goal(x,MUSCLE) ==>Training(x,HIGH)',
    'Gender(x,MALE) & Schedule(x,OPEN) & Goal(x,ENDURANCE)  ==>Training(x,HIGH)',
    'Gender(x,MALE) & Schedule(x,OPEN) & Goal(x,LOSS)  ==>Training(x,HIGH)'
]

#training program : ppl, bbb, cf, ....
TRAINING_PROGRAM = [
    'Age(x,CHILD) ==> Program(x,Active_Start)',
    'Age(x,OLD) ==> Program(x,SilverSneakers)',
    'Training(x,low) ==>Program(x,Circuit)',
    'Training(x,low) ==>Program(x,CrossFit)',

    'Training(x,AVERAGE) & Goal(x,LOSS)==>Program(x,HIIT)',
    'Training(x,AVERAGE) & Goal(x,GAIN)==>Program(x,StrongLifts)',
    'Training(x,AVERAGE) & Goal(x,GAIN)==>Program(x,PPL)',
    'Training(x,AVERAGE) & Goal(x,GENRAL)==>Program(x,CrossFit)',
    'Gender(x,FEMALE) & Training(x,AVERAGE) & Goal(x,GENRAL)==>Program(x,CrossFit)',
    'Training(x,AVERAGE) & Goal(x,GENRAL)==>Program(x,Circuit)',
    'Training(x,AVERAGE) & Goal(x,MUSCLE)==>Program(x,PPL)',
    'Training(x,AVERAGE) & Goal(x,MUSCLE)==>Program(x,GVT)',
    'Training(x,AVERAGE) & Goal(x,MUSCLE)==>Program(x,FourDay_SPLIT)',
    'Training(x,AVERAGE) & Goal(x,ENDURANCE)==>Program(x,Long_Slow_Distance)',

    'Training(x,HIGH) & Goal(x,MUSCLE)==>Program(x,PPLx2)',
    'Training(x,HIGH) & Goal(x,MUSCLE)==>Program(x,ARNOLD_SPLIT)',
    'Training(x,HIGH) & Goal(x,LOSS)==>Program(x,HIIT)',
    'Training(x,HIGH) & Goal(x,ENDURANCE)==>Program(x,The_Murph)',
    'Training(x,HIGH) & Goal(x,ENDURANCE)==>Program(x,Mike_Tyson)'
]

#food to eat
EAT_FOOD = [
    'Goal(x,LOSS)==>EAT(x,Lean_protein)',
    'Goal(x,LOSS)==>EAT(x,Whole_grains)',
    'Goal(x,LOSS)==>EAT(x,Fruits)',

    'Goal(x,GAIN)==>EAT(x,Calorie_dense_foods)',
    'Goal(x,GAIN)==>EAT(x,Lean_protein)',
    'Goal(x,GAIN)==>EAT(x,Healthy_fats)',

    'Goal(x,GENRAL)==>EAT(x,Lean_protein)',
    'Goal(x,GENRAL)==>EAT(x,Whole_grains)',
    'Goal(x,GENRAL)==>EAT(x,Fruits)',

    'Goal(x,MUSCLE)==>EAT(x,Protein)',
    'Goal(x,MUSCLE)==>EAT(x,Complex_carbohydrates)',
    'Goal(x,MUSCLE)==>EAT(x,Healthy_fats)',

    'Goal(x,ENDURANCE)==>EAT(x,Complex_carbohydrates )',
    'Goal(x,ENDURANCE)==>EAT(x,Protein)',
    'Goal(x,ENDURANCE)==>EAT(x,Healthy_fats)'
]

#food to avoid
AVOID_FOOD = [
    'Avoid(Processed_snacks)',
    'Avoid(Soda)',
    'Avoid(Fried_food)',
]

#advice
ADVICE = [
    'Health(x,OBESE)==>Advice(x,A1)',
    'Health(x,FAT)==>Advice(x,A1)',
    'Health(x,SKINNY)==>Advice(x,A2)',
    'Health(x,TOO_SKINNY)==>Advice(x,A14)',
    'Goal(x,LOSS)==>Advice(x,A1)',
    'Goal(x,GAIN)==>Advice(x,A2)',
    'Goal(x,MUSCLE)==>Advice(x,A4)',
    'Goal(x,ENDURANCE)==>Advice(x,A11)',
    'Goal(x,GENERAL)==>Advice(x,A9)',

    'Training(x,HIGH) & Goal(x,MUSCLE) ==> Advice(x,A13)',
    'Training(x,HIGH) & Goal(x,ENDURANCE) ==> Advice(x,A7)',
    'Health(x,FAT) & Goal(x,MUSCLE) ==> Advice(x,A15)',
    'Health(x,GOOD) & Goal(x,MUSCLE) ==> Advice(x,A8)',
    'Health(x,FAT) & Age(x,OLD) ==> Advice(x,A16)',
]

Aj = {
    'A1' : 'Eat fewer calories, move more',
    'A2' : 'Eat more, lift weights',
    'A3' : 'Consistency is key, progress gradually',
    'A4' : 'Lift heavy, eat protein',
    'A5' : 'Train smart, increase gradually',
    'A6' : 'Drink plenty of water.',
    'A7' : 'Get enough sleep',
    'A8' : 'Prioritize protein and fiber',
    'A9' : 'Find activities you enjoy',
    'A10' : 'Eat more protein and carbs',
    'A11' : 'Stay hydrated and fueled',
    'A12' : 'Focus on form and breathing',
    'A13' : 'Dont neglect cardio',
    'A14' : 'Eat eat eat!',
    'A15' : 'Focus on protein more than calories',
    'A16' : 'Its not too late to lose some weight!',
}