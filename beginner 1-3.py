x = input('')

if (x>='a' and x<='z') or (x>='A' and x<='Z'):

    if x in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
	    print('Vowel')
    else:
	    print('Consonant')
	    
else:
    print('invalid')
