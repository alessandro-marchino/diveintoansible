from __future__ import annotations

DOCUMENTATION = """
    name: items
    author: James Spurin
    version_added: 2.10
    short_description: list of items, sorted
    description:
      - this lookup returns a list of items given to it, if any of the top level items is also a list it will flatten it, but it will not recurse. The resulting list will be sorted
    notes:
      - this is the standard lookup used for loops in most examples
      - check out the 'flattened' lookup for recursive flattening
      - if you do not want flattening nor any other transformation look at the 'list' lookup.
    options:
      _terms:
        description: list of items
        required: True
"""

EXAMPLES = """
- name: "loop through list"
  ansible.builtin.debug:
    msg: "An item: {{ item }}"
  with_sorted_items:
    - 1
    - 2
    - 3

- name: add several users
  ansible.builtin.user:
    name: "{{ item }}"
    groups: "wheel"
    state: present
  with_sorted_items:
     - testuser1
     - testuser2

- name: "loop through list from a variable"
  ansible.builtin.debug:
    msg: "An item: {{ item }}"
  with_sorted_items: "{{ somelist }}"

- name: more complex items to add several users
  ansible.builtin.user:
    name: "{{ item.name }}"
    uid: "{{ item.uid }}"
    groups: "{{ item.groups }}"
    state: present
  with_sorted_items:
     - { name: testuser1, uid: 1002, groups: "wheel, staff" }
     - { name: testuser2, uid: 1003, groups: staff }

"""

RETURN = """
  _raw:
    description:
      - once flattened list
    type: list
"""

from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):

    def run(self, terms, **kwargs):

        return self._flatten(sorted(terms, key=str))
