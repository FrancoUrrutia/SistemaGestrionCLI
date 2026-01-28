class Tarea():
    def __init__(self,titulo,descripcion):
        self.titulo=titulo
        self.descripcion=descripcion
        self.completada=False

    def marcar_completada(self):
        self.completada=True

    def __str__(self):
        if self.completada == True:
            return(f"Tarea = {self.titulo}\nDescripcion = {self.descripcion}\nTarea Completada!")
        else:
            return(f"Tarea = {self.titulo}\nDescripcion = {self.descripcion}\nAun no se he realizado la tarea!")
class TareaConFecha(Tarea):
    def __init__(self,titulo_tfecha,descripcion_tfecha,fecha):
        super().__init__(titulo_tfecha,descripcion_tfecha)
        self.fecha=fecha
    def __str__(self):
        if self.completada == True:
            return(f"Tarea = {self.titulo}\nDescripcion = {self.descripcion}\nFecha limite de la tarea = {self.fecha}\nTarea Completada!")
        else:
            return(f"Tarea = {self.titulo}\nDescripcion = {self.descripcion}\nFecha limite de la tarea = {self.fecha}\nAun no se he realizado la tarea!")


# print("=======================Tarea Simple==========================")
# tarea1=Tarea("Estudiar", "Hay que seguir estudiando")
# tarea1.marcar_completada()
# print(str(tarea1))
# print("=======================Tarea con Fecha==========================")
# tareaFecha=TareaConFecha("Bicicleta","Andar en Bicicleta", "19/01/2026")
# #tareaFecha.marcar_completada()
# # __str__Tareas(tareaFecha)
# print(str(tareaFecha))