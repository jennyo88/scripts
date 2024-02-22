# Scripts Repository

A collection of bash scripts for various file conversion and system update tasks.

## Table of Contents

- [Description](#description)
- [Scripts](#scripts)
  - [cfiles](#cfiles)
  - [script](#script)
  - [update-debian](#update-debian)
  - [update-fedora](#update-fedora)
  - [upinst](#upinst)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description
This repository contains a set of bash scripts designed for different tasks. The scripts include video file conversion, system updates for Debian and Fedora, and a versatile script for installing and managing Debian-based systems.

## Scripts

### cfiles

**Description:**
A bash script for converting video files using ffmpeg.

**Usage:**
```bash
./cfiles
```

### script

**Description:**
A bash script for performing system updates on Debian-based systems.

**Usage:**
```bash
./script
```

### update-debian

**Description:**
A prompted update script for Debian systems.

**Usage:**
```bash
sudo ./update-debian
```

**Options:**

`-h` or `--help`: Display usage information.

### update-fedora

**Description:**
A prompted update script for Fedora systems.

**Usage:**
```bash
sudo ./update-fedora
```

**Options:**

`-h` or `--help`: Display usage information.


### upinst

**Description:**
A bash script with options for installing, updating, and managing Debian-based systems.

**Usage:**
```bash
sudo ./upinst [options]
```

**Options:**

`-i`: Install
`-u`: Update check
`-U`: Upgrade
`-r`: Uninstall
`-R`: Reboot
`-m`: Show interactive menu
`-h`: Show help

**Usage Examples:**
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

## Usage
Refer to each script's individual section for specific usage instructions.
Make sure to check the respective scripts for details on how to use them effectively.

## Contributing

If you have improvements, bug fixes, or new scripts to contribute, feel free to open a pull request.

## License

This project is licensed under the [MIT License] - see the [LICENSE.md](LICENSE.md) file for details.

MIT License:
```
Copyright (c) 2024 Jennifer Romero

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
