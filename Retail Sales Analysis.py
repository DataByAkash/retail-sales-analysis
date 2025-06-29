# ================================ Retail Sales Analysis ========================

menu = []

# Function to add new item
def add_item():
  name = input('Enter the name of the item :')
  category = input('Enter the category of the item :')
  price = float(input('Enter the price of the item :'))
  qty = int(input('Enter the quantity of the item :'))
  
  menu.append({
    'name': name,
    'category': category,
    'price' : price,
    'qty' : qty
  })
  
  print('Item added to menu :')
  print('Name :', name)
  print('Category :', category)
  print('Price :{:.2f}'.format(price))
  print('Quantity :', qty)
  

# Function to update qty
def update_quantity():
  print('Current menu :')
  print('Name\tCategory\tPrice\tQuantity')
  
  for item in menu:
    print(f'{item['name']}\t{item['category']}\t{item['price']}\t{item['qty']}')
    
  name = input('Enter the name of the item you want to update :')
  qty = int(input('Enter the new quantity :'))
  
  for item in menu:
    if item['name'] == name:
      if item['qty'] == qty:
        print('Item quantity updated :')
        print('Name', name)
        print('New qty :', qty)
        return
  
  print('Item not found in menu')    
  
  
  
# Function to view sales summary

def view_summary():
  print("Sales summary:")
  print('Name\tCategory\tPrice\tQuantity\tTotal sales')
  
  for itme in menu:
    total_sales = itme['price'] * itme['qty']
    print(f'{itme['name']}\t{itme['category']}\t{itme['price']}\t{itme['qty']}\t{total_sales}')
    

# Function to view sales by highest first

def get_top():
  sales = []
  for item in menu:
    sales.append((item['name'], item['price'] * item['qty']))
    
    print('Item Sales :')
    sales.sort(key= lambda a:a[-1], reverse=True)
    
    for name, value in sales:
      print(f'{name} : {value}')
      


while True:
    print("\nWelcome to the cafe inventory and sales tracker!\n")
    print("What would you like to do?")
    print("1. Add new item to menu")
    print("2. Update item quantities")
    print("3. View sales summary")
    print("4. View Sales Analysis")
    print("5. Quit")
    
    
    choice = input('\nEnter your choice (1-4) :')
    
    if choice == '1':
      add_item()
    elif choice == '2':
      update_quantity()
    elif choice == '3':
      view_summary()
    elif choice == '4':
        get_top()
    elif choice == '5':
      print('Goodbye')
      break
    else:
      print('Invaild choice')
    


  

        