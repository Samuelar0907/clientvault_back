class Client :

    def __init__ (
        self,
        id_paciente,
        pnombre,
        appaterno,
        pais_id,
        identificacion_id,
        num_identificacion,
        f_reg_alma,
        f_nac,
        genero,
        prevision_id,
        ocupacion_id,
        sucursal_id,
        academico_id,
        mail_princ,
        ult_visita,
        snombre= None,
        apmaterno= None,
        mail_sec= None,
        direccion_id= None,
        telefono_id= None,
    )-> None:

            self.id_paciente=id_paciente
            self.pnombre=pnombre
            self.snombre=snombre
            self.appaterno=appaterno
            self.apmaterno=apmaterno
            self.pais_id=pais_id
            self.identificacion_id=identificacion_id
            self.num_identificacion=num_identificacion
            self.f_reg_alma=f_reg_alma
            self.f_nac=f_nac
            self.genero=genero
            self.prevision_id=prevision_id
            self.ocupacion_id=ocupacion_id
            self.telefono_id=telefono_id
            self.direccion_id=direccion_id
            self.sucursal_id=sucursal_id
            self.academico_id=academico_id
            self.mail_princ=mail_princ
            self.mail_sec=mail_sec
            self.ult_visita=ult_visita




        