from requests import Session,Response
from .tweet import Tweet
from .errors import *
from json import JSONDecodeError

class Client(Tweet,ClientError) : 

    def __init__(self,csrf_token,auth_token,user_agent=None) : 
        self.logged_in = False
        self.session   = Session()
        self.session.headers = {'user-agent': user_agent if user_agent else "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                                'authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                                'x-csrf-token': csrf_token}
        self.session.cookies.update({'auth_token':auth_token,
                                     'ct0':csrf_token})
    


    def _handle_response(self,response : Response ,response_type : str) : 
        print(response.text)
        print(response.status_code)
        try : 
            response_json = response.json()
            data = response_json.get("data")
            if data : 
                    return True
            error = response_json.get('errors') 
            if error : 
                self._error_handler(error,response_type)
        except JSONDecodeError as e :  
            raise UnknowError(f'Unknow error occured :{response_type}')
        

    def _make_request(self,endpoint,method,params=None,data=None,json=None,graphql=True,response_type=None) : 
        if graphql : 
            url = "https://twitter.com/i/api/graphql"+endpoint
        else :
            url = "https://twitter.com/i/api/1.1"+endpoint
        if method == "GET" : 
            response =  self.session.get(url,
                                         params=params,
                                         data=data,
                                         json=json)
            return self._handle_response(response=response,response_type=response_type)
            
        elif method == "POST" : 
            response =  self.session.post(url,
                                          params=params,
                                          data=data,
                                          json=json)
            return self._handle_response(response=response,response_type=response_type)
            

