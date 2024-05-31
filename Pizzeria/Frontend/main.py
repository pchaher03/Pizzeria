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

def purchase(page, pizzaType, price):
    try:
        payload = {
            "userId": page.session.get("usuario")["id"],
            "pizza": pizzaType,
            "price": price,
        }

        response = requests.post("http://localhost:8080/orders/addOrder", json = payload)
        jsonResponse = json.loads(response.content)

        if response.status_code == 202:
            showSnackBar(page, {jsonResponse["mensaje"]}, success=True)
        else:
            showSnackBar(page, f"Error: {response.status_code} - {jsonResponse["mensaje"]}", success=False)
    except Exception as ex:
        print(payload)

        showSnackBar(page, f"Error: {str(ex)}", success=False)


def showPurchaseView(page, pizzaType, price):
    page.controls.clear()

    title = ft.Text(f"Compra de Pizza {pizzaType}", size=30, weight="bold")
    priceText = ft.Text(f"Total: ${price}", size=20)
    purchaseButton = ft.ElevatedButton(text="Comprar", on_click=lambda _: purchase(page, pizzaType, price))
    backButton = ft.ElevatedButton(text="Regresar", on_click=lambda _: showMenuView(page))

    page.add(
        ft.Column(
            [
                title,
                priceText,
                purchaseButton,
                backButton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )
    page.update()

def showMenuView(page):
    page.controls.clear()

    title = ft.Text("Menú", size=32, weight="bold")

    hawaianaColumn = ft.Column(
        [
            ft.Image(src="https://cdn2.cocinadelirante.com/800x600/filters:format(webp):quality(75)/sites/default/files/images/2019/11/como-hacer-pizza-hawaiana.jpg", width=400, height=200),
            ft.ElevatedButton(
                text="Hawaiana",
                on_click=lambda _: showPurchaseView(page, "Hawaiana", 120)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    peperonniColumn = ft.Column(
        [
            ft.Image(src="https://www.simplyrecipes.com/thmb/X2B0QCVdGJWGO1gW6GR7cz1rhe0=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/__opt__aboutcom__coeus__resources__content_migration__simply_recipes__uploads__2019__09__easy-pepperoni-pizza-lead-3-8f256746d649404baa36a44d271329bc.jpg", width=400, height=200),
            ft.ElevatedButton(
                text="Peperonni",
                on_click=lambda _: showPurchaseView(page, "Peperonni", 129)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    vegetalesColumn = ft.Column(
        [
            ft.Image(src="https://api.pizzahut.io/v1/content/images/pizza/veg-supreme.6fcf716cd4ec19d7723f14b0b84459ec.1.jpg", width=400, height=200),
            ft.ElevatedButton(
                text="Vegetales",
                on_click=lambda _: showPurchaseView(page, "Vegetales", 110)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    backButton = ft.ElevatedButton(text="Regresar", on_click=lambda _: showPizzeriaView(page))

    page.add(
        createNavBar(page),
        ft.Column(
            [
                title,
                ft.Row(
                    [
                        hawaianaColumn,
                        peperonniColumn,
                        vegetalesColumn,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=20,
                ),
                backButton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )
    page.update()

def showPizzeriaView(page):
    page.controls.clear()

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
            #guardar token en la sesion
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

def update(page, passwordInput, firstNameInput, lastNameInput, cellphoneInput):
    password = passwordInput.value
    firstName = firstNameInput.value
    lastName = lastNameInput.value
    cellphone = cellphoneInput.value

    payload = {
        "id": page.session.get("usuario")["id"],
        "password": password,
        "firstName": firstName,
        "lastName": lastName,
        "cellphone": cellphone
    }

    try:
        response = requests.put("http://localhost:8080/auth/updateAccount", json = payload)

        #guardar token en la sesion
        jsonResponse = json.loads(response.content)
        token = jsonResponse["token"]
        jwtToken = jwt.decode(token, options={"verify_signature": False})
        page.session.set("token", token)
        page.session.set("usuario", jwtToken["usuario"])

        if response.status_code == 202:
            showSnackBar(page, {jsonResponse["mensaje"]}, success=True)
        else:
            showSnackBar(page, f"Error: {response.status_code} - {jsonResponse["mensaje"]}", success=False)
    except Exception as ex:

        showSnackBar(page, f"Error: {str(ex)}", success=False)

    page.update()

def delete(page):
    try:
        payload = {
            "id": page.session.get("usuario")["id"],
        }

        response = requests.delete("http://localhost:8080/auth/deleteAccount", json = payload)
        jsonResponse = json.loads(response.content)

        if response.status_code == 202:
            showSnackBar(page, {jsonResponse["mensaje"]}, success=True)
            registerAndLoginPage(page)
        else:
            showSnackBar(page, f"Error: {response.status_code} - {jsonResponse["mensaje"]}", success=False)
    except Exception as ex:
        showSnackBar(page, f"Error: {str(ex)}", success=False)

def showEditAccountView(page):
    page.controls.clear()

    passwordInput = ft.TextField(label="Contraseña", password=True)
    firstNameInput = ft.TextField(label="Nombre")
    lastNameInput = ft.TextField(label="Apellido")
    cellphoneInput = ft.TextField(label="Teléfono")

    registerButton = ft.ElevatedButton(text="Cambiar Datos", on_click=lambda e: update(page, passwordInput, firstNameInput, lastNameInput, cellphoneInput))
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
