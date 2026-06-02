import asyncio
import socket
from datetime import datetime
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}
async def scan_port(target_ip, port):
    try:
        conn = asyncio.open_connection(target_ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=2.0)
        writer.close()
        await writer.wait_closed()
        return True, port, COMMON_PORTS.get(port, "Bilinmeyen Servis")
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        return False, port, None

async def main():
    # Test amaçlı localhost (127.0.0.1) hedef alınmıştır.
    TARGET = "127.0.0.1" 
    print("-" * 50)
    print(f"Hedef Taranıyor: {TARGET}")
    print(f"Tarama Başlangıcı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    ports_to_scan = list(range(1, 1025))
    for p in COMMON_PORTS.keys():
        if p not in ports_to_scan:
            ports_to_scan.append(p)        
    ports_to_scan.sort()
    tasks = [scan_port(TARGET, port) for port in ports_to_scan]
    results = await asyncio.gather(*tasks)
    open_ports_count = 0
    for is_open, port, service in results:
        if is_open:
            print(f"[+] Port Açık: {port} | Servis: {service}")
            open_ports_count += 1
    print("-" * 50)
    print(f"Tarama Tamamlandı. Toplam {open_ports_count} açık port bulundu.")
    print("Enes tarafından yapılmıştır.")
    print("-" * 50)

if __name__ == "__main__":
    asyncio.run(main())
