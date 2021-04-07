"""empty message

Revision ID: 3d3886d90563
Revises: 
Create Date: 2021-03-30 15:40:22.515027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d3886d90563'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drink',
    sa.Column('id', sa.Integer().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('recipe', sa.String(length=180), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('drink')
    # ### end Alembic commands ###
