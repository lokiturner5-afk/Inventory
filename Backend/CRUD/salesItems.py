from CRUD.crud import CRUDBase
from sqlalchemy.orm import Session
from schemas.saleitemBase import SaleItemCreate
import models

class CRUDSaleItems(CRUDBase[models.SaleItem, SaleItemCreate]):
    pass

saleItem_crud = CRUDSaleItems(models.SaleItem)