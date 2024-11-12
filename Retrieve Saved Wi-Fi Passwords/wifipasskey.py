import subprocess

def get_wifi_passwords():
    try:
        # Get a list of saved Wi-Fi profiles
        profiles_data = subprocess.check_output("netsh wlan show profiles", shell=True, encoding='utf-8')
        profiles = [line.split(":")[1].strip() for line in profiles_data.splitlines() if "All User Profile" in line]

        wifi_credentials = {}
        for profile in profiles:
            # Get the password for each profile
            try:
                profile_info = subprocess.check_output(f"netsh wlan show profile name=\"{profile}\" key=clear", shell=True, encoding='utf-8')
                password_line = [line.split(":")[1].strip() for line in profile_info.splitlines() if "Key Content" in line]
                
                # Store profile and password if available
                wifi_credentials[profile] = password_line[0] if password_line else None
            except subprocess.CalledProcessError:
                wifi_credentials[profile] = None

        return wifi_credentials

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    wifi_passwords = get_wifi_passwords()
    for wifi, password in wifi_passwords.items():
        print(f"Wi-Fi: {wifi}, Password: {password or 'No password saved'}")
