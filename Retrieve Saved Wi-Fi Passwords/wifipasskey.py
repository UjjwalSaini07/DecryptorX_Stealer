import subprocess
import re
from datetime import datetime

def get_wifi_profiles():
    try:
        # Run command to get saved Wi-Fi profiles
        command = "netsh wlan show profiles"
        profiles_output = subprocess.check_output(command, shell=True, text=True)
        
        # Extract profile names
        profiles = re.findall(r"All User Profile\s*:\s*(.*)", profiles_output)
        wifi_details = []
        
        for profile in profiles:
            profile_info = {"SSID": profile.strip()}
            
            # Get profile details
            profile_command = f'netsh wlan show profile name="{profile.strip()}" key=clear'
            profile_output = subprocess.check_output(profile_command, shell=True, text=True)
            
            # Extract details like Authentication and Key Content
            auth_match = re.search(r"Authentication\s*:\s*(.*)", profile_output)
            key_match = re.search(r"Key Content\s*:\s*(.*)", profile_output)
            
            profile_info["Authentication"] = auth_match.group(1) if auth_match else "N/A"
            profile_info["Password"] = key_match.group(1) if key_match else "N/A"
            
            # Add timestamp
            profile_info["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            wifi_details.append(profile_info)
        
        return wifi_details
    
    except subprocess.CalledProcessError as e:
        print(f"Error while retrieving Wi-Fi profiles: {e}")
        return []

# Call the function and display Wi-Fi details
wifi_profiles = get_wifi_profiles()
for wifi in wifi_profiles:
    print(wifi)
