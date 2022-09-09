from pynput import keyboard as kboard


def on_press(key):
    try:
        print("\nBye")
        quit()
    except AttributeError:
        print("Press 'esq' to quit correctly.")


def on_release(key):
    print("\nBye")
    if key == kboard.Key.esc:
        quit()
