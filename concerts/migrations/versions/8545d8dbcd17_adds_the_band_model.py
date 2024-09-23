"""Adds the Band Model

Revision ID: 8545d8dbcd17
Revises: 13b5f77b521a
Create Date: 2024-09-23 12:20:35.365197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8545d8dbcd17'
down_revision: Union[str, None] = '13b5f77b521a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
