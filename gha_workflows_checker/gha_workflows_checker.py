# Copyright 2022 – present, UBC EOAS MOAD Group and The University of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# SPDX-License-Identifier: Apache-2.0


from pathlib import Path
import shlex
import subprocess

from rich import print
import yaml


def main():
    orgs_repos_path = Path("orgs_repos.yaml")
    with orgs_repos_path.open("rt") as f:
        orgs_repos = yaml.safe_load(f)
    for org in orgs_repos:
        for repo in orgs_repos[org]:
            print(f"[bold magenta]{org}/{repo}:")
            cmd = f"gh -R {org}/{repo} workflow list -a"
            subprocess.run(shlex.split(cmd))
            print()


if __name__ == "__main__":
    main()
