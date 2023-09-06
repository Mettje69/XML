import requests
from xml.etree import ElementTree
import mysql.connector

try:
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                    <soap:Body>
                        <FullCountryInfoAllCountries xmlns="http://www.oorsprong.org/websamples.countryinfo">
    					</FullCountryInfoAllCountries>
                    </soap:Body>
                </soap:Envelope>"""

    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_xml = response.text.replace('soap:', '').replace('m:', '')
    print(response_xml)

    xml_text = ElementTree.fromstring(response_xml)

    names = xml_text.findall('.//tCountryInfo/sName')
    codes = xml_text.findall('.//sISOCode')
    currencies = xml_text.findall('.//sCurrencyISOCode')

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='countries'
    )

    cursor = connection.cursor()

    for name, code, currency in zip(names, codes, currencies):
        country_name = name.text
        country_code = code.text
        country_currency = currency.text

        insert_query = "INSERT INTO countries (name, code, currency) VALUES (%s, %s, %s)"
        data = (country_name, country_code, country_currency)

        cursor.execute(insert_query, data)

    connection.commit()

    cursor.close()
    connection.close()

except Exception as e:
    print(f"An error occurred: {e}")
