import os
import time

def linux_menu():

    CH = """

    \033[0;34m
    1. Press 1 : Run Linux Command or eneter "exit" to exit from the command line
    Enter 'Exit' to exit from the command line
    2. Press 2 : Create Partition
    3. Press 3 : Create LVM
    4. Press 4 : Check mounted disk
    5. Press 5 : Volume Group List
    6. Press 6 : Yum Configure
    7. Press 7 : To run ifconfig command
    8. Press 8 : To get current date
    9. Press 9 : To get present working directory
    10.Press A : To get memory usage
    11.Press B : To start httpd service
    12.Press C : To list the files and directories
    13.Press D : To create a folder
    14.Press E : To get WLAN IP Address
    15.Press F : To start python 
    16.Press G : To start espeak engine
    17.Press H : To get list of running processes
    18.Press I : To start vim editor
    19.Press J : To get list of all the users
    20.Press K : To get list of all the groups
    21.Press L : To create a new user
    22.Press M : To find process ID of a process
    23.Press N : To kill a process using process ID
    24.Press O : To shutdown the system
    25.Press P : To start live terminal clock
    26.Press Q : To exit
    """


    while True:
        try:
            print("\n\n\t\t\t  Welcome to Linux Menu. How may we help you?")

            os.system("tput setaf 3")

            print(CH)

            a = input("\nEnter your choice: ")
            a = a.upper()
            os.system("tput setaf 3")

            if a == "1":
                while True:
                    command = input("\nInput the command: ")
                    os.system(command)
                    print()
                    if command == "exit":
                        print()
                        break

            elif a == "2":
                os.system("fdisk -l")
                print()
                b = input("\tEnter disk name: ")
                print()
                os.system("fdisk {}".format(b))
                print()
                time.sleep(2)

                print("\n\nFormatting the Partition")
                os.system("mkfs.ext4 {}".format(b))
                print("Successfully Formatted")
                time.sleep(2)

                d = input("\n\n Make Directory for mounting: ")
                os.system("mkdir /{}".format(d))
                print("Directory successfully Created")
                time.sleep(2)

                os.system("\n\nfdisk -l")
                m = input("\t Mount The Directory, Please enter the disk name: ")
                os.system("mount {} {} ".format(m, d))
                print("successfully Mounted")
                time.sleep(2)
                print()

            elif a == "3":
                os.system("\n\nfdisk -l")
                print("Enter the both disks name: ")
                i = input("pvcreate ")
                j = input("pvcreate ")
                os.system("pvcreate {} {}".format(i, j))
                print("Successfully pv created")
                time.sleep(2)

                print("\n\nCreate volume group")
                l = input("Give me group name: ")
                os.system("vgcreate {} {} {}".format(l, i, j))
                print("Successfully volume group created")
                time.sleep(2)

                print("\n\nSet the Size of lv")
                n = input("Size(in GB) -  ")
                o = input("Set Name -")
                os.system("lvcreate --size {}GB --name {} {}".format(n, o, l))
                print("Successfully lv created")
                time.sleep(2)

                print("\n\nFormat the lv")
                os.system("mkfs.ext4 /dev/{}/{}".format(l, o))
                print("Successfully Formatted")
                time.sleep(2)

                print("\n\nBefore the mounting please create Directory")
                p = input("mkdir ")
                os.system("mkdir {}".format(p))
                print("Directory created")
                time.sleep(2)

                print("\n\nMount your Directory")
                os.system("mount /dev/{}/{} /{}".format(l, o, p))
                print("Successfully Mounted please check with df -h command ")
                print("\n Back to the menu")
                print()

            elif a == "4":
                os.system("df -h")
                print()
                input("Hit Enter to Continue")

            elif a == "5":
                os.system("vgdisplay")
                print()
                input("Hit Enter to Continue")
                

            elif a == "6":
                os.system(
                    "yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm"
                )
                print()
                input("Hit Enter to Continue")
                

            elif a == "7":
                os.system("ifconfig")
                print()
                input("Hit Enter to Continue")
                

            elif a == "8":
                os.system("date")
                print()
                input("Hit Enter to Continue")
                
            elif a == "9":
                os.system("pwd")
                print()
                input("Hit Enter to Continue")
                
            elif a == "A":
                os.system("free - m")
                print()
                input("Hit Enter to Continue")
                
            elif a == "B":
                os.system("systemctl start httpd")
                os.system("systemctl status httpd")
                print()
                input("Hit Enter to Continue")
                
            elif a == "C":
                os.system("ls")
                print()
                input("Hit Enter to Continue")
                
            elif a == "D":
                folder_name = input("Enter the folder name: ")
                print()
                os.system(f"mkdir {folder_name}")
                print() 
                input("Hit Enter to Continue")
                
            elif a == "E":
                os.system("ifconfig enp0s3 | grep inet")
                print()
                input("Hit Enter to Continue")
                
            elif a == "F":
                os.system("python&")
                print()
                input("Hit Enter to Continue")
                
            elif a == "G":
                text = input("Enter the text to be spoken by Espeak: ")
                print()
                os.system(f"speak-ng {text}")
                print()
                input("Hit Enter to Continue")
                
            elif a == "H":
                os.system("ps -aux")
                print()
                input("Hit Enter to Continue")
                
            elif a == "I":
                file_name = input("Enter the file name: ")
                print()
                os.system(f"vim {file_name}")
                print()
                input("Hit Enter to Continue")
                
            elif a == "J":
                os.system("cat /etc/passwd")
                print()
                input("Hit Enter to Continue")
                
            elif a == "K":
                os.system("cat /etc/group")
                print()
                input("Hit Enter to Continue")
                
            elif a == "L":
                user_name = input("Enter the user name: ")
                print()
                os.system(f"useradd {user_name}")
                print()
                input("Hit Enter to Continue")
                
            elif a == "M":
                process_name = input("Enter the process name: ")
                print()
                os.system(f"pgrep {process_name}")
                print()
                input("Hit Enter to Continue")
                
            elif a == "N":
                process_id = input("Enter the process id: ")
                print()
                os.system(f"kill {process_id}")
                print()
                input("Hit Enter to Continue")
                
            elif a == "O":
                os.system("shutdown -h now")
                print()
                input("Hit Enter to Continue")
                
            elif a == "P":
                os.system("bash mytime")
                print()
                input("Hit Enter to Continue")
                
            elif a == "Q":
                break
        except Exception as e:
            print(f"Error Occured as {e}")

if __name__ == "__main__":
    linux_menu()