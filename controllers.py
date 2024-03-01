
from sqlalchemy.orm import sessionmaker
from database import session

class Menu_Controller:
    def __init__(self, view=None):
        self.view = view
        self.view.set_controller(self)

        if self.view:
            self.view.set_controller(self)

    def handle_button_click(self, button_index):
        # Get the view to update the right frame based on the button clicked
        self.view.update_right_frame(button_index)

    def update_equipment_dropdown(self):
        equipment_owners = session.query(EquipmentOwner).all()
        owner_names = [owner.client_name for owner in equipment_owners]
        self.view.update_equipment_dropdown(owner_names)

    def set_window(self, window):
        self.window = window