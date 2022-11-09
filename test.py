sentence = "there are $1 $2 and 5$ candies $ma2 in the shop"
discount = int(input('Discount value:'))
s = sentence.split(" ")
#len(s)
for x in range(len(s)):
            if s[x][0] =='$':
              price = int(s[x][1:])
              new_price = ''
              new_price+=s[x][0]
              dis = (price*discount) / 100
              apply = price - dis
              apply = "{:.2f}".format(apply)
              s[x] = new_price+apply
              print(s[x])
            else:
              continue