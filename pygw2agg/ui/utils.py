from PySimpleGUI import Window


def simple_extend_element(window: Window, element):
    window.extend_layout(
        window,
        [[element]],
    )
    window.refresh()


def remove_element(window: Window, key: str):
    window[key].update(visible=False)
    window[key].Widget.master.pack_forget()
