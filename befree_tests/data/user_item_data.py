import dataclasses
from typing import Optional


@dataclasses.dataclass
class Item:
    item_title: str
    item_price: str
    product_variation_id_in_catalog: int
    product_variation_id_in_card: int
    code: Optional[str] = None
    color_code: Optional[str] = None
    color: Optional[str] = None


card_blouse = Item(
    item_title='блузка (боди) женская',
    item_price='999',
    product_variation_id_in_catalog=643054,
    product_variation_id_in_card=643055
)

card_jacket = Item(
    item_title='куртка женская',
    item_price='5999',
    product_variation_id_in_catalog=761678,
    product_variation_id_in_card=761678
)

card_bomber_jacket = Item(
    item_title='бомбер женский',
    item_price='7999',
    product_variation_id_in_catalog=642437,
    product_variation_id_in_card=642437
)

card_cardigan = Item(
    item_title='джемпер женский',
    item_price='2999',
    product_variation_id_in_catalog=643267,
    product_variation_id_in_card=643267
)
card_for_find = Item(
    item_title='летающая тарелка фрисби с принтом',
    item_price='519',
    product_variation_id_in_catalog=643267,
    product_variation_id_in_card=643267,
    code='2236004017'
)

card_t_shirt = Item(
    item_title='футболка укороченная с котиком-ангелом',
    item_price='999',
    product_variation_id_in_catalog=744549,
    product_variation_id_in_card=744546,
    code='2412120013',
    color_code='95'
)

card_oversize = Item(
    item_title='куртка-бомбер oversize с булавками и молниями',
    item_price='7999',
    product_variation_id_in_catalog=642436,
    product_variation_id_in_card=642436,
    code='2411601444',
    color_code='50'
)

card_dress = Item(
    item_title='Платье-комбинация миди атласное',
    item_price='2599',
    product_variation_id_in_catalog=770524,
    product_variation_id_in_card=770524,
    code='2421414109',
    color_code='55'
)

card_t_shirt_cropped = Item(
    item_title='Майка-топ укороченная в рубчик',
    item_price='799',
    product_variation_id_in_catalog=15107,
    product_variation_id_in_card=15107,
    code='2422121007',
    color_code='55',
    color='бежевый'
)