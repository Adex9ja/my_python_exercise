# ex8_file = open('ex1_data_copy.txt', mode='w')
# print(ex8_file)
# print(type(ex8_file))
# some_jibberish = ["Doe, a deer", "a female deer", "far", "a long long way to run!"]
# for item in some_jibberish:
#     ex8_file.write(item + "\n")
# ex8_file.close()


some_jibberish = ["Doe, a deer", "a female deer", "far", "a long long way to run!"]
with open('ex1_data_copy.txt', mode='w') as f:
    print(f)
    print(type(f))
    for item in some_jibberish:
        f.write(item + "\n")

try:
    with open('./file_not_exist.txt') as f:
        pass
except FileNotFoundError as not_found:
    print('Uh ohm we are in trouble!')
    print(not_found)

def authenticate(username, password):
    if username == 'ade' and password == 'olu':
        print('Login Successful')
    else:
        print('Incorrect username/password')

authenticate('ade', 'olu')