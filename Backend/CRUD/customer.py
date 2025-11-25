from CRUD.crud import CRUDBase
from sqlalchemy.orm import Session
from schemas.customerschema import CustomerCreate
import models

class CRUDCustomer(CRUDBase[models.Customer, CustomerCreate]):
    pass

customer_crud = CRUDCustomer(models.Customer)