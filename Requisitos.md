# Projeto Seguro e Interoperável de Sistema IoT em Ambiente Heterogêneo



##### Objetivos da Atividade



* Compreender os desafios reais de interoperabilidade, segurança e privacidade em sistemas IoT modernos.

* Projetar uma arquitetura IoT multiplataforma e multi-protocolo capaz de operar em ambientes heterogêneos.

* Aplicar mecanismos robustos de controle de acesso, criptografia e autenticação.

* Simular ou modelar interações seguras entre sensores, atuadores e aplicações externas.



##### Descrição da Atividade



Você deverá desenvolver um projeto de sistema IoT simulado, que atue em um cenário de conectividade realista. O foco principal deverá estar em:

* Garantir interoperabilidade entre dispositivos IoT heterogêneos.

* Implementar ou propor camadas de segurança e privacidade robustas.

* Demonstrar como protocolos, APIs e padrões contribuem para a confiabilidade do sistema.



##### Cenários Escolhido

1\. irrigação inteligente em regiões distintas (urbanas e remotas). A arquitetura integra sensores com protocolos diferentes (MQTT simulado, LoRaWAN via UDP).



##### Componentes Obrigatórios



1. ###### Arquitetura Detalhada (Desenho Técnico)

Diagrama lógico com:

* Dispositivos e sensores envolvidos
* Gateways e servidores
* Camadas de rede e aplicação
* Interface de visualização



###### 2\. Interoperabilidade

* Uso de pelo menos dois protocolos distintos (MQTT, CoAP, AMQP, HTTP REST, LoRaWAN)
* Explicação sobre o uso de APIs, middlewares ou conversores (ex: bridges MQTTHTTP)
* Justificativa da escolha com base em interoperabilidade



###### 3\. Segurança e Privacidade

Implementação ou proposta dos seguintes elementos:

* Criptografia em trânsito
* Controle de acesso (JWT)
* Proteção contra interceptação e falsificação de pacotes
* Mecanismos de consentimento ou anonimização de dados (se aplicável)



###### 4\. Simulação Funcional ou Prova de Conceito

Pode ser realizada via:

* Simulação com Python, aiocoap, Cooja, etc.
* Ferramentas como Wokwi, Tinkercad, Packet Tracer IoT



###### 5\. Registro e Monitoramento

* Logs de autenticação e comunicação
* Captura de pacotes (Wireshark, logs do broker) — **apenas para UDP/REST, pois MQTT é simulado**
* Tabelas com análise de falhas e tentativas inválidas



##### Entrega Esperada

1. Relatório Técnico em PDF contendo:

* Introdução e justificativa do cenário
* Diagrama de arquitetura
* Tabela comparativa de protocolos e segurança adotada
* Explicações de interoperabilidade e APIs
* Medidas de segurança aplicadas
* Análise de privacidade (LGPD, boas práticas, se aplicável)
* Conclusões sobre robustez, confiabilidade e riscos mitigados

2\. Códigos e capturas de tela da simulação ou protótipo

3\. Arquivos suplementares: Códigos Python, configurações de broker, etc.

