# Imagem base
FROM python:3.11-slim

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Diretório da app
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    netcat-openbsd gcc postgresql-client libpq-dev \
    && apt-get clean

# Copia os arquivos
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Entrypoint (para esperar o banco subir)
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
