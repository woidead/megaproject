from distutils.sysconfig import customize_compiler
from multiprocessing import connection
import psycopg2

connect = psycopg2.connect(
    host = '127.0.0.1',
    database = 'ww',
    user = 'postgres',
    password = '8659', 
    port = '5432')

print('добро пожаловать в магазин')
cursor = connect.cursor()
connect.commit()
l = input('кто ты ? админ или пользователь?  ')

if l =='пользователь':
    cursor.execute("select  productname,price from products")
    connect.commit()
    data = cursor.fetchall()
    for i in data:
        print (f'{i}')
    x = input('что вы хотите купить? ')
    cursor.execute(f"select ProductCount from products where productname = '{x}' ")
    connect.commit()
    f = cursor.fetchall()
    print((f'всего есть: {f[0][0]}'))
    y = int(input(f'выберите количество '))
    if f[0][0] >= y:
        cursor.execute(f"select price from products where productname = '{x}' ")
        connect.commit()
        d = cursor.fetchall()
        p = y * d[0][0]
        print(f"""счет: 
        Товар: {x}
        количество: {y} 
        цена: {d[0][0]} 
        общая сумма: {y} x {d[0][0]} =""", p)
        s = input('хотите продолжить покупку?(отвечать в формате: да или нет) ')
        if s == 'да':
            e = input('перейдем к оформлению заказа, введите ваше ФИО ')
            z = int(input('ваш номер без +'))
            t = int(input('напечатайте номер карты, срок и cvv код в фомате 123456789000-12/34-123 '))
            print(f"""чек: 
            Товар: {x}
            количество: {y} 
            цена: {d[0][0]} 
            общая сумма: {y} x {d[0][0]} =""", p
            )
            print(f'{e}, благодарим за покупку. с вашей карты будет списано в скором времени {p} рубликов')
            k = f[0][0]- y
            cursor.execute(f"update products set ProductCount = {k} where productname = '{x}'")
            connect.commit()
            cursor.execute(f"""insert into orders(orderer, product, count, price, cost, number, card) values('{e}', '{x}', {y}, {d[0][0]},{p}, {z}, {t});""")
            connect.commit()
        if s == 'нет':
            print(f'в скором времени ваш телефон взорвется, хорошего дня))')

    if f[0][0] < y:
        r = input(f'на нашем складе есть только {f[0][0]} штуки, хотите купить в меньшем количестве? ')

        if r == 'да':
            y = int(input(f'выберите количество '))

            if f[0][0] > y:
                cursor.execute(f"select price from products where productname = '{x}' ")
                connect.commit()
                d = cursor.fetchall()
                p = y * d[0][0]
                print(f"""счет: 
                Товар: {x}
                количество: {y} 
                цена: {d[0][0]} 
                общая сумма: {y} x {d[0][0]} =""", p)

                s = input('хотите продолжить покупку?(отвечать в формате: да или нет) ')
                if s == 'да':
                    e = input('перейдем к оформлению заказа, введите ваше ФИО ')
                    z = int(input('ваш номер без +'))
                    t = int(input('напечатайте номер карты, срок и cvv код в фомате 123456789000-12/34-123 '))
                    print(f"""чек: 
                    Товар: {x}
                    количество: {y} 
                    цена: {d[0][0]} 
                    общая сумма: {y} x {d[0][0]} =""", p
                    )

                    print(f'{e}, благодарим за покупку. с вашей карты будет списано в скором времени {p} рубликов')
                    k = f[0][0]- y
                    cursor.execute(f"update products set ProductCount = {k} where productname = '{x}'")
                    connect.commit()
                    cursor.execute(f"""insert into orders(orderer, product, count, price, cost, number, card) values('{e}', '{x}', {y}, {d[0][0]},{p}, {z}, {t});""")
                    connect.commit()

        else:
                    print('ты дурак?')

        if r == 'нет':
            print(f'в скором времени ваш телефон взорвется, хорошего дня))')

    if f[0][0] < 0:
        print(f' у нас в данный момент нет {x}, приходите позже. хотите быть в курсе событий? подпишитесь на нашу рассылку))')

