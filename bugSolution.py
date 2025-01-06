def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or another appropriate default value or error handling

result = function(10, 0)
print(result) # Output: 0