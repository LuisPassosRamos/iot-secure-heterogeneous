import time
import json
import random

MQTT_TOPIC = "irrigação/urbana/sensor"


def gerar_dados_sensor():
    return {
        "sensor_id": "urbano_001",
        "umidade": round(random.uniform(30.0, 70.0), 2),
        "temperatura": round(random.uniform(20.0, 35.0), 2),
        "timestamp": time.time()
    }


def main():
    try:
        while True:
            dados = gerar_dados_sensor()
            payload = json.dumps(dados)
            print(f"[MQTT] Publicado em '{MQTT_TOPIC}': {payload}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[INFO] Encerrando sensor MQTT...")


if __name__ == "__main__":
    main()