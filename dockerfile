# Usar una imagen base de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requisitos y el código fuente
COPY requirements.txt requirements.txt
COPY . .

# Instalar las dependencias
RUN apt-get update && apt-get install -y \
  wget \
  gnupg \
  unzip \
  && wget -q -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt-get install -y /tmp/google-chrome.deb \
  && wget -q -N https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip -P /tmp \
  && unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ \
  && chmod +x /usr/local/bin/chromedriver \
  && rm /tmp/google-chrome.deb /tmp/chromedriver_linux64.zip

RUN pip install -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "app/main.py"]
