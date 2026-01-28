from tareas import Tarea, TareaConFecha
class Usuario():
    def __init__(self,nombre,email,tareas=None):
        self.nombre=nombre
        self.email=email
        self.__tareas=tareas

    def agregar_tarea(self):
        pass

    def listar_tareas(self):
        pass

    def tareas_pendientes(self):
        pass

    def tareas_completadas(self):
        pass