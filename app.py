import matplotlib.pyplot as plt
import mplfinance as mpf
import io
from flask import send_file

def plot_candlestick_chart(df, liquidity_zones):
    # Configuración del estilo y tamaño del gráfico
    mpf_style = mpf.make_mpf_style(base_mpf_style='charles', rc={'font.size': 8})
    fig, ax = mpf.plot(df, type='candle', style=mpf_style, returnfig=True)

    # Añadir zonas de liquidez como áreas sombreadas en el gráfico
    for zone in liquidity_zones:
        ax[0].axhspan(zone['lower'], zone['upper'], color='gray', alpha=0.3)

    # Guardar el gráfico en un buffer de bytes
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf

@app.route('/get_chart/<string:ticker_symbol>')
def get_chart(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    df = ticker.history(period="1mo")

    if df.empty:
        return jsonify({"error": "No data available for the specified ticker"}), 404

    # Supongamos que esta función devuelve las zonas de liquidez como {'lower': precio1, 'upper': precio2}
    liquidity_zones = [{'lower': 150, 'upper': 155}, {'lower': 160, 'upper': 165}]

    buf = plot_candlestick_chart(df, liquidity_zones)
    return send_file(buf, mimetype='image/png', as_attachment=True, attachment_filename='chart.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
