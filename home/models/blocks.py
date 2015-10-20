from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ImagePairBlock(blocks.StructBlock):
    image_one = ImageChooserBlock()
    image_two = ImageChooserBlock()

    class Meta:
        icon = 'image'
        template = 'home/image_pair_block.html'


class ImageTriadBlock(blocks.StructBlock):
    image_one = ImageChooserBlock()
    image_two = ImageChooserBlock()
    image_three = ImageChooserBlock()

    class Meta:
        icon = 'image'
        template = 'home/image_triad_block.html'


class BustOutBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.RichTextBlock()
    inverted = blocks.BooleanBlock(required=False)

    class Meta:
        icon = 'openquote'
        template = 'home/bust_out_block.html'


class BustOutQuoteBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    quote = blocks.TextBlock()
    source = blocks.TextBlock()
    inverted = blocks.BooleanBlock(required=False)

    class Meta:
        icon = 'openquote'
        template = 'home/bust_out_quote_block.html'


class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock(max_length=30)
    page_link = blocks.PageChooserBlock()
    button_type = blocks.ChoiceBlock(choices=[
        ('default', 'Default'),
        ('primary', 'Primary'),
        ('success', 'Success'),
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('danger', 'Danger'),
        ('link', 'Link'),
    ])

    class Meta:
        icon = 'radio-full'
        template = 'home/button.html'