package main

import (
	"fmt"
	"net"
	"syscall"
)

// isValidIP checks if a given string is a valid IP address.
func isValidIP(ip string) bool {
	return net.ParseIP(ip) != nil
}

// getDriveStorage retrieves the total and free storage of a drive.
func getDriveStorage(path string) (uint64, uint64, error) {
	var stat syscall.Statfs_t
	if err := syscall.Statfs(path, &stat); err != nil {
		return 0, 0, err
	}

	total := stat.Blocks * uint64(stat.Bsize) // Total storage
	free := stat.Bavail * uint64(stat.Bsize) // Free storage
	return total, free, nil
}

func main() {
	fmt.Println("Enter an IP address to validate:")
	var ip string
	fmt.Scanln(&ip)

	if isValidIP(ip) {
		fmt.Printf("%s is a valid IP address.\n", ip)
	} else {
		fmt.Printf("%s is not a valid IP address.\n", ip)
	}

	// Drive storage checking
	fmt.Println("Enter the path to check storage (e.g., / or C:\\):")
	var path string
	fmt.Scanln(&path)
	total, free, err := getDriveStorage(path)
	if err != nil {
		fmt.Printf("Error retrieving storage info: %v\n", err)
	} else {
		fmt.Printf("Total Storage: %.2f GB\n", float64(total)/(1024*1024*1024))
		fmt.Printf("Free Storage: %.2f GB\n", float64(free)/(1024*1024*1024))
	}
}
