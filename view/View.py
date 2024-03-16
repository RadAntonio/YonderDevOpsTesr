from controller.Controller import Controller


class View:
    def __init__(self):
        self._controller = Controller()

    def print_suspended_licenses(self):
        for license in self._controller.get_suspended_licenses():
            print(f"{license.nume} {license.prenume} - Suspended License")

    def print_valid_licenses(self):
        for license in self._controller.extract_valid_licenses():
            print(f"{license.nume} {license.prenume} {license.dataDeExpirare} - Valid License")

    def print_licenses_by_category(self):
        category_id = input("Enter category ID: ")
        license_count = self._controller.count_lincese_by_category(category_id)
        print(f"Count of licenses for category {category_id}: {license_count}")


