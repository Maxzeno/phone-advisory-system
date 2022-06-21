

class RecomCred(object):
    """ Base class from which all wrappers inherit."""

    def __init__(self,
                 apiKey: str=None,
                 timeout: int=None):
        """Returns a Api instance.
        Args:
          apiKey (str):
            API key.
          timeout (int):
            Timeout limit for requests.
        """

        self.__set_credentials(apiKey)
        if timeout:
            self._timeout = timeout
        else:
            self._timeout = 20


    def __set_credentials(self,
                          apiKey):
        """Setter for credentials.
        Args:
          apiKey (str):
            API key.
        """
        self._apiKey = apiKey