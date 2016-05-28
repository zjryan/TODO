"""task timestamp

Revision ID: 1763409e2279
Revises: cf0ac9e62bd8
Create Date: 2016-05-28 16:56:36.496407

"""

# revision identifiers, used by Alembic.
revision = '1763409e2279'
down_revision = 'cf0ac9e62bd8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(u'ix_tasks_timestamp', 'tasks', ['timestamp'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(u'ix_tasks_timestamp', table_name='tasks')
    op.drop_column('tasks', 'timestamp')
    ### end Alembic commands ###
