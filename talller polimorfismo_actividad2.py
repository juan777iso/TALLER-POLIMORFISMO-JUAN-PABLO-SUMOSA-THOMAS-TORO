class notificacion():
    pass

    def enviar_mensaje(self):
        pass

class sms(notificacion):
    def __init__(self,numero,mensaje):
        self.numero=numero
        self.mensaje=mensaje
       
    def enviar_mensaje(self):
        if self.numero>999999999:
            return f"al numero {self.numero} se ha enviado el mensaje: {self.mensaje}"
        else:
            return "numero no valido"
   
class notificacion_app(notificacion):
    def __init__(self,id_dispositivo,mensaje):
        self.id_dispositivo=id_dispositivo
        self.mensaje=mensaje
    def enviar_mensaje(self):
        if self.id_dispositivo !="":
            return f"al dispositivo {self.id_dispositivo} se ha enviado el mensaje: {self.mensaje}"
        else:
            return"error id de dispositivo no valido"


class correo_electronico(notificacion):
    def __init__(self,correo,mensaje):
        self.correo=correo
        self.mensaje=mensaje
    def enviar_mensaje(self):
        character="@"
        if character in self.correo:
            return f"al correo {self.correo} se ha enviado el mensaje: {self.mensaje}"
        else:
            return "correo electronico no valido"

mensaje="mañana no hay clase"
lista=[sms(314320901,mensaje),notificacion_app("",mensaje),correo_electronico("eljuanpqblogmail.com",mensaje)]

for i in lista:
    print(i.enviar_mensaje())
            



        
        

        