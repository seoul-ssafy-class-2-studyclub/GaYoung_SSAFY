user_input = '121'
user_input = user_input + '0'
answer = 'true'
for i in range(len(user_input)-1):
    if user_input[i] == '1':
        if user_input[i+1] == '1' or user_input[i+1] == '0':
            answer = 'false'
            break
print(answer)