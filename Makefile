build:
	flatpak install -y org.freedesktop.Sdk//24.08 org.freedesktop.Platform//24.08 org.freedesktop.Sdk.Compat.i386/x86_64/24.08 org.winehq.Wine/x86_64/stable-24.08 org.freedesktop.Sdk.Extension.dotnet9//24.08
	flatpak-builder --ccache --force-clean build-dir io.thenexusavenger.Nexus-LU-Launcher.yml
	flatpak-builder --force-clean --user --install build-dir io.thenexusavenger.Nexus-LU-Launcher.yml
run:
	flatpak run io.thenexusavenger.Nexus-LU-Launcher
lint:
	flatpak install -y flathub org.flatpak.Builder
	flatpak run --command=flatpak-builder-lint org.flatpak.Builder manifest io.thenexusavenger.Nexus-LU-Launcher.yml
update-sources:
	python3 ./update-sources.py
clean:
	rm -rf .flatpak-builder
	rm -rf build-dir
uninstall:
	flatpak remove io.thenexusavenger.Nexus-LU-Launcher --delete-data

.PHONY: build run lint clean uninstall