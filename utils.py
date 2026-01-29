import re


def validar_email(email: str) -> bool:
    """
    Valida un email de forma sencilla.
    Devuelve True si el formato es válido, False en caso contrario.
    """
    try:
        if not isinstance(email, str):
            raise TypeError("El email debe ser un texto.")

        email = email.strip()
        if not email:
            raise ValueError("El email está vacío.")

        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(patron, email) is not None

    except (TypeError, ValueError) as e:
        print(f"Error al validar el email: {e}")
        return False


def pedir_email_valido(prompt: str = "Ingresá tu email: ") -> str:
    """
    Pide al usuario un email hasta que el formato sea válido.
    """
    while True:
        try:
            email = input(prompt).strip()
            if validar_email(email):
                return email
            print("Email inválido, intentá de nuevo (ejemplo: usuario@dominio.com).")
        except KeyboardInterrupt:
            print("\nEntrada de email cancelada por el usuario.")
            raise


def pedir_campo_no_vacio(prompt: str) -> str:
    """
    Pide al usuario un texto no vacío.
    """
    while True:
        try:
            valor = input(prompt).strip()
            if valor:
                return valor
            print("El valor no puede estar vacío. Intentá de nuevo.")
        except KeyboardInterrupt:
            print("\nEntrada cancelada por el usuario.")
            raise