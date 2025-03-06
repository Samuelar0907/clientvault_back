class Telefono :

    def __init__(self,celular,tel_fijo,familiar,id_comuna = None) -> None:
        self.celular = celular
        self.tel_fijo = tel_fijo
        self.familiar = familiar
        self.id_telefonos = id_comuna