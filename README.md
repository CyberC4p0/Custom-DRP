# Custom-DRP

This is a custom Discord Rich Presence application built using customtkinter for the GUI and pypresence for interacting with Discord’s Rich Presence API. The application allows you to update your Discord status with custom details, state, and text.

## Features
* **Customizable Presence**: Update your Discord Rich Presence with custom state, details, large image, large text, small image, and small text.
* **System Tray Integration**: Minimize the application to the system tray and restore it when needed.
* **Dynamic Client ID**: Change the client ID on the fly and update the presence accordingly.

## Discord Developer Portal

### 1. Create a Discord Developer Account:
* Visit the Discord Developer Portal.
* Log in with your Discord account or create a new one if you don’t have an account.

### 2. Create a New Application:
* Click on the “New Application” button.
* Enter a name for your application and click “Create”.

### 3. Configure Application Settings:
* General Information: Fill in the necessary details such as the application’s description, icon, and tags.
* Rich Presence: Scroll to the bottom and add assets (images) that you will use for the large and small images in your script under “Rich Presence Assets”.

### 4. Copy the Application ID:
* Go to the “General Information” section and copy the application ID.

### 5. Set Up Your Application:
* Open your application and navigate to the section where you can enter the Discord Application Token.
* Paste the application ID you copied earlier into the appropriate field.

### 6. Configure Image Names:
* In your application, enter the names of the images you uploaded to the assets section in the corresponding fields for large and small images. Remember, the names are case-sensitive and should not include file extensions.

### 7. Apply and Test:
* Hit “Apply” and give it a moment. Your application should now display the images you set in Discord.

## Installation
### 1. Clone the repository OR [Download]() the EXE File (unsigned):
```
git clone https://github.com/yourusername/discord-rich-presence-app.git
cd discord-rich-presence-app
```

### 2. Install the required libraries :
```
pip install customtkinter pypresence pystray pillow
```

## Usage
### 1. Run the application:
```
python app.py
```

### 2. Fill in the fields:
* **Client ID**: Your Discord application’s client ID.
* **State**: The state to display in your Discord status.
* **Details**: The details to display in your Discord status.
* **Large Image**: The key for the large image asset in your Discord application.
* **Large Text**: The text to display when hovering over the large image.
* **Small Image**: The key for the small image asset in your Discord application.
* **Small Text**: The text to display when hovering over the small image.

### 3. Update Presence:
* Click the `Update` button to update your Discord Rich Presence with the provided details.

### 4. Minimize to Tray:
* Close the main window to minimize the application to the system tray.
* Right-click the tray icon to show or quit the application.

## License
This project is licensed under the MIT License.
