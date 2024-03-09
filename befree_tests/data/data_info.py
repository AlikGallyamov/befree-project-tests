import dataclasses


@dataclasses.dataclass
class Card:
    card_name: str
    brand_name: str
    card_article: str
    non_existent_article: str


card = Card(
    card_name='Набор металлических машинок молния маквин',
    brand_name='MITU',
    card_article='76566619',
    non_existent_article='8944165849321186418794'
)


@dataclasses.dataclass
class Texts:
    nothing_found: str = 'Попробуйте поискать по-другому или сократить запрос'
    empty_cart: str = 'В корзине пока пусто'
