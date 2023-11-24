"""edit registered_at

Revision ID: 18208e126b8c
Revises: c5a087520f38
Create Date: 2023-11-24 13:05:22.998547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18208e126b8c'
down_revision: Union[str, None] = 'c5a087520f38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'registered_at',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'registered_at',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    # ### end Alembic commands ###