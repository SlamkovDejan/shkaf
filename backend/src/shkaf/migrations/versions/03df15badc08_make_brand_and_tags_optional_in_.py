"""make brand and tags optional in clothing piece

Revision ID: 03df15badc08
Revises: 416275146e2e
Create Date: 2025-09-07 16:22:24.532900

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "03df15badc08"
down_revision: Union[str, Sequence[str], None] = "416275146e2e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column("clothing_pieces", "brand", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column("clothing_pieces", "tags", existing_type=sa.VARCHAR(), nullable=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column("clothing_pieces", "tags", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column("clothing_pieces", "brand", existing_type=sa.VARCHAR(), nullable=False)
