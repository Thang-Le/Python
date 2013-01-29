class calculate(object):
    
    def __init__(self,number1,number2,):
        self.number1 = number1
        self.number2 = number2
    def display(self):
        answer = str(input("enter Operation:"))
        elif(str(answer) == 'add'):
            total = float(self.number1)+float(self.number2)
        elif(str(answer) == 'subtract'):
            total = float(self.number1)-float(self.number2)
        elif(str(answer)== 'multiply'):
            total = float(self.number1)*float(self.number2)
        elif(str(answer)== 'divide'):
            if(self.number2 == 0):
                print("WARNING")
            else:
                total = float(self.number1)/float(self.number2)
        else: print ("wrong ope")
        return total
