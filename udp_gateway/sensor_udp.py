import socket
import json
import time
import random

UDP_IP = "udp_gateway"
UDP_PORT = 6000


def gerar_dados_sensor():
    return {
        "id_sensor": "remoto-001",
        "temperatura": round(random.uniform(15, 30), 2),
        "umidade": round(random.uniform(40, 80), 2),
        "timestamp": time.time()
    }


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        dados = gerar_dados_sensor()
        mensagem = json.dumps(dados).encode("utf-8")
        sock.sendto(mensagem, (UDP_IP, UDP_PORT))
        print(f"[Sensor-UDP] Dados enviados: {dados}")
        time.sleep(5)


if __name__ == "__main__":
    main()
