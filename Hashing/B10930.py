# BOJ 문제
# 문자열 s가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 문자열 s를 입력
# s는 알파벳 대문자와 소문자, 그리고 숫자로만 이루어져 있으며, 길이는 최대 50
# 첫째 줄에 s의 SHA-256 해시값을 출력

import hashlib

string = str(input())

encode_string = string.encode()
sha256_string = hashlib.sha256(encode_string).hexdigest()

print(sha256_string)