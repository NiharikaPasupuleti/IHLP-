import socket
ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 8000

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
card_suit= 'Diamonds'
used_cards= []
length = len(cards)
print(length)
i =0
while i<length:
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
    Input = input('Hello: Select a card \n{}'.format(cards))
    print(Input)
    input_value= cards.index(Input) +1
    card_sent = (input_value,card_suit)
    if Input in cards and Input not in used_cards:
        used_cards.append(Input)
        print('in')
        ClientMultiSocket.send(str.encode(str(card_sent)))
        i=i+1
    else:
        print('Card has been already used')
        print(used_cards)
        





