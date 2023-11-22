from PyQt6.QtCore import QDir, QSettings, QStandardPaths
from PyQt6.QtWidgets import QApplication

def get_all_apps():
    # Get the list of directories where desktop files are typically stored ApplicationsLocation
    desktop_entry_dirs = QStandardPaths.standardLocations(QStandardPaths.StandardLocation.ApplicationsLocation)

    all_apps = []

    for dir_path in desktop_entry_dirs:
        # Iterate through all desktop files in the directory
        dir = QDir(dir_path)
        name_filters = ['*.desktop']
        entries = dir.entryInfoList(name_filters)

        for entry in entries:
            desktop_file_path = entry.filePath()

            # Use QSettings to read the desktop file
            settings = QSettings(desktop_file_path, QSettings.Format.IniFormat)
            settings.beginGroup("Desktop Entry")

            # Retrieve relevant information from the desktop file
            display_name = settings.value("Name")
            description = settings.value("Comment")

            settings.endGroup()

            # Create a dictionary with application information
            app_info = {
                'display_name': display_name,
                'description': description
            }

            all_apps.append(app_info)

    return all_apps

if __name__ == "__main__":
    app = QApplication([])

    all_apps = get_all_apps()

    # For example, print display name and description of all apps
    for app_info in all_apps:
        print(app_info['display_name'])
        print(f"\t{app_info['description']}")
