def generate_appsflyer_link(base_path: str, allowed_path: list, url_to_wrap: str) -> str:
    """
    Wrap allowed link appsflyer for statistics
    
    Example of usage:
        apppsflyer_link = generate_appsflyer_link(base_path='https://test.onelink.com', allowed_path=['/', '/feed', '/list', '/user'], url_to_wrap='https://google.com/feed') 
    
    @ base_path: string param: https://test.onelink.me/Kefas
    @ allowed_path: list: /, feed, list, user
    @ url_to-wrap: str: https://google.com/feed
    
    If page not in allowed path: return original url
    Returning must be: https://google.com/feed -> https://test.onelink.me/Kefas?af_web_dp=https://google.com/feed&af_dp=kittify://kittify.com
    @ returning: str
    """
    for allowed in allowed_path:
      if not url_to_wrap.endswith(allowed):
        return url_to_wrap
    
    link = f'{base_path}/Kefas?af_web_dp={url_to_wrap}&af_dp=kittify://kittify.com'
    
    return link
