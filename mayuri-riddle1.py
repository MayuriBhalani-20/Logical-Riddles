'''
Question: given input is [-1,0,5,12,3,9] and the output is [0,1,9,25,81,144]
write the logic for the given question.
'''


a = [-1, 0, 5, 12, 3, 9]
def function(a):
   i = 0
   j = 1
   ans = []

   abc = 0
   pqr = 0
   count = 0
   while i < len(a):
      if len(a) == 1:
         abc = a[i] ** 2
         pqr = a[i]
         ans.append(abc)
         break
      else:
         if count == 0:
            if a[i] ** 2 >= a[j] ** 2:
                  abc = a[j] ** 2
                  pqr = a[j]
                  j += 1
            else:
                  abc = a[i] ** 2
                  pqr = a[i]
                  j += 1
         else:
            if abc >= a[j] ** 2:
               abc = a[j] ** 2
               pqr = a[j]
               j += 1
            else:
               j += 1
         count += 1
         if j >= len(a):
            ans.append(abc)
            j = 1
            a.remove(pqr)
            count = 0
            continue
         else:
            continue
   return ans

print(function(a))