import dns.resolver
domain = "www.baidu.com"
A = dns.resolver.query(domain, 'A')


# for i in A.response.answer:
#     for j in i.items:
#         print(j)


print("qname:" , A.qname)
print("reclass:", A.rdclass)

