FROM python:3.10-slim

WORKDIR /app

# Copia o script do simulador
COPY simulator.py .

# Instala a versão estável do paho-mqtt compatível
RUN pip install --no-cache-dir paho-mqtt==1.6.1

# Comando para rodar o simulador
CMD ["python", "simulator.py"]
