from PIL import Image
import os
os.chdir('Images')
filelist = []
for c in os.listdir():
	filelist.append(c)
pil_im = Image.open('empire.png')
print(filelist)
#print(os.getcwd())
for infile in filelist:
	outfile= os.path.splitext(infile)[0] + ".jpg" # outfile = file in path jpg ending
	if infile != outfile: # if each file isnt one of the existing jpg files...
		try:
			Image.open(infile).save(outfile)
		except IOError:
			print("cannot convert", infile)

def get_imlist(path):
	"""Returns a list of filenames for all jpg images in a directory"""
	return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
print(get_imlist(os.getcwd()))

#Creating Thumbnails
pil_im.thumbnail((128,128))

#crop an image
box = (100,100,400,400)
region = pil_im.crop(box)

region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box) # rotate image and put it back

#resize and rotate
out = pil_im.resize((128,128))
out = pil_im.rotate(45)