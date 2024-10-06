

while True:
        print("Pizza Restaurant System")
        print("1. View Menu And Order ")
        print("2. Check Order for Kitchen")
        print("5. Exit")
        
        user = int(input("Enter opretion:  "))
        if user == 1:
            from readJsonFile import MenuJson
            data = MenuJson()
            x = data.readData()
            print(x)
            tableNumber = int(input("Enter Your Table Number: "))
            from customStack import Stack
            stack= Stack()
            
            while True:
                orderUser = int(input("Enter Order Nubr: "))
                order_row = x.iloc[orderUser]
                print("This is your order")
                stack.pushItem(order_row,tableNumber)
                yes = input("Do you to order more thing y/n: ").lower()
                if yes == 'y':
                     continue
                else:
                     break
        
        elif user == 2:
          pass
             
