from CRUD.crud import CRUDBase
# from sqlalchemy.orm import Session
from schemas.warehouseschema import WarehouseCreate
import models


class CRUDWarehouse(CRUDBase[models.Warehouse, WarehouseCreate]):
    pass


warehouse_crud = CRUDWarehouse(models.Warehouse)