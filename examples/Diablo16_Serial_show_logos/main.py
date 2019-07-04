# fourdsystems diablo16 example
# Created at 2018-04-04 14:24:13.665334

# import diablo16 serial interface lib
# note how switching from 4dsystems chips exposing the same API could be made effortless changing a single line of code
# i.e. from fourdsystems.picaso.serial import diabloserial as fourserial
from fourdsystems.diablo16.serial import diabloserial as fourserial
import streams

streams.serial()

# note: a more Pythonic interface to 4dsystems chip has been developed, but classic 4dsystems API
# is still available (openComm, file_Mount, ...)

try:
    print('> open serial')
    fourserial.init(SERIAL2, 9600)
    print('> serial open')
    fourserial.file.mount()
    print('> mounted')
    # load multiple images at once, big_logos and small_logos variables will contain an image object instance
    big_logos, small_logos = fourserial.file.load_image_control(("logos",1), ("slogos",1))
    print('> images loaded')
    while True:
        fourserial.gfx.cls()
        for i in range(3):
            # directly call img_ functions as image object methods without the need to pass an handler
            big_logos.show(i)
            sleep(1000)
        fourserial.gfx.cls()
        for i in range(3):
            small_logos.show(i)
        sleep(5000)
except Exception as e:
    print(e)