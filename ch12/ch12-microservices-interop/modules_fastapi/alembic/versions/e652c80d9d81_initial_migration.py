"""Initial migration

Revision ID: e652c80d9d81
Revises: 
Create Date: 2024-05-03 23:57:06.495232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e652c80d9d81'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('faculty_borrower',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('empid', sa.String(length=55), nullable=False),
    sa.Column('firstname', sa.String(length=55), nullable=False),
    sa.Column('lastname', sa.String(length=55), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('empid')
    )
    op.create_table('borrowed_hist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('empid', sa.String(), nullable=False),
    sa.Column('borrowed_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['empid'], ['faculty_borrower.empid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrowed_hist')
    op.drop_table('faculty_borrower')
    # ### end Alembic commands ###
