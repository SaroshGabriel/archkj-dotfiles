# archkj-dotfiles

> 🔴 KJ's Arch Linux + Hyprland system — clone and replicate in one script.

![Arch Linux](https://img.shields.io/badge/Arch_Linux-1793D1?style=flat&logo=arch-linux&logoColor=white)
![Hyprland](https://img.shields.io/badge/Hyprland-58E1FF?style=flat)
![Waybar](https://img.shields.io/badge/Waybar-EF3946?style=flat)

---

## What's included

| Category | Details |
|---|---|
| **WM** | Hyprland 0.54+ with dual-monitor workspace system |
| **Bar** | Waybar — netspeed, media, VPN-ready, custom modules |
| **Launcher** | Rofi with cyberpunk red/pink theme |
| **Terminal** | Kitty with JetBrains Mono Nerd Font, cyberpunk colors |
| **Shell** | Bash with magenta prompt, useful aliases |
| **Wallpapers** | 100+ wallpapers with random rotation every 5 min (awww) |
| **Lock screen** | Hyprlock with custom cyberpunk theme |
| **Clipboard** | cliphist + wl-clipboard (Super+V to open history) |
| **Auto-mount** | udiskie for USB drives, ntfs-3g for NTFS HDDs |
| **VPN** | ProtonVPN CLI ready |
| **Backups** | Timeshift daily snapshots via cron |

---

## Theme

**Cyberpunk Red/Pink Neon**
- Background: `#32111C`
- Accent: `#EF3946`
- Font: JetBrainsMono Nerd Font

---

## Installation

### Requirements
- Fresh Arch Linux install (base system, internet working)
- A normal user with sudo access
- At least 10GB free disk space

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/SaroshGabriel/archkj-dotfiles.git
cd archkj-dotfiles

# 2. Make install script executable
chmod +x install.sh

# 3. Run it
bash install.sh
```

The script will:
- Install all pacman and AUR packages
- Copy all dotfiles to the right locations
- Copy wallpapers to ~/Pictures/Wallpapers
- Enable required services (NetworkManager, bluetooth, SDDM, cronie)
- Set up Timeshift daily auto-snapshots
- Back up any existing configs before overwriting

### After install

1. **Reboot** your system
2. At the SDDM login screen, **select Hyprland**
3. Sign in to ProtonVPN: `protonvpn signin <your_email>`
4. Set up Git: `git config --global user.name "YourName" && git config --global user.email "you@email.com"`
5. If you have NTFS drives, see [docs/HDD_MOUNT.md](docs/HDD_MOUNT.md)

---

## Keybinds

| Key | Action |
|---|---|
| `Super + Enter` | Open Kitty terminal |
| `Super + V` | Open clipboard history |
| `Super + W` | Restart Waybar |
| `Print Screen` | Screenshot (Spectacle) |
| `Super + Q` | Close window |

---

## Repo Structure

```
archkj-dotfiles/
├── install.sh              ← Run this
├── README.md
├── configs/
│   ├── hypr/               ← Hyprland config + wallpaper script
│   ├── waybar/             ← Waybar config + netspeed script
│   ├── rofi/               ← Rofi launcher theme
│   ├── kitty/              ← Kitty terminal config
│   ├── hyprlock/           ← Lock screen config
│   └── bashrc              ← Shell config
├── wallpapers/             ← All wallpapers
└── docs/
    └── HDD_MOUNT.md        ← NTFS drive mount guide
```

---

## Notes

- Wallpapers rotate randomly every 5 minutes across both monitors
- The install script backs up your existing configs before overwriting
- HDD/partition mounts are **not** automated — they're machine-specific (see docs)
- ProtonVPN credentials are **not** stored in this repo

---

## Credits

Built and maintained by [SaroshGabriel](https://github.com/SaroshGabriel)
