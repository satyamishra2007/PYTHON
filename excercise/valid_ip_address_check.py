"""
Valid IP Address check

"""

def validIpAdresscheck(ip):
    ip_part = ip.split('.')
    flag = 0
    if len(ip_part) != 4:
        return False

    else:
        for s in ip_part:
            if s.isdigit():
                if s < 0 and s > 128:
                    flag = 1
            else:
                return False
        #print(flag)
        return False if flag == 1 else True


print(validIpAdresscheck('123.abc.0.1'))

