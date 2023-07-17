class Calculator:
    def __init__(self):
        self.op=input("Enter the operator\n")
        self.a=float(input("Enter the value of a\n"))
        self.b=float(input("Enter the value of b\n"))
    def operation(self):
         if(self.op=='+'):
             print(self.a+self.b)
         elif(self.op=='-'):
             print(self.a-self.b)
         elif(self.op=='*'):
             print(self.a*self.b)
         elif(self.op=='/'):
             print(self.a/self.b)
           
calc=Calculator()
calc.operation()