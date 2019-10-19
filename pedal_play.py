#!/usr/bin/python3
# 
# pedal_play
# Copyright (C) 2019  Markus Peröbner
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

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
