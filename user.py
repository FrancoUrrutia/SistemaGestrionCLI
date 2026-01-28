from tareas import *
class Usuario():
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.__tareas=[]

    def agregar_tarea(self):
        tipo = input("[1] Simple / [2] Con fecha: ").strip()
        titulo = input("Título: ").strip()
        descripcion = input("Descripción: ").strip()

        if tipo == "1":
            self.__tareas.append(Tarea(titulo, descripcion))
        elif tipo == "2":
            fecha = input("Fecha límite: ").strip()
            self.__tareas.append(TareaConFecha(titulo, descripcion, fecha))
        else:
            print("Opción inválida.")

    def listar_tareas(self):
        if not self.__tareas:
            print("No hay tareas ingresadas!!")
        else:
            for tarea in self.__tareas:
                print(tarea)

    def tareas_pendientes(self):
        pendientes = [t for t in self.__tareas if not t.completada]
        if not pendientes:
            print("No hay tareas pendientes.")
        else:
            for tarea in pendientes:
                print(tarea)

    def tareas_completadas(self):
        completadas = [t for t in self.__tareas if t.completada]
        if not completadas:
            print("No hay tareas completadas.")
        else:
            for tarea in completadas:
                print(tarea)
    
franco=Usuario("Franco","franco@gmail.com")
franco.agregar_tarea()
print("==================Listar tarea================")
franco.listar_tareas()