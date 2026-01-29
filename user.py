from tareas import Tarea, TareaConFecha


class Usuario():
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.__tareas = []

    def agregar_tarea(self):
        try:
            tipo = input("[1] Simple / [2] Con fecha: ").strip()
            titulo = input("Título de la tarea: ").strip()
            descripcion = input("Descripción de la tarea: ").strip()

            if not titulo or not descripcion:
                print("El título y la descripción no pueden estar vacíos.")
                return

            if tipo == "1":
                self.__tareas.append(Tarea(titulo, descripcion))
                print("Tarea simple agregada correctamente.")
            elif tipo == "2":
                fecha = input("Fecha límite de la tarea (ej: 2026-01-31): ").strip()
                if not fecha:
                    print("La fecha límite no puede estar vacía.")
                    return
                self.__tareas.append(TareaConFecha(titulo, descripcion, fecha))
                print("Tarea con fecha agregada correctamente.")
            else:
                print("Opción inválida. Debes elegir 1 (simple) o 2 (con fecha).")

        except KeyboardInterrupt:
            print("\nOperación de alta de tarea cancelada por el usuario.")
        except Exception as e:
            print(f"\nSe produjo un error al agregar la tarea: {e}")

    def listar_tareas(self):
        if not self.__tareas:
            print("No hay tareas cargadas.")
        else:
            print("\n=== Lista de tareas ===")
            for tarea in self.__tareas:
                print(tarea)
                print("=" * 25)

    def tareas_pendientes(self):
        pendientes = [t for t in self.__tareas if not t.completada]
        if not pendientes:
            print("No hay tareas pendientes.")
        else:
            print("\n=== Tareas pendientes ===")
            for tarea in pendientes:
                print(tarea)
                print("=" * 25)

    def tareas_completadas(self):
        completadas = [t for t in self.__tareas if t.completada]
        if not completadas:
            print("No hay tareas completadas.")
        else:
            print("\n=== Tareas completadas ===")
            for tarea in completadas:
                print(tarea)
                print("=" * 25)