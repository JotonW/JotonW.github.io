import qrdecode
import ybc_box as box
def decode(filename):
   res = qrdecode.decode(filename)
   return res
filename = box.fileopenbox()
if filename != None:
   url = decode(filename)
   print(url)