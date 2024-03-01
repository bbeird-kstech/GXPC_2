
class Menu_Controller:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)


    def handle_button_click(self, button_index):
        # Get the view to update the right frame based on the button clicked
        self.view.update_right_frame(button_index)

    def set_window(self, window):
        self.window = window