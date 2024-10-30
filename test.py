import pandas as pd

def check_letters(text):
    letters="abcdefghijklmnopqrstuvwxyz"
    count_not_same =0
    for i in text.lower():
        if not i in letters:
            return False
    return True

def validate_supplier(supplier):
    splitted_supplier = supplier.split()
    last_word_index=len(splitted_supplier)-1
    if splitted_supplier[last_word_index]=="Supplier":
        return True
    else:
        return False

list_of_item=[]

program_status=True
while program_status:
    print("1. Insert\n2. View\n3. Exit")
    selected_menu = input("Choose the menu:")
    if selected_menu == "1":
        validation=False
        while validation==False:
            item_name = input("Input Item Name (Letters Only):")
            validation=check_letters(item_name)
            if validation==False:
                print("Invalid input. Item Name shouuld contain only letters.")
        
        empty_validation =False
        while empty_validation==False:
            input_category = input("Input Category [Cannot be Empty]:")
            if len(input_category) == 0:
                print("Invalid input. Category should no be empty.")
            else:
                empty_validation=True
        
        qty_validation=False
        while qty_validation==False:
            input_qty = int(input("Input Quantity [Must be > 0]:"))
            if input_qty <= 0:
                print("Invalid input. Quantity must be more then 0.")
            else:
                qty_validation=True

        price_validation=False
        while price_validation==False:
            input_price = int(input("Input Price [10000 - 20000 IDR]:"))
            if input_price >= 10000 and input_price<=20000:
                price_validation=True
            else:
                print("Invalid input. Price must be between 10000 and 20000 IDR.")
        
        supplier_validation=False
        while supplier_validation==False:
            input_supplier = input("Input Supplier. [Ends with 'Supplier']:")
            supplier_validation=validate_supplier(input_supplier)
            if supplier_validation==False:
                print("Invalid input. Supplier should end with ' Supplier'.")

        total_price = input_qty*input_price
        print("Item Details")
        print("====================================")
        print("Item name: ",item_name)
        print("Category: ",input_category)
        print("Price: ",input_price)
        print("Supplier: ",input_supplier)
        print("Total Price: ",total_price)
        print("====================================")

        item_detail ={
            "Item name: ":item_name,
            "Category: ":input_category,
            "Price: ":input_price,
            "Supplier: ":input_supplier,
            "Total Price: ":total_price
        }

        list_of_item.append(item_detail)

    elif selected_menu =="2":
        if len(list_of_item)==0:
            print("No entries available.")
            input("Press enter to continue...")
            continue
        data = pd.DataFrame(list_of_item)
        print("====================================")
        print(data)
        print("====================================")

    elif selected_menu =="3":
        print("Exiting application...")
        program_status=False