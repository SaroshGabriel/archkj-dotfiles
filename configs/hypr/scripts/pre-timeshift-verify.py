#!/usr/bin/env python3
import subprocess
import os
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
report_path = f"/home/KJ/preTimeshiftReports/preTimeshiftReport_{timestamp}.log"

def run(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return result.stdout.strip() or result.stderr.strip() or "OK"
    except:
        return "TIMEOUT/ERROR"

def check_file(path):
    return "✅ EXISTS" if os.path.exists(path) else "❌ MISSING"

report = []
report.append("=" * 60)
report.append(f"PRE-TIMESHIFT VERIFICATION REPORT")
report.append(f"Generated: {datetime.datetime.now()}")
report.append("=" * 60)

report.append("\n[ SYSTEM ]")
report.append(f"Hostname: {run('hostname')}")
report.append(f"Kernel: {run('uname -r')}")
report.append(f"Uptime: {run('uptime -p')}")
report.append(f"Disk Usage: {run('df -h / | tail -1')}")
report.append(f"RAM Usage: {run('free -h | grep Mem')}")
report.append(f"Failed Services: {run('systemctl --failed --no-legend | wc -l')} failed")

report.append("\n[ HYPRLAND ]")
report.append(f"hyprland.conf: {check_file('/home/KJ/.config/hypr/hyprland.conf')}")
report.append(f"hypridle.conf: {check_file('/home/KJ/.config/hypr/hypridle.conf')}")
report.append(f"hyprlock.conf: {check_file('/home/KJ/.config/hyprlock/hyprlock.conf')}")
report.append(f"wallpaper.sh: {check_file('/home/KJ/.config/hypr/wallpaper.sh')}")
report.append(f"Monitors: {run('hyprctl monitors | grep Monitor')}")

report.append("\n[ WAYBAR ]")
report.append(f"config.jsonc: {check_file('/home/KJ/.config/waybar/config.jsonc')}")
report.append(f"style.css: {check_file('/home/KJ/.config/waybar/style.css')}")
report.append(f"netspeed.sh: {check_file('/home/KJ/.config/waybar/netspeed.sh')}")
report.append(f"Waybar running: {'✅ YES' if run('pgrep waybar') else '❌ NO'}")

report.append("\n[ ROFI ]")
report.append(f"cyberpunk.rasi: {check_file('/home/KJ/.config/rofi/cyberpunk.rasi')}")
report.append(f"powermenu.sh: {check_file('/home/KJ/.config/rofi/powermenu.sh')}")

report.append("\n[ SDDM ]")
report.append(f"SDDM enabled: {run('systemctl is-enabled sddm')}")
report.append(f"Theme config: {check_file('/etc/sddm.conf.d/theme.conf')}")
report.append(f"Random bg service: {run('systemctl is-enabled sddm-random-bg')}")

report.append("\n[ SERVICES ]")
report.append(f"NetworkManager: {run('systemctl is-active NetworkManager')}")
report.append(f"Bluetooth: {run('systemctl is-active bluetooth')}")
report.append(f"Cronie: {run('systemctl is-active cronie')}")
report.append(f"Timeshift cron: {run('sudo crontab -l 2>/dev/null | grep timeshift')}")

report.append("\n[ DFT SETUP ]")
report.append(f"DFT folder: {check_file('/home/KJ/Projects/dft')}")
report.append(f"Python venv: {check_file('/home/KJ/Projects/dft/dft-env')}")
report.append(f"dft-fundamentals: {check_file('/home/KJ/Projects/dft/dft-fundamentals')}")
report.append(f"bsr-cell: {check_file('/home/KJ/Projects/dft/bsr-cell')}")
report.append(f"atpg-python-tool: {check_file('/home/KJ/Projects/dft/atpg-python-tool')}")
report.append(f"dft-readiness-checker: {check_file('/home/KJ/Projects/dft/dft-readiness-checker')}")
report.append(f"openroad-dft-flow: {check_file('/home/KJ/Projects/dft/openroad-dft-flow')}")

report.append("\n[ GIT ]")
report.append(f"Git user: {run('git config --global user.name')}")
report.append(f"Git email: {run('git config --global user.email')}")
report.append(f"SSH key: {check_file('/home/KJ/.ssh/id_ed25519')}")
report.append(f"GitHub connection: {run('ssh -T git@github.com 2>&1')}")

report.append("\n[ INSTALLED APPS ]")
apps = ['hyprland', 'waybar', 'kitty', 'brave-bin', 'firefox',
        'spotify', 'telegram-desktop', 'vlc', 'deluge',
        'timeshift', 'btop', 'htop', 'code', 'thunar',
        'libreoffice-fresh', 'whatsapp-for-linux']
for app in apps:
    result = run(f'pacman -Q {app} 2>/dev/null')
    status = f"✅ {result}" if result and 'error' not in result.lower() else "❌ NOT INSTALLED"
    report.append(f"{app}: {status}")

report.append("\n[ WALLPAPERS ]")
report.append(f"Total wallpapers: {run('find /home/KJ/Pictures/Wallpapers -type f | wc -l')}")
report.append(f"awww running: {'✅ YES' if run('pgrep awww') else '❌ NO'}")

report.append("\n" + "=" * 60)
report.append("END OF REPORT")
report.append("=" * 60)

with open(report_path, 'w') as f:
    f.write('\n'.join(report))

print(f"Report saved to: {report_path}")
print('\n'.join(report))
