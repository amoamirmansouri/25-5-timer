""" a timer 
"""
from timer import timer      
       
counter: int = 0
if __name__ == "__main__":
    while True:
        timer(1500)
        counter += 0.5
        print(f'< u stady for {counter*2}round, ({counter} of hour) >')
        aging:str = input("do u want to contnue(y/n)? ")
        if 'n' in aging:
            print("good job!!!")
            break
        else :
            print(f'lets go for round {counter*2+1}')
            
   