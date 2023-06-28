import winreg

def modify_usbstor_registry():
    # Открываем раздел реестра для USBSTOR
    usbstor_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0, winreg.KEY_SET_VALUE)

    # Изменяем нужные значения
    # Устанавливаем значение Start на 3 (Enabled), на 4 (Disabled)
    winreg.SetValueEx(usbstor_key, "Start", 0, winreg.REG_DWORD, 3)
    
    # Закрываем раздел реестра
    winreg.CloseKey(usbstor_key)

# Вызываем функцию для внесения изменений
modify_usbstor_registry()
