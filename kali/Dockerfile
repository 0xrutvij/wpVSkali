FROM kalilinux/kali-rolling

# Apt
RUN apt -y update && apt -y upgrade && apt -y autoremove && apt clean

# Tools
RUN apt install aircrack-ng crackmapexec crunch curl dirb dirbuster dnsenum dnsrecon dnsutils dos2unix enum4linux exploitdb ftp git gawk gobuster hashcat hping3 hydra impacket-scripts john joomscan masscan metasploit-framework mimikatz nano nasm ncat netcat-traditional nikto nmap patator iputils-ping php powersploit proxychains python3-impacket python3-pip python2 python3 recon-ng responder samba samdump2 smbclient smbmap snmp socat sqlmap sslscan theharvester vim wafw00f weevely wfuzz wget whois wordlists wpscan -y --no-install-recommends

# Set working directory to /root
WORKDIR /root

# Open shell
CMD ["/bin/bash"]
