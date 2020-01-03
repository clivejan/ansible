#!/bin/env python

import pwd
from ansible.module_utils.basic import AnsibleModule

class check_user:
    def __init__(self, user):
        self.user = user

    # Check if user exists
    def check(self):
        uid = ''
        gid = ''
        try:
            user = pwd.getpwnam(self.user)
            success = True
            ret_msg = "User %s exists" % self.user
            uid = user.pw_uid
            gid = user.pw_gid
        except KeyError:
            success = False
            ret_msg = "User %s does not exists" % self.user
        return success, ret_msg, uid, gid

def main():
    # Parsing argument file
    module = AnsibleModule(
        argument_spec = dict(user = dict(required=True))
    )
    user = module.params.get('user')

    chkusr = check_user(user)
    success, ret_msg, uid, gid = chkusr.check()

    # Error handling and JSON return
    if success:
        module.exit_json(msg=ret_msg, uid=uid, gid=gid)
    else:
        module.fail_json(msg=ret_msg)

if __name__ == "__main__":
    main()

