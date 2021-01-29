"""Added how_much_read to User

Revision ID: af66054c0640
Revises: 
Create Date: 2021-01-28 21:07:47.210172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af66054c0640'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('users', 'how_much_read',
                existing_type=sa.VARCHAR(),
                type_=sa.Integer(),
                existing_nullable=True,
                postgresql_using='how_much_read::integer')
    

def downgrade():
     op.drop_table('users') 

