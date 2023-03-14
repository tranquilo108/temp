import view
import model
def run():
    view.greeting()
    while True:
        view.menu()
        choice = int(input())
        match choice:
            case 1:
                a = model.find()
                if a == 'Контакт не найден':
                    print(a)
                    continue
                else:
                    print(a)
                    view.find_menu()
                    find_choice = int(input())
                    match find_choice:
                        case 1:
                            model.edit(a)
                        case 2:
                            model.delete(a)
                        case 3:
                            continue
                        case 4:
                            choice = 4
                        case _:
                            print('Введено неверное знаечние, попробуем снова =)')
            case 2:
                model.add_contact()
            case 3:
                view.show_phonebook()
            case 4:
                break    
            case _:
                print('Введено неверное знаечние, попробуем снова =)')
                view.menu()