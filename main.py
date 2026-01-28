from user import Usuario
from utils import pedir_campo_no_vacio, pedir_email_valido
def mostrar_menu():
    print("\n=== Menú de Tareas ===")
    print("[1] Agregar tarea")
    print("[2] Listar todas las tareas")
    print("[3] Ver tareas pendientes")
    print("[4] Ver tareas completadas")
    print("[5] Salir")

def main():
    print("=== Sistema de Gestión de Tareas ===")
    nombre = pedir_campo_no_vacio("Ingresá tu nombre: ")
    email = pedir_email_valido()

    usuario = Usuario(nombre, email)
    print(f"\nUsuario creado: {usuario.nombre} - {usuario.email}")

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            usuario.agregar_tarea()
        elif opcion == "2":
            usuario.listar_tareas()
        elif opcion == "3":
            usuario.tareas_pendientes()
        elif opcion == "4":
            usuario.tareas_completadas()
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

if __name__ == "__main__":
    main()