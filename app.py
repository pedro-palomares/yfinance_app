import os
import pickle
import redis
import yfinance as yf
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuración de Redis
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_db = int(os.getenv('REDIS_DB', 0))
r = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

def get_data_from_cache(ticker_symbol):
    """Intenta recuperar los datos del ticker desde la caché."""
    try:
        data = r.get(ticker_symbol)
        if data:
            return pickle.loads(data)
    except Exception as e:
        print(f"Error al obtener datos de la caché: {e}")
    return None

def set_data_to_cache(ticker_symbol, data):
    """Guarda los datos del ticker en la caché por una hora."""
    try:
        r.setex(ticker_symbol, 3600, pickle.dumps(data))  # Caché expira en 3600 segundos (1 hora)
    except Exception as e:
        print(f"Error al guardar datos en la caché: {e}")

@app.route('/ticker/<string:ticker_symbol>')
def get_ticker_data(ticker_symbol):
    """Endpoint para obtener datos del ticker."""
    data = get_data_from_cache(ticker_symbol)
    if data is None:
        ticker = yf.Ticker(ticker_symbol)
        data = ticker.history(period="1mo").to_dict()  # Obtiene datos históricos del último mes
        set_data_to_cache(ticker_symbol, data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
