import tkinter as tk
from views import MyWindow
from controllers import Menu_Controller


def main():
    root = tk.Tk()
    root.withdraw()

    window = MyWindow()
    controller = Menu_Controller(window)

    window.set_controller(controller)

    root.mainloop()

if __name__ == "__main__":
    main()
