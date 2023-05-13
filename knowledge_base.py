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
    'Training(x,LOW) ==>Program(x,Circuit)',
    'Training(x,LOW) ==>Program(x,CrossFit)',

    'Training(x,AVERAGE) & Goal(x,LOSS)==>Program(x,HIIT)',
    'Training(x,AVERAGE) & Goal(x,GAIN)==>Program(x,StrongLifts)',
    'Training(x,AVERAGE) & Goal(x,GAIN)==>Program(x,PPL)',
    'Training(x,AVERAGE) & Goal(x,GENERAL)==>Program(x,CrossFit)',
    'Gender(x,FEMALE) & Training(x,AVERAGE) & Goal(x,GENERAL)==>Program(x,CrossFit)',
    'Training(x,AVERAGE) & Goal(x,GENERAL)==>Program(x,Circuit)',
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
    'Goal(x,LOSS)==>Eat(x,Lean_protein)',
    'Goal(x,LOSS)==>Eat(x,Whole_grains)',
    'Goal(x,LOSS)==>Eat(x,Fruits)',

    'Goal(x,GAIN)==>Eat(x,Calorie_dense_foods)',
    'Goal(x,GAIN)==>Eat(x,Lean_protein)',
    'Goal(x,GAIN)==>Eat(x,Healthy_fats)',

    'Goal(x,GENERAL)==>Eat(x,Lean_protein)',
    'Goal(x,GENERAL)==>Eat(x,Whole_grains)',
    'Goal(x,GENERAL)==>Eat(x,Fruits)',

    'Goal(x,MUSCLE)==>Eat(x,Protein)',
    'Goal(x,MUSCLE)==>Eat(x,Complex_carbohydrates)',
    'Goal(x,MUSCLE)==>Eat(x,Healthy_fats)',

    'Goal(x,ENDURANCE)==>Eat(x,Complex_carbohydrates )',
    'Goal(x,ENDURANCE)==>Eat(x,Protein)',
    'Goal(x,ENDURANCE)==>Eat(x,Healthy_fats)'
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