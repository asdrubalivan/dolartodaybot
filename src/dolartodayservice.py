import requests

class DolarTodayService(object):
    """Docstring for DolarTodayService. """

    def __init__(self,url):
        if not isinstance(url,str):
            raise ValueError("Only Strings allowed")
        self.url = url

    def getJSON(self):
        """Returns JSON data from Dolar Today
        :returns: dictionary with data

        """
        data = requests.get(self.url)
        return data.json()
