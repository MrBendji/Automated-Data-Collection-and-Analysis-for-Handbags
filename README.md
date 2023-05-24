# Price Comparison WebApp Dataset Generation

This project aims to generate a dataset for a Price Comparison WebApp, focusing on the hand-bags product category. The goal is to collect product and price information from various online sellers on a daily basis. While some sellers provide APIs for accessing their data, not all follow the same route. Therefore, web scraping becomes necessary to gather the required information.

## Project Overview

In this project, web spiders will be developed using Python and Scrapy to scrape data from four different sellers. Each spider will be tailored to extract specific information from a particular seller's website. The following steps will be followed:

1. **Target Sellers**: Identify the four online sellers from which data needs to be collected for the Price Comparison WebApp.
2. **Scrapy Spiders**: Create web spiders using the Scrapy framework to crawl and scrape data from each seller's website.
3. **Data Extraction**: Utilize Scrapy selectors, XPath, or CSS selectors to extract product and price information from the HTML structure of the web pages.
4. **Data Storage**: Determine the appropriate method for storing the scraped data, such as saving it to CSV or a database.
5. **Apache Airflow Integration**: Automate the web scraping process using Apache Airflow. Define tasks and workflows to schedule the scraping tasks periodically, eliminating the need for manual intervention.
6. **Execution and Monitoring**: Run the Apache Airflow tasks to execute the web scraping process and monitor its progress and success.
7. **Data Processing**: Implement data processing tasks as needed, such as cleaning, filtering, and transforming the scraped data using Python.
8. **Dataset Generation**: Generate a comprehensive dataset containing product and price information for hand-bags from different sellers.

## Getting Started

To get started with this project, follow these steps:

1. Clone the GitHub repository to your local machine.
2. Set up a Python virtual environment and activate it.
3. Install the required dependencies listed in the project's `requirements.txt` file.
4. Review the project structure, including the Scrapy spiders and Apache Airflow configuration.
5. Configure the necessary settings, such as target sellers' websites and data storage options, in the project files.
6. Execute the Scrapy spiders manually to ensure they correctly extract the desired data.
7. Set up and start Apache Airflow to automate the web scraping process based on the defined schedule.
8. Monitor the execution of the web scraping tasks and verify the generated dataset.

## Contribution Guidelines

If you would like to contribute to this project, please follow these guidelines:

- Fork the repository and create a new branch for your contributions.
- Make your changes and additions, adhering to the project's coding style and best practices.
- Test your changes thoroughly to ensure they don't introduce any errors.
- Create a pull request with a clear description of the changes you've made and the rationale behind them.

## Conclusion

By combining the power of Python, Scrapy, and Apache Airflow, this project aims to generate a comprehensive dataset for a Price Comparison WebApp. The automated web scraping process eliminates the need for manual interventions and ensures the regular collection of product and price information from different online sellers. The dataset generated can be utilized for analysis, comparison, and providing valuable insights to users of the Price Comparison WebApp.

