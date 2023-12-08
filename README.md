# Blink reminder
## A reminder to blink your eyes every once in a while.

### Requirements
A linux machine, python plyer package installed.

to install plyer - ```pip3 install plyer```

### Step 1
Creating a user mode systemd service file

```
mkdir -p ~/.config/systemd/user/
nano ~/.config/systemd/user/blink-reminder.service
```

### Step 2
Add blink-reminder.service file

```
[Unit]
Description=Blink Reminder Service
After=user.target

[Service]
Type=simple
Restart=no
#ExecStart=python_interpreter_path repo_directory_path [the space is intentional]
ExecStart=/usr/bin/python3 /home/karthikmsd/Code/random/blink-reminder/blink_reminder.py
#environment path for systemd to use plyer library
Environment="PYTHONPATH=/home/karthikmsd/.local/lib/python3.10/site-packages"
WorkingDirectory=/home/karthikmsd/Code/random/blink-reminder/

[Install]
WantedBy=multi-user.target
```

### Step 3
Enable and start the systemd service

```
systemctl --user enable blink-reminder.service
systemctl --user start blink-reminder.service
```

### Step 4
This is intended to run as a daemon along with other systemd service, so to start this at every boot.

```
sudo loginctl enable-linger <linux_username>
systemctl --user daemon-reload
systemctl --user enable blink-reminder.service
systemctl --user start blink-reminder.service
```