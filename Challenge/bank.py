class Bank:
    def __init__(self, BankId=0, Name="Null", Location="Null"):
        self.BankId = BankId
        self.Name = Name
        self.Location = Location

    @property
    def BankId(self):
        return self.__BankId

    @BankId.setter
    def BankId(self, BankId):
        self.__BankId = BankId

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name):
        self.__Name = Name

    @property
    def Location(self):
        return self.__Location

    @Location.setter
    def Location(self, Location):
        self.__Location = Location

    def __str__(self):
        return "Bank Name: %s",self.Name, "\n", "Bank Location: %s",self.Location

class Customer:
    def __init__(self,id,Name,Address,PhoneNo,AcctNo):
        self.Name = Name
        self.id = id
        self.Address = Address
        self.PhoneNo = PhoneNo
        self.AcctNo = AcctNo

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name):
        self.__Name = Name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, Address):
        self.__Address = Address

    @property
    def PhoneNo(self):
        return self.__PhoneNo

    @PhoneNo.setter
    def PhoneNo(self, PhoneNo):
        self.__PhoneNo = PhoneNo

    @property
    def AcctNo(self):
        return self.__AcctNo

    @AcctNo.setter
    def AcctNo(self, AcctNo):
        self.__AcctNo = AcctNo

    def GeneralInquiry(self):
        print("Customer Name: ",self.Name)
        print("Customer Address: ", self.Address)
        print("Customer PhoneNo: ", self.PhoneNo)














































































































