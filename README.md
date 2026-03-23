# tsooyts (ցույց) — Show Page Number

Electronic display to show the congregation the current page number.
Also show when it is appropriate to stand, sit, or kneel.  A TV
remote directs the page number on the screen.

![page 142](./docs/screenshots/main_display.png)

Implemented with a Raspberry Pi, 7" touchscreen display, IR receiver,
and a standard TV remote.

## Quick Start

1. Follow the [Installation Guide](docs/installation_guide.md) to assemble
   the hardware, flash the Pi, and deploy the software.
2. After first boot, open the Settings dialog (gear button, lower-right corner)
   and switch to the **Teach** tab to map your TV remote's buttons to functions.
3. See the [User Guide](docs/user_guide.md) for day-to-day operation.
4. If something does not work, see the [Troubleshooting Guide](docs/troubleshooting.md).

## Documentation

| Document | Description |
|----------|-------------|
| [User Guide](docs/user_guide.md) | How to operate the display and remote |
| [Installation Guide](docs/installation_guide.md) | Parts list, hardware assembly, OS setup, service configuration |
| [Troubleshooting Guide](docs/troubleshooting.md) | Diagnosing IR receiver, service, and display problems |

## Installation

```bash
sudo apt install -y python3-pyqt5 python3-evdev
cd /home/pi/Documents
git clone https://github.com/prjemian/tsooyts.git
cd tsooyts
python3 -m venv --system-site-packages .venv
.venv/bin/pip install .
```

The `tsooyts` command is now available at `.venv/bin/tsooyts`.
See the [Installation Guide](docs/installation_guide.md) for full details.

## Source Files

| File | Description |
|------|-------------|
| `src/tsooyts/display.py` | Main Python application (PyQt5 + evdev) |
| `src/tsooyts/icons/*.png` | Posture cue stick-figure icons (stand, sit, kneel) |
| `tsooyts.service` | systemd service unit — copy to `/etc/systemd/system/` |
| `pyproject.toml` | Python packaging configuration |
| `Ararat-and-Khor-Virap.png` | Desktop wallpaper image |
