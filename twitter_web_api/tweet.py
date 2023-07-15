class Tweet : 
    def favorite_tweet(self,tweet_id) :
        json_data = {
            'variables': {'tweet_id': str(tweet_id),},
            'queryId': 'lI07N6Otwv1PhnEgXILM7A',
            }
        return self._make_request(endpoint="/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet",
                                   method  ="POST",
                                   json    = json_data,
                                   response_type="favorite_tweet")
    def unfavorite_tweet(self,tweet_id) : 
        json_data = {
            'variables': {'tweet_id': str(tweet_id),},
            'queryId': 'ZYKSe-w7KEslx3JhSIk5LA',
            }
        return self._make_request(endpoint="/ZYKSe-w7KEslx3JhSIk5LA/UnfavoriteTweet",
                                   method  ="POST",
                                   json    = json_data,
                                   response_type="unfavorite_tweet")
    