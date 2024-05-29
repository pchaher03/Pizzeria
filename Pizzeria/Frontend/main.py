import flet as ft
import requests
import json
import jwt

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
            jsonResponse = json.loads(response.content)
            token = jsonResponse["token"]

            jwtToken = jwt.decode(token, options={"verify_signature": False})

            page.session.set("token", token)
            page.session.set("usuario", jwtToken["usuario"])

            showSnackBar(page, "Inicio de sesión exitoso", success=True)
            showPizzeriaView(page)
        else:
            showSnackBar(page, f"Error: {response.status_code} - Error en los datos de inicio de sesion.", success=False)
    except Exception as ex:
        showSnackBar(page, f"Error: {str(ex)}", success=False)

    page.update()

def registerAndLoginPage(page):
    page.controls.clear()

    page.session.clear()

    emailInput = ft.TextField(label="Email")
    passwordInput = ft.TextField(label="Contraseña", password=True)
    firstNameInput = ft.TextField(label="Nombre")
    lastNameInput = ft.TextField(label="Apellido")
    cellphoneInput = ft.TextField(label="Teléfono")

    registerButton = ft.ElevatedButton(text="Registrar", on_click=lambda e: register(page, emailInput, passwordInput, firstNameInput, lastNameInput, cellphoneInput))
    loginButton = ft.ElevatedButton(text="Iniciar sesión", on_click=lambda e: login(page, emailInput, passwordInput))

    result = ft.Text()

    page.add(
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

def update(page, payload):
    userId = page.session.get("usuario")["id"]

    try:
        response = requests.put("http://localhost:8080/auth/updateAccount/{userId}", json=payload)
        jsonResponse = json.loads(response.content)

        if response.status_code == 202:

            showSnackBar(page, "Registro exitoso", success=True)
        else:
            #showSnackBar(page, userId, success=True)
            showSnackBar(page, f"Error: {response.status_code} - {jsonResponse["mensaje"]}", success=False)
    except Exception as ex:

        showSnackBar(page, f"Error: {str(ex)}", success=False)

    page.update()

def delete(page):
    return

def showEditAccountView(page):
    page.controls.clear()

    passwordInput = ft.TextField(label="Contraseña", password=True)
    firstNameInput = ft.TextField(label="Nombre")
    lastNameInput = ft.TextField(label="Apellido")
    cellphoneInput = ft.TextField(label="Teléfono")

    payload = {
        "password": passwordInput.value,
        "firstName": firstNameInput.value,
        "lastName": lastNameInput.value,
        "cellphone": cellphoneInput.value
    }

    registerButton = ft.ElevatedButton(text="Cambiar Datos", on_click=lambda e: update(page, payload))
    deleteButton = ft.ElevatedButton(text="Borrar cuenta", on_click=lambda e: delete(page))

    result = ft.Text()

    page.add(
        createNavBar(page),
        ft.Column(
            [
                ft.Text("Cambia tu informacion"),
                passwordInput,
                firstNameInput,
                lastNameInput,
                cellphoneInput,
                registerButton,
                deleteButton,
                result
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )

    page.update()

def createNavBar(page):
    homeButton = ft.ElevatedButton(text="Inicio", on_click=lambda _: showPizzeriaView(page))
    logoutButton = ft.ElevatedButton(text="Cerrar sesión", on_click=lambda _: registerAndLoginPage(page))
    accountButton = ft.ElevatedButton(text="Cuenta", on_click=lambda _: showEditAccountView(page))

    navBar = ft.Row(
        [
            homeButton,
            accountButton,
            logoutButton,
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing=10,
    )

    return navBar

def main(page: ft.Page):
    page.title = "Pizzeria"
    registerAndLoginPage(page)

ft.app(target=main)
