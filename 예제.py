import re

pattern = re.compile(r'(\d{3})-(\d{3,4})-(\d{4})')

phone_number = '010-1234-5678'
match = pattern.match(phone_number)
if match:
    print('유효한 전화번호입니다.')
    area_code = match.group(1)
    exchange_code = match.group(2)
    subscriber_number = match.group(3)
    print('지역 코드:', area_code)
    print('국번:', exchange_code)
    print('가입자 번호:', subscriber_number)
else:
    print('유효하지 않은 전화번호입니다.')
