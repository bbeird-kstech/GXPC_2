import tkinter as tk


class EquipmentView(tk.Frame):
    def __init__(self, parent, equipment_owners, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text="Select Equipment Owner:")
        self.label.pack(fill="both", expand=True)

        # Create a dropdown list of equipment owners
        self.equipment_owners = tk.StringVar()
        self.equipment_owners.set("Choose an equipment owner")  # default value
        self.equipment_owner_dropdown = tk.OptionMenu(self, self.equipment_owners,
                                                      *[equipment_owner.client_name for equipment_owner in
                                                        equipment_owners])
        self.equipment_owner_dropdown.pack()

    def __str__(self):
        return ".!frame2.!equipment" if self.master.winfo_toplevel() == self.master else ""

    def update_dropdown(self, owners):
        menu = self.dropdown["menu"]
        menu.delete(0, "end")
        for owner in owners:
            menu.add_command(label=owner.client_name, command=lambda: self.owner_var.set(owner.client_name))