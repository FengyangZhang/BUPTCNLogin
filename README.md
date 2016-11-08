# BUPTCNLogin
## Automatic login for BUPT Campus Network written in python

一点微小的脚本，省了每次开机都要手动登陆的麻烦。
命令行直接调用:

    POST.py -u <username> -p <passwd> -l <loginurl> -o <host>
    
要开机自动运行，linux写到.bashrc:
    
    python POST.py -u <username> -p <passwd> -l <loginurl> -o <host>

windows可能稍微麻烦一点了，至少win10家庭版比较麻烦。

注意用的是python2。


//TODO:
    
    
    1. 加个文件保存加密后的上次调用的参数，这样没有填参数的也不用每次填参数。
    
    
    2. 加个自动找出loginurl和host的地址的脚本，减少两个手动填的参数。
