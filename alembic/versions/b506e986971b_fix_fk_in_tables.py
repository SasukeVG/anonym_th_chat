"""fix_fk_in_tables

Revision ID: b506e986971b
Revises: 761b9e86e3fa
Create Date: 2024-08-02 21:42:11.497609

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b506e986971b'
down_revision: Union[str, None] = '761b9e86e3fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('messages_author_id_fkey', 'messages', type_='foreignkey')
    op.create_foreign_key(None, 'messages', 'users', ['author_id'], ['user_id'])
    op.alter_column('users', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.create_foreign_key('messages_author_id_fkey', 'messages', 'users', ['author_id'], ['id'])
    # ### end Alembic commands ###
