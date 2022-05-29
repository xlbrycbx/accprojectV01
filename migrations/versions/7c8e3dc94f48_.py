"""empty message

Revision ID: 7c8e3dc94f48
Revises: 
Create Date: 2022-05-29 21:38:41.842404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c8e3dc94f48'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('itemCode', sa.String(length=7), nullable=False),
    sa.Column('modelCode', sa.String(length=7), nullable=False),
    sa.Column('modelLable', sa.String(length=30), nullable=False),
    sa.Column('rdatetime', sa.DateTime(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('itemCode')
    )
    op.create_table('supplier',
    sa.Column('supplierCode', sa.String(length=10), nullable=False),
    sa.Column('supplierName', sa.String(length=30), nullable=False),
    sa.Column('contactPerson', sa.String(length=10), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('rdatetime', sa.DateTime(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('supplierCode')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('role', sa.Enum('admin', 'njfUser', 'supplier'), nullable=True),
    sa.Column('rdatetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('product_supplier',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('supplierCode', sa.String(length=10), nullable=False),
    sa.Column('itemCode', sa.String(length=7), nullable=False),
    sa.ForeignKeyConstraint(['itemCode'], ['product.itemCode'], ),
    sa.ForeignKeyConstraint(['supplierCode'], ['supplier.supplierCode'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_supplier')
    op.drop_table('user')
    op.drop_table('supplier')
    op.drop_table('product')
    # ### end Alembic commands ###