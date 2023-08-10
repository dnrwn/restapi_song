def response(a):
    if a == 0:
        return {
            "result": "NG"
        }
    else:
        return {
            "Error"
        }


print(type(response(0)))
print(response(0))

a = response(0)
a['ddd'] = {""
            "rrr":"aa"}

print(a)