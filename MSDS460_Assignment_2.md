```python
from pulp import *

```


```python
# Create a dictionary of the activities and their durations
#best case
activities = {'A':8, 'B':16, 'C':16,'D1':24, 'D2':40, 'D3':40, 'D4':80, 'D5':16,
              'D6':24,'D7':32,'D8':16,'E':24,'F':16,'G':24,'H':16}

```


```python
# Create a list of the activities
activities_list = list(activities.keys())
```


```python
# Create a dictionary of the activity precedences
precedences = {'A': [], 'B': [], 'C': ['A'],'D1': ['A'], 
               'D2': ['D1'],'D3': ['D1'], 'D4': ['D2','D3'], 'D5':['D4'],
              'D6':['D4'],'D7':['D4'],'D8':['D5','D7'],
               'E':['B','C'],'F':['D8','E'],'G':['A','D8'],'H':['F','G']}
```


```python
# Create the LP problem
prob = LpProblem("Critical_Path", LpMinimize)
```


```python
# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in
activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in
activities_list}
```


```python
# Add the constraints
for activity in activities_list:
    prob += end_times[activity] == start_times[activity] + activities[activity], f"{activity}_duration"
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"
```


```python
# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]),"minimize_end_times"
```


```python
# Solve the LP problem
status = prob.solve()
```

    Welcome to the CBC MILP Solver 
    Version: 2.10.3 
    Build Date: Dec 15 2019 
    
    command line - /opt/anaconda3/lib/python3.12/site-packages/pulp/solverdir/cbc/osx/64/cbc /var/folders/p4/prvgygc14vd8rmhsv2qx4rxc0000gn/T/3ab1bb8219b842c69e8456536a06be0f-pulp.mps -timeMode elapsed -branch -printingOptions all -solution /var/folders/p4/prvgygc14vd8rmhsv2qx4rxc0000gn/T/3ab1bb8219b842c69e8456536a06be0f-pulp.sol (default strategy 1)
    At line 2 NAME          MODEL
    At line 3 ROWS
    At line 39 COLUMNS
    At line 123 RHS
    At line 158 BOUNDS
    At line 159 ENDATA
    Problem MODEL has 34 rows, 30 columns and 68 elements
    Coin0008I MODEL read with 0 errors
    Option for timeMode changed from cpu to elapsed
    Presolve 0 (-34) rows, 0 (-30) columns and 0 (-68) elements
    Empty problem - 0 rows, 0 columns and 0 elements
    Optimal - objective value 1832
    After Postsolve, objective 1832, infeasibilities - dual 0 (0), primal 0 (0)
    Optimal objective 1832 - 0 iterations time 0.002, Presolve 0.00
    Option for printingOptions changed from normal to all
    Total time (CPU seconds):       0.00   (Wallclock seconds):       0.01
    



```python
# Print the results
print("Critical Path time:")
for activity in activities_list:
    if value(start_times[activity]) == 0:
        print(f"{activity} starts at time 0")
    if value(end_times[activity]) == max([value(end_times[activity]) for activity
in activities_list]):
        print(f"{activity} ends at {value(end_times[activity])} hours in duration")
```

    Critical Path time:
    A starts at time 0
    B starts at time 0
    H ends at 240.0 hours in duration



```python
# Print solution
print("\nBest Case Solution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)
```

    
    Best Case Solution variable values:
    end_A = 8.0
    end_B = 16.0
    end_C = 24.0
    end_D1 = 32.0
    end_D2 = 72.0
    end_D3 = 72.0
    end_D4 = 152.0
    end_D5 = 168.0
    end_D6 = 176.0
    end_D7 = 184.0
    end_D8 = 200.0
    end_E = 48.0
    end_F = 216.0
    end_G = 224.0
    end_H = 240.0
    start_A = 0.0
    start_B = 0.0
    start_C = 8.0
    start_D1 = 8.0
    start_D2 = 32.0
    start_D3 = 32.0
    start_D4 = 72.0
    start_D5 = 152.0
    start_D6 = 152.0
    start_D7 = 152.0
    start_D8 = 184.0
    start_E = 24.0
    start_F = 200.0
    start_G = 200.0
    start_H = 224.0


