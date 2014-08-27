#coding:utf-8

import msgpack
import msgpackrpc

def run_call_async():
    client = msgpackrpc.Client(msgpackrpc.Address("localhost", 8888))
    
    future = client.call_async('sum', 45, 49)
    sum = future.get()
    print msgpack.unpackb(sum, encoding='utf-8')
    
    future = client.call_async('hello', "chenghao")
    hello = future.get()
    print msgpack.unpackb(hello, encoding='utf-8')
    
    future = client.call_async('showUser', "aaa")
    showUser = future.get()
    print msgpack.unpackb(showUser, encoding='utf-8')
    
    sourceFilePath = "E:\\logs\\xiaohuoban.log.1"
    targetFilePath = "xiaohuoban_t1.log"
    bufsize = 1024 * 10
    flag = 0
    try:
        fp = open(sourceFilePath, "rb")
        while True:
            filedata = fp.read(bufsize)
            if not filedata:
                break
            client.call('uploadFile', filedata, targetFilePath, flag)
            flag += 1

        print "success"
    finally:
        fp.close()
    
run_call_async()