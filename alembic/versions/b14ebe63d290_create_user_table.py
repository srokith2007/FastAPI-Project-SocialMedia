"""create user table

Revision ID: b14ebe63d290
Revises: 65474634d7e6
Create Date: 2026-06-07 14:28:28.814568

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b14ebe63d290'
down_revision: Union[str, Sequence[str], None] = '65474634d7e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa. Integer(), nullable=False),
    sa.Column('email', sa. String(), nullable=False),
    sa.Column('password', sa. String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
    server_default=sa.text('now()'), nullable=False),
    sa. PrimaryKeyConstraint('id'),
    sa. UniqueConstraint('email')
)
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
