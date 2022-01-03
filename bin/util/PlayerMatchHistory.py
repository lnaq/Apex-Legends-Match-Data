from time import time, sleep
import configparser
import requests
import json

class GetPlayerMatchHistory():
    '''
        This class returns the match history of any tracked
        player.

        Functionallity:
        We first get the API key and the players.json path
        from the config.ini file.

        We asked the player's name & platform in order to
        get it's uid. Using the player_to_uid function
        it than makes a /nametouid request to get the
        player's uid using the player's name & platform
        and converts it into a dictionary.

        It than determines whether the user's
        platform is PC or another one ie: (PS4, X1).
        If the player's platform is "PC" than the
        uid key it's gonna be "uid" otherwise the
        uid it's gonna be "result".

        After returning the uid we make a /games
        request to get the player's match history
        using the earlier acquired uid and it
        returns a dict type object.

        Example:
        player = belleeunHeart
        platform = PC

        Example Output:
        {match_result: 2, kills: 1}
    '''
    def __init__(self) -> dict:

        self.__CONFIG_PATH = 'util\\config\\config.ini'
        self.API_KEY = self.get_api_key()

    def get_api_key(self) -> str:
        '''
            This function returns the API key
            from the config.ini file.
        '''
        config = configparser.ConfigParser()
        config.read(self.__CONFIG_PATH)

        API = config['app']['API']

        return API

    def player_to_uid(self,
                      player: str,
                      platform: str) -> str:
        '''
            This function returns the uid of any tracked
            player.

            It sends a request with the player's name &
            platform and we recive a respond that then
            get's converted into json format.

            If the tracked player's platform is
            PC than the uid key it's gonna be "uid"
            otherwise the uid it's gonna be "result".

            Keywords arguments:
            player -- player's in game name
            platform -- player's platform (PC, PS4 or X1)
        '''

        uid_request = requests.get(f'https://api.mozambiquehe.re/nametouid? \
                    player={player}&platform={platform}&auth={self.API_KEY}')

        uid_json  = uid_request.json() # Converts request to json

        try:
            if platform == 'PC':
                return uid_json['uid'] # PC uid
            else:
                return uid_json['result'] # Console UID
        except Exception as err:
            raise Exception(f"Player's name or platform does not exist: {err}")

    def get_match_history(self,
                          player: str,
                          platform: str) -> dict:
        '''
            This function returns the match history
            of any tracked player.

            We frist get the player's uid using
            the player_to_uid function. Then it
            makes a /games request to get the
            player's match history using the
            earlier acquired uid and it returns
            a dict type object.

            Keywords arguments:
            player -- player's in game name (John Doe)
            platform -- player's platform (PC, PS4 OR X1)
        '''
        # Get the player's uid
        player_uid = self.player_to_uid(player,
                                        platform)

        # Make /games request in order to get the match history
        match_history = requests.get(f'https://api.mozambiquehe.re/games?\
                                       auth={self.API_KEY}&uid={player_uid}')

        # Return the match history as a dict type object
        return match_history.json()
