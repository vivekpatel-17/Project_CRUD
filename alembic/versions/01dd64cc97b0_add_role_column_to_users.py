"""add role column to users

Revision ID: 01dd64cc97b0
Revises: 1fd32ba6f83b
Create Date: 2026-05-15 15:32:39.433436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '01dd64cc97b0'
down_revision: Union[str, Sequence[str], None] = '1fd32ba6f83b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        'users',
        sa.Column(
            'role',
            sa.String(length=50),
            nullable=False,
            server_default='user'
        )
    )

def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column('users', 'role')
