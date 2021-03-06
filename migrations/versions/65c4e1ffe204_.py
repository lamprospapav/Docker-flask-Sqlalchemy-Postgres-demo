"""empty message

Revision ID: 65c4e1ffe204
Revises: f363f7332d82
Create Date: 2019-02-11 00:25:52.973658

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '65c4e1ffe204'
down_revision = 'f363f7332d82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('pub_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_name'), 'book', ['name'], unique=False)
    op.drop_index('ix_demoObject_name', table_name='demoObject')
    op.drop_table('demoObject')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('demoObject',
    sa.Column('id', sa.INTEGER(), server_default=sa.text(u'nextval(\'"demoObject_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('rating', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('pub_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'demoObject_pkey')
    )
    op.create_index('ix_demoObject_name', 'demoObject', ['name'], unique=False)
    op.drop_index(op.f('ix_book_name'), table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###
