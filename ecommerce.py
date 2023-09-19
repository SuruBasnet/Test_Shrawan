# Program need (FileHandling)
# While Registering user Ask the usertype whether he/she is buyer or seller
# While Login get the user type
# If usertype while login is buyer he/she can see all the products and he/she can buy all the products.
# If usertype while login is seller he/her can add products and he/she can see their products sold.

# Task
# Let the (buyer/seller)user to continue the system even after running a function, but if he/she wants to logout then logout
# Let the seller view his/her total revenue

# asndbajsbdjs
# asdnbasjhdbjasbh

import json

def login():
    user_username  = input('Enter your username: ')
    f = open('D:/MindrisersTeaching/Shrawan/Day 17/user_db.txt','r')
    user_info = f.read()
    user_info_list = user_info.split('\n')
    for i in user_info_list:
        if i != '':
            user_dict_data = json.loads(i)
            if user_username == user_dict_data.get('username'):
                user_password = input('Enter your password: ')
                if user_password == user_dict_data.get('password'):
                    print('Login success!')
                    user_usertype = user_dict_data.get('usertype')
                    if user_usertype == 'seller':
                        seller_choice  = input('''
                                               1. Add product
                                               2. See all the purchase infos
                                               3. Logout
                                               select a id option :''')
                        if seller_choice == '1':
                            seller_product(user_dict_data.get('username'))
                        elif seller_choice == '2':
                            seller_product_purchase(user_dict_data.get('username'))
                    if user_usertype == 'buyer':
                        buyer_choice  = input('''
                                               1. View all product
                                               2. Logout
                                               select a id option :''')
                        buyer(user_dict_data.get('username'))
                else:
                    print('Invalid password!')
    f.close()
    

def register():
    user_username = input('Enter a username : ')
    user_password = input('Enter a password : ')
    user_usertype = input('Enter your usertype (buyer/seller)?').lower()
    user_dict_data = {'username':user_username,'password':user_password,'usertype':user_usertype}
    f = open('D:/MindrisersTeaching/Shrawan/Day 17/user_db.txt','a')
    f.write(json.dumps(user_dict_data) + '\n')
    f.close()

def buyer(buyer_name):
    f = open(r'D:/MindrisersTeaching/Shrawan/Day 17/product_db.txt','r')
    product_content  = f.read()
    f.close()
    product_list = product_content.split('\n')
    for i in product_list:
        print(i)
    product_choice = input('which product do you want to buy? ')
    for i in product_list:
        if i != '':
            product_dict_data = json.loads(i)
            if product_choice == product_dict_data.get('name'):
                print(i)
                quantity = int(input('How many quantity do you want? '))
                total_price = int(product_dict_data.get('price')) * quantity
                purchase_info = {'buyer':buyer_name,'product_name':product_dict_data.get('name'),'total_price':total_price,'seller':product_dict_data.get('seller')}
    f = open('D:/MindrisersTeaching/Shrawan/Day 17/purchase_db.txt','a')
    f.write(json.dumps(purchase_info)+'\n')
    f.close()

def seller_product(seller_name):
    product_name = input('Enter your product name : ')
    product_detail = input('Enter your product detail : ')
    product_price = input('Enter your product price : ')
    f = open('D:/MindrisersTeaching/Shrawan/Day 17/product_db.txt','a')
    product_info = {'name':product_name,'detail':product_detail,'price':product_price,'seller':seller_name}
    f.write(json.dumps(product_info)+'\n')
    f.close()

def seller_product_purchase(seller_name):
    f = open(r'D:/MindrisersTeaching/Shrawan/Day 17/purchase_db.txt','r')
    purchase_content  = f.read()
    f.close()
    purchase_list = purchase_content.split('\n')
    for i in purchase_list:
        if i != '':
            purchase_dict_data = json.loads(i)
            if seller_name == purchase_dict_data.get('seller'):
                print(purchase_dict_data)



while True:
    user_choice = input('Do you want to login / register / exit? ').lower()

    if user_choice == 'login':
        login()
    elif user_choice == 'register':
        register()
    elif user_choice == 'exit':
        print('Thank you for using our ecommerce cli!')
        break
    else:
        print('Invalid input!')