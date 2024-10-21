# %%
from pulp import *


# %%
pip install ipynb-py-convert


# %%
# Create a dictionary of the activities and their durations
#best case
activities = {'A':8, 'B':16, 'C':16,'D1':24, 'D2':40, 'D3':40, 'D4':80, 'D5':16,
              'D6':24,'D7':32,'D8':16,'E':24,'F':16,'G':24,'H':16}


# %%
# Create a list of the activities
activities_list = list(activities.keys())

# %%
# Create a dictionary of the activity precedences
precedences = {'A': [], 'B': [], 'C': ['A'],'D1': ['A'], 
               'D2': ['D1'],'D3': ['D1'], 'D4': ['D2','D3'], 'D5':['D4'],
              'D6':['D4'],'D7':['D4'],'D8':['D5','D7'],
               'E':['B','C'],'F':['D8','E'],'G':['A','D8'],'H':['F','G']}

# %%
# Create the LP problem
prob = LpProblem("Critical_Path", LpMinimize)

# %%
# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in
activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in
activities_list}

# %%
# Add the constraints
for activity in activities_list:
    prob += end_times[activity] == start_times[activity] + activities[activity], f"{activity}_duration"
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"

# %%
# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]),"minimize_end_times"

# %%
# Solve the LP problem
status = prob.solve()

# %%
# Print the results
print("Critical Path time:")
for activity in activities_list:
    if value(start_times[activity]) == 0:
        print(f"{activity} starts at time 0")
    if value(end_times[activity]) == max([value(end_times[activity]) for activity
in activities_list]):
        print(f"{activity} ends at {value(end_times[activity])} hours in duration")

# %%
# Print solution
print("\nBest Case Solution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)

# %%
"""
Expectedhours
"""

# %%
#expectedhours
activities = {'A':16, 'B':24, 'C':24,'D1':32, 'D2':56, 'D3':80, 'D4':120, 'D5':24,
              'D6':40,'D7':56,'D8':24,'E':40,'F':24,'G':40,'H':24}

# %%
# Create a list of the activities
activities_list = list(activities.keys())

# %%
# Create a dictionary of the activity precedences
precedences = {'A': [], 'B': [], 'C': ['A'],'D1': ['A'], 
               'D2': ['D1'],'D3': ['D1'], 'D4': ['D2','D3'], 'D5':['D4'],
              'D6':['D4'],'D7':['D4'],'D8':['D5','D7'],
               'E':['B','C'],'F':['D8','E'],'G':['A','D8'],'H':['F','G']}

# %%
# Create the LP problem
prob = LpProblem("Critical_Path", LpMinimize)

# %%
# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in activities_list}

# %%
# Add the constraints
for activity in activities_list:
    prob += end_times[activity] == start_times[activity] + activities[activity], f"{activity}_duration"
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"

# %%
# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]),"minimize_end_times"

# %%
# Solve the LP problem
status = prob.solve()

# %%
# Print the results
print("Critical Path time:")
for activity in activities_list:
    if value(start_times[activity]) == 0:
        print(f"{activity} starts at time 0")
    if value(end_times[activity]) == max([value(end_times[activity]) for activity
in activities_list]):
        print(f"{activity} ends at {value(end_times[activity])} hours in duration")

# %%
# Print solution
print("\nExpected Case Solution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)

# %%
#worstcase
activities = {'A':24, 'B':32, 'C':32,'D1':48, 'D2':80, 'D3':160, 'D4':160, 'D5':32,
              'D6':48,'D7':64,'D8':32,'E':48,'F':32,'G':48,'H':32}

# %%
# Create a list of the activities
activities_list = list(activities.keys())
# Create a dictionary of the activity precedences
precedences = {'A': [], 'B': [], 'C': ['A'],'D1': ['A'], 
               'D2': ['D1'],'D3': ['D1'], 'D4': ['D2','D3'], 'D5':['D4'],
              'D6':['D4'],'D7':['D4'],'D8':['D5','D7'],
               'E':['B','C'],'F':['D8','E'],'G':['A','D8'],'H':['F','G']}
# Create the LP problem
prob = LpProblem("Critical_Path", LpMinimize)
# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in activities_list}
# Add the constraints
for activity in activities_list:
    prob += end_times[activity] == start_times[activity] + activities[activity],f"{activity}_duration"
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor],f"{activity}_predecessor_{predecessor}"
# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]),"minimize_end_times"
# Solve the LP problem
status = prob.solve()

# %%
# Print the results
print("Critical Path time:")
for activity in activities_list:
    if value(start_times[activity]) == 0:
        print(f"{activity} starts at time 0")
    if value(end_times[activity]) == max([value(end_times[activity]) for activity
in activities_list]):
        print(f"{activity} ends at {value(end_times[activity])} hours in duration")

# %%
# Print solution
print("\nWorst Case Solution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)

# %%
