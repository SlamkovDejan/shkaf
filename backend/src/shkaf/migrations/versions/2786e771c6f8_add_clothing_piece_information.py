"""Add clothing piece information

Revision ID: 2786e771c6f8
Revises: 8c346f1119ba
Create Date: 2025-06-26 21:18:01.185871

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2786e771c6f8"
down_revision: Union[str, Sequence[str], None] = "8c346f1119ba"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "clothing_piece_fabric",
        sa.Column("name_en", sa.String(), nullable=False),
        sa.Column("name_mk", sa.String(), nullable=True),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "clothing_piece_size",
        sa.Column("name_en", sa.String(), nullable=False),
        sa.Column("name_mk", sa.String(), nullable=True),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "clothing_piece_status",
        sa.Column("name_en", sa.String(), nullable=False),
        sa.Column("name_mk", sa.String(), nullable=True),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "colors",
        sa.Column("hex", sa.String(), nullable=False),
        sa.Column("name_en", sa.String(), nullable=False),
        sa.Column("name_mk", sa.String(), nullable=True),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "weather_seasons",
        sa.Column("name_en", sa.String(), nullable=False),
        sa.Column("name_mk", sa.String(), nullable=True),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "clothing_pieces_colors",
        sa.Column("clothing_piece_id", sa.UUID(), nullable=False),
        sa.Column("color_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(["clothing_piece_id"], ["clothing_pieces.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["color_id"], ["colors.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("clothing_piece_id", "color_id"),
    )
    op.create_table(
        "clothing_pieces_fabric",
        sa.Column("clothing_piece_id", sa.UUID(), nullable=False),
        sa.Column("fabric_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(["clothing_piece_id"], ["clothing_pieces.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["fabric_id"], ["clothing_piece_fabric.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("clothing_piece_id", "fabric_id"),
    )
    op.create_table(
        "clothing_pieces_statuses",
        sa.Column("clothing_piece_id", sa.UUID(), nullable=False),
        sa.Column("status_id", sa.UUID(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("is_current", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["clothing_piece_id"], ["clothing_pieces.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["status_id"], ["clothing_piece_status.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("clothing_piece_id", "status_id"),
    )
    op.create_table(
        "clothing_pieces_weather_seasons",
        sa.Column("clothing_piece_id", sa.UUID(), nullable=False),
        sa.Column("weather_season_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(["clothing_piece_id"], ["clothing_pieces.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["weather_season_id"], ["weather_seasons.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("clothing_piece_id", "weather_season_id"),
    )
    op.add_column("clothing_pieces", sa.Column("descriptor", sa.String(), nullable=False))
    op.add_column("clothing_pieces", sa.Column("brand", sa.String(), nullable=False))
    op.add_column("clothing_pieces", sa.Column("purchase_date", sa.Date(), nullable=True))
    op.add_column("clothing_pieces", sa.Column("place_of_purchase", sa.String(), nullable=True))
    op.add_column("clothing_pieces", sa.Column("price", sa.Float(), nullable=True))
    op.add_column("clothing_pieces", sa.Column("price_currency", sa.String(), nullable=True))
    op.add_column("clothing_pieces", sa.Column("tags", sa.String(), nullable=False))
    op.add_column("clothing_pieces", sa.Column("comment", sa.String(), nullable=True))
    op.add_column("clothing_pieces", sa.Column("favorite", sa.Boolean(), nullable=False))
    op.add_column("clothing_pieces", sa.Column("size_id", sa.UUID(), nullable=True))
    op.create_foreign_key(
        None, "clothing_pieces", "clothing_piece_size", ["size_id"], ["id"], ondelete="SET NULL"
    )
    op.drop_constraint(
        op.f("outfit_clothing_pieces_outfit_id_fkey"), "outfit_clothing_pieces", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("outfit_clothing_pieces_clothing_piece_id_fkey"),
        "outfit_clothing_pieces",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "outfit_clothing_pieces",
        "clothing_pieces",
        ["clothing_piece_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None, "outfit_clothing_pieces", "outfits", ["outfit_id"], ["id"], ondelete="CASCADE"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, "outfit_clothing_pieces", type_="foreignkey")
    op.drop_constraint(None, "outfit_clothing_pieces", type_="foreignkey")
    op.create_foreign_key(
        op.f("outfit_clothing_pieces_clothing_piece_id_fkey"),
        "outfit_clothing_pieces",
        "clothing_pieces",
        ["clothing_piece_id"],
        ["id"],
    )
    op.create_foreign_key(
        op.f("outfit_clothing_pieces_outfit_id_fkey"),
        "outfit_clothing_pieces",
        "outfits",
        ["outfit_id"],
        ["id"],
    )
    op.drop_constraint(None, "clothing_pieces", type_="foreignkey")
    op.drop_column("clothing_pieces", "size_id")
    op.drop_column("clothing_pieces", "favorite")
    op.drop_column("clothing_pieces", "comment")
    op.drop_column("clothing_pieces", "tags")
    op.drop_column("clothing_pieces", "price_currency")
    op.drop_column("clothing_pieces", "price")
    op.drop_column("clothing_pieces", "place_of_purchase")
    op.drop_column("clothing_pieces", "purchase_date")
    op.drop_column("clothing_pieces", "brand")
    op.drop_column("clothing_pieces", "descriptor")
    op.drop_table("clothing_pieces_weather_seasons")
    op.drop_table("clothing_pieces_statuses")
    op.drop_table("clothing_pieces_fabric")
    op.drop_table("clothing_pieces_colors")
    op.drop_table("weather_seasons")
    op.drop_table("colors")
    op.drop_table("clothing_piece_status")
    op.drop_table("clothing_piece_size")
    op.drop_table("clothing_piece_fabric")
