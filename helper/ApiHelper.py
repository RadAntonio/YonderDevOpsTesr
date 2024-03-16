import requests

from entity.DriversLicense import DriversLicense


class ApiHelper:

    def __init__(self, url):
        self._url = url
        self._drivers_licenses = []
        self._categories = {}

    def fetch_data(self):
        try:
            response = requests.get(self._url)
            if response.status_code == 200:
                data = response.json()
                for item in data:
                    drivers_license = DriversLicense(
                        item['id'],
                        item['nume'],
                        item['prenume'],
                        item['categorie'],
                        item['dataDeEmitere'],
                        item['dataDeExpirare'],
                        item['suspendat'],
                    )
                    self._drivers_licenses.append(drivers_license)
                    if not self._categories.get(item['categorie']):
                        self._categories[item['categorie']] = item['categorie']
            else:
                raise Exception('Failed to fetch data')
        except Exception as child:
            raise child

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def drivers_licenses(self):
        return self._drivers_licenses

    @drivers_licenses.setter
    def drivers_licenses(self, drivers_licenses):
        self._drivers_licenses = drivers_licenses

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self,categories):
        self._categories = categories