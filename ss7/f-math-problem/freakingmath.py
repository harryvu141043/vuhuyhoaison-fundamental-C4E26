from random import *
from b1 import *
from random import randint,shuffle

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x=randint(1,10)
    y=randint(1,10)
    o=["+","-","*","/"]
    
    o1=sample(o,1)
    op=o1[0]
    error=randint(-1,1)
    result=evaluate(x,y,op)+error
    return x,y,op,result

def check_answer(x, y, op, result, user_choice):
    if result==evaluate(x,y,op) and user_choice==True:
       return True
    elif result==evaluate(x,y,op) and user_choice==False:
        return False
    elif result!=evaluate(x,y,op) and user_choice==False:
        return True
    elif result!=evaluate(x,y,op) and user_choice==True:
        return False
    
    