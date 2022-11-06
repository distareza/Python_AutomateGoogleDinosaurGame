import pynput


def get_coord(x, y, button, pressed):
    print(f"({x}, {y}) {button} {pressed}")

with pynput.mouse.Listener(on_click=get_coord) as listen:
    listen.join()
