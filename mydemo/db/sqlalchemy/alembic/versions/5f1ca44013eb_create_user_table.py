"""Create user table

Revision ID: 5f1ca44013eb
Revises: 
Create Date: 2017-12-18 18:58:12.431737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f1ca44013eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String(255), nullable=False),
        sa.Column('name', sa.String(64), nullable=False, unique=True),
        sa.Column('email', sa.String(255))
    )


def downgrade():
    op.drop_table('user')
