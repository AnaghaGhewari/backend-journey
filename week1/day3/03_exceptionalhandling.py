# EXCEPTION HANDLING
#In a backend, an unhandled error crashes the request and returns a 500 to the user. Always catch exceptions, handle them gracefully, and return a clear error response instead.
def validate_vitals(
        heart_rate:int,
        sleep: float,
        steps: int
        ) ->dict:
    
    try:
        errors = []


        if not(30 <= heart_rate <= 220):
         errors.append("heart_rate must be between 30 and 220")

        if not(0 <= sleep <= 24):
         errors. append("sleep must be between 0 to 24 hrs")

        if(steps < 0):
           errors.append("steps cannot be less then 0")    

        if errors:
           return{"valid":False,
                   "errors":errors} 
        
        return{"valid":True,
                "error": []}
    
    except TypeError as e:

        return {"valid": False, "errors": [f"Wrong data type: {e}"]}

# Test it
print(validate_vitals(250, 5.5, 4000))
# {"valid": False, "errors": ["heart_rate must be between 30 and 220"]}

print(validate_vitals(88, 5.5, 4000))
# {"valid": True, "errors": []}