from PIL import Image
from pylab import *
#read an image to array
im = array(Image.open('Images/empire.jpg'))

#plot the image
imshow(im)


#some points
x = [100,100,400,400]
y = [200,500,200,500]

#plot the points with red-star markers
plot(x,y,'r*')

#line plot connecting the first two points
plot(x[:2],y[:2])

# add title and show the plot
title('Plotting: "empire.jpg"')
show()

axis('off')

#Commands
# plot(x,y) #default blue solid line

# plot(x,y,'r*') # red star-markers

# plot(x,y,'go-') # green line with circle-markers

# plot(x,y,'ks:') # black dotted line with square-markers

#Image contours and histograms

# #color
# 'b' = blue
# 'g' = green
# 'r' = red
# 'c' = cyan
# 'm' = magenta
# 'y' = yellow
# 'k' = black
# 'w' = white

# # line style
# '-' = solid
# '--' = dashed
# ':' = dotted

# #marker
# '.' = point
# 'o' = circle
# 's' = square
# '*' = star
# '+' = plus
# 'x' = x

im = array(Image.open('Images/empire.jpg').convert('L'))

#create a new figure
figure()
#dont use colors
gray()
# show contours with origin upper left corner
contour(im, origin='image')
axis('equal')
axis('off')
show()

imshow(im)
# print('Please click 3 points')
# x = ginput(3)
# print('You clicked:',x)
show()