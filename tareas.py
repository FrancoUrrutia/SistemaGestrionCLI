class Tarea():
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        if self.completada:
            return (
                f"Tarea: {self.titulo}\n"
                f"Descripción: {self.descripcion}\n"
                "Estado: Completada ✅"
            )
        else:
            return (
                f"Tarea: {self.titulo}\n"
                f"Descripción: {self.descripcion}\n"
                "Estado: Pendiente ⏳"
            )


class TareaConFecha(Tarea):
    def __init__(self, titulo_tfecha, descripcion_tfecha, fecha):
        super().__init__(titulo_tfecha, descripcion_tfecha)
        self.fecha = fecha

    def __str__(self):
        if self.completada:
            return (
                f"Tarea: {self.titulo}\n"
                f"Descripción: {self.descripcion}\n"
                f"Fecha límite: {self.fecha}\n"
                "Estado: Completada ✅"
            )
        else:
            return (
                f"Tarea: {self.titulo}\n"
                f"Descripción: {self.descripcion}\n"
                f"Fecha límite: {self.fecha}\n"
                "Estado: Pendiente ⏳"
            )
