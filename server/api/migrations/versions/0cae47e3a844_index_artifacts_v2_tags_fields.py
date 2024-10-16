# Copyright 2024 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Index artifacts_v2_tags fields

Revision ID: 0cae47e3a844
Revises: aa28cdc5bb17
Create Date: 2024-06-19 13:17:06.718804

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "0cae47e3a844"
down_revision = "aa28cdc5bb17"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        "idx_artifacts_v2_tags_project_name_obj_name",
        "artifacts_v2_tags",
        ["project", "name", "obj_name"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        "idx_artifacts_v2_tags_project_name_obj_name", table_name="artifacts_v2_tags"
    )
    # ### end Alembic commands ###
