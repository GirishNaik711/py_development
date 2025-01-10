"""adding content column

Revision ID: 4054ea1031c3
Revises: c1d503fb5116
Create Date: 2025-01-07 23:33:48.360242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4054ea1031c3'
down_revision: Union[str, None] = 'c1d503fb5116'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
