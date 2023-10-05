import platform
import linux_menu
import windos_menu

def get_system():
    return platform.system()


def show_menu(sys_name):
    if sys_name == "Linux":
        print("Auto-Detected: You are on Linux System \n")
        linux_menu.linux_menu()
        
    elif sys_name == "Windows":
        print("Auto-Detected: You are on Windows System \n")
        windos_menu.windows_menu()
    else:
        "This system is not supported yet! We are working on it!"

system_name = get_system()
show_menu(system_name)

