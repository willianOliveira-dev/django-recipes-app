from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """Representa as categorias de receita"""

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    name = models.CharField(
        max_length=65,
        unique=True,
        verbose_name="Nome da categoria",
        help_text="Nome único para a categoria (máx. 65 caracteres)",
        db_index=True,
    )

    icon_key = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        default="utensils",
        verbose_name="Ícone da categoria",
        help_text="Nome do ícone da biblioteca Lucide (ex: 'fish', 'cake'). Consulte lucide.dev",
    )

    description = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Descrição curta",
        help_text="Breve descrição da categoria (máx. 250 caracteres)",
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Slug da URL",
        help_text="Versão amigável para a URL (gerada automaticamente)",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Recipe(models.Model):
    """Modelo principal contendo as informações da receita"""

    TIME_UNIT_CHOICES = [
        ("s", "segundo(s)"),
        ("min", "minuto(s)"),
        ("h", "hora(s)"),
    ]

    DIFFICULTY_LEVEL_CHOICES = [
        ("facil", "Fácil"),
        ("medio", "Médio"),
        ("dificil", "Difícil"),
        ("expert", "Expert / Profissional"),
    ]

    SERVING_UNIT_CHOICES = [
        ("porcoes", "porção(ões)"),
        ("pessoas", "pessoa(s)"),
        ("unidades", "unidade(s)"),
        ("fatias", "fatia(s)"),
        ("pedacos", "pedaço(s)"),
        ("copos", "copo(s)"),
        ("tacas", "taça(s)"),
        ("pratos", "prato(s)"),
        ("un", "item(ns)"),
        ("docinhos", "docinho(s) (cento)"),
        ("salgadinhos", "salgadinho(s) (cento)"),
        ("massa", "massa(s) (kg)"),
        ("rendimento_livre", "a gosto"),
    ]

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["is_published", "-created_at"]),
        ]

    title = models.CharField(
        max_length=150,
        verbose_name="Título da receita",
        db_index=True,
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Descrição curta",
        help_text="Resumo da receita para as listagens",
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Slug da URL",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="recipes",
        verbose_name="Categoria",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name="Autor",
        help_text="Usuário responsável pela criação desta receita",
    )

    preparation_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        verbose_name="Tempo de preparo",
    )
    preparation_time_unit = models.CharField(
        max_length=20,
        choices=TIME_UNIT_CHOICES,
        default="min",
        verbose_name="Unidade do tempo de preparo",
    )
    servings = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        verbose_name="Rendimento",
    )
    serving_unit = models.CharField(
        max_length=20,
        choices=SERVING_UNIT_CHOICES,
        default="porcoes",
        verbose_name="Unidade do rendimento",
    )
    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        verbose_name="Tempo de cozimento",
    )
    cooking_time_unit = models.CharField(
        max_length=20,
        default="min",
        choices=TIME_UNIT_CHOICES,
        verbose_name="Unidade do tempo de cozimento",
    )
    difficulty_level = models.CharField(
        max_length=10,
        choices=DIFFICULTY_LEVEL_CHOICES,
        default="medio",
        verbose_name="Nível de dificuldade",
    )

    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Visualizações",
        help_text="Número total de vezes que a receita foi visualizada",
        db_index=True,
    )

    cover = models.ImageField(
        upload_to="recipes/covers/%Y/%m/%d",
        verbose_name="Imagem de capa",
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Publicado",
        help_text="Se marcado, a receita ficará visível no site",
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Recipe.objects.filter(slug=slug).exists():
                slug = f"{slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.title


class Ingredient(models.Model):
    """Representa a biblioteca global de ingredientes"""

    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Nome do ingrediente",
    )
    image = models.ImageField(
        upload_to="ingredients/covers/%Y/%m/%d",
        verbose_name="Imagem do ingrediente",
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Slug da URL",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Ingredient.objects.filter(slug=slug).exists():
                slug = f"{slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class RecipeSection(models.Model):
    """Representa blocos da receita como 'Massa' ou 'Recheio'"""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name="Receita",
    )

    title = models.CharField(
        max_length=100,
        verbose_name="Título da seção",
        help_text="Ex: Massa, Recheio, Cobertura",
    )

    ingredients = models.ManyToManyField(
        Ingredient, through="RecipeSectionIngredient", related_name="sections"
    )

    position = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Ordem da seção",
    )

    class Meta:
        verbose_name = "Seção da receita"
        verbose_name_plural = "Seções da receita"
        ordering = ["position"]

    def __str__(self) -> str:
        return f"{self.title} - {self.recipe.title}"


