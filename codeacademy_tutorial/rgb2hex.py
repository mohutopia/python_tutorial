def rgb_hex():
  invalid_msg = 'Error: Invalid Input'
  red = int(raw_input('Enter the value of red: '))
  green = int(raw_input('Enter the value of green: '))
  blue = int(raw_input('Enter the value of blue: '))
  if (0 > red or red > 255):
    print invalid_msg
    return
  if (0 > green or green > 255):
    print invalid_msg
    return
  if (0 > blue or blue > 255):
    print invalid_msg
    return
  val = (red << 16) + (green << 8) + blue
  print str((hex(val)[2:]).upper())

def hex_rgb():
  hex_val = raw_input('Enter a hexadecimal value: ')
  if len(hex_val) != 6:
    print 'Error: Invalid Input'
    return
  else:
    hex_val = int(hex_val, 16)
  
  two_hex_digits = 2 ** 8
  
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  
  red = hex_val % two_hex_digits
  print "Red: %s Green: %s Blue: %s" % (red, green, blue)
  
def convert():
  while True:
    option = 'Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: '
    if (option == '1'):
      print 'RGB to HEX...'
      rgb_hex()
    elif (option == '2'):
      print 'HEX to RGB'
      hex_rgb()
    elif (option == 'X' or option == 'x'):
      break
    else:
      print 'Error: Invalid Input'

convert()