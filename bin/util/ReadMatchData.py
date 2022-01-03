from typing import Union

class ReadMatchData:

    def __init__(self,
                 match_history: dict,
                 *filters: Union[str, tuple[str]]):

        self.match_history = match_history
        self.filters = filters

    def get_graph_info(self,
                       filtered_data: dict) -> dict:
        '''
            This function gets the data that is essential
            to make graphs like the name and the filtered
            data arguments.

            Keywords arguments:
            filtered_data -- it's the filtered data that
                             it's needed to make graphs.
        '''

        arguments = [str(arg) for arg in self.filters]
        name = self.match_history[0]['name']

        info = {'arguments': arguments, 'name': name}

        return info

    def filter_match_data(self) -> dict:
        '''
            This function filters the data from a given file
            and returns a dict type object. A nested dict
            will not work because the data that is currenetly
            being stored in there is irelevant for the project.
            An example will be: 'cosmetics'; therefore the
            data stored in the cosmetics dict it's irelevant
            to us.

            Keywords arguments:
            match_history -- A dictionary with the match
                          -- history of any given player.

            filters       -- A tuple of arguments called filters
                          -- in order to filter the data and
                          -- return a new dict only with the
                          -- relevant match data.
        '''

        filtered_data = {
            filter: [
                match[filter]
                for match in self.match_history[0::]
            ]
            for filter in self.filters
        }

        info = self.get_graph_info(filtered_data)

        return (filtered_data, info)
