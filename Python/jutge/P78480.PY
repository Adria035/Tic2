from easyinput import read

n = read(int)

img = Image.new('RGB', (1+n*8, 1+n*8), 'White')
dib = ImageDraw.Draw(img)

dib.ellipse([0,0,8*n,8*n],"blue")
dib.ellipse([n,n,7*n,7*n],"yellow")
dib.ellipse([2*n,2*n,6*n,6*n],"red")
dib.ellipse([3*n,3*n,5*n,5*n],"green")
dib.ellipse([3.5*n,3.5*n,4.5*n,4.5*n],"blue