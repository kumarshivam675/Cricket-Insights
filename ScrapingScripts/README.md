This folder contains scripts used to scrape data for analysis purposes.

i) scrape_controller.rb: This is a Rails framework controller which scrapes player information and statistics from the official iplt20 website and stores it in MySQL db.

ii) dimensionScraping.py: The controller script mentioned above does not extract crucial player info. such as his role, batting style etc,. This script uses the available player data in databse to form web links and extract HTML data from iplt20 site. Further string processing done to fetch the desired information.


