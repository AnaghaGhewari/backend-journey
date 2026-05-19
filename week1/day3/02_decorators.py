#DECORATORS
#A decorator is a function that wraps another function to add behaviour. When you write @app.get("/vitals") in FastAPI, you're telling FastAPI: "register this function as the handler for GET /vitals". That's all it is.
#A decorator is a function which takes a function and returns another function
import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start =time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {round((end-start)*1000)}ms")
        return result
    return wrapper
@log_time
def predict_risk(vitals:dict)->dict:
    time.sleep(0.05)
    return {"risk":"high"}
predict_risk({"heart_rate":88})