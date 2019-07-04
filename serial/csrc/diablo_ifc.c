/*
* @Author: Lorenzo
* @Date:   2018-04-04 16:13:16
* @Last Modified by:   Lorenzo
* @Last Modified time: 2018-04-09 10:58:38
*/

// #define ZERYNTH_PRINTF
#include "zerynth.h"

#include <diabloSerial.h>
#include <Diablo_Types4D.h>
#include <Diablo_const4D.h>

/******* DEMO ***********/

int demo_main(void);

C_NATIVE(difc_diablodemo) {
    NATIVE_UNWARN();

    demo_main();

    return ERR_OK;
}

/****** DEMO END *********/

/******* COMMUNICATION *********/

C_NATIVE(difc_openComm) {
    NATIVE_UNWARN();

    int serdrv, serbaud;

    if (parse_py_args("ii", nargs, args, &serdrv, &serbaud) != 2)
        return ERR_TYPE_EXC;

    if (ZOpenComm(serdrv & 0xff, serbaud) < 0) {
        return ERR_IOERROR_EXC;
    }
    return ERR_OK;
}

/******* COMMUNICATION END *****/

/******* MEDIA COMMANDS **********/

C_NATIVE(difc_media_Init) {
    NATIVE_UNWARN();

    if (!media_Init()) {
        return ERR_IOERROR_EXC;
    }
    return ERR_OK;
}

/******* MEDIA COMMANDS END*******/


/******* FILE MANAGEMENT ***********/

C_NATIVE(difc_file_Mount) {
    NATIVE_UNWARN();

    if (!file_Mount()) {
        return ERR_IOERROR_EXC;
    }
    return ERR_OK;
}

C_NATIVE(difc_file_Open) {
    NATIVE_UNWARN();

    uint8_t *filename, *mode;
    uint32_t filename_len, mode_len;

    uint32_t file_handle;

    if (parse_py_args("ss", nargs, args, &filename, &filename_len, &mode, &mode_len) != 2)
        return ERR_TYPE_EXC;

    if (mode_len != 1) return ERR_TYPE_EXC;

    file_handle = file_Open((char*)filename, (char)mode[0]);
    if (!file_handle) {
        return ERR_IOERROR_EXC;
    }

    *res = PSMALLINT_NEW(file_handle);
    return ERR_OK;
}

C_NATIVE(difc_file_LoadImageControl) {
    NATIVE_UNWARN();

    uint8_t *datname, *gciname;
    uint32_t datname_len, gciname_len;
    int mode;

    uint32_t image_handle;

    if (parse_py_args("ssi", nargs, args, &datname, &datname_len, &gciname, &gciname_len, &mode) != 3)
        return ERR_TYPE_EXC;

    if (mode < 0 || mode > 2)
        return ERR_TYPE_EXC;

    image_handle = file_LoadImageControl((char *) datname, (char *) gciname, mode);
    if (!image_handle) {
        return ERR_IOERROR_EXC;
    }

    *res = PSMALLINT_NEW(image_handle);
    return ERR_OK;
}

/******* FILE MANAGEMENT END *******/

/******* IMAGE CONTROL COMMANDS ********/

C_NATIVE(difc_img_Show) {
    NATIVE_UNWARN();

    int image_handle, image_index;

    if (parse_py_args("ii", nargs, args, &image_handle, &image_index) != 2)
        return ERR_TYPE_EXC;

    if (!img_Show(image_handle, image_index)) {
        return ERR_IOERROR_EXC;
    }

    return ERR_OK;
}

C_NATIVE(difc_img_Enable) {
    NATIVE_UNWARN();

    int image_handle, image_index;

    if (parse_py_args("ii", nargs, args, &image_handle, &image_index) != 2)
        return ERR_TYPE_EXC;

    if (!img_Enable(image_handle, image_index)) {
        return ERR_IOERROR_EXC;
    }

    return ERR_OK;
}

C_NATIVE(difc_img_Disable) {
    NATIVE_UNWARN();

    int image_handle, image_index;

    if (parse_py_args("ii", nargs, args, &image_handle, &image_index) != 2)
        return ERR_TYPE_EXC;

    if (!img_Disable(image_handle, image_index)) {
        return ERR_IOERROR_EXC;
    }

    return ERR_OK;
}

/******* IMAGE CONTROL COMMANDS END ****/

/******* GRAPHICS COMMANDS *************/

C_NATIVE(difc_gfx_Cls) {
    NATIVE_UNWARN();

    gfx_Cls();

    return ERR_OK;
}

/******* GRAPHICS COMMANDS END *********/