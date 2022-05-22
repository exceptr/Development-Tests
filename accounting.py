documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def call_help_menu():
    print("""
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит 
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится 
    l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться
    d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень
    """)


def moving_document_shelf(storage_place=directories):
    document_id = input("Введите номер документа: ")
    shelf = input("Введите номер полки: ")
    count_shelf = ''
    if shelf not in storage_place.keys() or document_id not in output_document_list():
        command_error()
    else:
        for directory in storage_place.items():
            if document_id in directory[1]:
                count_shelf = directory[0]
                storage_place[count_shelf].remove(document_id)
                storage_place[shelf].append(document_id)
        print(f'\nДокумент успешно перемещён на полку "{shelf}"')


def add_shelf(storage_place=directories):
    shelf = input("Введите номер полки: ")
    if shelf in storage_place.keys():
        command_error()
    else:
        storage_place[shelf] = []
        return shelf, True
    return shelf, False


def output_document_list():
    doc_list = []
    for shelf, val in directories.items():
        doc_list.extend(val)
    return doc_list


def output_shelf_list():
    shelf_list = []
    for shelf, val in directories.items():
        shelf_list.extend(shelf)
    return shelf_list


def add_new_document(doc=documents, storage_place=directories, shelf=str, type=str, number=str, name=str):
    doc_dic = dict()
    # shelf = input("Введите номер полки: ")
    if shelf not in output_shelf_list():
        command_error()
    elif shelf in output_shelf_list():
        doc_dic["type"] = type
        doc_dic["number"] = number
        doc_dic["name"] = name
        doc.append(doc_dic)
        storage_place[shelf].append(doc_dic["number"])
        print("\nДокумент добавлен")
    return f'{doc_dic["number"]}'


def dell_document(doc=documents, document_id=str):
    # document_id = input("Введите номер документа: ")
    if document_id not in output_document_list():
        command_error()
    elif document_id in output_document_list():
        for document in doc:
            if document["number"] == document_id:
                documents.remove(document)
        for shelf, val in directories.items():
            if document_id in val:
                val.remove(document_id)
                print("\nДокумент удалён")
        return document_id


def get_the_person_name(doc=documents, document_id=str):
    # document_id = input("Введите номер документа: ")
    for person in doc:
        if (person["number"]) == document_id:
            print(f'Владелец документа: {person["name"]}')
            return f'{person["name"]}'


def find_store_place(storage_place=directories, document_id=str):
    # document_id = input("Введите номер документа: ")
    if document_id not in output_document_list():
        command_error()
    for store, item_store in storage_place.items():
        if document_id in item_store:
            print(f'Номер полки: {store}')
            return f'{store}'


def withdraw_all_documents(doc=documents):
    print("\nВсе документы: ")
    count = 0
    for document in doc:
        count += 1
        print()
        print(f'Документ {count}: {document["type"]} "{document["number"]}" "{document["name"]}"')
    return count


def command_error():
    print("\nОшибка ввода данных")


def my_program():
    while True:
        print('\nВведите команду / help для вызова меню помощи')
        command = input()
        command_dict.get(command.lower(), command_error)()


command_dict = {
    'p': get_the_person_name,
    's': find_store_place,
    'l': withdraw_all_documents,
    'a': add_new_document,
    'd': dell_document,
    'm': moving_document_shelf,
    'as': add_shelf,
    'help': call_help_menu
}

# my_program()
if __name__ == '__main__':
    # get_the_person_name(document_id='11-2')
    # find_store_place(document_id='10006')
    # withdraw_all_documents()
    # add_new_document(shelf="3", type="passport", number="1337", name="Daniil")
    # print(output_document_list()[-1])
    # print(documents)
    dell_document(document_id="2207 876234")