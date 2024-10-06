
class Stack:
    def __init__(self):
        self.top = -1
        self.stack = {}

    def pushItem(self, orderData, tableNumber):
        self.top += 1  

        if tableNumber in self.stack:
            current_orders = self.stack[tableNumber]["order"]
            newList = [0] * (len(current_orders) + 1)
            for i in range(len(current_orders)):
                newList[i] = current_orders[i]
            newList[len(current_orders)] = orderData
            self.stack[tableNumber]["order"] = newList

        else:
            self.stack[tableNumber] = {
            "order": [orderData]  
        }
    
        print("Complete order:", self.stack)

        from customQueue import Queue
        qu = Queue()
        qu.enqueue(self.stack)
        # 
        
    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            emptystack = [0] * self.top 
            removeitem = self.stack[self.top]
            for i in range(self.top):
                emptystack[i] = self.stack[i]   
            self.top -= 1    
            self.stack=emptystack    
            print(f"After remove {removeitem}: now updated stack is {self.stack}")

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Peek Value is: ",self.stack[self.top])

    def topValue(self):
        print("Top value: ",self.top)  

    
