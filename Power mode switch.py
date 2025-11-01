import subprocess
import time
import os

GUIDS = {
    "eco": "a1841308-3541-4fab-bc81-f71556f20b4a",
    "perf": "66666666-6666-6666-6666-666666666666"
}

def get_scheme():
    out = subprocess.run(["powercfg", "/getactivescheme"], capture_output=True, text=True).stdout.lower()
    for name, guid in GUIDS.items():
        if guid in out:
            return name
    return "unknown"

def set_scheme(mode):
    os.system(f"powercfg /setactive {GUIDS[mode]}")

mode = get_scheme()

print("\n" + "#" * 50)
if mode == "eco":
    print("ТЕКУЩИЙ РЕЖИМ: ЭКОНОМНЫЙ".center(50))
    set_scheme("perf")
    print("ПЕРЕКЛЮЧЕНО НА: ВЫСОКАЯ ПРОИЗВОДИТЕЛЬНОСТЬ".center(50))
elif mode == "perf":
    print("ТЕКУЩИЙ РЕЖИМ: ВЫСОКАЯ ПРОИЗВОДИТЕЛЬНОСТЬ".center(50))
    set_scheme("eco")
    print("ПЕРЕКЛЮЧЕНО НА: ЭКОНОМНЫЙ".center(50))
else:
    print("НЕ УДАЛОСЬ ОПРЕДЕЛИТЬ ТЕКУЩИЙ РЕЖИМ".center(50))
print("#" * 50 + "\n")

time.sleep(3)
