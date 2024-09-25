# Usar una imagen base de Python
FROM python:3.12

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requisitos y el código fuente
COPY requirements.txt requirements.txt
COPY . .

# Instalar dependencias necesarias para instalar Chrome y ChromeDriver
RUN apt-get update && apt-get install -y \
  wget gnupg unzip curl libnss3 gconf-service\
  libasound2 libatk1.0-0 libc6 libcairo2 libcups2\
  libdbus-1-3 libexpat1 libfontconfig1 libgcc1\
  libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0\ 
  libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0\
  libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1\
  libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6\ 
  libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates\
  fonts-liberation libappindicator1 lsb-release xdg-utils 

RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "app/main.py"]