Expectedhours


```python
#expectedhours
activities = {'A':16, 'B':24, 'C':24,'D1':32, 'D2':56, 'D3':80, 'D4':120, 'D5':24,
              'D6':40,'D7':56,'D8':24,'E':40,'F':24,'G':40,'H':24}
```


```python
# Create a list of the activities
activities_list = list(activities.keys())
```


```python
# Create a dictionary of the activity precedences
precedences = {'A': [], 'B': [], 'C': ['A'],'D1': ['A'], 
               'D2': ['D1'],'D3': ['D1'], 'D4': ['D2','D3'], 'D5':['D4'],
              'D6':['D4'],'D7':['D4'],'D8':['D5','D7'],
               'E':['B','C'],'F':['D8','E'],'G':['A','D8'],'H':['F','G']}
```


```python
# Create the LP problem
prob = LpProblem("Critical_Path", LpMinimize)
```


```python
# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in activities_list}
```


```python
# Add the constraints
for activity in activities_list:
    prob += end_times[activity] == start_times[activity] + activities[activity], f"{activity}_duration"
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"
```


```python
# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]),"minimize_end_times"
```


```python
# Solve the LP problem
status = prob.solve()
```

    Welcome to the CBC MILP Solver 
    Version: 2.10.3 
    Build Date: Dec 15 2019 
    
    command line - /opt/anaconda3/lib/python3.12/site-packages/pulp/solverdir/cbc/osx/64/cbc /var/folders/p4/prvgygc14vd8rmhsv2qx4rxc0000gn/T/b36ddf34356a487f8a4dc99702c9316e-pulp.mps -timeMode elapsed -branch -printingOptions all -solution /var/folders/p4/prvgygc14vd8rmhsv2qx4rxc0000gn/T/b36ddf34356a487f8a4dc99702c9316e-pulp.sol (default strategy 1)
    At line 2 NAME          MODEL
    At line 3 ROWS
    At line 39 COLUMNS
    At line 123 RHS
    At line 158 BOUNDS
    At line 159 ENDATA
    Problem MODEL has 34 rows, 30 columns and 68 elements
    Coin0008I MODEL read with 0 errors
    Option for timeMode changed from cpu to elapsed
    Presolve 0 (-34) rows, 0 (-30) columns and 0 (-68) elements
    Empty problem - 0 rows, 0 columns and 0 elements
    Optimal - objective value 2992
    After Postsolve, objective 2992, infeasibilities - dual 0 (0), primal 0 (0)
    Optimal objective 2992 - 0 iterations time 0.002, Presolve 0.00
    Option for printingOptions changed from normal to all
    Total time (CPU seconds):       0.00   (Wallclock seconds):       0.01
    



```python
# Print the results
print("Critical Path time:")
for activity in activities_list:
    if value(start_times[activity]) == 0:
        print(f"{activity} starts at time 0")
    if value(end_times[activity]) == max([value(end_times[activity]) for activity
in activities_list]):
        print(f"{activity} ends at {value(end_times[activity])} hours in duration")
```

    Critical Path time:
    A starts at time 0
    B starts at time 0
    H ends at 392.0 hours in duration



