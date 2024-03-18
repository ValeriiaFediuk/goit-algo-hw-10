import pulp

model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit Juice", lowBound=0, cat='Integer')

model += lemonade + fruit_juice, "Total Production"

model += 2 * lemonade + fruit_juice <= 100 #Обмеження для води
model += lemonade <= 50 #Обмеження для цукру
model += lemonade <= 30 #Обмеження для лимонного соку
model += 2 * fruit_juice <= 40 #Обмеження для фруктового пюре


model.solve()

print("Production Results:")
print("Lemonade:", lemonade.varValue)
print("Fruit Juice:", fruit_juice.varValue)
print("Total Production:", model.objective.value())
