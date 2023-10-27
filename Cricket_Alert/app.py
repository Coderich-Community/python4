from bs4 import BeautifulSoup
import requests

url = 'https://sports.ndtv.com/cricket/live-scores'
html_text = requests.get(url).text

print(html_text)                # web scraping tool

soup = BeautifulSoup(html_text, "html.parser")
sections = soup.find_all('div', class_='sp-scr_wrp ind-hig_crd vevent')

if len(sections) > 0:
    for section in sections:
        description = section.find('span', class_='description').text
        location = section.find('span', class_='location').text
        current = section.find('div', class_='scr_dt-red').text
        link = "https://sports.ndtv.com/" + section.find('a', class_='scr_ful-sbr-txt').get('href')

        try:
            status = section.find_all('div', class_="scr_dt-red")[1].text
            block = section.find_all('div', class_='scr_tm-wrp')
            team1_block = block[0]
            team1_name = team1_block.find('div', class_='scr_tm-nm').text
            team1_score = team1_block.find('span', class_='scr_tm-run').text
            team2_block = block[1]
            team2_name = team2_block.find('div', class_='scr_tm-nm').text
            team2_score = team2_block.find('span', class_='scr_tm-run').text

            print("Match Description:", description)
            print("Location:", location)
            print("Status:", status)
            print("Current Score:", current)
            print("Team 1:", team1_name.strip())
            print("Team 1 Score:", team1_score.strip())
            print("Team 2:", team2_name.strip())
            print("Team 2 Score:", team2_score.strip())
            print("Link:", link)
            print("\n")
        except:
            print("Data not available")
else:
    print("No live scores found on the page.")
