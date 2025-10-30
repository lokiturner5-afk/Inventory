from CRUD.crud import CRUDBase
from schemas.supplierschema import SupplierCreate
import models


class CRUDSupplier(CRUDBase[models.Supplier, SupplierCreate]):
    pass


supplier_crud = CRUDSupplier(models.Supplier)