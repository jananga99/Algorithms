# 3-SAT

## Problem statement

There are n boolean n variables. You are given a CNF (Conjunctive Normal Form i.e. product(AND) of sums(ORs)). Each clause hase three variables. If there is a correct assignment for all n variables to satify the given CNF, output that assignment. Otherwise, output not found/False.


## 3-SAT Algorithm
SAT3(expression)  
&emsp;if expression has no clauses  
&emsp;&emsp;return True    
&emsp;if expression contains an empty clause  
&emsp;&emsp;return False  
&emsp;unassigned<--unassigned variable of expression   
&emsp;if SAT3(expression[unassigned=0]) ="sat"   
&emsp;&emsp;return True   
&emsp;if SAT3(expression[unassigned=1]) ="sat"   
&emsp;&emsp;return True   
&emsp;return false


## Checkball Algorithm
Here, alfa means a certain assginement of values to variables.

