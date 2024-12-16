package main

import (
	"fmt"
	"log"
	"net"
	"os"
	"time"
)

// Function to perform a DNS lookup
func lookupDNS(domain string) {
	// Get the current time
	timestamp := time.Now().Format("2006-01-02 15:04:05")

	// Perform DNS lookup
	ips, err := net.LookupIP(domain)
	if err != nil {
		log.Printf("[%s] Failed to lookup DNS for %s: %v\n", timestamp, domain, err)
		return
	}

	// Log DNS lookup details
	for _, ip := range ips {
		log.Printf("[%s] Domain: %s -> IP: %s\n", timestamp, domain, ip.String())
	}
}

func main() {
	// Create a log file
	file, err := os.OpenFile("dns_history.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Printf("Failed to create log file: %v\n", err)
		return
	}
	
	defer file.Close()

	// Set log output to the file
	log.SetOutput(file)

	// Define domains to lookup
	domains := []string{
		"google.com",
		"github.com",
		"openai.com",
		"linkedin.com",
	}

	// Perform DNS lookups and log the results
	for _, domain := range domains {
		lookupDNS(domain)
	}

	fmt.Println("DNS lookup completed. Check dns_history.log for details.")
}
