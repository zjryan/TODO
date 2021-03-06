"""task model

Revision ID: cf0ac9e62bd8
Revises: 3804dc9388e9
Create Date: 2016-05-28 16:17:40.359842

"""

# revision identifiers, used by Alembic.
revision = 'cf0ac9e62bd8'
down_revision = '3804dc9388e9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    ### end Alembic commands ###
