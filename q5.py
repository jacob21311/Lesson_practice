
# 輸入Email地址，判斷是自定義域還是熱門域名稱
# get user email address
email = input("what is your email address?: \n").strip()   # strip表示去除前後空白處

# slice out the user name 切割出小老鼠以前的用戶名稱
user_name = email[0:email.index('@')]

# slice out the domain name 切割小老鼠後網域的名稱
domain_name = email[email.index('@')+1:len(email)]

# Format message
output = 'Your username is "{}" and your domain name is "{}"'.format(user_name,domain_name)
print(output)

# 區別屬於哪一個網域
domain = {'gmail.com':'Google','yahoo.com.tw':'Yahoo','hotmail.com':'Hotmail'}
if domain_name in domain:
    output = '這是註冊在{}底下的email地址'.format(domain[domain_name])
else:
    output = '這是在{}之下自定義域'.format(domain_name)
print(output)







