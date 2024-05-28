import flet as ft
import requests

def showSnackBar(page, message, success=True):
    color = ft.colors.GREEN if success else ft.colors.RED
    snack = ft.SnackBar(
        content=ft.Text(message),
        bgcolor=color,
        duration=3000
    )
    page.snack_bar = snack
    snack.open = True
    page.update()

def showMenuView(page):
    page.controls.clear()

    # Elementos de la vista del menú
    title = ft.Text("Menú", size=32, weight="bold")
    hawaianaButton = ft.ElevatedButton(text="Hawaiana", on_click=lambda _: showSnackBar(page, "Pedido Hawaiana realizado"))
    peperonniButton = ft.ElevatedButton(text="Peperonni", on_click=lambda _: showSnackBar(page, "Pedido Peperonni realizado"))
    vegetalesButton = ft.ElevatedButton(text="Vegetales", on_click=lambda _: showSnackBar(page, "Pedido Vegetales realizado"))
    backButton = ft.ElevatedButton(text="Regresar", on_click=lambda _: showPizzeriaView(page))

    # Elementos de la página
    page.add(
        createNavBar(page),
        ft.Column(
            [
                title,
                hawaianaButton,
                peperonniButton,
                vegetalesButton,
                backButton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )
    page.update()

def showPizzeriaView(page):
    page.controls.clear()

    # Elementos de la vista de la pizzería
    title = ft.Text("Pizzeria", size=32, weight="bold")
    pizzaImage = ft.Image(src="https://2trendies.com/hero/2023/04/pizzapepperoni.jpg?width=1200&aspect_ratio=16:9", width=400, height=200)
    orderButton = ft.ElevatedButton(text="Ordenar pedido", on_click=lambda _: showMenuView(page))

    page.add(
        createNavBar(page),
        ft.Column(
            [
                title,
                pizzaImage,
                orderButton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )
    page.update()

def register(page, emailInput, passwordInput, firstNameInput, lastNameInput, cellphoneInput):
    email = emailInput.value
    password = passwordInput.value
    firstName = firstNameInput.value
    lastName = lastNameInput.value
    cellphone = cellphoneInput.value

    payload = {
        "email": email,
        "password": password,
        "firstName": firstName,
        "lastName": lastName,
        "cellphone": cellphone
    }

    try:
        response = requests.post("http://localhost:8080/auth/register", json=payload)
        if response.status_code == 202:
            showSnackBar(page, "Registro exitoso", success=True)
        else:
            showSnackBar(page, f"Error: {response.status_code} - {response.text}", success=False)
    except Exception as ex:
        showSnackBar(page, f"Error: {str(ex)}", success=False)

    page.update()

def login(page, emailInput, passwordInput):
    email = emailInput.value
    password = passwordInput.value

    payload = {
        "email": email,
        "password": password
    }

    try:
        response = requests.post("http://localhost:8080/auth/login", json=payload)
        if response.status_code == 202:
            showSnackBar(page, "Inicio de sesión exitoso", success=True)
            showPizzeriaView(page)
        else:
            showSnackBar(page, f"Error: {response.status_code} - {response.text}", success=False)
    except Exception as ex:
        showSnackBar(page, f"Error: {str(ex)}", success=False)

    page.update()

def registerAndLoginPage(page):
    page.controls.clear()
    emailInput = ft.TextField(label="Email")
    passwordInput = ft.TextField(label="Contraseña", password=True)
    firstNameInput = ft.TextField(label="Nombre")
    lastNameInput = ft.TextField(label="Apellido")
    cellphoneInput = ft.TextField(label="Teléfono")

    registerButton = ft.ElevatedButton(text="Registrar", on_click=lambda e: register(page, emailInput, passwordInput, firstNameInput, lastNameInput, cellphoneInput))
    loginButton = ft.ElevatedButton(text="Iniciar sesión", on_click=lambda e: login(page, emailInput, passwordInput))

    result = ft.Text()

    page.add(
        createNavBar(page),
        ft.Column(
            [
                ft.Text("Registro"),
                emailInput,
                passwordInput,
                firstNameInput,
                lastNameInput,
                cellphoneInput,
                registerButton,
                ft.Text("Inicio de Sesión"),
                emailInput,
                passwordInput,
                loginButton,
                result
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )

def createNavBar(page):
    homeButton = ft.ElevatedButton(text="Inicio", on_click=lambda _: showPizzeriaView(page))
    logoutButton = ft.ElevatedButton(text="Cerrar sesión", on_click=lambda _: registerAndLoginPage(page))

    navBar = ft.Row(
        [
            homeButton,
            logoutButton
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing=10,
    )

    return navBar

def main(page: ft.Page):
    page.title = "Pizzeria"
    registerAndLoginPage(page)

ft.app(target=main)
