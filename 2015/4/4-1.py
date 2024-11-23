import hashlib

key = "bgvyzdsv"
flag = 0
step = 1

while flag == 0:
    result = hashlib.md5(f"{key}{step}".encode())
    hex_result = result.hexdigest()
    if hex_result[:5] == "00000":
        flag = 1
    else:
        step += 1

print(f"Lowest positive number: {step}")
