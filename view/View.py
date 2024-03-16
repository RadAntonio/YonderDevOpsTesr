from controller.Controller import Controller


class View:
    def __init__(self):
        self._controller = Controller()

    def display_menu(self):
        print("-------SELECTION MENU-------")
        print("Select Function:")
        print("1. Print Suspended Licenses")
        print("2. Print Valid Licenses")
        print("3. Print Licenses by Category")
        print("0. Exit")

    def execute_function(self, option):
        if option == "1":
            self.print_suspended_licenses()
        elif option == "2":
            self.print_valid_licenses()
        elif option == "3":
            self.print_licenses_by_category()
        elif option == "0":
            print("Exiting...")
            return
        else:
            print("Invalid option")

    def print_suspended_licenses(self):
        for license in self._controller.get_suspended_licenses():
            print(f"{license.nume} {license.prenume} - Suspended License")

    def print_valid_licenses(self):
        for license in self._controller.extract_valid_licenses():
            print(f"{license.nume} {license.prenume} {license.dataDeEmitere} - Valid License")

    def print_licenses_by_category(self):
        try:
            category_id = input("Enter category ID: ")
            license_count = self._controller.count_lincese_by_category(category_id)
            print(f"Count of licenses for category {category_id}: {license_count}")
        except Exception as e:
            print(e)


