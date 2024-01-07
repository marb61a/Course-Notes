<b><p align=center>   
Practical TLS </br>
  Course Notes </br>
https://classes.pracnet.net/courses/practical-tls  
  

<br />
<h1><p align=center>Module 1 - TLS/SSL Overview</h1><br/>

What is SSL? What is TLS?
  -
  - The internet is many routers that are owned by different ISP's
  - As soon as you put data on the wire you no longer have control of it
  - The most common data transferred on the internet is related to websites
  - SSL/TSL build a protected tunnel across the internet
  - HTTPS is HTML transferred using HTTP in an SSL tunnel
  - SSL is an acronym standing for Secure Sockets Layer
  - TLS is an acronym standing for Transport Layer Security
  - IETF renamed SSL to TLS when taking it over in 1999, TLS is the newer version

How do SSL/TLS Protect your Data?
  -
  - What must be done to data to be considered protected
  - Data sent across a wire can be captured by anybody in the middle
    - This is the scenario that SSL/TLS tries to protect users from 
  - SSL/TLS cannot prevent the capture of data, it instead seeks to protect data in 3 ways
    - It will provide confidentiality to that data so that it is only accessible by certain parties
      - It is provided by encryption 
    - It also provides integrity to the data ensuring that it is not modified by unwanted people
      - It does not actually prevent the modification but will instead show when a modification has occurred
      - Integrity is provided by the use of hashing
    - Authentication is the final part where users show that they are who they say they are
      - Authentication is provided by using Public Key Infrastructure 
  - SSL/TLS tunnel is only a conceptual idea, there is no tunnel involved
  
Anti-Replay and Non-Repudiation
  -
  - The best way to understand anti-replay is to understand the problem it seeks to resolve
    - The problem is that certain part of communications could be predicted eg a part of a bank transaction
    - This would allow for the financial part to be repeated over and over again
    - The solution is to use sequence numbers which would stop malicious copies of certain parts of communications being repeatedly sent
    - The sequence number is built into the integrity and authentication mechanism in SSL/TLS
  - Non-repudiation is not about protecting from a man in the middle
    - It is instead about protection from a dishonest sender
  
Key Players
  -
  -
  
TLS / SSL Versions - Part 1
  -
  -
  
TLS / SSL Versions - Part 2
  -
  -

<br /> <br /> <br />
<h1><p align=center>Module 2 - Cryptography</h1><br/>

Hashing
  -
  -
  
Data-Integrity
  -
  -

Encryption
  -
  -
  
Public and Private Keys
  -
  -
  
How TLS and SSL use Cryptography
  -
  -
  
Public Key Infrastructure (PKI)
  -
  -
  
RSA
  -
  -
  
Diffie-Hellman
  -
  -
  
Digital Signature Algorithm
  -
  -

<br /> <br /> <br />
<h1><p align=center>Module 3 - x509 Certificates and Keys</h1><br/>

Overview of the SSL Process
  -
  -
  
What is in a Certificate?
  -
  -
  
Inspecting a Certificate
  -
  -
  
Certificate Extensions
  -
  -
  
LAB 3.0 - Setting up your Lab Environment
LAB 3.1 - Inspecting the certificate of your favorite website
What is in a Private Key?
LAB 3.2 - Matching Certificates to Private Keys
What is in a CSR?
File Formats
LAB 3.3 - Creating a Certificate Authority and two Signed Certificates
LAB 3.4 - File Conversions


<br /> <br /> <br />
<h1><p align=center>Module 4 - Security through Certificates</h1><br/>

Overview of the SSL Process, part 2
  -
  -
  
Certificate Validation - Part 1
  -
  -
  
Certificate Validation - Part 2
  -
  -
  
Certificate Chains - Part 1
Certificate Chains - Part 2
LAB 4.1 - Certificate Chains
Basic Constraints
Certificate Types (DV, OV, EV)
Certificate Revocation
Checking Revocation Status
LAB 4.2 - Certificate Revocation


Module 5 - Cipher Suites

Cipher Suites
CS - Key Exchange - Part 1
CS - Forward Secrecy - Key Exchange - Part 2
CS - Authentication
CS - Encryption - Part 1
CS - Encryption - Part 2
CS - Hashing
Cipher Suites - Avoid, Accept, Prefer
Enumerating Cipher Suites
LAB 5.1 - Cipher Suite Enumeration
Module 6 - TLS/SSL Handshake
15 Lessons

Records - Part 1
Records - Part 2
TLS Handshake
LAB 6.1 - Inspecting a TLS Handshake in Wireshark
Handshake: Ephemeral Diffie-Hellman
Handshake: Session Resumption
Handshake: Mutual Authentication
LAB 6.2 - Inspecting TLS Handshake Variants
TLS Extensions
Extension: OCSP Stapling
Extension: Server Name Indication (SNI)
Extension: Session Tickets
LAB 6.3 - Inspecting Handshake Extensions
Decrypting TLS
LAB 6.4 - Decrypting TLS
Module 7 - TLS Defenses
6 Lessons

Major SSL/TLS Failures over the Years
HTTP Strict Transport Security
Certificate Authority Authorization
Certificate Transparency - Part 1 - Overview
Certificate Transparency - Part 2 - Process and Demonstration
Certificate Transparency - Part 3 - Merkle Hash Trees
Module 8 - TLS Attacks & Vulnerabilities
2 Lessons

Module Description
Insecure Renegotiation (Session Renegotiation)
Module 9 - What's new in TLS 1.3?
9 Lessons

Differences with TLS 1.3
Changes to Cipher Suites
Changes to Handshake
Changes to Renegotiation
Changes to Session Resumption
Middleboxes and Complications with migrating to TLS 1.3
Forward Secrecy and TLS 1.3
Decrypting TLS 1.3
LAB 9.1 - Capturing and Filtering TLS 1.3 Traffic
Module 10 - TLS 1.3 Under the Hood
10 Lessons

TLS 1.3 Key Schedule - Part 1
TLS 1.3 Handshake
LAB 10.1 - Inspecting & Decrypting a TLS 1.3 Handshake
TLS 1.3 Key Schedule - Part 2
TLS 1.3 Session Resumption
TLS 1.3 PSK Mode Handshake
TLS 1.3 Session Tickets
TLS 1.3 0-RTT Handshake
LAB 10.2 - Inspecting TLS 1.3 PSK Handshakes
TLS 1.3 Mutual Authentication
Module 11 - TLS 1.3 Extensions
6 Lessons

Extensions Overview
Review of TLS 1.3 Extensions already discussed
Extension: Signature Algorithm & Signature Algorithm Certificate
Extension: Cookies
Extension: ALPN - Application Layer Protocol Negotiation
Extension: PHA - Post Handshake Authentication
Bonus Content
2 Lessons

Free access to OpenSSL Training Course
Infographics -- free to share