if l == 'админ':
    b = int(input('введите пароль: '))
    
    if b == 5432:
        g = input('какая таблица? ')
        if g == 'продукстс':
            h = input('какой запрос нужно исполнить?(апдейт, дроп, инсерт) ') 
            
            if h == 'апдейт':
                tt = input('изменить что? (название, компанию, количество, цену) ')
                i = int(input('id товара: '))
                if tt == 'название':
                    o = (input('новое название: '))
                    cursor.execute(f"update products set productname = '{o}'  where id = {i}")
                    connect.commit()
                    print(f'количество товара с id {i} обновлено до {o}')
                if tt == 'количество':
                    o = int(input('количество на складе: '))
                    cursor.execute(f"update products set productcount = {o}  where id = {i}")
                    connect.commit()
                    print(f'количество товара с id {i} обновлено до {o}')
                if tt == 'компанию':
                    o = (input('новое название компании: '))
                    cursor.execute(f"update products set Company = '{o}'  where id = {i}")
                    connect.commit()
                    print(f'название компании товара с id {i} обновлено до {o}')
                if tt == 'цену':
                    o = int(input('новая цена: '))
                    cursor.execute(f"update products set price = {o}  where id = {i}")
                    connect.commit()
                    print(f'цена товара с id {i} обновлено до {o}')
                    
                
            if h == 'дроп':
                i = int(input('id товара: '))
                cursor.execute(f"delete from products where id = {i}")
                connect.commit()
                print(f'товар с id {i} удален')
            if h == 'инсерт':
                m = input('введите новую позицию("модель", "компания", количество, цена)')
                cursor.execute(f'INSERT INTO Products(ProductName, Company, ProductCount, Price) VALUES({m}) ')
                connect.commit()
        if g == 'заказы':
            h = input('какой запрос нужно исполнить?(апдейт, дроп, инсерт) ') 
            
            if h == 'апдейт':
                
                tt = input('изменить что? (заказчика, продукт, количество, цену, итоговая цена, номер, карту) ')
                i = int(input('nums заказа: '))
                if tt == 'заказчика':
                    o = (input('имя заказчика: '))
                    cursor.execute(f"update orders set orderer = '{o}'  where nums = {i}")
                    connect.commit()
                    print(f"строчка orderer обновлена до {o}")
                if tt == 'количество':
                    o = (input('количество: '))
                    cursor.execute(f"update orders set productcount = {o}  where nums = {i}")
                    connect.commit()
                    print(f'количество товара в заказе с nums {i} обновлено до {o}')
                if tt == 'продукт':
                    o = (input('новое название продукта: '))
                    cursor.execute(f"update orders set product = '{o} ' where nums = {i}")
                    connect.commit()
                    print(f"название товара в заказе с nums {i} обновлено до '{o}'")
                if tt == 'цену':
                    o = int(input('новая цена: '))
                    cursor.execute(f"update orders set price = {o}  where nums = {i}")
                    connect.commit()
                    print(f"цена товара в заказе с nums {i} обновлено до {o}'")
                if tt == 'итог':
                    o = int(input('новая итоговая цена: '))
                    cursor.execute(f"update orders set cost = {o}  where nums = {i}")
                    connect.commit()
                    print(f"итоговая цена товара в заказе с nums {i} обновлено до {o}'")
                if tt == 'номер':
                    o = int(input('новый номер: '))
                    cursor.execute(f"update orders set number = {o}  where nums = {i}")
                    connect.commit()
                    print(f"номер заказчика в заказе с nums {i} обновлено до {o}'")
                if tt == 'карта':
                    o = int(input('новая карта: '))
                    cursor.execute(f"update orders set card = {o}  where nums = {i}")
                    connect.commit()
                    print(f"карта заказчика с nums {i} обновлено до {o}'")
                

            if h == 'дроп':
                i = int(input('nums товара: '))
                cursor.execute(f"delete from orders where nums = {i}")
                connect.commit()
                print(f'товар с nums {i} удален')
            if h == 'инсерт':
                m = input('введите новую позицию("заказчик","модель", количество, цена, общая сумма, номер, карта)')
                cursor.execute(f'INSERT INTO orders(orderer, product, count, Price, cost, number, card) VALUES({m})')
                connect.commit()


cursor.close()
connect.close()