#!/usr/bin/env python

import subprocess

DURATION_TIC = 0.1
DURATION_TAC = 0.1
DURATION_PAUSE = 0.9  # fill 1 second

FREQUENCY_TIC = 1760  # A6
FREQUENCY_TAC = 220
FREQUENCY_PAUSE = 0  # silence

PLAY_COMMAND = "play -n"
SIGNAL_ARGS_STR = "synth {duration} sin {frequency}"

TIC = SIGNAL_ARGS_STR.format(duration=DURATION_TIC, frequency=FREQUENCY_TIC)
TAC = SIGNAL_ARGS_STR.format(duration=DURATION_TAC, frequency=FREQUENCY_TAC)
PAUSE = SIGNAL_ARGS_STR.format(duration=DURATION_PAUSE,
                               frequency=FREQUENCY_PAUSE)

#  inn = 10
#  out = 10
#  breathes = 10
out = 4
after_out_retention = 4
inn = 4
after_in_retention = 4
breathes = 3


def make_code(times, string=True):
    code_list = list()

    for i in range(times):
        if i == 0:
            code_list = [TAC, PAUSE]
        else:
            code_list.extend([TIC, PAUSE])

    if string:
        code = " : ".join(code_list)
        return code

    else:
        return code_list

out_list = make_code(times=out, string=False)
after_out_list = make_code(times=after_out_retention, string=False)
in_list = make_code(times=inn, string=False)
after_in_list = make_code(times=after_in_retention, string=False)

pargs = {"end": "\n" * 2}

print("in: ", in_list, **pargs)
print("after in: ", after_in_list, **pargs)
print("out: ", out_list, **pargs)
print("after out: ", after_out_list, **pargs)

full_list = list()
for full in range(breathes):
    full_list.extend(out_list)
    full_list.extend(after_out_list)
    full_list.extend(in_list)
    full_list.extend(after_in_list)

full_str = " : ".join(full_list)

command = f"{PLAY_COMMAND} {full_str}".split(' ')

print("command is:", ' '.join(command))

# https://docs.python.org/3/library/subprocess.html#subprocess.run
subprocess.run(command, capture_output=True)
