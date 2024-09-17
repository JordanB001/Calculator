class MyAppException(Exception):
    pass


class SymboleSansChiffreAvant(MyAppException):
    def __init__(self, message="Impossible d'utiliser ce symbole lorqu'il n'y a rien avant", *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class SymboleDouble(MyAppException):
    def __init__(self, message="Impossible d'avoir deux symboles d'affilé", *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class VirguleDouble(MyAppException):
    def __init__(self, message="Attention il ne peut pas y avoir de nombre avec 2 virgule !", *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class PourcentageSymbole(MyAppException):
    def __init__(self, message="On ne peut pas faire un pourcetage avec un Symbole!", *args, **kwargs):
        super().__init__(message, *args, **kwargs)