import json
import os

PASSWORD_FILE = "passwords.json"

def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def save_passwords(passwords):
    with open(PASSWORD_FILE, "w", encoding="utf-8") as file:
        json.dump(passwords, file, indent=4)

def add_password(website, username, password):
    passwords = load_passwords()
    passwords[website] = {"username": username, "password": password}
    save_passwords(passwords)
    print(f"{website} 的密码已成功保存！")

def view_passwords():
    passwords = load_passwords()
    if passwords:
        for website, credentials in passwords.items():
            print(f"\n网站: {website}")
            print(f"用户名: {credentials['username']}")
            print(f"密码: {credentials['password']}")
    else:
        print("没有保存的密码。")

if __name__ == "__main__":
    print("欢迎使用密码管理器！")
    
    while True:
        print("\n请选择一个操作：")
        print("1. 添加密码")
        print("2. 查看密码")
        print("3. 退出")
        
        choice = input("请输入选项（1/2/3）：")
        
        if choice == "1":
            website = input("请输入网站名称：")
            username = input("请输入用户名：")
            password = input("请输入密码：")
            add_password(website, username, password)
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("感谢使用密码管理器，再见！")
            break
        else:
            print("无效选项，请重新选择。")
