# Life Quality and Crime Rate Worldwide 
## Problem Statement
The problem involves scraping two websites ([Life Quality](https://www.worlddata.info/quality-of-life.php) and [Crime Rate](https://worldpopulationreview.com/country-rankings/crime-rate-by-country)) for collecting life quality and crime rate data, merging them by country name and conducting EDA on Tableau to find insights. The [dashboard](https://public.tableau.com/app/profile/niful.islam/viz/LifeQualityandCrimeRateEDA/Dashboard1) presents the following:
- Two maps presenting the life quality and crime rate
- Finding correlation between crime rate and life quality
- Among safety, rights, cost, and stability, which one is mostly impacted by crime
## Findings from the [Dashboard](https://public.tableau.com/app/profile/niful.islam/viz/LifeQualityandCrimeRateEDA/Dashboard1):
- Australians enjoy a much better quality of life than that of many developed countries such as the US, UK, Canada, and even Nordic countries do.
- Bangladesh offers the same or lower quality of life compared to some poor African countries.
- Sudan has one of the lowest qualities of life (probably due to the civil war)
- Most of the South American countries have very high crime rate.
- Saudi Arabia has one of the lowest crime rate.
- Bangladesh has one of the heigh crime rates in Asia (behind Afghanistan).
- Crime has a disproportionate relationship with overall life quality.
- Among safety, rights, costs, and stability, safety is the aspect that is mostly impacted by crime, while cost is the least impacted.
# Steps to build this project
1. Install the dependencies mentioned in requirements.txt by runnig this command
   ```
   pip install -r requirements.txt
   ```
2. Install chrome web driver. For windows, install from the website. For linux, run the following code
   ```
   sudo mv ~/Downloads/chromedriver /usr/local/bin
   sudo chmod +x /usr/local/bin/chromedriver
   ```
3. run the following commands
   ```
   python3 scrap_life_quality.py
   python3 scrap_crime_rate.py
   ```
4. Merge both the files by runnig merge.py
   ```
   python3 merge.py
   ```

