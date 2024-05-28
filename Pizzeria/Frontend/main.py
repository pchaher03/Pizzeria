import flet
import requests

def showSnackBar(page, message, success=True):
    color = flet.colors.GREEN if success else flet.colors.RED
    snack = flet.SnackBar(
        content=flet.Text(message),
        bgcolor=color,
        duration=3000
    )
    page.snack_bar = snack
    snack.open = True
    page.update()

def showMenuView(page):
    page.controls.clear()

    # Elementos de la vista del menú
    title = flet.Text("Menú", size=32, weight="bold")
    hawaianaButton = flet.ElevatedButton(text="Hawaiana", on_click=lambda _: showSnackBar(page, "Pedido Hawaiana realizado"))
    peperonniButton = flet.ElevatedButton(text="Peperonni", on_click=lambda _: showSnackBar(page, "Pedido Peperonni realizado"))
    vegetalesButton = flet.ElevatedButton(text="Vegetales", on_click=lambda _: showSnackBar(page, "Pedido Vegetales realizado"))
    backButton = flet.ElevatedButton(text="Regresar", on_click=lambda _: showPizzeriaView(page))

    # Elementos de la página
    page.add(
        flet.Column(
            [
                title,
                hawaianaButton,
                peperonniButton,
                vegetalesButton,
                backButton
            ],
            alignment=flet.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )
    page.update()

def showPizzeriaView(page):
    page.controls.clear()

    # Elementos de la vista de la pizzería
    title = flet.Text("Pizzeria", size=32, weight="bold")
    pizzaImage = flet.Image(src="https://2trendies.com/hero/2023/04/pizzapepperoni.jpg?width=1200&aspect_ratio=16:9", width=400, height=200)
    orderButton = flet.ElevatedButton(text="Ordenar pedido", on_click=lambda _: showMenuView(page))

    page.add(
        flet.Column(
            [
                title,
                pizzaImage,
                orderButton
            ],
            alignment=flet.MainAxisAlignment.CENTER,
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
            showSnackBar(page, f"Error: {response.status_code} - Error en los datos.", success=False)
    except Exception as ex:
        showSnackBar(page, f"Error: {str(ex)}", success=False)

    page.update()

def registerAndLoginPage(page):
    emailInput = flet.TextField(label="Email")
    passwordInput = flet.TextField(label="Contraseña", password=True)
    firstNameInput = flet.TextField(label="Nombre")
    lastNameInput = flet.TextField(label="Apellido")
    cellphoneInput = flet.TextField(label="Teléfono")

    registerButton = flet.ElevatedButton(text="Registrar", on_click=lambda e: register(page, emailInput, passwordInput, firstNameInput, lastNameInput, cellphoneInput))
    loginButton = flet.ElevatedButton(text="Iniciar sesión", on_click=lambda e: login(page, emailInput, passwordInput))

    result = flet.Text()

    page.add(
        flet.Column(
            [
                flet.Text("Registro"),
                emailInput,
                passwordInput,
                firstNameInput,
                lastNameInput,
                cellphoneInput,
                registerButton,
                flet.Text("Inicio de Sesión"),
                emailInput,
                passwordInput,
                loginButton,
                result
            ],
            alignment=flet.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )

def main(page: flet.Page):
    page.title = "Pizzeria"
    registerAndLoginPage(page)

flet.app(target=main)
