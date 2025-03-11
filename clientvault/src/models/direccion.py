class Direcciones :

    def __init__(self,direccion,descripcion,comuna_id,id_direccion = None)-> None:
        self.id_direccion = id_direccion
        self.direccion = direccion
        self.descripcion = descripcion
        self.comuna_id = comuna_id