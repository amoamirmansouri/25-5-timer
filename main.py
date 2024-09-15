""" a timer for myself
"""
from timer import timer      
import tkinter
    
    
    
   
def main():
    counter: int = 0
    while True:
        timer()
        counter += 0.5
        print(f'< u stady for {counter*2}round, ({counter} of hour) >')
        aging:str = input("do u want to contnue(y/n)? ")
        if 'n' in aging:
            print("good job!!!")
            break
        else :
            print(f'lets go for round {counter*2+1}')
            
   
# window = tkinter.Tk()
# window.title("timer :)")
if __name__ == "__main__":
    
    main()
    # b1 = tkinter.Button()
    # window.geometry("250x76")
    # window.resizable(height=False,width=False)
    # window.mainloop()
    