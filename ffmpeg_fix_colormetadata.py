import os
import subprocess
import sys




##ULTIMATE FFMPEG FIX THE PRORES FROM FUCKING NUKE FINALLY FOREVER FUCK YOU FOUNDRY

ffmpeg_bin="/coppi/global/bin/static-ffmpeg/ffmpeg-4.2.2-amd64-static/ffmpeg"

def fix_nclc(input_file, output_file, primaries, transfer, matrix, gamma):

    if primaries == 1 :
        ff_primaries="bt709"
        print("setting primaries to 1 aka bt709")
    else :
        print ("only bt709 primaries are currently supported by this script, so we will set those.. HDR comming soon as well.")
        ff_primaries="bt709"


    if transfer == 1 :
        ff_trc="bt709"
        print("setting transfercurve to 1 aka bt709")
    elif transfer == 2 :
        ff_trc="unspecified"
        print("setting transfer curve to 2 aka unspecified it Quicktime will now fallback to the gamma tag ")
    else :
        print ("only 1 or 2 for TRC are currently supported by this script, so we will set it to 2 .. HDR comming soon as well.")
        ff_trc = "unspecified"


    if matrix == 1 :
        ff_matrix = "bt709"
        print("setting colormatrix to 1 aka bt709")
    else :
        print("only bt709 matrix are currently supported by this script, so we will set those.. HDR comming soon as well.")
        ff_matrix = "bt709"

    print(ffmpeg_bin)
    print(input_file)

    ffmpeg_args = {
        "ffmpeg_bin": ffmpeg_bin,
        "input_file": input_file,
        "output_file": output_file,
        "ff_primaries": ff_primaries,
        "ff_matrix": ff_matrix,
        "gamma": gamma,
        "ff_trc": ff_trc
    }
    print(ffmpeg_args)
    ffmpeg_command = (
        '{ffmpeg_bin} -i "{input_file}" -c:v copy -c:a copy '
        '-mov_gamma {gamma} -movflags write_colr+write_gama -color_trc {ff_trc} -color_primaries {ff_primaries} -colorspace {ff_matrix}'
        ' "{output_file}" -y'
    )
    print(ffmpeg_command)
    ffmpeg_str = ffmpeg_command.format(**ffmpeg_args)
    print(ffmpeg_str)
    os.popen(ffmpeg_str)


##sample
fix_nclc("/path/to/inputMOV.mov", "/path/to/outputMOV.mov", 1, 2, 1, 2.4)

