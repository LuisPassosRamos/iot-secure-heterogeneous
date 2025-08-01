import socket
import requests
import json
import os
import logging

LOG_FILE = '../logs/comms.log'


def get_jwt_token():
    return os.getenv("JWT_TOKEN", "token_simulado")


def registrar_comunicacao(payload):
    with open(LOG_FILE, 'a') as log:
        log.write(f"{payload}\n")


def main():
    udp_ip = "0.0.0.0"
    udp_port = 6000
    api_url = "https://api_rest:5000/sensores"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))
    print(f"[UDP-Gateway] Escutando em {udp_ip}:{udp_port}")

    while True:
        data, addr = sock.recvfrom(4096)
        try:
            payload = json.loads(data.decode("utf-8"))
            print(f"[UDP-Gateway] Recebido de {addr}: {payload}")
            registrar_comunicacao(payload)
            token = get_jwt_token()
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            response = requests.post(api_url, json=payload, headers=headers, verify=False)
            print(f"[UDP-Gateway] Enviado para API REST: {response.status_code}")
        except json.JSONDecodeError:
            print(f"[UDP-Gateway] Pacote inválido recebido de {addr}: {data}")
        except Exception as exc:
            print(f"[UDP-Gateway] Erro ao processar pacote: {exc}")


if __name__ == "__main__":
    main()
