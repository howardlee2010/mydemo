# Copyright 2013 - Noorul Islam K M
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from pecan import rest
from wsme import types as wtypes

from mydemo.api.controllers.v1 import users as v1_users
from mydemo.api import expose


class V1Controller(rest.RestController):
    users = v1_users.UsersController()

    @expose.expose(wtypes.text)
    def get(self):
        return 'mydemo v1controller'
