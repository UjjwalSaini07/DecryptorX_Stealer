# DecryptorX_Stealer - GO_Scripting

Retrieving DNS history directly from a system is not straightforward, as most operating systems don't natively store DNS query history. However, you can use **Go** to query and analyze DNS data in real-time or fetch logs from specific DNS servers or log files.

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
