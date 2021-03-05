from sqlalchemy.orm import Session

from . import models, schemas


def get_dealer(db: Session, dealer_id: int):
    return db.query(models.Dealer).filter(models.Dealer.id == dealer_id).first()


def get_dealer_by_email(db: Session, email: str):
    return db.query(models.Dealer).filter(models.Dealer.email == email).first()


def get_dealer_by_phone(db: Session, phone: str):
    return db.query(models.Dealer).filter(models.Dealer.phone == phone).first()


def get_dealers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dealer).offset(skip).limit(limit).all()


def create_dealer(db: Session, dealer: schemas.Dealer):
    db_dealer = models.Dealer(
        name=dealer.name,
        location=dealer.location,
        email=dealer.email,
        phone=dealer.phone,
        website=dealer.website,
    )
    db.add(db_dealer)
    db.commit()
    db.refresh(db_dealer)
    return db_dealer


#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
