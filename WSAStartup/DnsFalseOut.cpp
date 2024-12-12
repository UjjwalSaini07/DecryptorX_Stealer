// This Code Not Written By Me - Credit : Online Source...But i Modified it for my own purpose...
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/udp.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>

#define BUFFER_SIZE 65536

void parseDNSQuery(unsigned char *buffer, int size) {
    struct iphdr *iph = (struct iphdr *)buffer;
    unsigned short iphdrlen = iph->ihl * 4;

    struct udphdr *udph = (struct udphdr *)(buffer + iphdrlen);
    unsigned char *dnsPayload = buffer + iphdrlen + sizeof(struct udphdr);

    // DNS header is 12 bytes
    dnsPayload += 12;

    // Extract the query name (domain name)
    std::string domainName;
    while (*dnsPayload != 0) {
        int labelLength = *dnsPayload;
        dnsPayload++;

        for (int i = 0; i < labelLength; i++) {
            domainName += *dnsPayload;
            dnsPayload++;
        }
        domainName += ".";
    }

    // Remove trailing dot
    if (!domainName.empty()) {
        domainName.pop_back();
    }

    std::cout << "Visited Website: " << domainName << std::endl;
}

int main() {
    int sockfd;
    unsigned char buffer[BUFFER_SIZE];

    struct sockaddr_in addr;
    socklen_t addr_len = sizeof(addr);

    // Create a raw socket to capture DNS packets
    sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_UDP);
    if (sockfd < 0) {
        perror("Socket creation failed");
        return EXIT_FAILURE;
    }

    while (true) {
        // Receive packets
        int dataSize = recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&addr, &addr_len);
        if (dataSize < 0) {
            perror("recvfrom failed");
            close(sockfd);
            return EXIT_FAILURE;
        }

        struct iphdr *iph = (struct iphdr *)buffer;

        // Check if the packet is UDP and DNS
        if (iph->protocol == IPPROTO_UDP) {
            struct udphdr *udph = (struct udphdr *)(buffer + iph->ihl * 4);
            if (ntohs(udph->dest) == 53) { // Check for DNS port 53
                parseDNSQuery(buffer, dataSize);
            }
        }
    }

    close(sockfd);
    return EXIT_SUCCESS;
}
