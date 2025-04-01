# models/ventas.py

class Ventas:
    def __init__(self, venta_id, producto_id, cantidad, monto, fecha, vendedor, metodo_pago):
        self.venta_id = venta_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.monto = monto
        self.fecha = fecha
        self.vendedor = vendedor
        self.metodo_pago = metodo_pago

    def to_dict(self):
        return {
            "venta_id": self.venta_id,
            "producto_id": self.producto_id,
            "cantidad": self.cantidad,
            "monto": self.monto,
            "fecha": self.fecha,
            "vendedor": self.vendedor,
            "metodo_pago": self.metodo_pago
        }
