import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Pizzeria"
    
    def show_snack_bar(message, success=True):
        color = ft.colors.GREEN if success else ft.colors.RED
        snack = ft.SnackBar(
            content=ft.Text(message),
            bgcolor=color,
            duration=3000
        )
        page.snack_bar = snack
        snack.open = True
        page.update()

    def show_menu_view():
        # Limpiar la página actual
        page.controls.clear()
        
        # Crear elementos de la vista del menú
        title = ft.Text("Menú", size=32, weight="bold")
        hawaiana_button = ft.ElevatedButton(text="Hawaiana", on_click=lambda _: show_snack_bar("Pedido Hawaiana realizado"))
        peperonni_button = ft.ElevatedButton(text="Peperonni", on_click=lambda _: show_snack_bar("Pedido Peperonni realizado"))
        vegetales_button = ft.ElevatedButton(text="Vegetales", on_click=lambda _: show_snack_bar("Pedido Vegetales realizado"))
        
        # Añadir elementos a la página
        page.add(
            ft.Column(
                [
                    title,
                    hawaiana_button,
                    peperonni_button,
                    vegetales_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            )
        )
        page.update()
    
    def show_pizzeria_view():
        # Limpiar la página actual
        page.controls.clear()
        
        # Crear elementos de la vista de la pizzería
        title = ft.Text("Pizzeria", size=32, weight="bold")
        pizza_image = ft.Image(src="https://example.com/pizza.jpg", width=200, height=200)  # Asegúrate de usar una URL válida para la imagen
        order_button = ft.ElevatedButton(text="Ordenar pedido", on_click=lambda _: show_menu_view())
        
        # Añadir elementos a la página
        page.add(
            ft.Column(
                [
                    title,
                    pizza_image,
                    order_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            )
        )
        page.update()
    
    
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
        
        try:
            response = requests.post("http://localhost:8080/auth/register", json=payload)
            if response.status_code == 202:
                show_snack_bar("Registro exitoso", success=True)
            else:
                show_snack_bar(f"Error: {response.status_code} - {response.text}", success=False)
        except Exception as ex:
            show_snack_bar(f"Error: {str(ex)}", success=False)
        
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
        try:
            response = requests.post("http://localhost:8080/auth/login", json=payload)
            if response.status_code == 202:
                show_snack_bar("Inicio de sesión exitoso", success=True)
                show_pizzeria_view()  # Llama a la función para mostrar la vista de la pizzería
            else:
                show_snack_bar(f"Error: {response.status_code} - {response.text}", success=False)
        except Exception as ex:
            show_snack_bar(f"Error: {str(ex)}", success=False)
        
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
