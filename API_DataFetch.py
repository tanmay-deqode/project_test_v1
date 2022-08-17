from pandas import DataFrame
import pandas as pd
import requests
import schedule

from bs4 import BeautifulSoup


class API_DataFetch:

    def fetching_data():

        # data = "https://realpython.github.io/fake-jobs/"
        data = "https://www.imdb.com/search/title/?release_date=2022&sort=num_votes,desc&page=1"

        page = requests.get(data)

        soup = BeautifulSoup(page.content, "html.parser")

        movie_containers = soup.find_all(
            'div', class_='lister-item mode-advanced')

        print(len(movie_containers))

        names = []
        years = []
        imdb_ratings = []
        metascores = []
        votes = []

        # Extract data from individual movie container

        for container in movie_containers:
            if container.find('div', class_='ratings-metascore') is not None:
                name = container.h3.a.text
                names.append(name)
                year = container.h3.find(
                    'span', class_='lister-item-year').text
                years.append(year)
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)
                m_score = container.find('span', class_='metascore').text
                metascores.append(int(m_score))
                vote = container.find('span', attrs={'name': 'nv'})[
                    'data-value']
                votes.append(int(vote))

        test_df = pd.DataFrame({'movie': names,
                                'year': years,
                                'imdb': imdb_ratings,
                                'metascore': metascores,
                                'votes': votes
                                })
        print(test_df.info())
        print(test_df)

        test_df.to_csv("./data/test_df.csv")


if __name__ == '__main__':
    obj = API_DataFetch
    schedule.every(12).hours.do(obj.fetching_data)
    # schedule.every(1).seconds.do(obj.fetching_data)

    while True:
        schedule.run_pending()
