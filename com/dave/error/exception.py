class FieldException(Exception):
    def __init__(self, message, code=500 ):
        self.message = message
        self.code = code

class DataException(FieldException):
    def __init__(self, message, code=500):
        super(DataException, self).__init__(message, code)
