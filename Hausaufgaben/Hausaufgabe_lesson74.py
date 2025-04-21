import mysql.connector

#Шапка для отделения заданий
def print_task_number(task_numb) :

    text = (f'\033[35m+++++++++++++++++++++++++++++++++++\n'
            f'+++++++++++ Задание № {task_numb} +++++++++++\n'
            f'+++++++++++++++++++++++++++++++++++\033[0m')
    return text

DBCONFIG = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password', 
    'database': 'ich_edit'
}

try:
    conn = mysql.connector.connect(**DBCONFIG)
except mysql.connector.Error as e:
    print(f'Ошибка соединения : {e}')
    exit()
cursor = conn.cursor()


def dict_query(key):
    query_dict = {
        'table_name': 'SHOW TABLES',
        'column_name': '''SELECT COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s''',
        'column_info': '''SELECT COLUMN_NAME, DATA_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s''',
        'compare' : '''SELECT * FROM %s 
        WHERE %s %s %s'''

    }
    return query_dict.get(key)


def dict_data(key_query, schema, name_table):
    query = dict_query(key_query)
    dict_param = {}
    if query is None:
        print(f"Ошибка: Неверный ключ запроса: {key_query}")
        return dict_param
    if query.find('%s') < 0:
        cursor.execute(query)
    else:
        cursor.execute(query, (schema, name_table))
    data_query = cursor.fetchall()
    for index, data in enumerate(data_query, start=1):
        dict_param[index] = data
    return dict_param


def validation_select(inp_string, key_query, text_input, text_error, schema, name_table):
    data_dict = dict_data(key_query, schema, name_table)
    len_data_dict = len(list(data_dict))
    while True:
        if inp_string.isdigit():
            if 1 <= int(inp_string) <= len_data_dict:
                return ''.join(list(data_dict.get(int(inp_string))))
            print(f'Введенное число должно быть в диапазоне от 1 до {len_data_dict}')
            inp_string = input(f'{text_input}').strip()
        if not inp_string.isdigit():
            for key, value in data_dict.items():
                if value[0] == inp_string:
                    return value
            raise NameError(text_error % inp_string)

def operator() :
    list_operator = ['>','<','=']
    string_operator = ','.join(list_operator)
    while True:
        string_inp = input(f'Введите оператор для сравнения : ( {string_operator} ) : ').strip()
        if string_inp in list_operator :
            return string_inp
        print('Введен не верный оператор.')

def show_selection(key_query, inp_str, error_text, schema, name_table):
    data_dict = dict_data(key_query, schema, name_table)
    for key, value in data_dict.items():
         print(f'{key} - {value[0]}')
    string_input = input(f'{inp_str}').strip()
    try:
        selected_value = validation_select(string_input, key_query, inp_str, error_text, schema, name_table)
        return selected_value
    except NameError as err:
        print(err)
        return None

def dict_type(key_type) :
    type_dict = {
        'tinyint': int,
        'smallint': int,
        'mediumint': int,
        'int': int,
        'integer': int,
        'bigint': int,
        'float': float,
        'double': float,
        'real': float,
        'decimal': float,
        'numeric': float,
        'char': str,
        'varchar': str,
        'tinytext': str,
        'text': str,
        'mediumtext': str,
        'longtext': str,
        'binary': bytes,
        'varbinary': bytes,
        'tinyblob': bytes,
        'blob': bytes,
        'mediumblob': bytes,
        'longblob': bytes,
        'date': str,
        'time': str,
        'datetime': str,
        'timestamp': str,
        'year': int,
        'json': dict,
        'boolean': bool,
        'enum': str,
        'set': list,
        'geometry': bytes,
        'point': bytes,
        'linestring': bytes,
        'polygon': bytes
    }
    return type_dict.get(key_type)

def get_type_field(schema, name_table,name_field) :
    type_tmp = ''
    data_dict = dict_data('column_info', schema, name_table)
    for type_field in data_dict.values() :
        if type_field[0] == name_field :
            type_tmp = dict_type(type_field[1])
            break
    return type_tmp

def validation_type(name_field,schema, name_table) :
    type_tmp = get_type_field(schema, name_table, name_field)
    while True :
        try:
            value_inp = type_tmp(input(f'Введите сравниваемое значение оно должно иметь тип : {type_tmp.__name__} : ' ).strip())
            return  value_inp
        except ValueError :
            print(f'Введено значение с неверным типом.')

def show_result(name_field,schema, name_table) :
    str_tmp = ''
    oper =  operator()
    value_compare = validation_type(name_field,schema, name_table)
    data_dict = dict_data('column_name', schema, name_table)
    cursor.execute(dict_query('compare' ) % (name_table,name_field,oper,value_compare))
    result = cursor.fetchall()
    if not result :
        raise NameError ('Данных с таким значением не найдено')
    for value in data_dict.values() :
        str_tmp += f'{' '.join(value):<10}'
    print (str_tmp)
    for value in result :
        str_tmp =''
        for val in value :
            str_tmp += f'{val:<10}'
        print(str_tmp)
    return ''

def main():
    schema = DBCONFIG.get('database')
    text_inp = 'Выберете таблицу номер/название: '
    text_err = 'Таблица с именем %s не найдена в базе данных.'
    name_table = show_selection('table_name', text_inp, text_err, schema, None)
    text_inp = 'Выберете поле номер/название: '
    text_err = 'Поле с именем %s не найдено в таблице'
    name_field = show_selection('column_name', text_inp, text_err, schema, name_table)
    try:
        show_result(name_field, schema, name_table)
    except NameError as err :
        print(err)
    finally:
        cursor.close()
        conn.close()

print(print_task_number(1))
main()

