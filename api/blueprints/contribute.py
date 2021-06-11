import psycopg2
import datetime
from flask import Blueprint, jsonify, request
from config import config
from extensions import cache
from schema import Schema, Or
from decorators import validators, auth

bp = Blueprint('contribute', __name__, url_prefix='/contribute')

@cache.cached(key_prefix='all_countries')
def get_countries():
    with psycopg2.connect(**config['custom_data']) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM countries')
        return cursor.fetchall()

def datetime_validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')

        return True
    except ValueError:
        return False

schema = Schema({
    'data': [
        {
            'period_start_date': Schema(datetime_validate, error='date should be in "YYYY-MM-DD" format'),
            'period': Schema(lambda s: s in ('daily', 'weekly', 'biweekly', 'monthly',),
                                error='"period" should be "daily", "weekly", "biweekly" or "monthly"'),
            'country': Schema(lambda s: s in [row[0] for row in get_countries()], error='"country" should be one from the list, see documentation'),
            'province': Schema(Or(str, None), error='"province" should be string or null'),
            'average_hashrate': Schema(Or(float, int), error='"average_hashrate" should be numeric'),
            'unit': Schema(lambda s: s in ('th/s', 'ph/s', 'eh/s',), error='"unit" should be "th/s", "ph/s" or "eh/s"')
        }
    ]
}, ignore_extra_keys=True)

