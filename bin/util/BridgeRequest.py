from time import time, sleep
from typing import Union
import configparser
import requests
import json


class BridgeRequest():
    '''
        To get the match data you have to make a /bridge
        request every 3/4mins (in a loop), and a /games
        request when you want to get the match played
        for a player.
    '''

    def __init__(self) -> None:

        self.__CONFIG_PATH = 'config\\config.ini'

        self.config = self.get_config()

        self.API_KEY = self.config[0]
        self.data_file = self.config[1]

    def get_config(self) -> tuple:
        '''
            This function returns the API key
            & the path to the players.json
            from the config.ini file.
        '''
        config = configparser.ConfigParser()
        config.read(self.__CONFIG_PATH)

        players = config['paths']['players']
        API = config['app']['API']

        return (API, players)

    def extract_json(self) -> dict:
        '''
            This function extracts all the data from the data file
            and returns a dict type object that contains the players
            to witch we are gonna send /bridge requests.
        '''
        with open(self.data_file, 'r') as f:
            return json.loads(f.read())

    def bridge_request(self,
                       platform: str,
                       players: Union[list, tuple]) -> None:
        '''
            This function makes a /bridge request for each player
            from the data file.

            Keywords arguments:
            platform -- each player has it's platform ([PC, PS4, X1])
            players -- list of players from each platform ([name1, name2, name3])
        '''
        for player in players:
            requests.get(f'https://api.mozambiquehe.re/bridge?version=5&\
                    platform={platform}&player={player}&auth={self.API_KEY}')

            sleep(0.1) # too many requests at the same time will return a error

    def run(self) -> None:
        '''This function sends a /bridge request every 3 minutes.'''
        while True:
            data = self.extract_json() # Check for updates in the data file

            for platform, players in data.items():
                self.bridge_request(platform,
                                    players)

            sleep((60*3) - time() % 60) # Wait 3 minutes

def main():
    BridgeRequest().run()

if __name__ == '__main__':
    main()
