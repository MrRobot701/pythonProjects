def equals(phone1, phone2):
    phone1 = ''.join(list(filter(lambda c: c.isdigit(), phone1)))
    phone2 = ''.join(list(filter(lambda c: c.isdigit(), phone2)))
    l1 = len(phone1)
    l2 = len(phone2)
    if l1 == l2:
        if l1 == 7:
            return phone1 == phone2
        return phone1[1:] == phone2[1:]
    elif l1 == 7:
        phone1 = "495" + phone1
        return phone1 == phone2[1:]
    elif l2 == 7:
        phone2 = "495" + phone2
        return phone2 == phone1[1:]


new_phone_number = input()
telephone_book = [input(), input(), input()]
for record in telephone_book:
    print("YES" if equals(new_phone_number, record) else "NO")
