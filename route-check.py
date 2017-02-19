#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3


def main():

    '''
    route_check.py requires a IP address  argument.
    example route_check 8.8.8.8
    '''
    import re 
    import sys
    import ssh_connect as s
    if len(sys.argv) != 2:
        print ('route-check.py <ip address>')
        sys.exit(1)

    hostname = 'route-views.oregon-ix.net'
    password = '' 
    username = "rviews"
    port = 22

# Show IP route get network
    
    command = ('show ip route '+sys.argv[1])
    print(command)
    regex = r'Routing entry for\s(.*)'
    returned_ans = s.sshconnect(hostname, port, username, password, command, regex)
    network=(returned_ans.group(1))
    network=network.replace('\r', '')
    print ('Known by ', network)

# Show IP BGP for network get Originating ASN

    command = ('{1} {0} {2} {0}'.format(network, 'show ip bgp', 'longer-prefixes | include'))
    print(command)
    regex = r'.*' + re.escape(network) + '.*(\s\d*)\s.'
    returned_ans = s.sshconnect(hostname, port, username, password, command, regex)
    print('Originating AS' + returned_ans.group(1))

# Ping destination get results
    
    command = ('ping '+sys.argv[1])
    print(command)
    regex = r'.*(Success.*)'
    returned_ans = s.sshconnect(hostname, port, username, password, command, regex)
    print(returned_ans.group(1))

main()
