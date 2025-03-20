# Networks and Operating Systems - Internet Layer

## Notes
- In this Lab we looked at the Internet Protocol(IP).

### 1. Working with IP Addresses
- The IPv4 are divided into five differenct classes  (A, B, C, D, and E), which is based off the first 8 bits of the address. For example Class A is N.N.N.N. 
- CIDR (classless inter-domain routing) which is an IP addressing method replaces class-base system (A, B and C).

### 2. Dynamic Host Configuration Protocol (DHCP)
- DHCP is a network management protocol which is used to assign IP addresses to device on other networks. The DCHP has a four step process.  


## Exercises
- Exercise 1: Extend the script to calculate:
    - Broadcast address
    - First and last usable host addresses
    - Number of usable hosts
    - Change the IP address to have it CIDR prefix ( e.g. /24)  and compare resulting network
    print("Your Computer IP Address is:" + IPAddr)
- Exercise 2: Analyse your IP address to know if it is private/public and the network details.
- Exercise 3: Get the university website IP address and analyse it. Hint you can use seminar of week2 to know how to get the address.
- Exercise 4: Create a subnetting plan for a company with 4departments requiring the following hosts:
    • Engineering: 30 hosts
    • Marketing: 15 hosts
    • Finance: 10 hosts
    • HR: 5 hosts
- Exercise 5: use the client sever example from previous week to have a TCP server as DHCP server and create a client that would get the IP address from the server following the process above.

