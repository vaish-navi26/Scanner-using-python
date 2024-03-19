import socket
import time

def scan_port(target, port, timeout=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        conn = s.connect_ex((target, port))
        if conn == 0:
            return f'Port {port}: OPEN'
    except socket.error:
        pass
    return f'Port {port}: CLOSED'

if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    t_IP = socket.gethostbyname(target)
    print('Starting scan on host:', t_IP)

    start_port = int(input('Enter the start port: '))
    end_port = int(input('Enter the end port: '))

    timeout = float(input('Enter the timeout (e.g., 1.0 for 1 second): '))

    startTime = time.time()

    for port in range(start_port, end_port + 1):
        result = scan_port(t_IP, port, timeout)
        print(result)

    print('Time taken:', time.time() - startTime)