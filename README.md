# 🌱 Projeto IoT Seguro e Interoperável — Irrigação Inteligente Multirregional

Este projeto simula uma infraestrutura IoT segura e interoperável para irrigação inteligente em regiões distintas (urbanas e remotas). A arquitetura integra sensores com protocolos diferentes (MQTT, LoRaWAN via UDP), aplicando criptografia, autenticação e registros de comunicação.

### 1. Arquitetura Detalhada
O projeto inclui diagrama técnico em `docs/arquitetura.png` e detalhamento da estrutura dos componentes, sensores, gateways e camadas de rede/aplicação.

### 2. Interoperabilidade
São utilizados dois protocolos distintos: MQTT (simulado para sensores urbanos) e UDP/HTTP REST (para sensores remotos e gateway). A interoperabilidade é garantida pelo gateway UDP, que converte pacotes UDP em requisições HTTP REST para a API, permitindo integração entre diferentes tecnologias. Justificativa: permite conectar sensores heterogêneos e facilitar integração futura com outros protocolos (ex: LoRaWAN, CoAP).

### 3. Segurança e Privacidade
Todos os canais de comunicação utilizam criptografia (TLS/HTTPS). O controle de acesso é feito via JWT, exigido para envio de dados à API REST. Os sensores podem ter IDs ofuscados via hash SHA256 para anonimização. Logs de autenticação e eventos são registrados em arquivos dedicados. O sistema é projetado para evitar interceptação e falsificação de pacotes.

### 4. Simulação Funcional / Prova de Conceito
Todos os sensores, gateway e API REST são simulados em containers Docker, permitindo execução simultânea e testes realistas. O sensor MQTT simula publicação periódica, o sensor UDP envia dados para o gateway, e o gateway repassa para a API REST. Scripts e exemplos de execução estão incluídos.

### 5. Registro e Monitoramento
Logs de autenticação e comunicação são gerados em `logs/auth.log` e `logs/comms.log`. Pacotes podem ser capturados via tcpdump (`logs/packets.pcap`). O README inclui exemplos de comandos para análise e monitoramento. Falhas e tentativas inválidas são registradas para posterior análise.


* Simular sensores em regiões urbanas (MQTT) e remotas (LoRaWAN).
* Garantir interoperabilidade via bridges e APIs REST.
* Adotar protocolos seguros com autenticação robusta (JWT).
* Monitorar, logar e capturar tráfego de forma rastreável.
* Utilizar Docker para facilitar o deploy e a simulação completa.

---

## 🧰 Tecnologias Utilizadas

| Tecnologia          | Função                                                       |
| ------------------- | ------------------------------------------------------------ |
| Python 3            | Desenvolvimento dos sensores, gateway UDP, API Flask/FastAPI |
| MQTT (Simulado)     | Comunicação simulada entre sensores urbanos                 |
| HTTP REST (Flask)   | Endpoint seguro para ingestão de dados remotos via gateway   |
| TLS / DTLS          | Criptografia em trânsito (broker MQTT e REST API com HTTPS)  |
| JWT                 | Autenticação de sensores e gateway                           |
| Docker              | Contêineres isolados para cada componente                    |
| Wireshark / tcpdump | Captura e análise de pacotes                                 |
| Logging (Python)    | Geração de logs de acesso, falhas e comunicação              |

---

## 🏗️ Estrutura do Projeto

```
iot-irrigacao/
│
├── docker-compose.yml          # Orquestra todos os contêineres
├── certs/                      # Certificados TLS
│   ├── ca.crt
│   ├── server.crt / key
│   └── client.crt / key
│
├── mqtt/
│   └── sensor_mqtt.py          # Sensor urbano com comunicação MQTT simulada
│
├── udp_gateway/
│   ├── gateway_udp.py          # Gateway que recebe UDP e repassa via HTTP
│   └── sensor_udp.py           # Sensor remoto que envia via UDP
│
├── api_rest/
│   ├── app.py                  # API Flask segura (TLS + JWT)
│   ├── requirements.txt
│   └── Dockerfile
│
├── logs/
│   ├── auth.log                # Logs de autenticação
│   ├── comms.log               # Logs de comunicação dos sensores
│   └── packets.pcap            # Pacotes capturados
│
├── docs/
│   ├── arquitetura.png         # Diagrama da arquitetura
│   └── relatório.pdf           # Relatório técnico
│
└── README.md
```

---

## 🧪 Componentes do Sistema

1. 🧭 API REST (Flask/FastAPI)

   * Porta: 5000
   * HTTPS (TLS)
   * JWT para autenticação de sensores
   * Recebe dados JSON de sensores remotos via UDP Gateway

2. 📡 Gateway UDP (simula LoRaWAN)

   * Recebe pacotes UDP em JSON
   * Verifica autenticidade
   * Encaminha via POST à API REST usando token JWT
3. 🌆 Sensor Urbano (MQTT Simulado)

   * Publica dados periódicos (temperatura, umidade)
   * Comunicação simulada entre sensores urbanos (sem broker real)
   * Simulação de autenticação e criptografia

4. 🌄 Sensor Remoto (UDP)

   * Envia pacotes JSON com dados simulados
   * Aponta para o Gateway UDP

5. 🔐 Segurança

   * TLS: todos os canais são encriptados
   * JWT: gateway e sensores usam tokens válidos
   * Logs: falhas de autenticação e eventos são registrados
   * Consentimento/anônimos: IDs dos sensores podem ser ofuscados (hash SHA256)

6. 📋 Logs & Análise

   * Arquivos logs/\*.log armazenam falhas e eventos
   * Captura de pacotes pode ser feita via tcpdump (ex: gateway\_udp container)
   * Exemplo de comando: docker exec udp\_gateway tcpdump -w /logs/packets.pcap

---

## 🐳 Como Rodar com Docker

1. Clonar o repositório:

   ```bash
   git clone https://github.com/usuario/iot-irrigacao-segura.git
   cd iot-irrigacao-segura
   ```

2. Gerar certificados TLS (com script helper ou openssl manualmente)

   ```bash
   ./generate_certs.sh
   ```

3. Subir todos os serviços:

   ```bash
   docker-compose up --build
   ```

4. Visualizar logs:

   ```bash
   docker logs api_rest
   docker logs udp_gateway
   ```

---

## 📘 Atividades e Entregas Técnicas

| Atividade             | Entrega/Arquivo                                     |
| --------------------- | --------------------------------------------------- |
| Desenho técnico       | docs/arquitetura.png                                |
| Simulação funcional   | sensores + api + gateway em containers              |
| Segurança             | JWT implementado + TLS configurado                  |
| Logs e pacotes        | logs/auth.log, comms.log, packets.pcap              |
| Relatório             | docs/relatório.pdf (explicações técnicas + tabelas) |
| Códigos-fonte         | mqtt/sensor\_mqtt.py, udp\_gateway/, api\_rest/     |
| Códigos-fonte         | mqtt/sensor_mqtt.py (simulado), udp_gateway/, api_rest/     |
| Scripts suplementares | scripts de geração de tokens, certificados          |
