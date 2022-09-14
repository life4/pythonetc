---
published: 2020-11-17
id: 632
author: orsinium
topics:
  - stdlib
  - module
qname: ipaddress
python: "3.3"
---

# ipaddress

[ipaddress](https://docs.python.org/3/library/ipaddress.html) provides capabilities to work with IP addresses and networks (both IPv4 and IPv6).

```python
ip = ipaddress.ip_address('127.0.0.1')
ip.is_private     # True
ip.is_loopback    # True
ip.is_global      # False
ip.is_multicast   # False
ip.is_reserved    # False
ip.is_unspecified # False
ip.reverse_pointer # '1.0.0.127.in-addr.arpa'

net = ipaddress.ip_network('192.168.0.0/28')
net.is_private    # True
net.hostmask      # IPv4Address('0.0.0.15')
net.num_addresses # 16
```
