# nested loop = A loop within another loop ( outer, inner)
#               outer loop:
#                   inner loop:
# basically a loop inside a loop
# A while loop inside a while loop or a for loop inside a for loop
# or even while loop inside for loop and vice versa

for x in range(3): # ye outer loop hai iska kaam basically ye hai ki ye aandr wale loop aur print ko command dega jaise yaha pe x=3 hai i.e inner loop + print 3 baar chalega(SORRY IT'S IN HINDI BUT YOU CAN TRANSLATE IT FROM ANY TRANASLATOR)
    for y in range(1, 11): # harr outer loop ke liye ye ek ek chalega ( outer loop x =3)
        print(y, end=" ")  # normally print() harr naya line ke baad ek new line deta hai but end tag ki wajah se ek sath print ho rha

    print() # ye sirf naya line dalta hai so that each outer loop ka result next line me aa sakke ( for clear output)


