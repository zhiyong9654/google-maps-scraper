from flask import Flask, request, jsonify
from src.scraper import scrape_places, scrape_reviews
from loguru import logger

logger.add("google_maps_scrapper.log", retention="10 days")
app = Flask(__name__)


@app.route('/find_places', methods=['POST'])
def flask_find_places():
    if request.is_json:
        data = request.get_json()
        try:
            return jsonify(scrape_places(data)), 200
        except Exception as e:
            logger.error("Input: {data} met with error:\n{e}".format(data=data, e=e)) 
            return jsonify({"error": "Scraping places met with error"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/scrape_reviews', methods=['POST'])
def flask_scrape_reviews():
    if request.is_json:
        data = request.get_json()
        try:
            return jsonify(scrape_reviews(data)), 200
        except Exception as e:
            logger.error("Input: {data} met with error:\n{e}".format(data=data, e=e)) 
            return jsonify({"error": "Scraping reviews met with error"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8989)
    # app.run(host='0.0.0.0', port=8989)
