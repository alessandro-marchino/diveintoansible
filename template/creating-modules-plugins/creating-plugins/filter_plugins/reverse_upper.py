# (c) 2012, Jeroen Hoekx <jeroen@hoekx.be>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

import uuid

from ansible.utils.display import Display

display = Display()

UUID_NAMESPACE_ANSIBLE = uuid.UUID('361E6D51-FAEC-444A-9079-341386DA8E2E')

def reverse_upper(string):
    ''' Reverse and upper string '''
    return string[::-1].upper()

class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            'reverse_upper': reverse_upper,
        }
