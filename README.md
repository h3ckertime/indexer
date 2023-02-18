İndexer Tool 
This is a Python script that extracts all the links from a web page and saves them to a text file.

Prerequisites
Before running this script, you need to have Python 3 and the requests and beautifulsoup4 modules installed. You can install these modules by running the following command:

Copy code
pip install -r requirements.txt

Usage
Clone the repository or download the web_page_link_extractor.py file.
Open a terminal or command prompt and navigate to the directory where the file is saved.
Run the following command to execute the script:
Copy code
python indexer.py
Enter the URL of the web page you want to extract links from.
The script will print out all the links found on the page and save them to a text file in the format domain_com.txt, where "domain.com" is the domain of the URL.
If there were any errors accessing the web page, the script will save the error message to a separate text file in the format domain_com_errors.txt.
Repeat steps 4-6 as needed for other web pages.
