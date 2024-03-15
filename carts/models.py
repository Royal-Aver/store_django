from django.db import models
from users.models import User
from goods.models import Products


class CartQuerySet(models.QuerySet):

    def total_price(self):
        """
        Calculate the total price of all products in the cart.
        """
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        """
        Calculate the total quantity of items in the cart.

        :param self: The cart object.
        :return: The total quantity of items in the cart.
        """
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Пользователь",
    )  # blank=True, null=True - для того, чтобы неавторизованные пользователи могли добавлять в корзину
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, verbose_name="Товар"
    )
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления товара"
    )

    class Meta:
        db_table: "cart"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    objects = CartQuerySet.as_manager()

    def products_price(self):
        """
        Calculate the total price of the products by multiplying the sale price of each product by the quantity, and rounding the result to 2 decimal places.
        """
        return round(self.product.sale_price() * self.quantity, 2)

    def __str__(self):
        """
        Return a string representation of the object, including the username, product title, and quantity.
        """
        return f"Корзина {self.user.username} | Товар {self.product.title} | Количество {self.quantity}"
