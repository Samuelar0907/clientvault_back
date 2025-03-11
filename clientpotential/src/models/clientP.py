class ClientPotencial :

    def __init__ (
        self,
        pnombre,
        appaterno,
        email,
        numero_telefono,
        razon_contacto,
        cliente_status_id,
        fecha_creacion,
        snombre= None,
        apmaterno= None,
        id= None,
    )-> None:

            self.id=id
            self.pnombre=pnombre
            self.snombre=snombre
            self.appaterno=appaterno
            self.apmaterno=apmaterno
            self.razon_contacto=razon_contacto
            self.cliente_status_id=cliente_status_id
            self.numero_telefono=numero_telefono
            self.email=email
            self.fecha_creacion=fecha_creacion




        