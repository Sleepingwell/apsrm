# Copyright 2022 CSIRO
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import pkgutil
from math import floor

VACCINE_DATA = json.loads(pkgutil.get_data(__name__, 'vaccineefficacy.json'))


class Vaccine:
    """Vaccine.

    You can find the data for this vaccine in the file *vaccineefficacy.json* or
    simply view it :ref:`here<vaccine-efficacy-data>`.

    :param relative_protection_scalar: The relative level of protection
        against infection offered by the vaccine.
    """

    #: The default level of protection against infection offered when the
    #: vaccine is first administered.
    BASELINE_PROTECTION = VACCINE_DATA[0]

    def __init__(self, relative_protection_scalar: float = 1.):
        self.relative_protection_scalar = relative_protection_scalar

    @staticmethod
    def relative_infectiousness(person,
                                time_since_vaccination: float) -> float:
        """Relative infectiousness of *person*, *time_since_vaccination* periods after being vaccinated.

        :param apsrm.Person person: The person.
        :param time_since_vaccination: The time since they were vaccinated.
        """
        return 1.

    def relative_susceptibility(self, person,
                                time_since_vaccination: float) -> float:
        """Relative susceptibility of *person*, *time_since_vaccination* periods after being vaccinated.

        :param apsrm.Person person: The person.
        :param time_since_vaccination: The time since they were vaccinated.
        """

        if time_since_vaccination < 0.: return 1.
        return 1. - self.relative_protection_scalar * \
            VACCINE_DATA[min(floor(time_since_vaccination), len(VACCINE_DATA) - 1)]
