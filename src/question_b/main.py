#add import
import question_b

while True:
    print("MENU:")
    print("1-Display Stock Purchase History")
    print("2-Exit")
    opt = str(input("Select option 1 or 2: "))
    while opt not in ('1','2'):
        opt = str(input("Invalid. Select option 1 or 2:"))
    
    if opt == '1':
        question_b.stock_purchase_history()

    elif opt == '2':
        print("Now exiting the program.")
        break