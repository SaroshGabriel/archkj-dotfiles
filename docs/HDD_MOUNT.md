# NTFS HDD Mount Guide

This guide explains how to permanently mount internal NTFS drives on Arch Linux.

## Step 1 — Find your drive UUIDs

```bash
lsblk -f
```

Note the UUID of each NTFS partition you want to mount.

## Step 2 — Create mount points

```bash
sudo mkdir -p /mnt/HDD1 /mnt/HDD2
```

## Step 3 — Test mount manually first

```bash
sudo mount /dev/sdXN /mnt/HDD1
```

If it works, proceed to fstab.

## Step 4 — Add to /etc/fstab

```bash
echo "UUID=YOUR_UUID_HERE /mnt/HDD1 ntfs-3g defaults,uid=1000,gid=1000,dmask=022,fmask=133,nofail 0 0" | sudo tee -a /etc/fstab
```

Replace `YOUR_UUID_HERE` with the actual UUID from `lsblk -f`.

## Step 5 — Test fstab

```bash
sudo mount -a
```

If no errors, your drives will auto-mount on every boot.

## Notes

- `uid=1000,gid=1000` gives your user read/write access without sudo
- `dmask=022` sets directory permissions to 755
- `fmask=133` sets file permissions to 644
- Install `ntfs-3g` if not already: `sudo pacman -S ntfs-3g`
