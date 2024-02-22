# Scripts Repository

A collection of bash scripts for various file conversion and system update tasks.

## Table of Contents

- [Description](#description)
- [Scripts](#scripts)
  - [convert](#convert)
  - [tmux_ref](#tmux_ref)
  - [update-debian](#update-debian)
  - [update-fedora](#update-fedora)
  - [upinst](#upinst)
- [Contributing](#contributing)
- [License](#license)

## Description
This repository contains a set of bash scripts designed for different tasks. The scripts include video file conversion, system updates for Debian and Fedora, and a versatile script for installing and managing Debian-based systems.

## Scripts

### convert
`convert` is a script with service menu for converting media files. Anything you might need for your videos and subtitles.

### tmux_ref
`tmux_ref` is a bash script that serves as a quick reference guide for using tmux, a terminal multiplexer. It provides concise commands and tips for basic tmux operations, managing windows and panes, session management, and miscellaneous tasks. Customize your tmux experience with this handy script!

### update-debian
`update-debian` is a prompted update script for Debian systems.

### update-fedora
`update-fedora` is a prompted update script for Fedora systems.

### upinst
`upinst` is a bash script with options for installing, updating, and managing Debian-based systems.


***Usage Examples:***
```bash
# Install a package
sudo ./upinst -i package_name

# Check for updates
sudo ./upinst -u

# Upgrade system
sudo ./upinst -U

# Uninstall a package
sudo ./upinst -r package_name

# Reboot system
sudo ./upinst -R

# Show interactive menu
sudo ./upinst -m

# Display help
sudo ./upinst -h
```

## Contributing

If you have improvements, bug fixes, or new scripts to contribute, feel free to open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
