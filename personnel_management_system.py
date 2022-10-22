
import q04
import pickle


FIND = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


FILENAME = 'workers.dat'


def main():


    myworkers = load_workers()


    choice = 0



    while choice != QUIT:

        choice = get_menu_choice()


        if choice == FIND:
            find(myworkers)
        elif choice == ADD:
            add(myworkers)
        elif choice == CHANGE:
            change(myworkers)
        elif choice == DELETE:
            delete(myworkers)

    save_workers(myworkers)


def load_workers():
    try:

        input_file = open(FILENAME, 'rb')


        worker_dct = pickle.load(input_file)


        input_file.close()
    except IOError:


        worker_dct = {}


    return worker_dct



def get_menu_choice():
    print()
    print('МЕНЮ')
    print('-----------------------------------------------')
    print('1.Найти сотрудника')
    print('2.Добавить нового сотрудника')
    print('3.Изменить имя, отдел и должность сотрудника')
    print('4.Удалить сотрудника')
    print('5.Выйти из программы')
    print()


    choice = int(input('Введите выбранный пункт: '))


    while choice < FIND or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))


    return choice



def find(myworkers):

    ID = input('Введите идентификационный номер: ')


    print(myworkers.get(ID, 'идентификационный номер не найден.'))



def add(myworkers):
    ID = input('Идентификационный номер: ')
    name = input('Имя: ')
    dep = input('Отдел: ')
    job = input('Должность: ')


    entry = q04.Employee(name,ID,dep,job)




    if ID not in myworkers:
        myworkers[ID] = entry
        print('Запись добавлена.')
    else:
        print('Это имя уже существует.')



def change(myworkers):

    ID = input('Введите Идентификационный номер: ')

    if ID in myworkers:

        name = input('Введите новое имя: ')
        
        dep = input('Введите новый отдел: ')
        
        job = input('Введите новую должность: ')


        entry = q04.Employee(name,ID,dep,job)

        myworkers[ID] = entry
        print('Информация обновлена.')
    else:
        print('Идентификационный номер не найден.')



def delete(myworkers):

    ID = input('Введите Идентификационный номер: ')


    if ID in myworkers:
        del myworkers[ID]
        print('Запись удалена.')
    else:
        print('Идентификационный номер не найден.')



def save_workers(myworkers):

    output_file = open(FILENAME, 'wb')

    pickle.dump(myworkers, output_file)


    output_file.close()



main()