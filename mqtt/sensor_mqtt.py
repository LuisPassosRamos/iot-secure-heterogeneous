# manipulação de tempo, serialização de dados e geração de valores aleatórios
import time 
import json 
import random
#  Para configuração de conexão segura (TLS)
import ssl
#  Biblioteca para comunicação MQTT
import paho.mqtt.client as mqtt

# Configuração do Broker MQTT
MQTT_Broker = "localhost"
MQTT_PORT = 8883 # Porta com TLS
MQTT_TOPIC = "irrigação/urbana/sensor"
MQTT_USERNAME = "sensor_user"
MQTT_PASSWORD = "senha_segura"

# Caminhos para os certificados TLS
CA_CERT = "./certs/ca.crt"
CLIENT_CERT = "./certs/client.key"

def gerar_dados_sensor():
    return {
        "sensor_id": "urbano_001",
        "umidade": round(random.uniform(30.0, 70.0), 2),
        "temperatura": round(random.uniform(20.0, 35.0), 2),
        "timestamp": time.time()
    }

def on_connect(client, userdata, flags, rc):
    print(f"[INFO] Conectado ao broker com resultado {rc}")

def main():
    client = mqtt.Client()
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    client.tls_set(
        ca_certs=CA_CERT,
        certfile=CLIENT_CERT,
        keyfile=CLIENT_KEY,
        cert_reqs=ssl.CERT_REQUIRED,
        tls_version=ssl.PROTOCOL_TLSv1_2,
        ciphers=None
    )

    client.on_connect = on_connect
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    try:
        while True:
            dados = gerar_dados_sensor()
            payload = json.dumps(dados)
            client.publish(MQTT_TOPIC, payload)
            print(f"[MQTT] Dados enviados: {payload}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[INFO] Encerrando sensor MQTT...")
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()