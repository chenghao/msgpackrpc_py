#coding:utf-8

import msgpack
import msgpackrpc


class DemoServer(object):

    def sum(self, x, y):
        sum = x + y
        return msgpack.packb(sum, use_bin_type=True)
        
    def hello(self, name):
        result = "hello, %s" % name
        return msgpack.packb(result, use_bin_type=True)
        
    def showUser(self, name):
        users = {}
        if name == "aaa":
            users["name"] = "aaa"
            users["age"] = 20
            users["address"] = "成都"
        return msgpack.packb(users, use_bin_type=True)    

    def uploadFile(self, binaryData, filePath, flag):    
        import os
        if flag == 0:
            if os.path.exists(filePath):
                os.remove(filePath)
        # 以追加模式+二进制模式打开
        try:
            fp = open(filePath, "ab")
            fp.write(binaryData)
        finally:
            fp.close()
        
server = msgpackrpc.Server(DemoServer())
server.listen(msgpackrpc.Address("localhost", 8888))
server.start()