"""Create Lab, BuildLog model

Revision ID: 25773d2caa8a
Revises: 
Create Date: 2025-07-16 21:37:15.730639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25773d2caa8a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('labs',
    sa.Column('uid', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_index(op.f('ix_labs_uid'), 'labs', ['uid'], unique=False)
    op.create_table('build_logs',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('lab_uid', sa.String(), nullable=True),
    sa.Column('log_content', sa.Text(), nullable=False),
    sa.Column('is_error', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['lab_uid'], ['labs.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_build_logs_id'), 'build_logs', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_build_logs_id'), table_name='build_logs')
    op.drop_table('build_logs')
    op.drop_index(op.f('ix_labs_uid'), table_name='labs')
    op.drop_table('labs')
    # ### end Alembic commands ###
