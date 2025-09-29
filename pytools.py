import qrcode
import pyfiglet
from pathlib import Path
import shutil
import psutil
import platform
from datetime import datetime
import requests

def qr_code(): #qr code
    data = input("Enter text or URL to generate QR code: ")
    qr_img = qrcode.make(data)
    qr_img.save("my_qr.png")
    print("QR Code saved as my_qr.png")

def file_organiser(): #file organizer
    user_input = input("Enter the folder path to organize: ").strip()
    folder = Path(user_input)

    if not folder.exists() or not folder.is_dir():
        print(" Error: The path you entered is not a valid folder.")
        return

    thing = {
        ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images",
        ".bmp": "Images", ".tiff": "Images", ".svg": "Images", ".heic": "Images",
        ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
        ".xls": "Documents", ".xlsx": "Documents", ".ppt": "Documents",
        ".pptx": "Documents", ".odt": "Documents", ".rtf": "Documents",
        ".csv": "Documents", ".md": "Documents", ".txt": "Documents",
        ".html": "WebFiles", ".css": "WebFiles", ".js": "WebFiles",
        ".ts": "WebFiles", ".jsx": "WebFiles", ".tsx": "WebFiles",
        ".json": "WebFiles", ".xml": "WebFiles",
        ".py": "Code", ".java": "Code", ".c": "Code", ".cpp": "Code",
        ".cs": "Code", ".php": "Code", ".rb": "Code", ".go": "Code",
        ".rs": "Code", ".swift": "Code",
        ".mp3": "Audio", ".wav": "Audio", ".aac": "Audio",
        ".flac": "Audio", ".ogg": "Audio", ".m4a": "Audio",
        ".mp4": "Video", ".mkv": "Video", ".mov": "Video",
        ".avi": "Video", ".wmv": "Video", ".flv": "Video", ".webm": "Video",
        ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
        ".tar": "Archives", ".gz": "Archives", ".bz2": "Archives",
        ".exe": "Executables", ".msi": "Executables",
        ".dmg": "Executables", ".pkg": "Executables",
        ".sh": "Executables", ".bat": "Executables"
    }

    print("Organizing files...")
    for item in folder.iterdir():
        if item.is_file():
            try:
                ext = item.suffix.lower()
                category = thing.get(ext, "Unknown")
                target_folder = folder / category
                target_folder.mkdir(exist_ok=True)
                target_path = target_folder / item.name
                shutil.move(str(item), str(target_path))
                print(f" Moved {item.name} → {category}")
            except Exception as e:
                print(f" Could not move {item.name}: {e}")
    print(" Organizing complete!")

def ascii(): #asciii
    text = input("Enter text to turn into ASCII art: ")
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

def pc_stats(): #pc stats
    print("\nSystem Information\n")

    uname = platform.uname()
    print(f"System: {uname.system} {uname.release}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print(f"Node Name: {uname.node}")

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    print(f"Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")

    print("\n Memory Info")
    svmem = psutil.virtual_memory()
    print(f"Total: {svmem.total // (1024**3)} GB")
    print(f"Available: {svmem.available // (1024**3)} GB")
    print(f"Used: {svmem.used // (1024**3)} GB ({svmem.percent}%)")

    print("\n Disk Info")
    partitions = psutil.disk_partitions()
    for part in partitions:
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(f"{part.device} - {usage.used // (1024**3)}GB / {usage.total // (1024**3)}GB ({usage.percent}%)")
        except PermissionError:
            continue

    print("\n CPU Info")
    print(f"Cores: {psutil.cpu_count(logical=False)}")
    print(f"Threads: {psutil.cpu_count(logical=True)}")
    print(f"Usage: {psutil.cpu_percent(interval=1)}%")

def currency_converter():
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (e.g., USD, INR, EUR): ").upper()
    to_curr = input("To currency (e.g., USD, INR, EUR): ").upper()
    url=f"https://api.exchangerate.host/convert?from={from_curr}&to={to_curr}&amount={amount}"
    try:
        response=requests.get(url)
        if response.status_code == 200:
            data=response.json()
            result=data.get("result")
            if result:
                print(f"\n{amount} {from_curr} = {result:.2f} {to_curr}\n")
            else:
                print("Conversion error.")
        else:
            print("API error.")
    except Exception as e:
        print(f"Error: {e}")               

#main handle
pop="Hello!"
ascii_art = pyfiglet.figlet_format(pop)
print(ascii_art)
while True:
    print("Welcome to Pytools-Choose an option:")
    print("1 - QR Generator")
    print("2 - File Organiser")
    print("3 - PC Stats")
    print("4 - ASCII Art Converter")
    print("5 - Currency Conversion")
    print("00 - Exit")
    choice = input("Enter Your Option: ").strip()
    if choice == "00":
        break
    elif choice == "1":
        qr_code()
    elif choice == "2":
        file_organiser()
    elif choice== "3":
        pc_stats()
    elif choice == "4":
        ascii()
    elif choice=="5":
        currency_converter()
    else:
        print("Enter a valid choice")
#abd700ce70a6c5a96e87372b78261c73