@bp.route('/miners_geo_distribution', methods=('POST',))
@auth.bearer()
@validators.validate(schema)
def miners_geo_distribution(api_token):
    """
    Contribute to geographical hashrate distribution analysis
    ---
    tags:
      - Contribute
    security:
      - Bearer: []
    definitions:
      - schema:
          id: Hashrate
          properties:
            period_start_date:
             type: string
             format: date
             description: Information date. Should be in YYYY-MM-DD format
             example: "2020-01-01"
            period:
             type: string
             description: Data period. Should be from the list below
             example: "weekly"
             enum:
                - daily
                - weekly
                - biweekly
                - monthly
            country:
             type: string
             description: Country name. Should be from the [World Bank](https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups) list below.
             example: "United States"
             enum:
               - "\\"Afghanistan\\""
               - "\\"Albania\\""
               - "\\"Algeria\\""
               - "\\"American Samoa\\""
               - "\\"Andorra\\""
               - "\\"Angola\\""
               - "\\"Antigua and Barbuda\\""
               - "\\"Argentina\\""
               - "\\"Armenia\\""
               - "\\"Aruba\\""
               - "\\"Australia\\""
               - "\\"Austria\\""
               - "\\"Azerbaijan\\""
               - "\\"Bahrain\\""
               - "\\"Bangladesh\\""
               - "\\"Barbados\\""
               - "\\"Belarus\\""
               - "\\"Belgium\\""
               - "\\"Belize\\""
               - "\\"Benin\\""
               - "\\"Bermuda\\""
               - "\\"Bhutan\\""
               - "\\"Bolivia\\""
               - "\\"Bosnia and Herzegovina\\""
               - "\\"Botswana\\""
               - "\\"Brazil\\""
               - "\\"British Virgin Islands\\""
               - "\\"Brunei\\""
               - "\\"Bulgaria\\""
               - "\\"Burkina Faso\\""
               - "\\"Myanmar\\""
               - "\\"Burundi\\""
               - "\\"Cabo Verde\\""
               - "\\"Cambodia\\""
               - "\\"Cameroon\\""
               - "\\"Canada\\""
               - "\\"Cayman Islands\\""
               - "\\"Central African Republic\\""
               - "\\"Chad\\""
               - "\\"Chile\\""
               - "\\"China\\""
               - "\\"Colombia\\""
               - "\\"Comoros\\""
               - "\\"Cook Islands\\""
               - "\\"Costa Rica\\""
               - "\\"Cote D'Ivoire\\""
               - "\\"Croatia\\""
               - "\\"Cuba\\""
               - "\\"Curacao\\""
               - "\\"Cyprus\\""
               - "\\"Czech Republic\\""
               - "\\"Democratic Republic of the Congo\\""
               - "\\"Denmark\\""
               - "\\"Djibouti\\""
               - "\\"Dominica\\""
               - "\\"Dominican Republic\\""
               - "\\"Ecuador\\""
               - "\\"Egypt, Arab Rep.\\""
               - "\\"El Salvador\\""
               - "\\"Equatorial Guinea\\""
               - "\\"Eritrea\\""
               - "\\"Estonia\\""
               - "\\"Eswatini\\""
               - "\\"Ethiopia\\""
               - "\\"Falkland Islands (Islas Malvinas)\\""
               - "\\"Faroe Islands\\""
               - "\\"Federated States of Micronesia\\""
               - "\\"Fiji\\""
               - "\\"Finland\\""
               - "\\"France\\""
               - "\\"French Polynesia\\""
               - "\\"Gabon\\""
               - "\\"Gambia\\""
               - "\\"Georgia\\""
               - "\\"Germany\\""
               - "\\"Ghana\\""
               - "\\"Gibraltar\\""
               - "\\"Greece\\""
               - "\\"Greenland\\""
               - "\\"Grenada\\""
               - "\\"Guam\\""
               - "\\"Guatemala\\""
               - "\\"Guinea\\""
               - "\\"Guinea-Bissau\\""
               - "\\"Guyana\\""
               - "\\"Haiti\\""
               - "\\"Honduras\\""
               - "\\"Hong Kong SAR, China\\""
               - "\\"Hungary\\""
               - "\\"Iceland\\""
               - "\\"India\\""
               - "\\"Indonesia\\""
               - "\\"Iran, Islamic Rep.\\""
               - "\\"Iraq\\""
               - "\\"Ireland\\""
               - "\\"Israel\\""
               - "\\"Italy\\""
               - "\\"Jamaica\\""
               - "\\"Japan\\""
               - "\\"Jersey\\""
               - "\\"Jordan\\""
               - "\\"Kazakhstan\\""
               - "\\"Kenya\\""
               - "\\"Kiribati\\""
               - "\\"Kosovo\\""
               - "\\"Kuwait\\""
               - "\\"Kyrgyzstan\\""
               - "\\"Laos\\""
               - "\\"Latvia\\""
               - "\\"Lebanon\\""
               - "\\"Lesotho\\""
               - "\\"Liberia\\""
               - "\\"Libya\\""
               - "\\"Liechtenstein\\""
               - "\\"Lithuania\\""
               - "\\"Luxembourg\\""
               - "\\"Macau\\""
               - "\\"North Macedonia\\""
               - "\\"Madagascar\\""
               - "\\"Malawi\\""
               - "\\"Malaysia\\""
               - "\\"Maldives\\""
               - "\\"Mali\\""
               - "\\"Malta\\""
               - "\\"Marshall Islands\\""
               - "\\"Mauritania\\""
               - "\\"Mauritius\\""
               - "\\"Mexico\\""
               - "\\"Moldova\\""
               - "\\"Mongolia\\""
               - "\\"Montenegro\\""
               - "\\"Montserrat\\""
               - "\\"Morocco\\""
               - "\\"Mozambique\\""
               - "\\"Namibia\\""
               - "\\"Nauru\\""
               - "\\"Nepal\\""
               - "\\"Netherlands\\""
               - "\\"New Caledonia\\""
               - "\\"New Zealand\\""
               - "\\"Nicaragua\\""
               - "\\"Niger\\""
               - "\\"Nigeria\\""
               - "\\"Niue\\""
               - "\\"North Korea\\""
               - "\\"Norway\\""
               - "\\"Oman\\""
               - "\\"Pakistan\\""
               - "\\"Panama\\""
               - "\\"Papua New Guinea\\""
               - "\\"Paraguay\\""
               - "\\"Peru\\""
               - "\\"Philippines\\""
               - "\\"Poland\\""
               - "\\"Portugal\\""
               - "\\"Puerto Rico\\""
               - "\\"Qatar\\""
               - "\\"Republic of the Congo\\""
               - "\\"Romania\\""
               - "\\"Russian Federation\\""
               - "\\"Rwanda\\""
               - "\\"Saint Helena, Ascension, And Tristan Da Cunha\\""
               - "\\"Saint Kitts and Nevis\\""
               - "\\"Saint Lucia\\""
               - "\\"Saint Pierre and Miquelon\\""
               - "\\"Saint Vincent and the Grenadines\\""
               - "\\"Samoa\\""
               - "\\"Sao Tome and Principe\\""
               - "\\"Saudi Arabia\\""
               - "\\"Senegal\\""
               - "\\"Serbia\\""
               - "\\"Seychelles\\""
               - "\\"Sierra Leone\\""
               - "\\"Singapore\\""
               - "\\"Slovakia\\""
               - "\\"Slovenia\\""
               - "\\"Solomon Islands\\""
               - "\\"Somalia\\""
               - "\\"South Africa\\""
               - "\\"Korea, Rep\\""
               - "\\"South Sudan\\""
               - "\\"Spain\\""
               - "\\"Sri Lanka\\""
               - "\\"Sudan\\""
               - "\\"Suriname\\""
               - "\\"Sweden\\""
               - "\\"Switzerland\\""
               - "\\"Syria\\""
               - "\\"Taiwan\\""
               - "\\"Tajikistan\\""
               - "\\"Tanzania\\""
               - "\\"Thailand\\""
               - "\\"The Bahamas\\""
               - "\\"Togo\\""
               - "\\"Tonga\\""
               - "\\"Trinidad and Tobago\\""
               - "\\"Tunisia\\""
               - "\\"Turkey\\""
               - "\\"Turkmenistan\\""
               - "\\"Turks and Caicos Islands\\""
               - "\\"Uganda\\""
               - "\\"Ukraine\\""
               - "\\"United Arab Emirates\\""
               - "\\"United Kingdom\\""
               - "\\"United States\\""
               - "\\"Uruguay\\""
               - "\\"Uzbekistan\\""
               - "\\"Vanuatu\\""
               - "\\"Venezuela\\""
               - "\\"Vietnam\\""
               - "\\"Virgin Islands\\""
               - "\\"West Bank\\""
               - "\\"Yemen\\""
               - "\\"Zambia\\""
               - "\\"Zimbabwe\\""
            province:
             type: string
             description: Regional provenance within country. Format is open. If submitting country data as a whole, leave this field empty.
             example: null
            average_hashrate:
             type: number
             format: double
             description: Average hashrate for a given country or province over the selected period.
             example: 99.99
            unit:
             type: string
             description: Should be from the list below
             example: 'th/s'
             enum:
               - th/s
               - ph/s
               - eh/s
    parameters:
      - in: body
        name: body
        schema:
          properties:
            data:
              type: array
              description: List of your hashrate info items,
              items:
                $ref: "#/definitions/Hashrate"
    responses:
      200:
        description: Records created
        schema:
          type: object
          properties:
            data:
              type: array
              description: List of your hashrate info items,
              items:
                $ref: "#/definitions/Hashrate"
            status:
              type: string
              enum:
                - success
                - fail
              example: success
      422:
        description: Validation error
        schema:
          type: object
          properties:
            error:
              type: string
              description: Error text
              example: 'date should be in \"YYYY-MM-DD\" format'
    """
    data = request.json['data']
    if len(data) > 0:
        with psycopg2.connect(**config['custom_data']) as conn:
            cursor = conn.cursor()
            insert_sql = "INSERT INTO hashrate_geo_distribution (frequency, country, province, average_hashrate, unit, period_start_date, api_token_id)" \
                         " VALUES (%(frequency)s, %(country)s, %(province)s, %(average_hashrate)s, %(unit)s, %(period_start_date)s, %(api_token_id)s)"
            try:
                for row in data:
                    row['api_token_id'] = api_token[0]

                cursor.executemany(insert_sql, data)
            except Exception as error:
                return jsonify(data=data, status="fail", error=str(error))

    return jsonify(data=data, status="success")
