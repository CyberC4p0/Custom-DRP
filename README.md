# Custom-DRP

This is a custom Discord Rich Presence application built using customtkinter for the GUI and pypresence for interacting with Discord’s Rich Presence API. The application allows you to update your Discord status with custom details, state, and text.

## Features
* **Customizable Presence**: Update your Discord Rich Presence with custom state, details, large image, large text, small image, and small text.
* **System Tray Integration**: Minimize the application to the system tray and restore it when needed.
* **Dynamic Client ID**: Change the client ID on the fly and update the presence accordingly.

## Installation
1. Clone the repository OR [Download]() the EXE File (unsigned):
```
git clone https://github.com/yourusername/discord-rich-presence-app.git
cd discord-rich-presence-app
```

2. Install the required libraries :
```
pip install customtkinter pypresence pystray pillow
```

## Usage
1. Run the application:
```
python app.py
```

2. Fill in the fields:
* **Client ID**: Your Discord application’s client ID.
* **State**: The state to display in your Discord status.
* **Details**: The details to display in your Discord status.
* **Large Image**: The key for the large image asset in your Discord application.
* **Large Text**: The text to display when hovering over the large image.
* **Small Image**: The key for the small image asset in your Discord application.
* **Small Text**: The text to display when hovering over the small image.

3. Update Presence:
* Click the `Update` button to update your Discord Rich Presence with the provided details.

4. Minimize to Tray:
* Close the main window to minimize the application to the system tray.
* Right-click the tray icon to show or quit the application.

## License
This project is licensed under the MIT License.
