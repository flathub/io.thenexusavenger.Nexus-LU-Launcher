# Nexus LU Launcher Flatpak
Flatpak package for [Nexus LU Launcher](https://github.com/TheNexusAvenger/Nexus-LU-Launcher).

## `make` Commands
- `make` - Downloads the Flatpak build dependencies, builds, and installs the applications.
- `make run` - Runs the application. *Must run `make` first.*
- `make lint` - Checks the Flatpak manifest for issues. *Must run `make` first.*
- `make update-sources` - Regenerates the `nuget-sources.json` file.
- `make clean` - Removes the current build files.
- `make uninstall` - Uninstalls the app.