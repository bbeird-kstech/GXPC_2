import tkinter as tk
from views import MyWindow
from controllers import Menu_Controller


def main():
    root = tk.Tk()
    root.withdraw()

    controller = Menu_Controller(None)
    window = MyWindow(controller=controller)
    controller.set_view(view=window)
    root.mainloop()


if __name__ == "__main__":
    main()
