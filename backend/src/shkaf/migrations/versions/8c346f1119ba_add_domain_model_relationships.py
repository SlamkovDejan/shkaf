"""Add domain model relationships

Revision ID: 8c346f1119ba
Revises: 2de04320e14d
Create Date: 2025-06-24 19:43:51.710037

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "8c346f1119ba"
down_revision: Union[str, Sequence[str], None] = "2de04320e14d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "closets",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_table(
        "clothing_pieces",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("closet_id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["closet_id"], ["closets.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "outfits",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("closet_id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["closet_id"], ["closets.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "ootds",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("outfit_id", sa.UUID(), nullable=False),
        sa.Column("closet_id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["closet_id"], ["closets.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["outfit_id"], ["outfits.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "outfit_clothing_pieces",
        sa.Column("outfit_id", sa.UUID(), nullable=False),
        sa.Column("clothing_piece_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["clothing_piece_id"],
            ["clothing_pieces.id"],
        ),
        sa.ForeignKeyConstraint(
            ["outfit_id"],
            ["outfits.id"],
        ),
        sa.PrimaryKeyConstraint("outfit_id", "clothing_piece_id"),
    )
    op.drop_index(op.f("ix_accesstoken_created_at"), table_name="access_tokens")
    op.create_index(
        op.f("ix_access_tokens_created_at"), "access_tokens", ["created_at"], unique=False
    )
    op.drop_index(op.f("ix_user_email"), table_name="users")
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.create_index(op.f("ix_user_email"), "users", ["email"], unique=True)
    op.drop_index(op.f("ix_access_tokens_created_at"), table_name="access_tokens")
    op.create_index(
        op.f("ix_accesstoken_created_at"), "access_tokens", ["created_at"], unique=False
    )
    op.drop_table("outfit_clothing_pieces")
    op.drop_table("ootds")
    op.drop_table("outfits")
    op.drop_table("clothing_pieces")
    op.drop_table("closets")
