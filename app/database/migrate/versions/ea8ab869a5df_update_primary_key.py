"""update primary key

Revision ID: ea8ab869a5df
Revises: f98f566f9d56
Create Date: 2020-09-28 13:56:57.587142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea8ab869a5df'
down_revision = 'f98f566f9d56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('telegram_messages', sa.Column('message_id', sa.BigInteger(), nullable=False))
    op.create_index(op.f('ix_telegram_messages_message_id'), 'telegram_messages', ['message_id'], unique=False)
    op.drop_index('ix_telegram_messages_update_id', table_name='telegram_messages')
    op.drop_column('telegram_messages', 'update_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('telegram_messages', sa.Column('update_id', sa.BIGINT(), autoincrement=False, nullable=False))
    op.create_index('ix_telegram_messages_update_id', 'telegram_messages', ['update_id'], unique=False)
    op.drop_index(op.f('ix_telegram_messages_message_id'), table_name='telegram_messages')
    op.drop_column('telegram_messages', 'message_id')
    # ### end Alembic commands ###
