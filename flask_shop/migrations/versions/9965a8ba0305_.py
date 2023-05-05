"""empty message

Revision ID: 9965a8ba0305
Revises: a3ac8c33812d
Create Date: 2023-04-17 18:33:29.795824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9965a8ba0305'
down_revision = 'a3ac8c33812d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_user', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.add_column('t_user', sa.Column('update_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('t_user', 'update_time')
    op.drop_column('t_user', 'create_time')
    # ### end Alembic commands ###
