import re

def validar_email(email: str) -> bool:
    try:
        if not isinstance(email, str):
            raise TypeError("El email debe ser un string.")

        email = email.strip()
        if not email:
            raise ValueError("El email está vacío.")

        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(patron, email) is not None

    except (TypeError, ValueError) as e:
        print(f"Error al validar email: {e}")
        return False


def pedir_email_valido(prompt: str = "Ingresá tu email: ") -> str:
    while True:
        email = input(prompt).strip()
        if validar_email(email):
            return email
        print("Email inválido, intentá de nuevo.")


def pedir_campo_no_vacio(prompt: str) -> str:
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("El valor no puede estar vacío. Intentá de nuevo.")