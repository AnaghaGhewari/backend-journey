#TYPE HINTS
#Type Hints are used by FastAPI to validate and authentication

from typing import Optional, List


#Exapmle 1:

def log_vitals(
        heart_rate: int,
        sleep: float,
        steps: int,
        notes: Optional[str]=None
        
) -> dict:
 return{"logged":True}    
print("Logged Vitals",log_vitals(88,8.2,500))

#Example 2:

def stud_data(
       Name: str,
       Roll_no: int,
       Div: str,
       Marks: List[int],
       Achievements: Optional[str]=None
       
) ->dict:
   return{"Entered info":True}
print("Entered info",stud_data("Riddhi",65,"B",[89,90,95,91]))

 