"""Change to vote time again.

Revision ID: d59f1c519ece
Revises: 5ef51d774480
Create Date: 2023-07-12 16:44:54.233036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd59f1c519ece'
down_revision = '5ef51d774480'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vote', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vote_time', sa.Time(), nullable=False))
        batch_op.drop_column('vote_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vote', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vote_date', sa.DATE(), autoincrement=False, nullable=False))
        batch_op.drop_column('vote_time')

    # ### end Alembic commands ###
