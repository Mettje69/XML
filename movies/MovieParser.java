package movies;

import org.w3c.dom.*; 
import org.xml.sax.SAXException; 
import javax.xml.parsers.*; 
import java.io.*; 


public class MovieParser {
    public static void main(String[] args) {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();

            File xmlFile = new File("movies/movies.xml");
            Document document = builder.parse(xmlFile);

            File htmlFile = new File("movies/movie.html");
            FileWriter fileWriter = new FileWriter(htmlFile);
            BufferedWriter htmlWriter = new BufferedWriter(fileWriter);


            NodeList movieList = document.getElementsByTagName("movie");

            for (int i = 0; i < movieList.getLength(); i++) {
                Node movieNode = movieList.item(i);
                if (movieNode.getNodeType() == Node.ELEMENT_NODE) {
                    Element movieElement = (Element) movieNode;

                    htmlWriter.write("<link rel='stylesheet' type='text/css' media='screen' href='main.css'>");

                    String title = movieElement.getAttribute("title");
                    htmlWriter.write("<h2>Movie " + (i + 1) + "</h2>");
                    htmlWriter.write("<p>Title: " + title + "</p>");

                    String year = movieElement.getAttribute("year");
                    htmlWriter.write("<p>Year: " + year + "</p>");

                    String director = movieElement.getAttribute("director");
                    htmlWriter.write("<p>Director: " + director + "</p>");

                    String plot = movieElement.getAttribute("plot");
                    htmlWriter.write("<p>Plot: " + plot + "</p>");
                    
                    String actors = movieElement.getAttribute("actors");
                    htmlWriter.write("<p>Actors: " + actors + "</p>");
                
                }
            }htmlWriter.close();

        } catch (ParserConfigurationException | SAXException | IOException e) {
            e.printStackTrace();
            // OPENING WITH LIVE SERVER
            // http://127.0.0.1:5500/movies/movie.html
        }
    }
}