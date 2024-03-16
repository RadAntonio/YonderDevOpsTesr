class DriversLicense:
    def __init__(self, id, nume, prenume, categorie, dataDeEmitere, dataDeExpirare, suspendat):
        self._id = id
        self._nume = nume
        self._prenume = prenume
        self._categorie = categorie
        self._dataDeEmitere = dataDeEmitere
        self._dataDeExpirare = dataDeExpirare
        self._suspendat = suspendat

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nume(self):
        return self._nume

    @nume.setter
    def nume(self, value):
        self._nume = value

    @property
    def prenume(self):
        return self._prenume

    @prenume.setter
    def prenume(self, value):
        self._prenume = value

    @property
    def categorie(self):
        return self._categorie

    @categorie.setter
    def categorie(self, value):
        self._categorie = value

    @property
    def dataDeEmitere(self):
        return self._dataDeEmitere

    @dataDeEmitere.setter
    def dataDeEmitere(self, value):
        self._dataDeEmitere = value

    @property
    def dataDeExpirare(self):
        return self._dataDeExpirare

    @dataDeExpirare.setter
    def dataDeExpirare(self, value):
        self._dataDeExpirare = value

    @property
    def suspendat(self):
        return self._suspendat

    @suspendat.setter
    def suspendat(self, value):
        self._suspendat = value

    