```python
# Print solution
print("\nExpected Case Solution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)
```

    
    Expected Case Solution variable values:
    end_A = 16.0
    end_B = 24.0
    end_C = 40.0
    end_D1 = 48.0
    end_D2 = 104.0
    end_D3 = 128.0
    end_D4 = 248.0
    end_D5 = 272.0
    end_D6 = 288.0
    end_D7 = 304.0
    end_D8 = 328.0
    end_E = 80.0
    end_F = 352.0
    end_G = 368.0
    end_H = 392.0
    start_A = 0.0
    start_B = 0.0
    start_C = 16.0
    start_D1 = 16.0
    start_D2 = 48.0
    start_D3 = 48.0
    start_D4 = 128.0
    start_D5 = 248.0
    start_D6 = 248.0
    start_D7 = 248.0
    start_D8 = 304.0
    start_E = 40.0
    start_F = 328.0
    start_G = 328.0
    start_H = 368.0



```python
#worstcase
activities = {'A':24, 'B':32, 'C':32,'D1':48, 'D2':80, 'D3':160, 'D4':160, 'D5':32,
              'D6':48,'D7':64,'D8':32,'E':48,'F':32,'G':48,'H':32}
```


```python
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
```

    Welcome to the CBC MILP Solver 
    Version: 2.10.3 
    Build Date: Dec 15 2019 
    
    command line - /opt/anaconda3/lib/python3.12/site-packages/pulp/solverdir/cbc/osx/64/cbc /var/folders/p4/prvgygc14vd8rmhsv2qx4rxc0000gn/T/313203c76d3343f996bf589b3e50ae46-pulp.mps -timeMode elapsed -branch -printingOptions all -solution /var/folders/p4/prvgygc14vd8rmhsv2qx4rxc0000gn/T/313203c76d3343f996bf589b3e50ae46-pulp.sol (default strategy 1)
    At line 2 NAME          MODEL
    At line 3 ROWS
    At line 39 COLUMNS
    At line 123 RHS
    At line 158 BOUNDS
    At line 159 ENDATA
    Problem MODEL has 34 rows, 30 columns and 68 elements
    Coin0008I MODEL read with 0 errors
    Option for timeMode changed from cpu to elapsed
    Presolve 0 (-34) rows, 0 (-30) columns and 0 (-68) elements
    Empty problem - 0 rows, 0 columns and 0 elements
    Optimal - objective value 4496
    After Postsolve, objective 4496, infeasibilities - dual 0 (0), primal 0 (0)
    Optimal objective 4496 - 0 iterations time 0.002, Presolve 0.00
    Option for printingOptions changed from normal to all
    Total time (CPU seconds):       0.00   (Wallclock seconds):       0.01
    


    /opt/anaconda3/lib/python3.12/site-packages/pulp/pulp.py:1298: UserWarning: Spaces are not permitted in the name. Converted to '_'
      warnings.warn("Spaces are not permitted in the name. Converted to '_'")



```python
# Print the results
print("Critical Path time:")
for activity in activities_list:
    if value(start_times[activity]) == 0:
        print(f"{activity} starts at time 0")
    if value(end_times[activity]) == max([value(end_times[activity]) for activity
in activities_list]):
        print(f"{activity} ends at {value(end_times[activity])} hours in duration")
```

    Critical Path time:
    A starts at time 0
    B starts at time 0
    H ends at 568.0 hours in duration



```python
# Print solution
print("\nWorst Case Solution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)
```

    
    Worst Case Solution variable values:
    end_A = 24.0
    end_B = 32.0
    end_C = 56.0
    end_D1 = 72.0
    end_D2 = 152.0
    end_D3 = 232.0
    end_D4 = 392.0
    end_D5 = 424.0
    end_D6 = 440.0
    end_D7 = 456.0
    end_D8 = 488.0
    end_E = 104.0
    end_F = 520.0
    end_G = 536.0
    end_H = 568.0
    start_A = 0.0
    start_B = 0.0
    start_C = 24.0
    start_D1 = 24.0
    start_D2 = 72.0
    start_D3 = 72.0
    start_D4 = 232.0
    start_D5 = 392.0
    start_D6 = 392.0
    start_D7 = 392.0
    start_D8 = 456.0
    start_E = 56.0
    start_F = 488.0
    start_G = 488.0
    start_H = 536.0



```python

```
