x=int(input("Enter price of his purchasesin: ")[:-1])              
if x<100:
    print("shipping cost 15%")
elif x>=200:
    print("less shipping cost 20%")
elif x>=100:
    print("not shipping cost")
else:
    print("welcome")
