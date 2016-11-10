def remote(cmds):
    import ssh
    IP = '192.168.6.121'
    myclient = ssh.SSHClient()

    myclient.set_missing_host_key_policy(ssh.AutoAddPolicy())

    myclient.connect(IP,port=13780,username='root',password='wk5**((&6%.COM')

    stdin,stdout,stderr = myclient.exec_command(cmds)

    #return stdout.readlines()
    return  stdout.readlines()
