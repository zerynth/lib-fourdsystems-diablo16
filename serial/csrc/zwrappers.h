
#ifndef ZWRAPPERSH
#define ZWRAPPERSH

#define write(drv, buf, num) vhalSerialWrite(drv, buf, num)
#define ReadSerPort(buf, num) vhalSerialRead(cPort, buf, num)
#define close(drv) vhalSerialDone(drv)

#endif