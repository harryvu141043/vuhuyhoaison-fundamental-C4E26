from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]
#l=[["Red","#C62828",shapes[1]{"rect"}],['blue','#3F51B5',shapes[0]{"rect"}],['yellow','#FFD600',shapes[2]{"rect"}],[ 'green','#4CAF50',shapes[1]{"rect"}]]


def get_shapes():
    return shapes
l1=["blue","red","yellow","green"]
l2=["#3F51B5","#C62828","#FFD600","#4CAF50"]
l3=[[20, 60, 100, 100],[140, 60, 100, 100],[20, 180, 100, 100],[140, 180, 100, 100]]


    

def generate_quiz():
    # return [
    #             "Red",
    #             '#C62828',
    #             randint(0,1), # 0 : meaning, 1: color
    #         ]
    #l=[["Red","#C62828"],['blue','#3F51B5'],['yellow','#FFD600'],[ 'green','#4CAF50']]
   
    
        return  [
                choice(l1),
                choice(l2),
            
                


              
                randint(0,1), # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type==0:
        """if text=="Red":
            if 140<x<240 and 60<y<160:
                return True
            else:
                return False
        elif text=="Blue":
            if 20<x<120 and 60<y<160:
                return True
            else:
                return False
        elif text=="Yellow":
            if 20<x<120 and 180<y<280:
                return True
            else:
                return False
        elif text=="Green":
            if 140<x<240 and 180<y<280:
                return True
            else:
                return False"""
        for i in l1:
            if text==i:
                if shapes[l1.index(i)]["rect"][0]<x<shapes[l1.index(i)]["rect"][0]+shapes[l1.index(i)]["rect"][2] and shapes[l1.index(i)]["rect"][1]<y<shapes[l1.index(i)]["rect"][1]+shapes[l1.index(i)]["rect"][3]:
                
                    return True
                else:
                    return False




    elif quiz_type==1:
        """if color=="#C62828":
            if 140<x<240 and 60<y<160:
                return True
            else:
                return False
        elif color=="#3F51B5":
            if 20<x<120 and 60<y<160:
                return True
            else:
                return False
        elif color=="#FFD600":
            if 20<x<120 and 180<y<280:
                return True
            else:
                return False
        elif color=="#4CAF50":
            if 140<x<240 and 180<y<280:
                return True
            else:
                return False"""
        for j in l2:
            if color==j:
                if shapes[l2.index(j)]["rect"][0]<x<shapes[l2.index(j)]["rect"][0]+shapes[l2.index(j)]["rect"][2] and shapes[l2.index(j)]["rect"][1]<y<shapes[l2.index(j)]["rect"][1]+shapes[l2.index(j)]["rect"][3]:
                
                    return True
                else:
                    return False
