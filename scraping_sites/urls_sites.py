import requests
from bs4 import BeautifulSoup

class Site:
    # Função Inicial
    def __init__(self, site):
        self.site = site
        self.news = []
    # Função para ler todo o site, processar, entender e retornar o conteúdo
    def update_news(self):
        if self.site.lower() == 'globo':
            url = 'https://www.globo.com/'
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
            page = requests.get(url, headers=browsers)

            resposta = page.text
            soup = BeautifulSoup(resposta, 'html.parser')
            noticias = soup.find_all('a')

            tg_class1 = 'post__title'
            tg_class2 = 'post-multicontent__link--title__text'

            news_dict_globo = {}
            for noticia in noticias:
                if noticia.h2 != None:
                    if tg_class1 in noticia.h2.get('class') or tg_class2 in noticia.h2.get('class'):
                        news_dict_globo[noticia.h2.text] = noticia.get('href')

            self.news = news_dict_globo
            news_dict_globo

        if self.site.lower() == 'veja':     
            url = 'https://veja.abril.com.br/'
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
            page = requests.get(url, headers=browsers)
            
            resposta = page.text
            soup = BeautifulSoup(resposta, 'html.parser')
            noticias = soup.find_all('a')

            tg_class1 = 'related-article'
            tg_class2 = 'title'

            news_dict_veja = {}

            for noticia in noticias:
                if (noticia.get('class') != None) and (tg_class1 in noticia.get('class')):
                    news_dict_veja[noticia.text] = noticia.get('href')
                if (noticia.h2 != None) and (noticia.h2.get('class') != None) and (tg_class2 in noticia.h2.get('class')):
                    news_dict_veja[noticia.h2.text] = noticia.get('href')
                if (noticia.h3 != None) and (noticia.h3.get('class') != None) and (tg_class2 in noticia.h3.get('class')):
                    news_dict_veja[noticia.h3.text] = noticia.get('href')
                if (noticia.h4 != None) and (noticia.h4.get('class') != None) and (tg_class2 in noticia.h4.get('class')):
                    news_dict_veja[noticia.h4.text] = noticia.get('href')

            self.news = news_dict_veja
            news_dict_veja
        if self.opcao.lower() == 'cnn':
            url = 'https://www.cnnbrasil.com.br/'
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
            page = requests.get(url, headers = browsers)

            resposta = page.text
            soup = BeautifulSoup(resposta, 'html.parser')
            noticias = soup.find_all('a')

            target_class_1 = 'headline__primary_title'
            target_class_2 = 'home__title'
            target_class_3 = 'articles__title'
            target_class_4 = 'webstories_title'
            news_dict_cnn = {}

            for i in range(len(noticias)):
                if (noticias[i].h2 != None) and (noticias[i].h2.get('class') != None) and (target_class_1 in noticias[i].h2.get('class')):
                    news_dict_cnn[noticias[i].h2.text] = noticias[i].get('href')
                if noticias[i].h3 != None and (noticias[i].h3.get('class') != None):
                    if target_class_2 in noticias[i].h3.get('class'):
                        news_dict_cnn[noticias[i].h3.text] = noticias[i].get('href')
                    if target_class_3 in noticias[i].h3.get('class'):
                        news_dict_cnn[noticias[i].h3.text] = noticias[i].get('href')
                    if target_class_4 in noticias[i].h3.get('class'):
                        news_dict_cnn[noticias[i].h3.text] = noticias[i].get('href')

            self.news = news_dict_cnn
            news_dict_cnn


self = Site('veja')
