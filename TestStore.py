from pyfiglet import Figlet
import qrcode

PRODUCTS = []
address = 'E:/projects/session6/teststore/assignment6/database.txt'
qrcode_address = 'E:/projects/session6/teststore/assignment6/qrcode.png'

def show_menu():
    print('1-Add Product')
    print('2-Edit Product')
    print('3-Delete Product')
    print('4-Search')
    print('5-Show List')
    print('6-Buy')
    print('7-Qr Code')
    print('8-Exit')

def welcome():
    f = Figlet(font='standard')
    print(f.renderText('Test Store'))
    
def database(address):
    database_file = open(address, 'r')
    data = database_file.read()
    data = data.strip()
    return data

def load():
    print('Loading ...')
    data = database(address)
    products_list = data.split('\n')
    
    for i in range(len(products_list)):
        products_info = products_list[i].split(',')
        mydict = {}
        mydict['id'] = products_info[0]
        mydict['name'] = products_info[1]
        mydict['price'] = products_info[2]
        mydict['count'] = products_info[3]
        PRODUCTS.append(mydict)
    
    welcome()

def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])

def add_product():
    n = int(input('How many products do you want to add? '))
    add_dict = {}
    for i in range(n):
        print('Product', (i + 1))
        id = input('ID: ')
        name = input('NAME: ')
        price = input('PRICE: ')
        count = input('COUNT: ')
        add_dict['id'] = id
        add_dict['name'] = name
        add_dict['price'] = price
        add_dict['count'] = count
        PRODUCTS.append(add_dict)
        print('Product', (i + 1), 'added !')
              
def save():
    database_file = open(address, 'w')
    for i in range(len(PRODUCTS)):
        save_dict = PRODUCTS[i]
        id = save_dict['id']
        name = save_dict['name']
        price = save_dict['price']
        count = save_dict['count']
        database_file.write('%s,%s,%s,%s\n'%(id,name,price,count))

    database_file.close()
    print('Your changes saved')
    
def edit_product():
    print('Number of products:', len(PRODUCTS))
    while True:
        p = int(input('Product number: '))
        if 0 < p <= len(PRODUCTS):
            break
        else:
            print('Wrong Number. Number must between 1 - (number of product)')
            continue
    
    p -= 1
    id = PRODUCTS[p]['id']
    name = PRODUCTS[p]['name']
    price = PRODUCTS[p]['price']
    count = PRODUCTS[p]['count']
    print('ID: %s - NAME: %s - PRICE: %s - COUNT: %s ' %(id, name, price, count))
    while True:
        print('1.Edit id - 2.Edit name - 3.Edit price - 4.Edit count - 5.Exit editor')
        x = int(input('Select: '))
        if x == 1:
            new_id = input('New id = ')
            PRODUCTS[p]['id'] = new_id
        elif x == 2:
            new_name = input('New name = ')
            PRODUCTS[p]['name'] = new_name
        elif x == 3:
            new_price = input('New price = ')
            PRODUCTS[p]['price'] = new_price
        elif x == 4:
            new_count = input('New count = ')
            PRODUCTS[p]['count'] = new_count
        elif x == 5:
            print('Exit editor')
            break
        else:
            print('Wrong input! try again')
            continue
    
    print('New List: ')
    show_list()

def line():
    print('************************************')

def delete_product():
    print('Number of products:', len(PRODUCTS))
    while True:
        p = int(input('Product\'s number: '))
        if 0 < p <= len(PRODUCTS):
            break
        else:
            print('Wrong Number. Number must between 1 - (number of product)')
            continue
        
    p -= 1
    id = PRODUCTS[p]['id']
    name = PRODUCTS[p]['name']
    price = PRODUCTS[p]['price']
    count = PRODUCTS[p]['count']
    print('ID: %s - NAME: %s - PRICE: %s - COUNT: %s ' %(id, name, price, count))
    
    while True:
        print('1.Delete product! - 2.Exit deletor')
        x = int(input('Enter your option: '))
        if x == 1:
            PRODUCTS.pop(p)
            print('Delete this product and exit.')
            break
        elif x == 2:
            print('Exit deletor')
            break
        else:
            print('Please Choose a correct number!')
            continue
        
def qr_code():
    while True:
        code = input('Product code: ')
        flag = 0
        for i in range(len(PRODUCTS)):
            if PRODUCTS[i]['id'] == code:
                flag = 1
                index = i
                break
        
        if flag == 0:
            print('product does not exist!')
            print('Exit QR Code ...')
            break
        else:
            id = PRODUCTS[index]['id']
            name = PRODUCTS[index]['name']
            price = PRODUCTS[index]['price']
            count = PRODUCTS[index]['count']
            qr_code = id + ',' + name + ',' + price + ',' + count
            img = qrcode.make(qr_code)
            img.save(qrcode_address)
            print('QR Code saved!')
            break
            
def search():
    srch = input('Enter your product name: ')
    flag = 0
    
    for i in range(len(PRODUCTS)):
        if srch.upper().strip() == PRODUCTS[i]['name'].strip().upper() :
            index = i
            flag = 1
            break
        
    if flag == 1:
        print('product found!')
        print(PRODUCTS[index])
    else:
        print('product is not found')
        
def buy():
    factor = [['Name', 'Price', 'Count', 'Sum']]
    counter = 1
    total = 0
    while True:
        code = input('Enter a product code: ')
        flag = 0
        for i in range(len(PRODUCTS)):
            if PRODUCTS[i]['id'] == code:
                flag = 1
                index = i
                break
        
        if flag == 0:
            print('The product does not exist!')
        else:
            print('product exists!')
            c = int(input('How much do you want? '))
            if c > int(PRODUCTS[index]['count']):
                print('not enough inventory! we only have: ', PRODUCTS[index]['count'])
            else:
                count = int(PRODUCTS[index]['count'])
                count -= c
                PRODUCTS[index]['count'] = str(count)
                print('inventory available!')
                money = c * int(PRODUCTS[index]['price'])
                total += money
                
                factor.append([PRODUCTS[index]['name'].strip(), PRODUCTS[index]['price'].strip(), c, money])
                counter += 1
                
        
        q = input('1.Add some products\n2.Finish and print my factor  ')
        if q == "1":
            continue
        else:
            for i in range(counter):
                for j in range(4):
                    print(factor[i][j], end='   ')
                print()
                    
            print('Total: ', total)
            break
    

def STORE():   
    while True:
        line()
        show_menu()
        choice = int(input('Select:  '))
        line()

        if choice == 1: 
            add_product()

        elif choice == 2: 
            edit_product()

        elif choice == 3: 
            delete_product()

        elif choice == 4:
            search()

        elif choice == 5: 
            show_list()

        elif choice == 6: 
            buy()

        elif choice == 7: 
            qr_code()

        elif choice == 8: # exit
            ans = input('Do you want to commit changes? (yes, no) ')
            if ans == 'yes':
                save()
            print('nice to see you!')
            break
        
        else:
            print('Wrong input! try again')
            continue
        
load()
STORE()