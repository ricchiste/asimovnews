from scraping_sites.site import *
import os
from threading import Thread
import time
from datetime import datetime
import sys
import pickle
import webbrowser
from math import ceil
from pytimedinput import timedInput

class AsimovNews:
    def __init__(self):
        self.dict_site={}
        self.all_sites = ['globo', 'veja']

        self.screen = 0
        self.kill = False
        self.news = self._read_file('news') if 'news' in os.listdir() else []
        self._update_file(self.news, 'news')
        self.sites = self._read_file('sites') if 'sites' in os.listdir() else []
        self._update_file(self.sites, 'sites')

        for site in self.all_sites:
            self.dict_site[site] = Site(site)

        self.news_thread = Thread(target=self.update_news)
        self.news_thread.daemon
        self.news_thread.start()

    def _update_file(self, lista, mode='news'):
        with open(mode, 'wb') as fp:
            pickle.dump(lista, fp)

    def _read_file(self, mode='news'):
        with open(mode, 'rb') as fp:
            n_list = pickle.load(fp)
            return n_list

    def update_news(self):
        while not self.kill:
            for site in self.all_sites:
                self.dict_site[site].update_news()

                for key, value in self.dict_site[site].news.items():
                    dict_aux = {}
                    dict_aux['data'] = datetime.now()
                    dict_aux['fonte'] = site
                    dict_aux['materia'] = key
                    dict_aux['link'] = value
                    
                    if len(self.news) == 0:
                        self.news.insert(0, dict_aux)
                        continue

                    add_news = True
                    for news in self.news:
                        if dict_aux['materia'] == news['materia'] and dict_aux['fonte'] == news['fonte']:
                            add_news = False
                            break
                    if add_news:
                        self.news.insert(0, dict_aux)
            self.news = sorted(self.news, key=lambda d: d['data'], reverse = True)
            self._update_file(self.news, 'news')
            time.sleep(10)

    def _receive_command(self, valid_commands, timeout=30):
        command, timed = timedInput('>>', timeout)
        while command.lower() not in valid_commands and not timed:
            print('Comando inválido. Digite novamente!')
            command, timed = timedInput('>>', timeout)
        command = 0 if command == '' else command
        return command


    def main_loop(self):
        while True:
            os.system('cls' if os.name =='nt' else 'clear')
            
            match self.screen:
                case 0:
                    print('SEJA BEM VINDO AO ASIMOV NEWS.')
                    print('Por favor escolha algum item do menu')
                    print('')
                    print('1. Últimas notícias\n2. Adicionar site\n3. Remover sites\n4. Fechar o Programa')
                    self.screen = int(self._receive_command(['1', '2', '3', '4'], 5))
                    print(self.screen, type(self.screen))


                case 1:
                    pass
                case 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Digite um número do site que deseja adicionar para a lista de sites ativos. \nPressione 0 para voltar par ao menu.')
                    print('\tSITES ATIVOS ==========')
                    for i in self.sites:
                        print('\t', i)
                    print('\tSITES INATIVOS ==========')
                    offline_sites = [i for i in self.all_sites if i not in self.sites]
                    for i in range(len(offline_sites)):
                        print(f'\t{i+1}. {offline_sites[i]}')
                    site = int(self._receive_command([str(i) for i in range(len(offline_sites)+1)], 50))

                    if site == 0:
                        self.screen = 0
                        continue
                    self.sites += [offline_sites[site-1]]
                    self._update_file(self.sites, 'sites')

                case 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Digite o número do site para remove-lo. Caso queira voltar para o Menu, digite 0')
                    for i in range(len(self.sites)):
                        print(f'\t{i+1}. {self.sites[i]}')
                    site = int(self._receive_command([str(i) for i in range(len(self.sites)+1)], 50))
                    if site == 0:
                        self.screen = 0
                        continue
                    del self.sites[site-1]
                    self._update_file(self.sites, 'sites')

                case 4:
                    self.kill = True
                    sys.exit()

                
self = AsimovNews()
self.main_loop()