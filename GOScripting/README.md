# DecryptorX_Stealer - GO_Scripting

Retrieving DNS history directly from a system is not straightforward, as most operating systems don't natively store DNS query history. However, you can use **Go** to query and analyze DNS data in real-time or fetch logs from specific DNS servers or log files.

## How to Setup the Golang:
 - Install Go from Original Website [Download Link](https://go.dev/doc/install)
 - Install it:
   - Windows: Use the installer and follow the prompts.
   - Linux: Extract the tarball and add the Go binary to your PATH
  - Now Verify the Installation done successfully or not..
    - Open a terminal and run:
       ```bash
        go version
        ```
  - Set Up Your Environment
    - Configure the Workspace: By default, Go uses a workspace located in ~/go (Linux) or %USERPROFILE%\go (Windows)
    - Test the Environment: Run
      ```bash
        go env
      ```
  - Now follow How to Run Section for more details.
  - Need Further Guidance of Installing the Golang in Device and setup the environment so refer this documnetation [Link](https://go.dev/doc/).

## How to Run:
1. Run the code:
```bash
go run dns_logger.go
```
2. Now Check the generated dns_history.log file for DNS query results.

## Additionaly :
#### If you're trying to access historical DNS queries already made by the system:

- On Linux, tools like **_dnsmasq_** or **_logs_** in /var/log may help.
- On Windows, you might inspect the DNS cache using PowerShell:
```bash
Get-DnsClientCache
```
To integrate this into Go, you would need to execute system commands and parse the output.
