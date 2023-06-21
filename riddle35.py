'''
Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.

The first iteration is only a single dot. On the second, there are 6 dots. 
On the third, there are 16 dots, and on the fourth there are 31 dots.

Return the number of dots that exist in the whole pentagon on the Nth iteration.

pentagonal(1) ➞ 1

pentagonal(2) ➞ 6

pentagonal(3) ➞ 16

pentagonal(8) ➞ 141
--------------------------------------------------------------------------------------------------------------------------------------

Brain-storming!!

- pentagons have 5 sides
- each side increase by 1 from its inner serface
- like this i have to see for each layer !!

1 line = has how many dots ??(claculate)
if layer 3 then 1 line = 2 dots 
if layer 2 then 1 line = 1 dot

so, therefore no. of layer = (no. of layers - 1 )dots 

'''

layers = 3


def layer_dots(layer):
    pantagonSide = 5
    if layer == 1:
        totalDots = 1
    else:
        dots =  layer-1
        totalDots = pantagonSide * dots
    return totalDots

def final_function(no_layers):
    individual_layer = list(range(1,no_layers+1))
    total_dots = 0
    for i in individual_layer:
        total_layer_dots = layer_dots(i)
        total_dots = total_layer_dots + total_dots
    return total_dots

ans = final_function(layers)
print(ans)
