#!/usr/bin/env  python
def logs():
    h = open('./source/www.log')
    loglist=[]
    for _str in h:
        _ip = _str.split(' ')[0]
        _url = _str.split(' ')[6]
        _code = _str.split(' ')[8]
        _status = _str.split(' ')[8]
        _list = [_ip,_url,_code,_status]  
        loglist.append(_list)
    h.close()
    return loglist[:10]
logs()
