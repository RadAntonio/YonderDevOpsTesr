import datetime

from helper.ApiHelper import ApiHelper
from helper.FileHelper import FileHelper


class Controller:

    def __init__(self):
        self._api_helper = ApiHelper("http://localhost:30000/drivers-licenses/list?length=150")
        self._api_helper.fetch_data()
        self._file_helper = FileHelper()

    def get_suspended_licenses(self):
        suspended_licenses = [license for license in self._api_helper.drivers_licenses if license.suspendat]
        self._file_helper.write_to_excel_suspended_licenses(suspended_licenses)
        return suspended_licenses

    def extract_valid_licenses(self):
        valid_licenses = []
        current_date = datetime.date.today()
        for license in self._api_helper.drivers_licenses:
            if datetime.datetime.strptime(license.dataDeExpirare, "%d/%m/%Y").date() >= current_date:
                valid_licenses.append(license)
        self._file_helper.write_to_excel_valid_licenses(valid_licenses)
        return valid_licenses

    def count_lincese_by_category(self, category_name):
        count = 0
        licenses_with_given_id = []
        for license in self._api_helper.drivers_licenses:
            if license.categorie == category_name:
                count += 1
                licenses_with_given_id.append(license)
        self._file_helper.write_to_excel_by_category_licenses(licenses_with_given_id)
        return count
