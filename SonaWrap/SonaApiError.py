class SonaApiError(Exception):
    def __init__(self, message, api_response): #, errors

        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        #TODO more debugging info of failed http api request
        self.api_response = api_response
        # self.errors = errors
