def main():
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z' ]
    number = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
    phone = input("Enter a phone number in the format xxx-xxx-xxxx: ").lower()
    i = 0
    for i in range(len(phone)):
        if phone[i].isalpha():
            print(number[alpha.index(phone[i])])
        else:
            print(phone[i])

