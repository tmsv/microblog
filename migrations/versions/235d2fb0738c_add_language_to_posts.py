"""add language to posts

Revision ID: 235d2fb0738c
Revises: 9cfb6a8e6c48
Create Date: 2020-01-06 22:13:17.364258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '235d2fb0738c'
down_revision = '9cfb6a8e6c48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###