# class InsufficentFundsError(Exception):
#     def __init__(self,balance,amount):
#         self.balance=balance
#         self.amount=amount
#         super().__init__(f"Error:Insufficinet funds,Avaible balance:${balance},but attempted to withdraw ${amount}.")



# def withdraw_from_account(balance,amount):
#     if amount>balance:
#         raise InsufficentFundsError()


class InvalidMethodError(Exception):
    def __init__(self,method,num1,num2):
        self.method=method
        self.num1=num1
        self.num2=num2
        super().__init__(f"Error:Invalid Method {method} is not supported")

def calcuator(method,num1,num2):  
    supported_methods=["add","sub","mul","divide"]
    if method not in supported_methods:
        raise InvalidMethodError(method,num1,num2)

    elif method=="add":
        return num1+num2
    elif method=="sub":
        return num1-num2

try:
    num1=2 
    num2=4
    result=calcuator("sub",num1,num2)
    print(result)
except InvalidMethodError as e:
    print(e)       