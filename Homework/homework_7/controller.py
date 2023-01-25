from import_data import new_data
import view
import export_data


def start():
    contact_line = []
    option = view.get_welcome()
    if option == 1:
        new_data(contact_line)
    elif option == 2:
        search_name = export_data.get_search_name()
        export_data.find_data(search_name)
    elif option == 3:
        search_name = export_data.get_search_name()
        export_data.find_data_by_number(search_name)
    elif option == 4:
        view.get_phonebook()
    else:
        view.sort_phonebook()
