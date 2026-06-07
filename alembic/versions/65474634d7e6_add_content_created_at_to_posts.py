"""add content/created_at to posts

Revision ID: 65474634d7e6
Revises: ca5131f3f891
Create Date: 2026-06-07 14:15:11.973244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65474634d7e6'
down_revision: Union[str, Sequence[str], None] = 'ca5131f3f891'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    op.drop_column("posts", "created_at")
    pass
