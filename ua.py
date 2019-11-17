from fake_useragent import UserAgent

ua = UserAgent()

for i in range(0, 10):
    random_ua = ua.random
    print(random_ua)

