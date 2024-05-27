import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Pizzeria"

    def register(e):
        email = email_input.value
        password = password_input.value
        firstName = firstName_input.value
        lastName = lastName_input.value
        cellphone = cellphone_input.value

        payload = {
            "email": email,
            "password": password,
            "firstName": firstName,
            "lastName": lastName,
            "cellphone": cellphone
        }

        response = requests.post("http://localhost:8080/auth/register", json=payload)

        if response.status_code == 200:
            result.text = "Registro exitoso"
        else:
            result.text = f"Error: {response.status_code} - {response.text}"

        page.update()

    def login(e):
        #valores del formulario
        email = email_input.value
        password = password_input.value

        #payload para la solicitud de login
        payload = {
            "email": email,
            "password": password
        }

        #solicitud POST al servidor
        response = requests.post("http://localhost:8080/auth/login", json=payload)

        if response.status_code == 200:
            result.text = "Inicio de sesión exitoso"
        else:
            result.text = f"Error: {response.status_code} - {response.text}"

        page.update()



    #elementos de la interfaz
    email_input = ft.TextField(label="Email")
    password_input = ft.TextField(label="Contraseña", password=True)
    firstName_input = ft.TextField(label="Nombre")
    lastName_input = ft.TextField(label="Apellido")
    cellphone_input = ft.TextField(label="Teléfono")

    register_button = ft.ElevatedButton(text="Registrar", on_click=register)
    login_button = ft.ElevatedButton(text="Iniciar sesión", on_click=login)

    result = ft.Text()

    #elementos de la página
    page.add(
        ft.Column(
            [
                ft.Text("Formulario de Registro"),
                email_input,
                password_input,
                firstName_input,
                lastName_input,
                cellphone_input,
                register_button,
                ft.Text("Formulario de Inicio de Sesión"),
                email_input,
                password_input,
                login_button,
                result
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )

ft.app(target=main)
