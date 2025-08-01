from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import ssl
import logging
import os
import hashlib

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'supersecret')
jwt = JWTManager(app)

AUTH_LOG = '../logs/auth.log'
COMMS_LOG = '../logs/comms.log'
CONSENT_LOG = '../logs/consent.log'

logging.basicConfig(
    filename=AUTH_LOG,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def anonimizar_id(sensor_id):
    return hashlib.sha256(sensor_id.encode()).hexdigest()

def registrar_consentimento(sensor_id):
    with open(CONSENT_LOG, 'a') as consent_log:
        consent_log.write(f"{sensor_id}\n")

@app.route('/login', methods=['POST'])
def login():
    usuario = request.json.get('usuario')
    senha = request.json.get('senha')
    consentimento = request.json.get('consentimento', False)
    if usuario == 'sensor' and senha == 'senha123':
        token = create_access_token(identity=usuario)
        logging.info(f"Login bem-sucedido: {usuario}")
        if consentimento:
            registrar_consentimento(usuario)
        return jsonify(access_token=token), 200
    logging.warning(f"Falha login: {usuario}")
    return jsonify(msg='Credenciais inválidas'), 401

@app.route('/sensores', methods=['POST'])
@jwt_required()
def receber_dados():
    dados = request.get_json()
    sensor_id = dados.get('id_sensor', 'desconhecido')
    id_anon = anonimizar_id(sensor_id)
    dados['id_sensor_anon'] = id_anon
    logging.info(f"Dados recebidos: {dados}")
    with open(COMMS_LOG, 'a') as comms_log:
        comms_log.write(f"{dados}\n")
    return jsonify(msg='Dados recebidos com sucesso', id_anon=id_anon), 200

def main():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    try:
        context.load_cert_chain('/app/certs/server.crt', '/app/certs/server.key')
    except Exception as e:
        print(f"[ERRO] Falha ao carregar certificados SSL: {e}")
        exit(1)
    app.run(host='0.0.0.0', port=5000, ssl_context=context)

if __name__ == '__main__':
    main()
    """Inicializa a API Flask com TLS."""
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    try:
        context.load_cert_chain('/app/certs/server.crt', '/app/certs/server.key')
    except Exception as e:
        print(f"[ERRO] Falha ao carregar certificados SSL: {e}")
        exit(1)
    app.run(host='0.0.0.0', port=5000, ssl_context=context)


if __name__ == '__main__':
    main()
