# Weather App

Aplicación en Python que consume la API de OpenWeatherMap para obtener el pronóstico del tiempo y generar un resumen estructurado.

---

## Variables de entorno
Crear archivo `.env` en la raíz o crear secreto en GitHub:
WEATHER_API_KEY=tu_api_key_aqui

## ⚙️ Setup
```bash
git clone https://github.com/FranciscoAvaria/weather.git
cd weather
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt

## Run
python -m app.main
