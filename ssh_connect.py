#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
'''
ssh module using that uses the Paramiko libary
'''


def sshconnect(hostname, port, username, password, command, regex):
    '''
    sshconnect takes in the following parameters
    (hostname, port, username, password, command, regex),
    and will return a re.match'ed groups as returned_ans.
    '''
    import re
    import paramiko
    import sys
    import time

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
        client.connect(hostname, port=port, username=username, password=password)
        time.sleep(10)
        sys.stdout.flush()
        stdin, stdout, stder = client.exec_command(command)
      
        output = stdout.readlines()

        for line in output:
            print(line)
            matched = re.match(
                regex, line)
            if matched:
                break
        returned_ans = (matched)
    finally:
        client.close()
    
    return returned_ans
