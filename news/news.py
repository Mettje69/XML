from flask import Flask, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__, template_folder='.')

@app.route('/')
def news():
    file_path = "news/news.xml"
    tree = ET.parse(file_path)
    root = tree.getroot()

    articles = []
    for item in root.iter("item"):
        link = item.findtext("link")
        title = item.findtext("title")
        description = item.findtext("description")
        pub_date = item.findtext("pubDate")
        author = item.findtext("author")
        category = item.findtext("category")

        enclosure = item.find("enclosure")
        image_url = enclosure.attrib.get("url")

        article = {
            "link": link,
            "title": title,
            "description": description,
            "pub_date": pub_date,
            "author": author,
            "category": category,
            "image_url": image_url
        }
        articles.append(article)

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run()
    # http://127.0.0.1:5000