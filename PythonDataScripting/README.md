<table>
  <tr>
    <td>
      <h1>DecryptorX_Stealer: PassKey Retrieval</h1>
      <p>DecryptorX- PassKey Retrieval is a cybersecurity tool for password recovery, protocol analysis. It focuses on Wi-Fi credential extraction, helping professionals identify network weaknesses and security flaws, especially in Windows environments. DecryptorX aids penetration testing, vulnerability assessments, and improving network security.</p>
    </td>
    <td style="vertical-align: middle; margin-top: 8px;">
      <img src="https://github.com/UjjwalSaini07/DecryptorX_Stealer/blob/main/ArdiunoCracks/assests/ReadmeAssests/HackerEmoji.png?raw=true" alt="Hacker Emoji">
    </td>
  </tr>
</table>


## Features

- **Wi-Fi Profile Retrieval**: Extracts stored Wi-Fi profiles and their associated information from the system.
- **Password Cracking**: Retrieves Wi-Fi passwords from the stored profiles, if available.
- **Support for Various Protocols**: Focuses on breaking various network protocols for security testing purposes.
- **Colorful Output**: Displays the results in a clean, readable format with color-coded output for better visualization.
- **System Compatibility**: Works on Windows-based systems, utilizing the `netsh` command to interact with network settings.

## Libraries Used

- **subprocess**: Executes system commands to retrieve network information.
- **os**: Handles system-level interactions (though not explicitly used in this script).
- **time**: Introduces delays in script execution for better user experience.
- **colorama**: Provides colorful terminal output to enhance readability.
- **psutil**: Library is used to find accurate hardware details.

## Requirements

To run this script, you need the following Python library:

- `colorama` for terminal color formatting. Install it using:
  
  ```bash
  pip install colorama
  ```
- `psutil` This library is used for accurate hardware details like CPU core count and total RAM. Install it using:
  
  ```bash
  pip install psutil
  ```

## Disclaimer
This tool is intended for educational and security auditing purposes only. Use it responsibly and only on networks you own or have explicit permission to analyze. Unauthorized access to network information is illegal and unethical.
