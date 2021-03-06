"""task completed

Revision ID: e22bda1c1f7e
Revises: 1763409e2279
Create Date: 2016-05-28 19:59:52.654518

"""

# revision identifiers, used by Alembic.
revision = 'e22bda1c1f7e'
down_revision = '1763409e2279'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('completed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'completed')
    ### end Alembic commands ###
