from sqlalchemy import (
    Column, Integer, String, Text, Numeric, ForeignKey,
    DateTime, Boolean, CheckConstraint
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base



# ==========================================================
# Category
# ==========================================================
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    style = Column(String(100), unique=True, nullable=False)
    category_type = Column(String(100), unique=True, nullable=False)
    material = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    items = relationship("Item", back_populates="category")
    images = relationship("CategoryImage", back_populates="category", cascade="all, delete-orphan")


# ==========================================================
# Supplier
# ==========================================================
class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    contact_person = Column(String(100), nullable=True)
    email = Column(String(150))
    phone = Column(String(50))
    address = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    items = relationship("Item", back_populates="supplier")
    purchases = relationship("Purchase", back_populates="supplier")


# ==========================================================
# Warehouse
# ==========================================================
class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    location = Column(String(150))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    purchases = relationship("Purchase", back_populates="warehouse")
    sales = relationship("Sale", back_populates="warehouse")
    stock_movements = relationship("StockMovement", back_populates="warehouse")


# ==========================================================
# Customer
# ==========================================================
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(50))
    address = Column(Text)
    customer_type = Column(String(20), default="single", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("customer_type IN ('single', 'bulk')", name="check_customer_type"),
    )

    sales = relationship("Sale", back_populates="customer")


# ==========================================================
# Item (Product)
# ==========================================================
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    sku = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id", ondelete="SET NULL"))
    unit_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer, default=0)
    reorder_level = Column(Integer, default=10)
    status = Column(String(20), default="active", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("status IN ('active', 'inactive', 'damaged', 'expired')", name="check_item_status"),
    )

    category = relationship("Category", back_populates="items")
    supplier = relationship("Supplier", back_populates="items")
    images = relationship("ItemImage", back_populates="item", cascade="all, delete-orphan")
    purchase_items = relationship("PurchaseItem", back_populates="item")
    sale_items = relationship("SaleItem", back_populates="item")
    stock_movements = relationship("StockMovement", back_populates="item")


# ==========================================================
# ItemImage
# ==========================================================
class ItemImage(Base):
    __tablename__ = "item_images"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id", ondelete="CASCADE"), nullable=False)
    image_url = Column(String(255), nullable=False)
    description = Column(Text)
    is_main = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    item = relationship("Item", back_populates="images")


# ==========================================================
# CategoryImage
# ==========================================================
class CategoryImage(Base):
    __tablename__ = "category_images"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    image_url = Column(String(255), nullable=False)
    description = Column(Text)
    is_main = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    category = relationship("Category", back_populates="images")


# ==========================================================
# Purchase
# ==========================================================
class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id", ondelete="SET NULL"))
    warehouse_id = Column(Integer, ForeignKey("warehouses.id", ondelete="SET NULL"))
    purchase_date = Column(DateTime(timezone=True), server_default=func.now())
    total_amount = Column(Numeric(12, 2), default=0)
    status = Column(String(20), default="completed", nullable=False)
    reference = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("status IN ('pending', 'completed', 'cancelled')", name="check_purchase_status"),
    )

    supplier = relationship("Supplier", back_populates="purchases")
    warehouse = relationship("Warehouse", back_populates="purchases")
    purchase_items = relationship("PurchaseItem", back_populates="purchase", cascade="all, delete-orphan")


# ==========================================================
# PurchaseItem
# ==========================================================
class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id = Column(Integer, primary_key=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id", ondelete="CASCADE"))
    item_id = Column(Integer, ForeignKey("items.id", ondelete="RESTRICT"))
    quantity = Column(Integer, nullable=False)
    unit_cost = Column(Numeric(10, 2), nullable=False)

    purchase = relationship("Purchase", back_populates="purchase_items")
    item = relationship("Item", back_populates="purchase_items")


# ==========================================================
# Sale
# ==========================================================
class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id", ondelete="SET NULL"))
    warehouse_id = Column(Integer, ForeignKey("warehouses.id", ondelete="SET NULL"))
    sale_date = Column(DateTime(timezone=True), server_default=func.now())
    sale_type = Column(String(10))
    total_amount = Column(Numeric(12, 2), default=0)
    status = Column(String(20), default="completed", nullable=False)
    reference = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("sale_type IN ('single', 'bulk')", name="check_sale_type"),
        CheckConstraint("status IN ('pending', 'completed', 'cancelled')", name="check_sale_status"),
    )

    customer = relationship("Customer", back_populates="sales")
    warehouse = relationship("Warehouse", back_populates="sales")
    sale_items = relationship("SaleItem", back_populates="sale", cascade="all, delete-orphan")


# ==========================================================
# SaleItem
# ==========================================================
class SaleItem(Base):
    __tablename__ = "sale_items"

    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey("sales.id", ondelete="CASCADE"))
    item_id = Column(Integer, ForeignKey("items.id", ondelete="RESTRICT"))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)

    sale = relationship("Sale", back_populates="sale_items")
    item = relationship("Item", back_populates="sale_items")


# ==========================================================
# StockMovement
# ==========================================================
class StockMovement(Base):
    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id", ondelete="RESTRICT"))
    warehouse_id = Column(Integer, ForeignKey("warehouses.id", ondelete="RESTRICT"))
    movement_type = Column(String(10), nullable=False)  # IN or OUT
    quantity = Column(Integer, nullable=False)
    reference = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("movement_type IN ('IN', 'OUT')", name="check_movement_type"),
        CheckConstraint("quantity >= 0", name="check_positive_quantity"),
    )

    item = relationship("Item", back_populates="stock_movements")
    warehouse = relationship("Warehouse", back_populates="stock_movements")


# ==========================================================
# User
# ==========================================================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    role = Column(String(20), default="staff")
    profile_image = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("role IN ('staff', 'admin')", name="check_user_role"),
    )
