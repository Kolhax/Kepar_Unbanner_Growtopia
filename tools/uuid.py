import uuid
import winreg

def generate_random_uuid():
    return uuid.uuid4()

def change_uuid_fresh():
    new_uuid = uuid.uuid4()
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_ALL_ACCESS)

    # Set the new UUID value
    winreg.SetValueEx(key, "MachineGuid", 0, winreg.REG_SZ, new_uuid)
    winreg.CloseKey(key)