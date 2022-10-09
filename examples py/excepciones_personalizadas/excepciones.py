class NoAutorizadoException(Exception):
    def __init__(self):
        self.message = "¡No estas Autorizado!"

    def __str__(self):
        return self.message
