import flet as ft

from xiloswitcher import XiloSwitcher

def main(page: ft.Page):
    val: int = 0
    stokes = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    xs = XiloSwitcher(
        expand=True,
        controls=[
            ft.Container(expand=True, bgcolor="red"),
            ft.Container(expand=True, bgcolor="orange"),
            ft.Container(expand=True, bgcolor="yellow"),
            ft.Container(expand=True, bgcolor="green"),
            ft.Container(expand=True, bgcolor="blue"),
            ft.Container(expand=True, bgcolor="indigo"),
            ft.Container(expand=True, bgcolor="violet")
        ]
    )

    def next(event):
        nonlocal val, stokes
        if val == 0:
            stokes = True
        elif val == 6:
            stokes = False

        if stokes:
            xs.switch(val + 1)

            val += 1
        else:
            xs.switch(val - 1)

            val -= 1

        page.update()

    page.add(
        xs,
        ft.TextButton("Next", on_click=next)
    )


ft.app(main)
