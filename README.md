# clasificados_spider
## Description
Scrapy spider made to scrape rental listings from **Clasificados La Voz** website 

## Installation
1. Clone the repo
2. Create virtual environment (optional)
3. `pip install -r requirements.txt`

## Configuration
Modify `user_config.py`
### Default config
```
# use lowercase and replace spaces with hyphens
bot_config = {
    "base_url": "https://clasificados.lavoz.com.ar/inmuebles/todo",
    "operation": "alquileres",
    "min_price": "10000",
    "max_price": "35000",
    "currency": "pesos",
    "province": "cordoba",
    "city": "cordoba",
    "bedrooms": ['1-dormitorio'],
    "neighborhoods": ["nueva-cordoba", 'centro']
}
```

## Usage
```scrapy crawl clasificados -o output.csv```

## Observations
- Sometimes the website behaves inconsistently.
- Sellers might post incorrect data.
