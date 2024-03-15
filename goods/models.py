from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.0, verbose_name="Цена"
    )
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Скидка в %"
    )
    description = models.TextField(verbose_name="Описание")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    image = models.ImageField(
        upload_to="products_images", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title

    def display_id(self):
        """
    	Method to display the ID with leading zeros up to 5 digits.
    	"""
        return f"{self.id:05}"

    def sale_price(self):
        """
        Calculate the sale price based on the discount, if any.
        """
        if self.discount:
            return round(self.price - (self.price * self.discount) / 100, 2)
        else:
            return self.price
