import flet as ft


class Appbar(ft.AppBar):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.actions=[ft.Button(text="back")]
        self.leading=ft.Icon(ft.icons.PALETTE)
        self.leading_width=40
        self.title=ft.Text("AppBar Example")
        self.center_title=True
        self.bgcolor=ft.colors.SURFACE_VARIANT



class App:
    def __init__(self,page:ft.Page):
        self.page=page
        self.page.appbar=Appbar(page)
        self.page.controls.append(Screen(page))
        
    def set_app_platform(self):
        screen_width = self.page.window_width
        screen_height = self.page.window_height
        self.page.window_width = (screen_height * 9 / 16) * .8  
        self.page.window_height = screen_height * .8
        self.page.window_left =screen_width*.7
        self.page.window_resizable = False

class Screen(ft.Container):
    def __init__(self, page: ft.Page, **kwargs):
        super().__init__(bgcolor=ft.colors.RED, expand=True,alignment=ft.alignment.center)
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.content.controls.append(ft.Text("center text", text_align=ft.TextAlign.CENTER))
        
        

def main(page: ft.Page):
    page.title = "My First Flet App"
    app=App(page)
    # app.set_app_platform()
    
    page.update()

ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir="assets")
