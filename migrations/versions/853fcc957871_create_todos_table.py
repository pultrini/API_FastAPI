"""create todos table

Revision ID: 853fcc957871
Revises: ae9de8b2a5ed
Create Date: 2025-09-02 19:49:35.824984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '853fcc957871'
down_revision: Union[str, Sequence[str], None] = 'ae9de8b2a5ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
