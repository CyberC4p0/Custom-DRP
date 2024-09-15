import customtkinter as ctk
from pypresence import Presence
import pystray
from PIL import Image, ImageDraw

class DiscordRichPresenceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Discord Rich Presence")
        self.geometry("350x600") 

        self.rpc = None
        self.current_client_id = None

        self.client_id_label = ctk.CTkLabel(self, text="Client ID")
        self.client_id_label.pack(pady=5)
        self.client_id_entry = ctk.CTkEntry(self, width=300)
        self.client_id_entry.pack(pady=5)

        self.state_label = ctk.CTkLabel(self, text="State")
        self.state_label.pack(pady=5)
        self.state_entry = ctk.CTkEntry(self, width=300)
        self.state_entry.pack(pady=5)

        self.details_label = ctk.CTkLabel(self, text="Details")
        self.details_label.pack(pady=5)
        self.details_entry = ctk.CTkEntry(self, width=300)
        self.details_entry.pack(pady=5)

        self.large_image_label = ctk.CTkLabel(self, text="Large Image")
        self.large_image_label.pack(pady=5)
        self.large_image_entry = ctk.CTkEntry(self, width=300)
        self.large_image_entry.pack(pady=5)

        self.large_text_label = ctk.CTkLabel(self, text="Large Text")
        self.large_text_label.pack(pady=5)
        self.large_text_entry = ctk.CTkEntry(self, width=300)
        self.large_text_entry.pack(pady=5)

        self.small_image_label = ctk.CTkLabel(self, text="Small Image")
        self.small_image_label.pack(pady=5)
        self.small_image_entry = ctk.CTkEntry(self, width=300)
        self.small_image_entry.pack(pady=5)

        self.small_text_label = ctk.CTkLabel(self, text="Small Text")
        self.small_text_label.pack(pady=5)
        self.small_text_entry = ctk.CTkEntry(self, width=300)
        self.small_text_entry.pack(pady=5)

        self.update_button = ctk.CTkButton(self, text="Update", command=self.update_presence)
        self.update_button.pack(pady=5)

        self.protocol("WM_DELETE_WINDOW", self.minimize_to_tray)

    def update_presence(self):
        client_id = self.client_id_entry.get()
        state = self.state_entry.get()
        details = self.details_entry.get()
        large_image = self.large_image_entry.get()
        large_text = self.large_text_entry.get()
        small_image = self.small_image_entry.get()
        small_text = self.small_text_entry.get()

        if self.rpc is None or self.current_client_id != client_id:
            self.rpc = Presence(client_id)
            self.rpc.connect()
            self.current_client_id = client_id

        update_data = {}
        if state:
            update_data['state'] = state
        if details:
            update_data['details'] = details
        if large_image:
            update_data['large_image'] = large_image
        if large_text:
            update_data['large_text'] = large_text
        if small_image:
            update_data['small_image'] = small_image
        if small_text:
            update_data['small_text'] = small_text

        self.rpc.update(**update_data)

    def minimize_to_tray(self):
        self.withdraw()
        image = Image.new('RGB', (64, 64), color=(73, 109, 137))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, 64, 64), fill=(73, 109, 137))
        menu = (pystray.MenuItem('Quit', self.quit_window), pystray.MenuItem('Show', self.show_window))
        self.icon = pystray.Icon("name", image, "Discord Rich Presence", menu)
        self.icon.run()

    def quit_window(self, icon, item):
        self.icon.stop()
        self.destroy()

    def show_window(self, icon, item):
        self.icon.stop()
        self.after(0, self.deiconify)

def run_app():
    app = DiscordRichPresenceApp()
    app.mainloop()

if __name__ == "__main__":
    run_app()
