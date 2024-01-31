from python_course__dict__json_A import file_path, Pessoas
import json

instances = []
with open(file_path, 'r') as file:
    pessoas = json.load(file)

    #reseting the instances using loop (list comprehension)

    [instances.append(Pessoas(**pessoas[i])) for i in range(len(pessoas))]    
    [print(instances[ind].__dict__) for ind,i in enumerate(instances)]

# reseting the instances manually
print(2)

P_0 = Pessoas(**pessoas[0])
P_1 = Pessoas(**pessoas[1])
P_2 = Pessoas(**pessoas[2])
P_3 = Pessoas(**pessoas[3])
P_4 = Pessoas(**pessoas[4])
print(P_0.__dict__)
print(vars(P_1))
print(P_2.__dict__)
print(P_3.__dict__)
print(P_4.__dict__)

P_0.introduction()
P_1.introduction()
P_2.introduction()
P_3.introduction()
P_4.introduction()

