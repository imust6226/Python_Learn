#coding = utf-8

def sandwich(*toppings):
    print("\nTell me what you want: ")
    for topping in toppings:
        print("- " + topping)

sandwich('pepper')
sandwich('pepper', 'meat', 'apple pie')


sandwich('pepper', 'meat', 'apple pie', 'milk', 'juice')
