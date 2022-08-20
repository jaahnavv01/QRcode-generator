#install python package - qrcode
#using "pip intsall qrcode"
#import the module

import qrcode

data =  "https://github.com/jaahnavv01"

x = qrcode.QRCode(version=1, box_size=16, border=4)

x.add_data(data)
x.make(fit = True)

img = x.make_image(fill_color = 'white', back_color = 'black')

img.save("my github link.jpg")