class RecipeSectionIngredient(models.Model):
    """Vincula ingredientes a seções com quantidades e notas"""

    QUANTITY_UNIT_CHOICES = [
        ("", "N/A"),
        ("g", "g"),
        ("kg", "kg"),
        ("mg", "mg"),
        ("oz", "oz"),
        ("lb", "lb"),
        ("ml", "ml"),
        ("l", "l"),
        ("cubo", "cubo(s)"),
        ("xic", "xícara(s)"),
        ("col_sopa", "colher(es) de sopa"),
        ("col_cha", "colher(es) de chá"),
        ("col_sob", "colher(es) de sobremesa"),
        ("col_caf", "colher(es) de café"),
        ("copo", "copo(s)"),
        ("pitada", "pitada(s)"),
        ("fio", "fio(s)"),
        ("un", "unidade(s)"),
        ("dz", "dúzia(s)"),
        ("cento", "cento(s)"),
        ("pacote", "pacote(s)"),
        ("lata", "lata(s)"),
        ("garrafa", "garrafa(s)"),
        ("caixa", "caixa(s)"),
        ("rendimento_livre", "a gosto"),
    ]

    section = models.ForeignKey(
        RecipeSection,
        on_delete=models.CASCADE,
        verbose_name="Seção",
        related_name="section_ingredient",
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name="Ingrediente",
        related_name="ingredient_in_sections",
    )
    quantity = models.CharField(
        max_length=50,
        verbose_name="Quantidade",
        blank=True,
        null=True,
        help_text="Ex: 500, 2 1/2, 1",
    )
    unit = models.CharField(
        max_length=20,
        default="",
        blank=True,
        null=True,
        choices=QUANTITY_UNIT_CHOICES,
        verbose_name="Unidade de medida",
    )
    note = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Observação",
        help_text="Ex: gelada, picada, para pincelar",
    )

    class Meta:
        verbose_name = "Ingrediente da seção"
        verbose_name_plural = "Ingredientes da seção"
        ordering = ["id"]

    def __str__(self) -> str:
        if self.unit == "rendimento_livre":
            return f"{self.ingredient.name} a gosto" + (
                f" ({self.note})" if self.note else ""
            )

        if not self.unit:
            parts = [self.quantity, self.ingredient.name, self.note]
            return " ".join([p for p in parts if p])

        unit_display = self.get_unit_display()  # type: ignore
        base = f"{self.quantity or ''} {unit_display} de {self.ingredient.name}"
        return f"{base} {self.note}" if self.note else base


class PreparationMethod(models.Model):
    """Representa um passo individual do modo de preparo"""

    section = models.ForeignKey(
        RecipeSection,
        on_delete=models.CASCADE,
        verbose_name="Seção",
        related_name="preparations",
    )

    step = models.CharField(
        max_length=255,
        verbose_name="Descrição da etapa",
        help_text="Etapa do modo de preparo (máx. 255 caracteres)",
    )

    position = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Ordem",
    )

    class Meta:
        verbose_name = "Etapa de preparo"
        verbose_name_plural = "Etapas de preparo"
        ordering = ["position"]

    def __str__(self):
        return f"Passo {self.position}: {self.step[:30]}..."


class Favorite(models.Model):
    """Receitas favoritas dos usuários"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorite_recipes"
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="favorited_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        unique_together = ["user", "recipe"]

    def __str__(self) -> str:
        return f"{self.user.username} favoritou {self.recipe.title}"


class RecipeRating(models.Model):
    """Avaliações das receitas (1 a 5 estrelas)"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_ratings"
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Avaliação",
    )
    comment = models.TextField(blank=True, null=True, verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        unique_together = ["user", "recipe"]

    def __str__(self) -> str:
        return f"{self.user.username} - {self.recipe.title}: {self.rating}/5"
