"""
TheNexusAvenger

Updates the NuGet sources
"""

import os
import re
import subprocess
import urllib.request

# Get the freedesktop version, .NET version, and commit.
with open("io.thenexusavenger.Nexus-LU-Launcher.yml", encoding="utf8") as file:
    fileContents = file.read()
    freedesktopVersion = re.findall(r"runtime-version: '([^']+)", fileContents)[0]
    dotnetVersion = re.findall(r"dotnet(\d+)", fileContents)[0]
    commit = re.findall(r"commit: ([\dabcdef]+)", fileContents)[0]

# Prepare the directory for downloading files.
buildDir = os.path.join(os.path.dirname(__file__), "build-dir")
if not os.path.exists(buildDir):
    os.makedirs(buildDir)

# Download the generator script.
generatorFilePath = os.path.join(buildDir, "flatpak-dotnet-generator.py")
if not os.path.exists(generatorFilePath):
    print("Downloading NuGet sources generator script.")
    response = urllib.request.urlopen("https://raw.githubusercontent.com/flatpak/flatpak-builder-tools/master/dotnet/flatpak-dotnet-generator.py")
    with open(generatorFilePath, "wb") as file:
        file.write(response.read())

# Clone the repository.
repositoryPath = os.path.join(buildDir, "Nexus-LU-Launcher-" + commit)
if not os.path.exists(repositoryPath):
    print("Fetching GitHub repository from commit " + commit)
    os.mkdir(repositoryPath)
    subprocess.Popen(["git", "clone", "https://github.com/TheNexusAvenger/Nexus-LU-Launcher.git", repositoryPath]).wait()
    subprocess.Popen(["git", "reset", "--hard", commit], cwd=repositoryPath).wait()

# Run the script.
subprocess.Popen(["python3", generatorFilePath, "nuget-sources.json", os.path.join(repositoryPath, "Nexus.LU.Launcher.Gui", "Nexus.LU.Launcher.Gui.csproj"), "--freedesktop", freedesktopVersion, "--dotnet", dotnetVersion, "--runtime", "linux-x64"]).wait()