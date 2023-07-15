class ClientError(Exception) : 
    def __init__(self,message) : 
        self.message = message
    def _error_handler(self,error:list,response_type) : 
        if "was not found in actor" in error[0]['message'].lower() and response_type == "unfavorite_tweet" : 
            raise AlreadyUnfavorited("The tweet has already unfavorited.")
        elif "has already favorited tweet" in error[0]['message'].lower() : 
            raise AlreadyFavorited("The tweet has already favorited.")
        elif "NumericString value expected".lower() in error[0]['message'].lower() or "' not found" in error[0]['message'].lower() :
            raise TweetNotFound('There is no tweet with the entered tweet_id.') 
        elif "Could not authenticate you".lower() == error[0]["message"].lower() : 
            raise InvalidAuthToken(f'Invalid auth_token.{error[0]["message"]}.') 
        elif "This request requires a matching csrf cookie and header.".lower() == error[0]["message"].lower() : 
            raise InvalidCSRFToken(f'Invalid csrf_token.{error[0]["message"]}.') 
        elif "Invalid or expired token".lower() == error[0]["message"].lower() : 
            raise InvalidBearerToken(f'Invalid bearer_token.{error[0]["message"]}.') 

class AlreadyFavorited(ClientError) : 
    "Raise when a tweet that has already favorited."
    pass
class TweetNotFound(ClientError) : 
    "Raise when a tweet not found."
    pass
class AlreadyUnfavorited(ClientError) : 
    "Raise when a tweet that has already unfavorited."
    pass
class InvalidAuthToken(ClientError) : 
    "Raise when auth_token is invalid."
    pass
class InvalidCSRFToken(ClientError) : 
    "Raise when csrf_token is invalid."
    pass
class InvalidBearerToken(ClientError) : 
    "Raise when bearer_token is invalid."
    pass
class UnknowError(ClientError) : 
    "Raise when we face unknown errors."
    pass