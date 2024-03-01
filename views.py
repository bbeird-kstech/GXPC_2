import tkinter as tk
from tkinter import *


class HomeView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text="Home View")
        self.label.pack(fill="both", expand=True)

    def __str__(self):
        return ".!frame2.!homeview" if self.master.winfo_toplevel() == self.master else ""


class EquipmentView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text="Equipment View")
        self.label.pack(fill="both", expand=True)

    def __str__(self):
        return ".!frame2.!equipment" if self.master.winfo_toplevel() == self.master else ""

class MyWindow(tk.Tk):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.right_frame = None
        self.create_user_gui()

        self.home_view = HomeView(self.right_frame)
        self.equipment_view = EquipmentView(self.right_frame)

    def create_user_gui(self):

        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the width and height of the window to make it 80% of the screen size
        app_width = int(screen_width * 0.8)
        app_height = int(screen_height * 0.8)

        # Set the width and height of the window
        self.geometry(f"{app_width}x{app_height}")

        left_frame_width = int(app_width * 0.15)
        right_frame_width = int(app_width * 0.85)

        # Create two frames
        left_frame = tk.Frame(self, bg="red", width=left_frame_width)
        self.right_frame = tk.Frame(self, bg="blue", width=right_frame_width)

        # Set the height of the frames to be the same as the window height
        left_frame_height = app_height
        right_frame_height = app_height

        # Set the geometry of the left frame
        left_frame.grid(row=0, column=0, sticky="ns")
        left_frame.config(height=left_frame_height)

        # Set the geometry of the right frame
        self.right_frame.grid(row=0, column=1, sticky="ns")
        self.right_frame.config(height=right_frame_height)

        # Create and place 5 buttons in the left frame
        button_names = ["Home", "Equipment", "Clients", "Schedule", "Setup"]

        for i, name in enumerate(button_names):
            button = tk.Button(left_frame, text=name, command=lambda i=i: self.controller.handle_button_click(i) )
            # setting the width of the buttons relative to the width of the frame
            button.configure(width = int(left_frame_width / 24))
            # the following craziness positions the buttons relative to the frame size. Seems like there should
            # be a place.center construct but no such luck
            button.place(x=((left_frame_width / 2) - int(left_frame_width / 6)), y=(((left_frame_height / 6) * i) + (left_frame_height / 6)))

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def set_controller(self, controller):
        self.controller = controller

    def on_closing(self):
        self.quit()
        self.destroy()

    def update_right_frame(self, button_index):

        # Hide all views before showing the selected view
        for view in [self.home_view, self.equipment_view]:
            view.pack_forget()

        # Create and display the new content based on the button index
        if button_index == 0:
            self.show_home_view()
        elif button_index == 1:
            self.show_equipment_view()


    def show_home_view(self):
        #self.right_frame.pack_forget()
        self.home_view.pack(fill="both", expand=True)

    def show_equipment_view(self):
        #self.right_frame.pack_forget()
        self.equipment_view.pack(fill="both", expand=True)


def main():
    MyWindow(None)
    root.mainloop()

if __name__ == "__main__":
    main()