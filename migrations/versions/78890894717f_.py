"""empty message

Revision ID: 78890894717f
Revises: None
Create Date: 2016-03-01 09:36:59.659678

"""

# revision identifiers, used by Alembic.
revision = '78890894717f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articleTypeSettings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('protected', sa.Boolean(), nullable=True),
    sa.Column('hide', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_foreign_key(None, 'articleTypes', 'menus', ['menu_id'], ['id'])
    op.create_foreign_key(None, 'articleTypes', 'articleTypeSettings', ['setting_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'articleTypes', type_='foreignkey')
    op.drop_constraint(None, 'articleTypes', type_='foreignkey')
    op.drop_table('articleTypeSettings')
    ### end Alembic commands ###
