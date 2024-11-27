<table>
  <tr>
    <td>
      <h1>DecryptorX_Stealer: WSA Startup</h1>
      <p>DecryptorX_Stealer is a powerful cybersecurity tool designed to target and compromise Windows Security Architecture (WSA). It focuses on extracting sensitive information such as Wi-Fi credentials, system passwords, and other private data from Windows systems. Often used by attackers, it exploits vulnerabilities in the startup process, enabling stealthy execution and data theft.</p>
    </td>
    <td style="vertical-align: middle; margin-top: 8px;">
      <img src="https://github.com/UjjwalSaini07/DecryptorX_Stealer/blob/main/ArdiunoCracks/assests/ReadmeAssests/HackerEmoji.png?raw=true" alt="Hacker Emoji">
    </td>
  </tr>
</table>

# C++ Winsock Example: Hostname Resolution

## Features
- **Hostname Resolution**: The program resolves a given hostname (e.g., `www.example.com`) to its corresponding IP address.
- **Windows Sockets (Winsock)**: The program uses the Winsock API to interface with network-related functions and resolve domain names.
- **Error Handling**: The code contains robust error handling using exceptions to catch issues like failure in resolving the hostname or Winsock initialization.
- **Simple IP Address Output**: Once the hostname is resolved, the program outputs the corresponding IP address in the standard dotted-decimal format (e.g., `192.168.1.1`).

## Libraries Used
1. **`<windows.h>`**: 
   - Provides functions for Windows-specific operations, such as network programming with Winsock.
   
2. **`<winsock.h>`**:
   - Defines functions and structures for using the Windows Sockets (Winsock) API, which facilitates communication over the network.
   
3. **`<iostream>`**:
   - Used for input/output operations, such as reading command-line arguments and printing the resolved IP address or errors to the console.
   
4. **`<stdexcept>`**:
   - Includes standard exception classes, such as `runtime_error`, used to handle errors during Winsock initialization or hostname resolution.

## Code Breakdown

1. **`use_WSA` class**:
   - A wrapper class to initialize and clean up Winsock with proper error handling.
   - Constructor (`use_WSA()`) initializes Winsock using `WSAStartup()`, ensuring compatibility with the requested version of Winsock.
   - Destructor (`~use_WSA()`) cleans up Winsock using `WSACleanup()`.

2. **`main()` function**:
   - Takes a hostname as a command-line argument, resolves it using `gethostbyname()`, and prints the corresponding IP address.
   - If there are any issues (such as an invalid hostname or failed Winsock initialization), it catches exceptions and displays appropriate error messages.

## How to Compile and Run
To compile and run the program:
1. Ensure you have a Windows environment with access to the Winsock library.
2. Compile using a C++ compiler (e.g., `g++` or Visual Studio Code) with Winsock linked.
3. Run the executable, passing a valid hostname as a command-line argument.

Example:
```bash
resolve www.example.com
```

## Disclaimer
This tool is intended for educational and security auditing purposes only. Use it responsibly and only on networks you own or have explicit permission to analyze. Unauthorized access to network information is illegal and unethical.
