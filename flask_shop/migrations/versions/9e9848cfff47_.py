"""empty message

Revision ID: 9e9848cfff47
Revises: 9965a8ba0305
Create Date: 2023-04-20 15:25:42.531912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e9848cfff47'
down_revision = '9965a8ba0305'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('path', sa.String(length=32), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_menu')
    # ### end Alembic commands ###