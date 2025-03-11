class Telefono :

    def __init__(self,celular,tel_fijo=None,familiar=None, id_telefonos = None) -> None:
        self.id_telefonos = id_telefonos
        self.celular = celular
        self.tel_fijo = tel_fijo
        self.familiar = familiar