"""Initial migration.

Revision ID: 84a38ccb6049
Revises: 
Create Date: 2023-06-25 19:54:18.335851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84a38ccb6049'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('election',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('election_date', sa.Date(), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.Column('total_voters', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=45), nullable=True),
    sa.Column('password', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('candidate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('elect_id', sa.Integer(), nullable=False),
    sa.Column('cand_id', sa.String(length=20), nullable=False),
    sa.Column('firstname', sa.String(length=45), nullable=False),
    sa.Column('lastname', sa.String(length=45), nullable=False),
    sa.Column('middlename', sa.String(length=45), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('tel', sa.String(length=20), nullable=False),
    sa.Column('position', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['elect_id'], ['election.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cand_id')
    )
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=45), nullable=False),
    sa.Column('lastname', sa.String(length=45), nullable=False),
    sa.Column('middlename', sa.String(length=45), nullable=False),
    sa.Column('email', sa.String(length=45), nullable=False),
    sa.Column('mobile', sa.String(length=45), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('member_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['login.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vote_count',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('election_id', sa.Integer(), nullable=False),
    sa.Column('precinct', sa.String(length=45), nullable=False),
    sa.Column('final_tally', sa.Integer(), nullable=False),
    sa.Column('approved_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['election_id'], ['election.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mid', sa.Integer(), nullable=False),
    sa.Column('voter_id', sa.String(length=45), nullable=False),
    sa.Column('precinct', sa.String(length=45), nullable=False),
    sa.Column('last_vote_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['mid'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mid'),
    sa.UniqueConstraint('voter_id')
    )
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('voter_id', sa.String(length=45), nullable=False),
    sa.Column('election_id', sa.Integer(), nullable=False),
    sa.Column('cand_id', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['cand_id'], ['candidate.cand_id'], ),
    sa.ForeignKeyConstraint(['election_id'], ['election.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['voter.voter_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vote')
    op.drop_table('voter')
    op.drop_table('vote_count')
    op.drop_table('member')
    op.drop_table('candidate')
    op.drop_table('login')
    op.drop_table('election')
    # ### end Alembic commands ###
