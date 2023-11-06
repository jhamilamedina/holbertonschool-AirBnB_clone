"""En este modulo creamos la clase user"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    La clase User maneja los atributos del user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
