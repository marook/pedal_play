#!/usr/bin/python3
import os
import time
import vlc

play_file_path = os.path.join(os.path.expanduser('~'), '.local', 'var', 'pedal_play', 'play')

def main(file_path):
    play_file(file_path)

def play_file(file_path):
    file_abs_path = os.path.abspath(file_path)
    p = vlc.MediaPlayer('file://{}'.format(file_abs_path))
    p.play()
    print('Ready to play')
    while p.get_time() <= p.get_length():
        last_play_request = play_file_age()
        if last_play_request is None or last_play_request > 0.3:
            p.set_pause(True)
        else:
            p.set_pause(False)
        time.sleep(0.1)
    
def play_file_age():
    try:
        s = os.stat(play_file_path)
    except FileNotFoundError:
        return None
    return time.time() - s.st_mtime
    
if __name__ == '__main__':
    import sys
    main(sys.argv[1])
