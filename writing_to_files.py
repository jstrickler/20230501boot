colors = ['red', 'green', 'purple', 'orange', 'brown',
          'black', 'olive', 'navy', 'white', 'black',
          'pink', 'chartreuse']

with open('colors.txt', "w") as colors_out:
    for color in colors:
        colors_out.write(color + '\n')
