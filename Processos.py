import datetime
import math
import platform
import socket
import sys
import psutil
from typing import List


def gravarlog(self, status) -> None:
    if sys.platform == "win32":
        path = r'.\errorLog.txt'
    else:
        path = r'./paradoerrorLog.log'

    if status == "Sucess":
        if sys.platform == "win32":
            path = r'.\sucessLog.txt'
        else:
            path = r'./sucessLog.log'

    data_format = "%Y-%m-%d %H:%M:%S"  # ano-mês-dia hora:min:seg
    data = datetime.datetime.now().strftime( data_format )
    log = f"{data} {status} ({self.host},{self.name}, {int( self.memory )}, {int( self.cpu )}, {self.user}, {self.bytesRecv}, {self.bytesSent}, {self.ip}, {int( self.hd )}, {self.ProcessoTop}\n"
    try:

        with open( path, 'a' ) as f:
            f.writelines( log )
    except (IOError, OSError) as e:
        print( e )

