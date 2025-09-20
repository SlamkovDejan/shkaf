"""Add OutfitOccasion, OutfitAesthetic models and expand Outfit model

Revision ID: c86e8fd2928b
Revises: 03df15badc08
Create Date: 2025-09-20 22:49:50.567197

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "c86e8fd2928b"
down_revision: Union[str, Sequence[str], None] = "03df15badc08"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "outfit_aesthetics",
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("name_en", sa.String(), nullable=False),
        sa.Column("name_mk", sa.String(), nullable=True),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="cascade"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "outfit_occasions",
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("name_en", sa.String(), nullable=False),
        sa.Column("name_mk", sa.String(), nullable=True),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="cascade"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("outfits", sa.Column("name", sa.String(), nullable=True))
    op.add_column("outfits", sa.Column("try_on_photo_path", sa.String(), nullable=True))
    op.add_column("outfits", sa.Column("occasion_id", sa.UUID(), nullable=True))
    op.add_column("outfits", sa.Column("aesthetic_id", sa.UUID(), nullable=True))
    op.create_foreign_key(
        None, "outfits", "outfit_occasions", ["occasion_id"], ["id"], ondelete="SET NULL"
    )
    op.create_foreign_key(
        None, "outfits", "outfit_aesthetics", ["aesthetic_id"], ["id"], ondelete="SET NULL"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("outfits", "aesthetic_id")
    op.drop_column("outfits", "occasion_id")
    op.drop_column("outfits", "try_on_photo_path")
    op.drop_column("outfits", "name")
    op.drop_table("outfit_occasions")
    op.drop_table("outfit_aesthetics")
