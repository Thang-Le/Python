class calculate(object):
    
    def __init__(self,number1,number2,):
        self.number1 = number1
        self.number2 = number2
    def display(self):
        answer = str(input("enter Operation:"))
        if(str(answer) == 'add'):
            total = float(self.number1)+float(self.number2)
        if(str(answer) == 'subtract'):
            total = float(self.number1)-float(self.number2)
        if(str(answer)== 'multiply'):
            total = float(self.number1)*float(self.number2)
        if(str(answer)== 'divide'):
            total = float(self.number1)/float(self.number2)
        else: print ("wrong ope")
        return total
