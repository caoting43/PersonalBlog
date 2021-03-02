"""init tables

Revision ID: 042d44721547
Revises: 
Create Date: 2021-02-22 10:08:13.689250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '042d44721547'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_articles',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('aid', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=52), nullable=False),
    sa.Column('author', sa.String(length=10), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('img_url', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog_user',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('mobile', sa.String(length=11), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mobile'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_user')
    op.drop_table('blog_articles')
    # ### end Alembic commands ###