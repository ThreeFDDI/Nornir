#!/usr/local/bin/python3

'''
This script is used to update BGP route mapper
'''

from datetime import datetime
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks import text, files
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command
from pprint import pprint as pp
from ttp import ttp

# TODO get BGP config

# TODO get BGP summary

# TODO how to deal with multiple peers

# TODO get existing route maps

# TODO build new route maps

# TODO set communities

# TODO apply new route maps

# TODO verify route maps applied


#def grab_info(task):
    # show commands to be run
#    cmd = "show run | section bgp"

#    bgp_config = task.run(
#        task=netmiko_send_command, 
#        command_string=cmd,
#        )
    
    #print(bgp_config.result)
#    for line in bgp_config.result:
#        print(line)
        
#    commands = [
#        "show route-map",
#        "show routeIN in
#        "show route-description MPLS
#        "show ip bgp summary",
#        "show ip bgp neighbor",
#        ]

    # loop over commands
#    for cmd in commands:
#        # send command to device
#        output = task.run(
#            task=netmiko_send_command, 
#            command_string=cmd,
#            use_textfsm=True
#            )
#
#        for thing in output.result:
#            #pp(thing)
#            #print()
#            continue

def main():
    # initialize The Norn
    nr = InitNornir()
    # filter The Norn
    nr = nr.filter(platform="cisco_ios")
    # run The Norn
#    nr.run(task=grab_info)

    fake_bgp = """
    router bgp 65000
     network 10.10.192.0 mask 255.255.255.0
     network 10.10.193.0 mask 255.255.255.0
     network 10.10.194.0 mask 255.255.255.0
     aggregate-address 10.10.192.0 255.255.240.0 summary-only
     neighbor 11.11.11.11 remote-as 65111
     neighbor 11.11.11.11 next-hop-self
     neighbor 11.11.11.11 route-map VERIZON_OUT out
     neighbor 11.11.11.11 route-map VERIZON_IN in
     neighbor 11.11.11.11 route-map description MPLS1
     neighbor 22.22.22.22 remote-as 65222
     neighbor 22.22.22.22 route-map ATT_OUT out
     neighbor 22.22.22.22 route-map ATT_IN in
     neighbor 22.22.22.22 route-map description MPLS2
     neighbor 33.33.33.33 remote-as 65333
     neighbor 33.33.33.33 route-map CenturyLink_OUT out
     neighbor 33.33.33.33 route-map CenturyLink_IN in
     neighbor 33.33.33.33 route-map description MPLS3
    """

    ttp_template = """
    <group name="neighbors">
     neighbor {{ neighbor }} remote-as {{ remote_as }}
     neighbor {{ neighbor }} route-map {{ route_map_out }} out
     neighbor {{ neighbor }} route-map {{ route_map_in }} in
     </group>
    """

    parser = ttp(data=fake_bgp, template=ttp_template)
    parser.parse()
    print(parser.result(format='json')[0])



    print("\n\n")
if __name__ == "__main__":
    main()