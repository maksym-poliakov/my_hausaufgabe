import mysql.connector

#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text
# 1) В базе данных ich_edit три таблицы. Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна запросить у пользователя название таблицы и вывести все ее строки или сообщение, что такой таблицы нет.
DBCONFIG = { 'host' : 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database' : 'ich_edit'
            }

try:
    conn = mysql.connector.connect(**DBCONFIG)
except mysql.connector.Error as e:
    print(f'Ошибка соединения : {e}')
    exit()
cursor = conn.cursor()

def list_date_bases():
    cursor.execute("SHOW TABLES")
    date_bases = cursor.fetchall()
    list_database = [db[0] for db in date_bases]
    return list_database

def validation_data_base(name_table):
    list_bases = list_date_bases()
    list_name_base = []
    if name_table in list_bases :
        return name_table
    elif not  name_table in list_bases :
        for n_b in list_bases :
            if n_b.lower() == name_table.lower():
                list_name_base.append(n_b)
        if list_name_base :
            raise NameError (','.join(list_name_base))
    raise ValueError (f'Таблица с именем : {name_table} не найдена')


def date_base_info(inp_string) :
    while True :
        try:
            db_name = validation_data_base(inp_string)
            return db_name
        except NameError :
            print(f'Имя таблицы введено не корректно возможно вы имели в виду : {e} ')
            inp_string= input('Введите имя таблицы еще раз  ( users / product / sales / SaLes ) : ').strip()
            if inp_string == '' :
                return ''
        except ValueError as er :
            return er

def get_data_table(name_table):
    select_param = {'users': 'id , name , age',
                   'product': 'pid , prod , quantity',
                   'sales': 'sid , id , pid'
                   }
    if name_table is not None :
        cursor.execute(f"SELECT {select_param.get(name_table)} FROM  {name_table}")
        fields = cursor.fetchall()
        for field in fields :
            print(field)

print(print_task_number(1))
string_inp = input('Введите имя таблицы  ( users / product / sales / SaLes ) : ').strip()
get_data_table(date_base_info(string_inp))

# 2)В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity)
# и Sales с полями (sid, id, pid).
# Программа должна вывести все имена из таблицы users, дать пользователю выбрать
# одно из них и вывести все покупки этого пользователя.

def dict_query(key) :
    query_dictionary = {'users' : f'''SELECT id , name  FROM %s''',
        'sales' : f'''SELECT users.id,users.name,product.prod FROM %s
        LEFT JOIN sales on  sales.id  = users.id
        LEFT JOIN  product on product.pid = sales.pid
        WHERE  users.id = %s'''
    }
    return query_dictionary.get(key)

def query_dict_param(users_name):
    dict_param = {}
    for index, param in enumerate(users_name):
       dict_param[index] = param
    return dict_param

def data_collection(name_table = 'users' ,dict_query_key = 'users',user_id = 0) :
    query = dict_query(dict_query_key)
    if dict_query_key ==  'users' :
        cursor.execute(query % name_table)
    else :
        cursor.execute(query % (name_table,user_id))
    names = cursor.fetchall()
    dict_users = query_dict_param(names)
    return dict_users


def validation_selection(num_users,max_value) :
    while True:
        try:
            while True:
                if 1 <= num_users <= max_value:
                    return num_users
                num_users = int(input(f'Порядковый номер может быть только в диапазоне от 1 до {max_value} '))
        except ValueError:
            print('Порядковый номер может быть только числом ')
            num_users = int(input(f'Введите порядковый номер выбранного пользователя от 1 до {max_value}: '))


def show_selection(dict_param) :
    len_dict = len(list(dict_param.values()))
    for key , value in dict_param.items() :
       print(f'{key + 1} {value[1]}')
    int_inp = int(input(f'Введите порядковый номер выбранного пользователя от 1 до {len_dict}: '))
    int_inp = validation_selection(int_inp,len_dict)
    return dict_param[int_inp - 1][0]



def show_product(name_table = 'users' ,dict_query_key_any = 'users'):
    list_result = []
    id_users = show_selection(data_collection(name_table))
    sales = data_collection(name_table,dict_query_key_any, id_users)
    for _ ,data_user in sales.items() :
        if not data_user[1] in list_result  :
            list_result.append(data_user[1])
        list_result.append(data_user[2])
    len_list_result = len(list_result)
    if list_result[1] is None   :
        return f'Пользователь {list_result[0]} не совершил ни одной покупки.'

    return (f"Пользователь {list_result[0]} имеет кол-во покупок = {len_list_result - 1} шт."
            f"\nСписок покупок : {','.join(list_result[1:])}")

print(print_task_number(2))
print(show_product('users','sales'))

