#!/usr/bin/env python
from pprint import pprint as pp
from ciscoconfparse import CiscoConfParse
rt_conf = CiscoConfParse('class1_ciscoconf.txt')
print (' 1. Find lines that begin with "crypto map CRYPTO" : ')
rt_cryptomap = rt_conf.find_objects(r'^crypto map CRYPTO')
#print(type(rt_cryptomap[0]))
for cry_parent in rt_cryptomap:
    print(cry_parent.text) # output the parent line
#   print(type(i.children))
    for cry_children in cry_parent.all_children: # output the children lines
        print(cry_children.text)
print

print (' 2. Find all of the crypto map entries that are using PFS group2 :')
rt_crytomappfs = rt_conf.find_objects_w_child(parentspec = r'^crypto map', childspec =r'set pfs group2')
for crypfs_parent in rt_crytomappfs:
    print(crypfs_parent.text)
    for crypfs_children in crypfs_parent.all_children:
        print(crypfs_children.text)
print    

print (' 3. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name).\n Print these entries and their corresponding transform set name.')
# find transform set without AES, save as list  transform_list
rt_crypto_transform = rt_conf.find_objects(r'crypto ipsec transform-set')
transform_list = []
for transform_set in rt_crypto_transform:
    if 'aes' in transform_set.text:
        transform_list.append(transform_set.text.split()[3]) # get item 3 from crypto ipsec transform-set AES192-SHA xxxx
#print(transform_list)

# search child with transform set names from list transform_list:
for i in transform_list:
    #print(i)
    rt_crymap_aes = rt_conf.find_objects_w_child(parentspec = r'^crypto map', childspec = i)
    for rt_crymap_aes_parent in rt_crymap_aes:
        print(rt_crymap_aes_parent.text)
        for rt_crymap_aes_children in rt_crymap_aes_parent.all_children:
            print(rt_crymap_aes_children.text)
    
