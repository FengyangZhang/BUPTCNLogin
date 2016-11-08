import sys
import getopt
import urllib
import urllib2

def main(argv):
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)
    # Fill in the username, passwd, host and loginurl yourself.
    username=''
    passwd=''
    loginurl=''
    host=''

    try:
        opts, args = getopt.getopt(argv, "hu:p:l:o:", ["username=", "passwd=", "loginurl=", "host="])
    except getopt.GetoptError:
        print 'POST.py -u <username> -p <passwd> -l <loginurl> -o <host>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'POST.py -u <username> -p <passwd> -l <loginurl> -o <host>'
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--passwd"):
            passwd = arg
        elif opt in ("-l", "--loginurl"):
            loginurl = arg
        elif opt in ("-o", "--host"):
            host = arg
    try:
        data =  {'DDDDD':username,'upass':passwd, '0MKKey':''}
        data = urllib.urlencode(data)
        header = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            'Connection':'keep-alive',
            'Host':host,
            'Origin':loginurl,
            'Referer':loginurl,
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded',
            'Content-Length':'37',
            'X-Requested-With':'XMLHttpRequest',
        }
        req = urllib2.Request(
                        url = loginurl,
                        data = data,
                        headers = header
                    )
        response = urllib2.urlopen(req)
        print response.read()
    except urllib2.HTTPError, e:
        print 'error', e.code


if __name__ == "__main__":
    main(sys.argv[1:])