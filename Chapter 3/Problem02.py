letter = '''  Dear <|Name|>, 
You are selected! 
<|Date|> ''' 
            
print(letter.replace('<|Name|>',input()).replace('<|Date|>',input()))