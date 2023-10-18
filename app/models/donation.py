from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import DonationCharityProject


class Donation(DonationCharityProject):
    user_id = Column(
        Integer,
        ForeignKey('user.id')
    )
    comment = Column(Text)