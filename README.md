# YFinance App

## Descripción
YFinance App es una aplicación Flask que utiliza la biblioteca `yfinance` para obtener datos financieros. Está diseñada para proporcionar información del mercado en tiempo real, haciendo uso de la caché Redis para optimizar el rendimiento.

## Funcionalidades
- Recuperación de datos del mercado en tiempo real.
- Caché de datos para mejorar la respuesta y reducir las llamadas a la API.
- Interfaz API sencilla para obtener datos de cualquier ticker proporcionado.

## Tecnologías Utilizadas
- Python
- Flask
- Redis
- yfinance

## Configuración del Proyecto
Para ejecutar este proyecto, necesitarás Python y Redis instalados en tu entorno local o servidor.

### Dependencias
Instala todas las dependencias necesarias con:

```bash
pip install -r requirements.txt
