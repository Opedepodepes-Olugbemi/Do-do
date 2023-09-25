import reflex as rx


def index():
  return rx.text('Oba ni Jesu')


app = rx.App()
app.add_page(index)
app.compile()