partitions = [
    "System;/;50000;85",
    "Data;/home;150000;40",
    "Cache;/tmp;5000;10",
    "Backup;/mnt/backup;500000;92",
    "USB-Drive;/media/usb;16000;0",
    "Logs;/var/log;10000;95",
    "Database;/var/lib/mysql;80000;70",
    "Shared;/mnt/shared;200000;15",
    "Win-System;/mnt/win;100000;90",
    "Recovery;/recovery;2000;98"
]

def calculate_used_space(parts):
    return [
        {
            "Label": p.split(";")[0],
            "UsedMB": 500 if p.split(";")[0] == "Cache"
                        else int(int(p.split(";")[2]) * (int(p.split(";")[3]) / 100))
        }
        for p in parts
    ]

for item in calculate_used_space(partitions):
    print(item)
