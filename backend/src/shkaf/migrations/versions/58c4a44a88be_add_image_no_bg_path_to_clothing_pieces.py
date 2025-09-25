"""add image_no_bg_path to clothing_pieces

Revision ID: 58c4a44a88be
Revises: c86e8fd2928b
Create Date: 2025-09-25 19:08:25.391209

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "58c4a44a88be"
down_revision: Union[str, Sequence[str], None] = "c86e8fd2928b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("clothing_pieces", sa.Column("image_no_bg_path", sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("clothing_pieces", "image_no_bg_path")
