weight = int(input("Enter Weight :"))
unit = input(" (L) lbs (k)kg:")

if unit.lower() == 'l':
   ans = weight * 0.45
   print(f'you are {ans} kilos')
else:
    ans = weight / 0.45
    print(f'you are {ans} pounds')
