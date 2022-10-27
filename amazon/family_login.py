
import collections

def count_family_logins(logins):
    login_count = collections.Counter(logins)
    count = 0
    for i, login in enumerate(logins):
        family_login = ''
        for ch in login:
            value = ord(ch)
            if value == 122:
                new_ch = chr(97)
            else:
                new_ch = chr(value+1)
            family_login = family_login + new_ch
        if family_login in login_count:
            count += login_count[family_login]
    return count

if __name__ == '__main__':
    l = ['bag', 'sfe', 'cbh', 'cbh','red']
    l2 = ["corn", "horn", "dpso", "eqtp", "corn"]
    print(count_family_logins(l))
