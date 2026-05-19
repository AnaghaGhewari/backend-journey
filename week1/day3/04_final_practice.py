#PRACTICE FILE

from typing import Optional, List
from datetime import datetime
import time

#----DECORATORS----:log how long each function takes.
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        ms = round((end-start)*1000)
        print(f"[{func.__name__}] complete in {ms}ms")
        return result
    return wrapper

#----TYPE-HINTS + EXCEPTION HANDLING----
@log_time
def validate_vitals(
    heart_rate: int,
    sleep: float,
    steps: int,
    notes: Optional[str] = None
) -> dict:
    try:
        errors: List[str] = []

        if not(30 <= heart_rate <= 220):
            errors.append("heart_rate should be between 30 and 220")
        if not(0 <= sleep <= 24):
            errors.append("sleep should be between 0 and 24 hrs")
        if(steps < 0):
            errors.append("steps cannot be less the 0")

        return{
            "valid": len(errors) == 0,
            "errors": errors,
            "checked_at": datetime.now().isoformat(),
            "notes": notes
        }             
    except TypeError as e:
        return{"valid":False, "errors":[f"Type error:{e}"]}
    

#----Test it----
print(validate_vitals(88,5.5,4200,"Felt tires"))
print(validate_vitals(89,7,-10))
print(validate_vitals(72,7.0,9000))    